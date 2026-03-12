#!/usr/bin/env python3
"""
Convert The Sourdough Framework from LaTeX to Markdown.

Produces both individual chapter files and a single combined file
suitable for AI/LLM consumption.
"""

import re
import os
import sys

BOOK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "book")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "markdown")

# Chapter files in book order (from book.tex)
CHAPTERS = [
    ("intro/preface.tex", "00-preface.md"),
    ("intro/acknowledgments.tex", "01-acknowledgments.md"),
    ("history/sourdough-history.tex", "02-history.md"),
    ("basics/how-sourdough-works.tex", "03-how-sourdough-works.md"),
    ("sourdough-starter/sourdough-starter.tex", "04-sourdough-starter.md"),
    ("sourdough-starter/sourdough-starter-types.tex", "05-sourdough-starter-types.md"),
    ("flour-types/flour-types.tex", "06-flour-types.md"),
    ("bread-types/bread-types.tex", "07-bread-types.md"),
    ("wheat-sourdough/wheat-sourdough.tex", "08-wheat-sourdough.md"),
    ("non-wheat-sourdough/non-wheat-sourdough.tex", "09-non-wheat-sourdough.md"),
    ("mix-ins/mix-ins.tex", "10-mix-ins.md"),
    ("baking/baking.tex", "11-baking.md"),
    ("storing-bread/storing-bread.tex", "12-storing-bread.md"),
    ("troubleshooting/misc.tex", "13-troubleshooting.md"),
    ("troubleshooting/crumb-structures.tex", "14-crumb-structures.md"),
    ("glossary/glossary.tex", "15-glossary.md"),
]


def read_file(path):
    """Read a file and return its contents."""
    full_path = os.path.join(BOOK_DIR, path)
    if not os.path.exists(full_path):
        print(f"  Warning: File not found: {full_path}")
        return ""
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()


def convert_table_to_markdown(tex_content):
    """Convert a LaTeX tabular environment to a markdown table."""
    lines = tex_content.strip().split("\n")
    rows = []
    current_row = []

    for line in lines:
        line = line.strip()
        # Skip tabular environment markers and rules
        if any(line.startswith(cmd) for cmd in [
            "\\begin{tabular}", "\\end{tabular}",
            "\\toprule", "\\midrule", "\\bottomrule",
            "\\begin{longtable}", "\\end{longtable}",
        ]):
            if line.startswith("\\midrule") and current_row:
                rows.append(current_row)
                current_row = []
            continue

        if not line or line.startswith("%"):
            continue

        # Handle multiline rows (lines ending with \\)
        # Remove trailing \\ and hline
        clean = re.sub(r"\\\\.*$", "", line).strip()
        clean = re.sub(r"\\hline", "", clean).strip()

        if clean:
            current_row.append(clean)

        if "\\\\" in line:
            if current_row:
                rows.append(current_row)
                current_row = []

    if current_row:
        rows.append(current_row)

    if not rows:
        return ""

    # Parse cells from rows
    table_rows = []
    for row_parts in rows:
        combined = " ".join(row_parts)
        cells = [c.strip() for c in combined.split("&")]
        # Clean each cell
        cells = [clean_inline_latex(c) for c in cells]
        table_rows.append(cells)

    if not table_rows:
        return ""

    # Determine column count
    max_cols = max(len(r) for r in table_rows)
    # Pad rows
    for r in table_rows:
        while len(r) < max_cols:
            r.append("")

    # Build markdown table
    result = []
    result.append("| " + " | ".join(table_rows[0]) + " |")
    result.append("| " + " | ".join(["MDSEP"] * max_cols) + " |")
    for row in table_rows[1:]:
        result.append("| " + " | ".join(row) + " |")

    return "\n".join(result)


def inline_table(match_or_path):
    r"""Read and convert an \input{tables/...} reference."""
    if isinstance(match_or_path, str):
        path = match_or_path
    else:
        path = match_or_path.group(1)

    if not path.endswith(".tex"):
        path += ".tex"

    content = read_file(path)
    if not content:
        return f"*[Table: {path}]*"

    return convert_table_to_markdown(content)


def clean_inline_latex(text):
    """Clean inline LaTeX commands from text."""
    # \textbf{...}
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    # \textit{...}
    text = re.sub(r"\\textit\{([^}]*)\}", r"*\1*", text)
    # \emph{...}
    text = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", text)
    # \texttt{...}
    text = re.sub(r"\\texttt\{([^}]*)\}", r"`\1`", text)
    # \underline{...}
    text = re.sub(r"\\underline\{([^}]*)\}", r"\1", text)
    # \thead{...}
    text = re.sub(r"\\thead\{([^}]*)\}", r"**\1**", text)
    # \makecell{...}
    text = re.sub(r"\\makecell\{([^}]*)\}", r"\1", text)
    # \makecell[l]{...} etc
    text = re.sub(r"\\makecell\[[^\]]*\]\{([^}]*)\}", r"\1", text)
    # \text{...}
    text = re.sub(r"\\text\{([^}]*)\}", r"\1", text)
    # \mbox{...}
    text = re.sub(r"\\mbox\{([^}]*)\}", r"\1", text)
    return text


def extract_nested_braces(text, start):
    """Extract content within balanced braces starting at position start."""
    if start >= len(text) or text[start] != "{":
        return "", start
    depth = 0
    i = start
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return text[start + 1:], len(text)


def process_footnotes(text):
    """Convert \\footnote{...} to inline markdown footnotes.

    Handles nested braces properly.
    """
    result = []
    footnote_counter = [0]
    footnotes = []
    i = 0

    while i < len(text):
        # Look for \footnote{
        if text[i:].startswith("\\footnote{"):
            footnote_counter[0] += 1
            n = footnote_counter[0]
            content_start = i + len("\\footnote")
            content, end_pos = extract_nested_braces(text, content_start)
            result.append(f"[^{n}]")
            footnotes.append((n, content))
            i = end_pos
        else:
            result.append(text[i])
            i += 1

    return "".join(result), footnotes


def convert_latex_to_markdown(tex_content, chapter_title_override=None):
    """Convert a LaTeX chapter file to markdown."""
    text = tex_content
    footnotes_collected = []

    # Process footnotes first (before other transformations) to handle nested braces
    text, footnotes_collected = process_footnotes(text)

    # Remove comments (lines starting with %)
    text = re.sub(r"(?m)^%.*\n?", "", text)
    # Remove inline comments (but not \%)
    text = re.sub(r"(?<!\\)%.*$", "", text, flags=re.MULTILINE)

    # Remove \label{...}
    text = re.sub(r"\\label\{[^}]*\}", "", text)

    # Remove \phantomsection
    text = text.replace("\\phantomsection", "")

    # Remove \pageref and \nameref references
    text = re.sub(r"\\pageref\{[^}]*\}", "", text)
    text = re.sub(r"\\nameref\{([^}]*)\}", r"\1", text)

    # Remove \hypertarget
    text = re.sub(r"\\hypertarget\{[^}]*\}\{([^}]*)\}", r"\1", text)

    # Section references
    text = re.sub(r"Section~\\ref\{([^}]*)\}", r"the relevant section", text)
    text = re.sub(r"Table~\\ref\{([^}]*)\}", r"the table below", text)
    text = re.sub(r"Figure~\\ref\{([^}]*)\}", r"the figure", text)
    text = re.sub(r"Flowchart~\\ref\{([^}]*)\}", r"the flowchart", text)
    text = re.sub(r"Chapter~\\ref\{([^}]*)\}", r"the relevant chapter", text)
    text = re.sub(r"\\ref\{([^}]*)\}", r"", text)

    # Chapter headings
    if chapter_title_override:
        text = re.sub(r"\\chapter\{[^}]*\}", f"# {chapter_title_override}", text)
    else:
        text = re.sub(r"\\chapter\{([^}]*)\}", r"# \1", text)

    # Section headings (with optional short title [...]  )
    text = re.sub(r"\\section(?:\[[^\]]*\])?\{([^}]*)\}", r"## \1", text)
    text = re.sub(r"\\subsection(?:\[[^\]]*\])?\{([^}]*)\}", r"### \1", text)
    text = re.sub(r"\\subsubsection(?:\[[^\]]*\])?\{([^}]*)\}", r"#### \1", text)

    # Quoting environment → blockquote
    def convert_quoting(m):
        content = m.group(1).strip()
        lines = content.split("\n")
        return "\n".join("> " + line.strip() for line in lines if line.strip())

    text = re.sub(r"\\begin\{quoting\}(.*?)\\end\{quoting\}", convert_quoting, text, flags=re.DOTALL)

    # Helper to extract caption with nested braces
    def extract_caption(content):
        idx = content.find("\\caption")
        if idx < 0:
            return ""
        pos = idx + len("\\caption")
        # Skip optional argument [...]
        if pos < len(content) and content[pos] == "[":
            depth = 1
            pos += 1
            while pos < len(content) and depth > 0:
                if content[pos] == "[":
                    depth += 1
                elif content[pos] == "]":
                    depth -= 1
                pos += 1
        if pos < len(content) and content[pos] == "{":
            result, _ = extract_nested_braces(content, pos)
            return result
        return ""

    # Handle \input{tables/...} - inline the table content
    def handle_table_input(m):
        path = m.group(1)
        if not path.endswith(".tex"):
            path += ".tex"
        return inline_table(path)

    text = re.sub(r"\\input\{(tables/[^}]*)\}", handle_table_input, text)

    # Handle table environment wrapping \input
    def convert_table_env(m):
        content = m.group(0)
        # Find the table body (between centering and caption)
        body_match = re.search(r"\\centering\s*(.*?)\\caption", content, re.DOTALL)
        body = body_match.group(1).strip() if body_match else ""
        caption = clean_inline_latex(extract_caption(content))
        result = f"\n{body}\n"
        if caption:
            result += f"\n*{caption}*\n"
        return result

    text = re.sub(
        r"\\begin\{table\}\[?[^]]*\]?.*?\\end\{table\}",
        convert_table_env,
        text,
        flags=re.DOTALL,
    )
    # Remaining table environments
    text = re.sub(
        r"\\begin\{table\}.*?\\end\{table\}",
        lambda m: "\n*[Table]*\n",
        text,
        flags=re.DOTALL,
    )

    # Handle figures - extract caption
    def convert_figure(m):
        content = m.group(1)
        caption = clean_inline_latex(extract_caption(content))
        image_match = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", content)
        image_name = image_match.group(1) if image_match else ""

        parts = []
        if image_name:
            parts.append(f"![{caption}](images/{image_name})")
        if caption:
            parts.append(f"*{caption}*")
        return "\n" + "\n\n".join(parts) + "\n"

    text = re.sub(r"\\begin\{figure\}\[?[^]]*\]?(.*?)\\end\{figure\}", convert_figure, text, flags=re.DOTALL)

    # Handle flowcharts - extract caption
    def convert_flowchart(m):
        content = m.group(1)
        caption = clean_inline_latex(extract_caption(content))
        if not caption:
            caption = "Flowchart"
        return f"\n**Flowchart:** *{caption}*\n"

    text = re.sub(r"\\begin\{flowchart\}\[?[^]]*\]?(.*?)\\end\{flowchart\}", convert_flowchart, text, flags=re.DOTALL)

    # Handle remaining \input{figures/...} and \input{plots/...}
    text = re.sub(r"\\input\{figures/[^}]*\}", "", text)
    text = re.sub(r"\\input\{plots/[^}]*\}", "", text)

    # Description lists (glossary style)
    def convert_description(m):
        content = m.group(1)
        items = re.split(r"\\item\[", content)
        result = []
        for item in items:
            item = item.strip()
            if not item:
                continue
            # Find the closing bracket
            bracket_end = item.find("]")
            if bracket_end >= 0:
                term = item[:bracket_end].strip()
                desc = item[bracket_end + 1:].strip()
                result.append(f"**{term}**\n: {desc}")
            else:
                result.append(item)
        return "\n\n".join(result)

    text = re.sub(r"\\begin\{description\}(.*?)\\end\{description\}", convert_description, text, flags=re.DOTALL)

    # Itemize → bullet list
    def convert_itemize(m):
        content = m.group(1)
        items = re.split(r"\\item\s*", content)
        result = []
        for item in items:
            item = item.strip()
            if item:
                # Handle multi-line items
                item = " ".join(item.split())
                result.append(f"- {item}")
        return "\n".join(result)

    text = re.sub(r"\\begin\{itemize\}(.*?)\\end\{itemize\}", convert_itemize, text, flags=re.DOTALL)

    # Enumerate → numbered list
    def convert_enumerate(m):
        content = m.group(1)
        items = re.split(r"\\item\s*", content)
        result = []
        n = 0
        for item in items:
            item = item.strip()
            if item:
                n += 1
                item = " ".join(item.split())
                result.append(f"{n}. {item}")
        return "\n".join(result)

    text = re.sub(r"\\begin\{enumerate\}(.*?)\\end\{enumerate\}", convert_enumerate, text, flags=re.DOTALL)

    # Chemical formulas: \ch{CO2} → CO₂
    def convert_chem(m):
        formula = m.group(1)
        # Simple subscript numbers
        formula = re.sub(r"(\d+)", lambda n: ''.join(
            chr(0x2080 + int(d)) for d in n.group(1)
        ), formula)
        return formula

    text = re.sub(r"\\ch\{([^}]*)\}", convert_chem, text)

    # Units and quantities
    # \qty{100}{\degreeCelsius} → 100°C
    text = re.sub(r"\\qty\{([^}]*)\}\{\\degreeCelsius\}", r"\1°C", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\degF\}", r"\1°F", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\percent\}", r"\1%", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\gram\}", r"\1 g", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\kg\}", r"\1 kg", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\ml\}", r"\1 ml", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\hour\}", r"\1 hours", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{\\minute\}", r"\1 minutes", text)
    text = re.sub(r"\\qty\{([^}]*)\}\{[^}]*\}", r"\1", text)

    # \qtyrange{5}{10}{\degreeCelsius} → 5–10°C
    text = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{\\degreeCelsius\}", r"\1–\2°C", text)
    text = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{\\percent\}", r"\1–\2%", text)
    text = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{[^}]*\}", r"\1–\2", text)

    # \SI{...}{...}
    text = re.sub(r"\\SI\{([^}]*)\}\{\\percent\}", r"\1%", text)
    text = re.sub(r"\\SI\{([^}]*)\}\{\\gram\}", r"\1 g", text)
    text = re.sub(r"\\SI\{([^}]*)\}\{\\degreeCelsius\}", r"\1°C", text)
    text = re.sub(r"\\SI\{([^}]*)\}\{[^}]*\}", r"\1", text)
    text = re.sub(r"\\SI\{([^}]*)\}\{\}", r"\1", text)

    # \num{1500} → 1,500
    def format_num(m):
        val = m.group(1)
        try:
            n = int(val)
            return f"{n:,}"
        except ValueError:
            return val

    text = re.sub(r"\\num\{([^}]*)\}", format_num, text)
    # \numproduct{1400 x 0.6} → 1400 × 0.6
    text = re.sub(r"\\numproduct\{([^}]*)\}", lambda m: m.group(1).replace("x", "×"), text)

    # Inline formatting
    text = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    text = re.sub(r"\\textit\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\texttt\{([^}]*)\}", r"`\1`", text)
    text = re.sub(r"\\textsc\{([^}]*)\}", r"\1", text)

    # URLs
    text = re.sub(r"\\url\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", r"[\2](\1)", text)

    # Citations → remove or convert to simple reference
    text = re.sub(r"~?\\cite\*?\{([^}]*)\}", lambda m: f" [{m.group(1).replace('+', ' ')}]", text)

    # Non-breaking spaces and tildes
    text = re.sub(r"I~", "I ", text)
    text = text.replace("~", " ")

    # LaTeX dashes
    text = text.replace("---", "—")
    text = text.replace("--", "–")

    # Restore markdown table separators (protected from dash conversion)
    text = text.replace("MDSEP", "---")

    # \dots
    text = text.replace("\\dots", "…")
    text = text.replace("\\ldots", "…")

    # Backtick quotes ``...'' → "..."
    text = re.sub(r"``(.*?)''", r'"\1"', text)

    # Math mode $X$ → X
    text = re.sub(r"\$([^$]+)\$", r"\1", text)

    # \textsuperscript
    text = re.sub(r"\\textsuperscript\{([^}]*)\}", r"\1", text)
    # \textsubscript
    text = re.sub(r"\\textsubscript\{([^}]*)\}", r"\1", text)

    # \multicolumn{N}{...}{content}
    text = re.sub(r"\\multicolumn\{[^}]*\}\{[^}]*\}\{([^}]*)\}", r"\1", text)

    # \cmidrule and similar
    text = re.sub(r"\\cmidrule\([^)]*\)\{[^}]*\}", "", text)
    text = re.sub(r"\\cmidrule\{[^}]*\}", "", text)

    # \times → ×
    text = text.replace("\\times", "×")

    # \input{supporters.csv} and similar non-tex inputs
    text = re.sub(r"\\input\{[^}]*\.csv\}", "", text)

    # Remove stray tabular environments
    text = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", "", text, flags=re.DOTALL)

    # Remove \def commands
    text = re.sub(r"\\def\S*\s*", "", text)

    # Remove remaining LaTeX commands we don't need
    text = re.sub(r"\\centering\b", "", text)
    text = re.sub(r"\\noindent\b", "", text)
    text = re.sub(r"\\clearpage\b", "", text)
    text = re.sub(r"\\newpage\b", "", text)
    text = re.sub(r"\\bigskip\b", "", text)
    text = re.sub(r"\\medskip\b", "", text)
    text = re.sub(r"\\smallskip\b", "", text)
    text = re.sub(r"\\vspace\{[^}]*\}", "", text)
    text = re.sub(r"\\hspace\{[^}]*\}", "", text)
    text = re.sub(r"\\vfill\b", "", text)
    text = re.sub(r"\\par\b", "\n", text)
    text = re.sub(r"\\\\", "\n", text)
    text = re.sub(r"\\hline", "", text)
    text = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}", "", text)
    text = re.sub(r"\\setchapterstyle\{[^}]*\}", "", text)
    text = re.sub(r"\\setchapterimage(?:\[[^\]]*\])?\{[^}]*\}", "", text)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{[^}]*\}", "", text)

    # Remove remaining unknown \command{} patterns (conservative - only single-arg)
    text = re.sub(r"\\pHvalue\{([^}]*)\}", r"pH \1", text)

    # Catch-all: remaining \command{content} → content (run multiple times for nesting)
    for _ in range(3):
        text = re.sub(r"\\(?!begin|end)[a-zA-Z]+\{([^}]*)\}", r"\1", text)

    # Remove escaped special characters
    text = text.replace("\\&", "&")
    text = text.replace("\\%", "%")
    text = text.replace("\\$", "$")
    text = text.replace("\\#", "#")
    text = text.replace("\\_", "_")
    text = text.replace("\\{", "{")
    text = text.replace("\\}", "}")

    # Clean up excessive blank lines
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    # Clean up whitespace at end of lines
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # Add footnotes at the end
    if footnotes_collected:
        text = text.rstrip() + "\n\n---\n\n"
        for n, content in footnotes_collected:
            # Clean the footnote content too
            clean_content = content.strip()
            # Apply same inline conversions
            clean_content = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", clean_content)
            clean_content = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", clean_content)
            clean_content = re.sub(r"\\texttt\{([^}]*)\}", r"`\1`", clean_content)
            clean_content = re.sub(r"~?\\cite\{([^}]*)\}", lambda m: f" [{m.group(1).replace('+', ' ')}]", clean_content)
            clean_content = re.sub(r"I~", "I ", clean_content)
            clean_content = clean_content.replace("~", " ")
            clean_content = clean_content.replace("---", "—")
            clean_content = clean_content.replace("--", "–")
            clean_content = re.sub(r"\\qty\{([^}]*)\}\{\\degreeCelsius\}", r"\1°C", clean_content)
            clean_content = re.sub(r"\\qty\{([^}]*)\}\{\\percent\}", r"\1%", clean_content)
            clean_content = re.sub(r"\\qty\{([^}]*)\}\{[^}]*\}", r"\1", clean_content)
            clean_content = re.sub(r"\\SI\{([^}]*)\}\{[^}]*\}", r"\1", clean_content)
            clean_content = re.sub(r"\\url\{([^}]*)\}", r"\1", clean_content)
            clean_content = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{\\degreeCelsius\}", r"\1–\2°C", clean_content)
            clean_content = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{\\percent\}", r"\1–\2%", clean_content)
            clean_content = re.sub(r"\\qtyrange\{([^}]*)\}\{([^}]*)\}\{[^}]*\}", r"\1–\2", clean_content)
            clean_content = re.sub(r"\\textsuperscript\{([^}]*)\}", r"\1", clean_content)
            clean_content = re.sub(r"\\pageref\{[^}]*\}", "", clean_content)
            clean_content = re.sub(r"\\num\{([^}]*)\}", r"\1", clean_content)
            # Catch-all: remove remaining \command{content} → content
            clean_content = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", clean_content)
            text += f"[^{n}]: {clean_content}\n\n"

    return text.strip() + "\n"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_content = []
    all_content.append("# The Sourdough Framework\n")
    all_content.append("**By Hendrik Kleinwächter**\n")
    all_content.append("*An open-source guide to making sourdough bread at home.*\n\n")
    all_content.append("---\n\n")

    # Generate table of contents
    all_content.append("## Table of Contents\n\n")
    for i, (tex_path, md_name) in enumerate(CHAPTERS):
        title = md_name.replace(".md", "").split("-", 1)[-1].replace("-", " ").title()
        all_content.append(f"{i + 1}. [{title}](#{title.lower().replace(' ', '-')})\n")
    all_content.append("\n---\n\n")

    for tex_path, md_name in CHAPTERS:
        print(f"Converting: {tex_path} → {md_name}")
        tex_content = read_file(tex_path)
        if not tex_content:
            print(f"  Skipping (empty or not found)")
            continue

        # For troubleshooting/misc.tex, prepend the chapter heading
        title_override = None
        if tex_path == "troubleshooting/misc.tex":
            title_override = "Troubleshooting"

        md_content = convert_latex_to_markdown(tex_content, title_override)

        # Write individual chapter file
        out_path = os.path.join(OUTPUT_DIR, md_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"  Written: {out_path}")

        all_content.append(md_content)
        all_content.append("\n\n---\n\n")

    # Write combined file
    combined_path = os.path.join(OUTPUT_DIR, "the-sourdough-framework.md")
    with open(combined_path, "w", encoding="utf-8") as f:
        f.write("\n".join(all_content))
    print(f"\nCombined file written: {combined_path}")

    # Also write a metadata/summary file for AI consumption
    meta_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write("""# The Sourdough Framework — Markdown Edition

This directory contains a markdown conversion of **The Sourdough Framework**
by Hendrik Kleinwächter, converted from the original LaTeX source.

## Files

- `the-sourdough-framework.md` — Complete book in a single file (best for AI/LLM use)
- Individual chapter files (`00-preface.md` through `15-glossary.md`)

## About

The Sourdough Framework is an open-source book that provides a scientific
foundation for understanding sourdough baking. Rather than providing recipes,
it teaches the *why* behind each step of the bread-making process.

## Topics Covered

1. **History** — The history of sourdough and bread making
2. **How Sourdough Works** — Enzymatic reactions, yeast, and bacteria
3. **Sourdough Starter** — Creating and maintaining a starter, baker's math
4. **Starter Types** — Liquid vs stiff starters, conversions
5. **Flour Types** — Understanding different flours and their properties
6. **Bread Types** — Overview of different bread varieties
7. **Wheat Sourdough** — Complete guide to freestanding wheat sourdough
8. **Non-Wheat Sourdough** — Working with rye, spelt, and other grains
9. **Mix-ins** — Adding seeds, nuts, fruits, and other ingredients
10. **Baking** — The science of baking, steaming, and oven techniques
11. **Storing Bread** — Proper storage methods
12. **Troubleshooting** — Common problems and solutions
13. **Glossary** — Definitions of bread-making terms

## License

Original work licensed under CC-BY-SA.
Source: https://github.com/hendricius/the-sourdough-framework
""")
    print(f"README written: {meta_path}")


if __name__ == "__main__":
    main()
