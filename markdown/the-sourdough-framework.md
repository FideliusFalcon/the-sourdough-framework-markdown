# The Sourdough Framework

**By Hendrik Kleinwächter**

*An open-source guide to making sourdough bread at home.*


---


## Table of Contents


1. [Preface](#preface)

2. [Acknowledgments](#acknowledgments)

3. [History](#history)

4. [How Sourdough Works](#how-sourdough-works)

5. [Sourdough Starter](#sourdough-starter)

6. [Sourdough Starter Types](#sourdough-starter-types)

7. [Flour Types](#flour-types)

8. [Bread Types](#bread-types)

9. [Wheat Sourdough](#wheat-sourdough)

10. [Non Wheat Sourdough](#non-wheat-sourdough)

11. [Mix Ins](#mix-ins)

12. [Baking](#baking)

13. [Storing Bread](#storing-bread)

14. [Troubleshooting](#troubleshooting)

15. [Crumb Structures](#crumb-structures)

16. [Glossary](#glossary)


---


# Preface


If there is one food Germany is known for, it is probably bread.
There are thousands of varieties in Germany,
and making it has been an integral part of our culture.

My bread journey began during childhood. My mother, being a parent
of 3, would always use Saturdays to bake a delicious loaf for the family.
It was a white fluffy sandwich bread, and she made it within one to two hour using store-bought yeast.
Being a bit more experienced, I now realize it's
ideal to wait a little while before cutting into your bread, but back then,
we kids couldn't wait. Mom would cut for us a few slices straight from the oven, and we would
immediately proceed to pour butter or jam on each slice. Within minutes,
one kilogram of flour would be consumed. Bread became an integral part of my
weekly food.

I was lucky that my parents could afford a yearly ski trip to
Alto Adige in northern Italy. In the small town called Valdaora, we
would try new restaurants every year, yet always end up in our favorite
pizza place. The pizzas there were incredible. The dough
alone was so tasty that we would order just the bread with a
bit of olive oil and salt.

Of course, my question would always be, "Mom, can we make this at home, too, please?"
So over the years, we became friends with the owners and would receive
more and more clues as how to make the perfect pizza dough. There
are no secret ingredients inside. It's just flour, water, salt, and a bit of yeast.
How can such a simple combination of ingredients create such an incredibly delicious
pizza dough? My parents, being creatures of habit, would return every year with us,
and every year, my interest would grow. At home, Mom and I attempted to replicate
the recipe. We tried baking on a stone and on a steel. We tried adding oil to the dough and herbs
to the pizza sauce. We fell into an endless cycle of experiments. However, we never managed
to get close to the experience we had while on vacation.

Some years passed, and I eventually began my studies in the small German city of Göttingen.
For the first time, I was faced with shopping for my own bread. It was never
on my mind to actually start baking it for myself. I would just buy
a good loaf while shopping at the supermarket. My favorite variety
was a *Schwarzbrot: Korn an Korn*. It’s a very dark and hearty rye bread
with added berries and sunflower seeds.

Being a little naïve, I'd never before examined the packaging of what I was
buying. One day, that changed.  I looked at the label and was shocked. The
seemingly
healthy bread consisted of so many other things aside from flour and water.
The black color was not coming from the flour, but from caramelized sugar.
The packaging stated it was a sourdough bread, but then why was there additional yeast?
I thought that if it was really sourdough, it shouldn't require additional
yeast. I soon
realized that something was wrong with the bread I was buying.
I proceeded to check the other supermarket breads, only to discover that they, too,
contained ingredients I'd never heard of. That was the day I lost trust
in supermarket bread.

At home, I decided to research the proper way to make bread, and much to my surprise,
I learned that the recipes for making pizza and bread were actually quite similar, yet
there were also differences. For example, some recipes would call for fresh yeast, while
others would call for dry. Diving deep into various online forums and all their many
discussions, I became even more confused.
I tried using different flours and different brands, all in both organic and non-organic varieties.
I realized then that I knew nothing about making bread. Recipes would often contradict each other,
leaving me further confused. They seemed like little more than a collection of apparently random
steps to follow. The baking instructions and temperatures too were all
different…

Meanwhile, having completed my studies, I started work as an engineer.
We engineers are faced with many challenges. The compiler or runtime is
always screaming at you with errors, and it's your job to figure out how to fix them.
It can take hours, sometimes days, just to fix a simple problem. If you want
to become a software engineer, you have to develop a certain "never-give-up" attitude.

When writing code, software engineers often need to use a set of pre-made routines. These routines have been
written by other engineers and can then be used to ship code faster.
This pre-written code is commonly known as *a framework*. In many cases,
these frameworks are not built by a single person but by engineers from all around the world,
each of whom can help by improving and changing the source code. Frameworks have made many successful
businesses possible.
In most cases, frameworks do exactly what they claim they do. However,
sometimes you are faced with issues you don't understand. In 99.95%
of all software bugs, the developer is the issue. Sometimes, however, the framework has a
bug. That is when the developer must dig deeper to see the *what* and the
*why* behind what
the framework is doing. You will need to read other engineers' source code, and you will be forced
to understand *why* things are happening.

Being unhappy with what I was baking, my engineering mindset took over, and
I had to do my own deep dive to understand what was going on. Much to my
surprise, however, none of the recipes I'd encountered would tell me
*why* I should use amount X of water and amount Y of flour, or
*why* exactly I should use fresh yeast over dry yeast. Why should I slap
my dough while kneading it on the counter? Why is a stand mixer better than
kneading by hand? Why should I let the dough sit for this long?  Why is
steaming the dough during baking important? Do I really need to get myself an
expensive Dutch oven to bake bread?  The problem compounded when I started
reading about sourdough. It all sounded like black magic. Why were some
sourdoughs made from fruits, while others were made from flour?  Why should
one recipe use wheat while another used rye or spelt? How often should the
sourdough be fed? The questions I had then could have filled 20 pages. I was
confused, but I became even more determined to learn how decent bread should
be made at home.

The feedback I received from friends helped me to improve with each
iteration of homemade bread. Compared to coding, where you sometimes have to wait months
for this feedback, bread making is much more direct. Plus, you can eat your successes
(and failures!) And, much to my surprise, even those failures started tasting better than
most store-bought breads. Eating a homemade bread that takes you hours to make allows you
to develop a different relationship with your food, and baking bread from scratch with my
bare hands was a welcome change after hours of working on the computer.

I continued learning about the process of fermentation and various techniques of bread making.
I approached the topic of sourdough in a manner similar to software, and after years of
researching and documenting my progress, I decided it was time to share that progress with the
world.
When working on software projects, it is important to see their history and how the source
code changes over time. This way, you can easily jump back to previous versions. This was
the perfect tool for documenting my recipes, because they, too, would change with each
subsequent iteration. Much to my surprise, my open source work on sourdough was appreciated
by other engineers, and the project became popular on the website GitHub, originally built to
share open source software.

Now, when baking great bread, you also need to learn certain techniques. I figured it would be
easier to share these techniques in video form. Thus, my YouTube channel was born. I chose
the name `The Bread Code` to capture my engineering-oriented approach to bread. It took some
time to get it right, but after choosing more engaging thumbnails and titles for
the videos I made, the channel started gaining viewers.
Finally, three years later, I dedicate two days each week to follow my bread baking passion, while
the other three days I continue to work as a software engineer, writing code on a day-to-day
basis.

My bread days fill me with both joy and passion. To me, there is nothing better than seeing
how many people have made amazing bread thanks to my tips and explanations. The community has
continued to grow, spawning many interesting discussions and ideas surrounding the topic of
bread making. There is always something new to learn, and I feel that even now I am just barely
scratching the surface with what I know and teach. Would you ever have imagined that fruit
flies are like bees and are part of the wild yeast's success story? I made a video where
I tried to cultivate wild yeast spores coming from fruit flies in order
to bake bread. It worked; the bread turned out amazingly well and even tasted good! These kinds of
experiments spark my natural interest. Conducting them and seeing how other people share my
interest makes me incredibly happy.

The problem with running a YouTube channel is that all the information
you see is filtered and then provided to you through an algorithm. I am concerned
with how algorithms are shaping modern information, because they tend to
put users into certain categories where they will then only see news related to
those same fixed categories. A key metric determining visibility of your channel is how many
people have clicked on a video after it's been shown, and the content you create
is not even shown to every subscriber of your channel. If the algorithm determines the video
is not engaging enough, your content starts to decay in YouTube's nirvana. Even if your video
goes viral, the algorithm will stop showing it once engagement rates with new users goes down,
and older videos fade over time as the decay punishment factor increases. I know, because
I have developed similar algorithms myself as a software engineer.

I've since decided to take some time off from the algorithm cycle to work on something more
long term and meaningful. My mission has always been to share my knowledge with as many people
in the world as possible. That's also why my content has been provided in English rather than
German. After discussions with members of the community, I figured that writing a book could
help me achieve that goal. Most of the books that exist today are collections of recipes. My
idea, however, is to provide you with a deeper foundation of knowledge that you can use to
follow other recipes.
In software terms, this would be a *bread framework*.

It is my goal for this book to help everyone facing issues with flour, fermentation, baking,
and more. It should provide a detailed understanding as to why certain steps are necessary
and how to adapt them when things go wrong while making bread.
It is my desire for this knowledge to be accessible to everyone around the world, regardless
of budget, and as such, I do not want to charge for the book. That's why I've decided to make
it open source and have asked the community to support my work with
donations. The community's feedback has been amazing so far, and
I've already raised much more money than initially expected. The digital version of this book
will always remain free. There is also a hardcover version of the book available for purchase.
You can read more details here: https://breadco.de/physical-book

In this book, I will try to be as scientific as possible. I in no way claim, however, that
it will itself be a work of science. I have conducted several experiments that I will write
about here, but to truly call this science, you would probably need to repeat the same experiment
a thousand times in a lab environment, which I have not done. I will do my best, however, to provide
scientific references where possible and to clearly distinguish between facts and personal opinion.

I hope you have fun reading this and that you learn more about the fascinating world of bread
making, and it is my sincere wish that this work provides you with the solid toolchain that I wish
I'd had access to when starting my own journey with bread.

Thank you.

Hendrik



---


# Acknowledgments

This book would not have been possible without your help.
With all your donations I have been able to focus on finishing
this book. Your continuous support allows me to focus
on improving this book even more.

Furthermore many of you have contributed and improved the
instructions, fixed spelling mistakes and/or provided
feedback on the content. Each of you has made this book
better.

By providing this book free of charge,
we can enable more people around the world to bake delicious sourdough
bread at home.

Thank you very much for your support!


**Big shout-out to all the initial supporters who helped launching this
project:
**



---


# The history of sourdough

> We will start this book by briefly talking about the long history of
> sourdough bread from ancient time, and how people used similar process for
> other food like beer. The discovery of yeast and how, together with
> machine development, revolutionized bread making.  More recently
> communities formed around sourdough and home baking, trying to relearn
> lessons from the past.

The story of sourdough bread begins in prehistoric oceans. These oceans were the
birthplace of all life on Earth. To better envision the vast history of
our planet, lets create a timeline in one year/365 days. On this scale,
January 1 signifies Earth's
formation 4.54 billion years ago. Midnight on December 31 is the present.
Each day represents roughly 12 million years. This technique simplifies the
complexity of time but also renders the extraordinary expanse of our planet's
history into a more graspable timeframe. We humans, are in fact a recent
addition to our planet, so young that we made our first appearance on
the evening of December 31.  It seems that humans managed to arrive just
in time to join the celebration at the end of the year.

On March 25, the oceans birthed the first single-celled bacteria. In these
waters, another single-celled life form, *archaea*, also thrived. These
organisms inhabit extreme environments, from boiling vents to icy waters.


*Timeline of significant events
    starting from the first day of Earth's existence,
    divided into months, and extending to the present day,
    marked at midnight. This visualization shows the pivotal steps
    of life and sourdough on earth.*


Whoever comes first, bacteria or archaea, remains debated. For three
months (or approximately 1.1 billion years), these life forms dominated
the oceans. Then, on June 25 in a highly unlikely event, an archaeon consumed a bacterium.
Instead of digesting it, they formed a symbiotic relationship. This led to the
first nucleated organisms, marking an evolutionary milestone. This event lead
to the development of plants, fungi and also ultimately humans.

Life stayed aquatic for another three months.
On October 4, bacteria first colonized land. By October 15, the
first aquatic fungi appeared. They adapted and, by November 24, had colonized
land.

By December 3, yeasts emerged on land. This laid groundwork for bread-making.
Jump 140 million years to December 14, and dinosaurs arose. Just a couple
of days after their appearance on December 17 the super continent Pangea
started to rift apart, reshaping the continents into their current form.
The dinosaurs reigned until December 29 when they faced extinction.
Another 25 million years later, or our timeline's 2 days after the dinosaur
extinction, humans appeared.

A few hours later after the arrival of humans, a more subtle culinary
revolution was unfolding. By 12,000 BC, just 5 seconds before our
metaphorical midnight, the first sourdough breads were being baked in ancient
Jordan. A blink of an eye later, or 4 seconds in our time compression,
Pasteur's groundbreaking work with yeasts set the stage for modern
bread-making. From the moment this book began to take shape to your current
reading, only milliseconds have ticked by [Yong 2017].

Now delving deeper into the realm of sourdough, it can likely be traced to aforementioned
Ancient Jordan [jordan bread]. Looking at the earth's timeline sourdough
bread can be considered a very recent invention.


*Timeline of significant discoveries and
  events leading to modern sourdough bread.*


The exact origins of fermented
bread are, however, unknown. One of the most ancient preserved
sourdough breads has been excavated in Switzerland [switzerland bread].


![An ancient Einkorn flatbread. Note the
      dense crumb structure.](images/einkorn-crumb)

*An ancient Einkorn flatbread. Note the
      dense crumb structure.*


Another popular story is that a lady in Egypt was making
a bread dough close to the Nile river. The lady forgot the
dough and at her return a few days later, she noticed that the dough had
increased in size and smelled funky. She decided to bake
the dough anyway and was rewarded with a much
lighter, softer, better tasting bread dough. From that day
on she continued to make bread this way [egyptian bread].

Little did the people back then know that tiny microorganisms
were the reason the bread was better. It is not clear when
they started using a bit of the dough from the previous
day for the next batch of dough. But by doing so, sourdough
bread making—as we know it today—was born: Wild yeast
in the flour and in the air, with bacteria
starting to decompose the flour-water mixture.
The yeast makes the dough fluffy,
and the bacteria primarily creates acidity. The different
microorganisms work in a symbiotic relationship. Humans
appreciated the enhanced airy structure and slight acidity
of the dough. Furthermore, the shelf life of such bread
was extended due to the increased acidity.

Quickly, similar processes were discovered when brewing beer
or making wine. A small tiny batch of the previous production
would be used for the next production. In this way, humans created
modern bread yeasts, wine yeasts, and beer yeasts [egypt beer].

Over time with each batch, the yeasts and bacteria
would become better at consuming whatever they were thrown at.
By feeding your sourdough starter, you are selectively breeding
microorganisms that are good at eating your flour. With
each iteration, your sourdough knows how to better ferment the flour
at hand. This is also the reason[^1] why more mature sourdough starters sometimes tend to
leaven doughs faster [review of sourdough starters].  The sourdough in
itself is a symbiotic relationship, but the sourdough
also adapted to humans and formed a symbiotic relationship with us.
For food and water, we are rewarded with delicious bread. In exchange,
we shelter and protect the sourdough. Spores from the starter
are spread through aerial contamination or insects like fruit flies.
This allows the sourdough starter to spread its spores even
further all around the world.

Evidence suggests early grain grinding in northern Australia around
60,000 BC, notably at the Madjedbebe rock shelter in Arnhem
Land [aboriginal grinding stones].  However, a more significant
advancement occurred later, as documented by the ancient Greek geographer
Strabo in 71 BC\@.  Strabo's writings described the first water-powered
stone mill, known as a *gristmill*. These mills advanced flour production
from a few kilograms up to several metric tons per day [history mills].

These early mills featured horizontal paddle wheels, eventually termed
*Norse wheels* due to their prevalence in Scandinavia.  The paddle wheels
connected to a shaft, which, in turn, linked to the central runner stone for
grinding. Water flow propelled the paddle wheels, transferring the grinding
force to the stationary *bed*, typically a stone of similar size and
shape. This design was straightforward, avoiding the need for gears. However,
it had a limitation: the stone's rotation speed relied on water volume and
flow rate, making it most suitable for regions with fast-flowing streams,
often found in mountainous areas [mills scandinavia].

In the year 1,680, a remarkable scientist by the name of
Antonie van Leeuwenhoek introduced a groundbreaking innovation that would
forever alter our understanding of the microscopic world and ultimately bread
making.  Van Leeuwenhoek, a master of lens craftsmanship, possessed an
insatiable fascination with realms invisible to the naked eye. His pioneering
work birthed the first modern microscope.  What set Van Leeuwenhoek apart was
the exceptional quality of his lenses, capable of magnifying tiny
microorganisms by an astounding factor of 270.  Driven by an unrelenting
curiosity to unveil the unseen, he embarked on a journey of exploration. He
scrutinized flies, examined lice-infested hair, and ultimately turned his gaze
toward the tranquil waters of a small lake near Delft.

In this serene aquatic habitat, he made astonishing observations, discovering
algae and minuscule, dancing creatures hitherto hidden from human perception.
Eager to share his revelatory findings with the scientific community,
Van Leeuwenhoek faced skepticism, as it was difficult to fathom that someone
had witnessed thousands of diminutive, dancing entities—entities so tiny that
they eluded the human eye.

Undeterred by skepticism, he continued his relentless pursuit of the unseen,
directing his lens towards a brewer's beer sludge. In this obscure medium,
Van Leeuwenhoek made history by becoming the first human to lay eyes upon
bacteria and yeast, unraveling a previously concealed world that would
revolutionize our understanding of microbiology [Yong 2017 Leeuwen].

At the same time brewers would start to experiment with utilizing the muddy
leftovers of the beer fermentation to start making doughs. They would notice
that the resulting bread doughs were becoming fluffy and compared
to the sourdough process would lack the acidity in the final product.
A popular example is shown in a report from 1,875. Eben Norton Horsford
wrote about the famous *Kaiser Semmeln* (Emperor's bread rolls).
These are essentially bread rolls made with brewer's yeast instead
of the sourdough leavening agent. As the process is more expensive,
bread rolls like these were ultimately consumed by the noble people
in Vienna [vienna breadrolls].

Industrialization of the grist milling process, starting in the late
18th century with Oliver Evans (1,785) and his mill
designs for continuous hands-off flour production [evans mill], and
evolving to steam-powered mills, made possible significant advancements in
bread production.


![A bread made over the stove without an oven.](images/sourdough-stove)

*A bread made over the stove without an oven.*


The biggest advancement of industrial bread making happened in 1,857.
The French microbiologist Louis Pasteur discovered the process of alcoholic
fermentation. He would prove that yeast microorganisms are the reason for
alcoholic fermentation and not other chemical catalysts. He continued with his
research and was the first person to isolate and grow pure yeast strains.
Soon later in 1,868 the Fleischmann brothers Charles and Maximilian were
the first to patent pure yeast strains for bread making. The yeasts offered
were isolated from batches of sourdough. By 1,879 the machinery was built
to multiply the yeast in large centrifuges [fleischmann history].  The
pure yeast would prove to be excellent and turbocharged at leavening bread
doughs. What would previously take 10 hours to leaven a bread dough could now
be done within 1 hour.  The process became much more efficient. What
ultimately made making large batches of dough possible, was the invention of
the electrical kneader.  Rufus Eastman, an American inventor, is often
credited with an important advancement in mixer technology. In 1,885, he
received a patent for an electric mixer with a mechanical hand-crank
mechanism.  This device was not as advanced or as widely adopted as later
electric mixers, but it was an early attempt to mechanize mixing and kneading
processes in the kitchen using electricity.  Eastman's invention represented
an important step in the development of electric mixers, but it wasn't as
sophisticated or popular as later models like the KitchenAid mixer. The
KitchenAid mixer, introduced in 1,919, is often recognized as one of the
first widely successful electric mixers and played a significant role in
revolutionizing kitchen appliances for home
cooks [first mixer] [kitchenaid history].

During World War II the first packaged dry yeast was developed. This would
ultimately allow bakeries and home bakers to make bread much faster and more
consistently. Thanks to pure yeast, building industrial bread making machines
was now possible. Provided you maintain the same temperature, same flour and
yeast strains fermentation became precisely reproducible. This ultimately led
to the development of giga bakeries and flour blenders. The bakeries demanded
the same flour from year to year to bake bread in their machines.  For this
reason, none of the supermarket flour you buy today is single origin.  It is
always blended to achieve exactly the same product throughout the years.

Modern wheat, specifically the high-yielding and disease-resistant varieties
commonly grown today, began to be developed in the mid-20th
century. This period is often referred to as the *Green Revolution.*

One of the key figures in this development was American scientist Norman
Borlaug, who is credited with breeding high-yield wheat varieties,
particularly dwarf wheat varieties, that were resistant to diseases and could
thrive in various environmental conditions. His work, which started in the
1940s and continued through the 1,960s, played a crucial role in
increasing wheat production worldwide and alleviating food
shortages [green revolution].

As fermentation
times sped up, the taste of the final bread would deteriorate.
The sprouting process induced by certain enzymes is essential
to developing a fluffier texture and better tasting crust. This
can't be indefinitely sped up. Soon bakeries would start
to introduce additional enzymes to achieve similar properties
to sourdough bread in yeast-based doughs. Sourdough almost completely
vanished from the surface of the Earth. Only a handful
of true nerds would continue making bread with sourdough.

Suddenly people started to talk more often about celiac disease
and the role of gluten. The disease isn't new; it has first
been described in 250 AD [coeliac disease]. People
would note how modern bread has much more gluten compared
to ancient bread. The bread in ancient times probably was much flatter.
The grains over time have been bred more and more towards containing a higher
amount of gluten. Gluten is a protein that gives modern
bread its typical soft fluffy crumb structure. The
gluten proteins bind together once activated with water.
Throughout the course of the fermentation, CO₂ is trapped
in this protein matrix. The tiny created chambers expand
during the baking process. As the dough gelatinizes while
being heated, the structure is fortified. This makes the bread appear
soft and fluffy when tasting it. Similar to drinking raw cow's milk,
your immune system might react to the consumed proteins.
There is gluten intolerance
and celiac disease. When people say they don't handle
gluten well, it's mostly a gluten intolerance they describe.
Some people describe similar issues when consuming
too much lactose. If you eat a long-fermented cheese
however, most of the lactose has been fermented by
the tiny microorganisms. People would investigate and
note how sourdough bread can typically be handled better
compared to plain, fast-made factory bread. The
reason for this is that enzymes take time to work the dough.
Gluten is a storage protein of flour. Once
sprouting is activated by adding water, the protease
enzyme starts to convert the gluten into tinier amino acids
that are required for sprouting. Over time you are effectively
losing gluten as it's naturally broken down. Furthermore,
traditionally lactic acid bacteria would start to decompose
the flour-water mix. Almost everything is recycled in nature.
Part of their diet is to consume the proteins in the dough.
Modern bread is faster and no longer has lactic acid bacteria.
Both factors together mean that you are consuming products
with a much higher gluten value compared to ancient times
when natural fermentation was used [raffaella di cagno].

During the California Gold Rush, French bakers brought the sourdough
culture to Northern America. A popular bread became the
San Francisco sourdough. It's characterized by its unique
tang (which was previously common for every bread). It
however remained more of a niche food while industrial bread
was on the rise. What really expedited
the comeback of sourdough was the 2,020 COVID-19 pandemic.
Flour and yeast became scarce in the supermarkets. While
flour returned yeast couldn't be found. People started
to look for alternatives and rediscovered the ancient
way of making sourdough bread. Soon many realized
that making sourdough bread is more complex than modern
yeast-based bread. You need to maintain a sourdough starter
and have it in ideal shape to properly ferment your dough.
Furthermore, compared to a yeast-based dough, you can't just
punch the dough down and let the fermentation continue.
You can overferment your dough, resulting in a sticky
dough mess. This complexity led to many bakers looking
for help and many thriving communities formed around
the topic of homemade bread.

When interviewing Karl de Smedt (owner of the Sourdough
Library) he said something that changed my way of thinking
about bread: ``The future of
modern bread is in the past [interview karl de smedt].''

---

[^1]: It is crazy if you think about it.
People have been using this process despite not knowing what was going on for
thousands of years!



---


# How sourdough works

> In this chapter, we will cover the basics of how sourdough ferments.
> First, we will look at the enzymatic reactions that take place
> in your flour the moment you add water, triggering the fermentation
> process. Then, in order to understand this process better, we will
> learn more about the yeast and bacterial microorganisms involved.


![How amylases and proteases
      interact with flour.](images/infographic-enzymes)

*How amylases and proteases
      interact with flour.*


## Enzymatic reactions

To understand the many enzymatic reactions that take place when flour
and water are mixed, we must first understand seeds and their role in
the life cycle of wheat and other grains.

Seeds are the primary means by which many plants, including wheat,
reproduce. Each seed contains the embryo of another plant, and must
therefore contain all the nutrients that new plant requires to grow.

When the seed is dry, it is in hibernation mode and can sometimes be
stored for several years. The moment it comes into contact with water,
however, it begins to sprout. The seed turns into a germ, requiring the
stored nutrients to be converted into something the plant can use while
it grows. The catalyst that makes the associated reactions possible is water.

The seed typically contains the first prototypical leaves of the plant,
and it can put down roots using the stored nutrients inside. Once those leaves
break through the soil and come into contact with the sunlight above, they
begin to photosynthesize. This process is the plant's engine, and with the
energy photosynthesis produces, the plant can continue to grow more roots,
enabling it to access additional nutrients from the soil. These additional
nutrients allow the plant to grow more leaves, increasing its photosynthetic
activity so that it can thrive in its new environment.

Of course, a ground flour can no longer sprout. But the enzymes that
trigger this process are still present. That's why it's important not to
mill grains at too high a temperature, as doing so could damage some of
these enzymes[^1].

Normally, the grain seed shields the germ against pathogens. However, as the
grain is ground into flour, the contents of the seed are exposed. This is ideal
for our sourdough microorganisms.

Neither the yeast nor the bacteria can prepare their own food. However, as
the enzymes are activated, the food they need becomes available, allowing them
to feed and multiply.

The two main enzymes involved in this process are *amylase* and
*protease*. For reasons that will soon be made clear, they are of the
utmost importance to the home baker, and their role in the making of sourdough
is a key puzzle piece to making better-tasting bread.

### Amylase

Sometimes, when you chew on a potato or a piece of bread for a long period
of time, you'll perceive a sweet flavor on your tongue. That's because your
salivary glands produce amylase. Amylase breaks down complex starch molecules
into easily-digestible sugars. Your body uses amylase to start the digestive
process. The germ works similarly by using the same enzyme. The amylase
is used to create sugars out of the starch to then produce more plant matter.

Normally,
the microorganisms on the surface of the grain can't consume the freed maltose
molecules, which remain hidden inside the germ. But as we grind the flour, a
feeding frenzy takes place.  Generally, the warmer the temperature, the faster
this reaction occurs. However, it takes time for the amylase
to break down most of the starch into simple sugars—which are not only
consumed by the yeast but are also
essential to the *Maillard reaction*—responsible for
enhanced browning during the baking process.
That's why a long fermentation is key to making great bread.

If you're a hobby brewer, you'll know that it's important to keep your beer at
certain temperatures to allow the different amylases to convert the contained
starches into sugar [beer amylase]. This process is so important that
there's a frequently used test to determine whether or not all the starches
have been converted.
This test, called the *Iodine Starch Test*, involves mixing iodine into
a sample of your brew and checking the color. If it's blue or black, you know
you still have unconverted starches. I wonder if such a test would also work
for bread dough?

Industrial bakers who add especially active yeast to produce bread in a short
period of time face a similar issue. Their approach is to add malted flour to
the dough, this malted flour contains many enzymes and thus speeds up the
fermentation process. The next time you're at the supermarket, check the
packaging of the bread you buy. If you find *malt* in the list of
ingredients, chances are this strategy was used.

Note that there are actually two categories of malt. One is *enzymatically
active malt*, which has not been heated to above  70°C, where the amylases begin
to degrade. The other is *inactive malt*, which has been heated to higher
temperatures and thus has no impact on your flour.

### Protease

Just as amylase breaks starches down into simple sugars, protease breaks
complex proteins down into simpler proteins and amino acids. Because wheat
contains gluten, a protein that's essential to the structure of bread,
protease necessarily plays a crucial role in the baking of sourdough.

Since the grain seeds require smaller amino acids to build roots and other
plant materials, the gluten in those seeds will begin to break down the moment
they sprout, and since adding water to flour activates those same enzymes,
the same process occurs in bread dough.

If you've ever tried to make a wheat-based dough and kept it at room
temperature for several days, you'll have discovered for yourself that the
gluten network breaks down to the point that the dough can no longer hold together. Once
this happens, the dough easily tears, holds no structure, and is no
longer suitable for baking bread.

This happened to me once when I tried to make sourdough directly from a dried
starter. At three to four days, the fermentation speed was so slow that the
gluten network broke down. The root cause for this issue was protease.
By adding water to your dough, you activate the protease, and this gets to work
in readying amino acids for the germ.

Here's another interesting experiment you can try to better visualize the
importance of protease: Make a fast-proofing dough using a large quantity
of active dry yeast. In 1–2 hours, your dough should have leavened and
increased in size. Bake it, then examine the crumb structure. You should see
that it's quite dense and nowhere near as fluffy as it could have been. That's
because the protease enzyme wasn't given enough time to do its job.

At the start, while kneading, a dough becomes elastic and holds together very
well. As that dough ferments, however, it becomes more loose and
extensible [protease enzyme bread]. This is because some of the gluten
bonds have
been broken down naturally by the protease through a process known as
*proteolysis*. This is what makes it easier for the yeast to inflate the
dough, and it's why a long fermentation process is critical when you want to
achieve a fluffy, open crumb with your sourdough bread.

Aside from using great ingredients, the slow fermentation process is one of the
main reasons Neapolitan pizza tastes so great: because the protease creates an
extensible and easy-to-inflate dough a soft and airy edge is achieved.

Because the fermentation process typically takes longer than 8 hours, a
flour with a higher gluten content should be used. This gives the dough more
time to be broken down by the protease without negatively affecting its
elasticity. If you were to use a weaker flour, you might end up with a dough
that's broken down so much that it tears during stretching, making it
impossible, for example, to shape it into a pizza pie.

Traditionally, pizza has been made with sourdough, but in modern times it is
made with active dry yeast. As the dough stays good for a longer period of time
it is much easier to handle on a commercial scale. If you were to use
sourdough, you might have a window of thirty to ninety minutes before the dough
begins to deteriorate, due to both the protease acting for a longer period
of time and the byproducts of bacteria, which we'll discuss in more detail later
in this chapter.

### Improving enzymatic activity

As explained previously, malt is a common trick used to speed up enzymatic
activity. Personally, however, I prefer to avoid malt and instead use a
trick I learned while making whole-wheat breads.

When I first started making whole-wheat bread, I could never achieve the
crust, crumb, or texture I desired no matter what I tried. Instead, my dough
tended to overferment rather quickly. When using a white flour with a similar
gluten content, however, my bread always turned out great.

At the time, I utilized an extended autolyse, which is just a fancy word for
mixing flour and water in advance and then letting the mixture sit. Most
recipes call for it as the process gives the dough an enzymatic head start,
and in general it's a great idea. However, as an equally effective
alternative, you could simply reduce the amount of leavening agent used—in
the case of sourdough, this would be your starter. This would allow the same
biochemical reactions to occur at roughly the same rate without requiring you
to mix your dough several times. My whole-wheat game improved dramatically
after I stopped autolysing my doughs.

Now that I've had time to think about it, the result I observed makes sense.
In nature, the outer parts of the seed come into contact with water first, and
only after penetrating this barrier would the water slowly find its way to the
center of the grain. The seed needs to sprout first to outcompete other nearby
seeds, requiring water to enter quickly. Yet the seed must also defend itself
against animals and potentially hazardous bacteria and fungi, requiring some
barrier to protect the embryo inside. A way for the plant to achieve both
goals would be for most of the enzymes to exist in the outer parts of the
hull. As a result, they are activated
first [enzymatic activity whole wheat]. Therefore, by just adding a
little bit of whole flour to your dough, you should be able to significantly
improve the enzymatic activity of your dough. That's why, for plain white
flour doughs, I usually add 10–20% whole-wheat flour.


*A whole-wheat sourdough bread.*


By understanding the two key enzymes *amylase* and *protease*, you
will be better equipped to make bread to your liking. Do you prefer a softer
or stiffer crumb? Do you desire a lighter or darker crust? Do you wish to reduce
the amount of gluten in your final bread? These are all factors that you can
tweak just by adjusting the speed of your dough's fermentation.

## Yeast

Yeasts are single-celled microorganisms belonging to the fungi kingdom. They
can reproduce through either budding or by building spores. The spores are
incredibly tiny and resistant to external factors. Scientists have found
undamaged spores that are hundreds of million years old. There are a wide
variety of species—so far, about 1,500 have been identified. Unlike
other members of the fungi kingdom such as mold, yeasts do not ordinarily
create a mycelium network [molecular mechanisms yeast].[^2]


![Saccharomyces cerevisiae: Brewer's yeast under the
      microscope.](images/saccharomyces-cerevisiae-microscope)

*Saccharomyces cerevisiae: Brewer's yeast under the
      microscope.*


Yeasts are saprotrophic fungi. This means that they do not produce their own
food, but instead rely on external sources that they can decompose and break
down into compounds that are more easily metabolized. What we today
refer to as the fermentation process, is the yeast breaking down carbohydrates
into carbon dioxide and alcohol. This process has been known for thousands
of years, and has been used since ancient times for the making of bread as well
as alcoholic beverages.

Yeast can grow and multiply under both aerobic and anaerobic conditions. When
oxygen is present, they produce carbon dioxide and water almost exclusively.
When oxygen is not present, their metabolism changes to produce alcoholic
compounds [effects oxygen yeast growth].

The temperatures at which yeast grows varies. Some yeasts, such as
*Leucosporidium frigidum*, do best at temperatures ranging from -2°C to
 20°C, while others prefer higher temperatures. In general, the warmer the
environment, the faster the yeast's metabolism. The variety of yeast
that you cultivate in your sourdough starter should work best within the range
of temperatures where the grain was grown and harvested. So, if you are from a
cooler place and cultivate a sourdough starter from a nordic rye variety,
chances are your yeast will prefer a colder environment.

As an example, beer makers discovered a beneficial yeast living in the cold
caves around the city of Pilsen, Czech Republic. This yeast has since become
known for producing excellent beers at lower temperatures and varieties of
these strains are now used for brewing popular lagers.

Yeasts in general are very common organisms. They can be found on cereal
grains, fruits, and many other plants in the soil. They can even be found
inside your gut! As it happens, the types of yeast we use for baking are
cultivated on the leaves of plants, though very little is known about the
ecology involved.

Plants are protected by thick cell walls that few fungi or bacteria can
penetrate. However, there are some species that produce enzymes capable of
breaking down those cell walls so they can infect the plant.

Some fungi and bacteria live inside plants without causing them any distress.
These are known as *endophytes*. Not only do they *not* damage their
host, they actually live in a symbiotic relationship. They help the plants in
which they dwell to protect themselves from other pathogens that might also
come to infect them through their leaves. In addition to this protection, they
also help with water and heat stress, as well as the availability of nutrients.
In exchange for their service to their host plants, these fungi and bacteria
receive carbon for energy.

However, the relationship between endophyte and plant is not always mutually
beneficial, and sometimes, under stress, they become invasive pathogens and
ultimately cause their host to decay [endophytes in plants].

There are other microorganisms that, unlike endophytes, do not penetrate cell
walls but instead live on the plant's surface and receive nutrients from rain
water, the air, or other animals. Some even feed on the honeydew produced by
aphids or the pollen that lands on the surface of the leaves. Such organisms
are called *epiphytes*, and included among them are the types of yeast
we use for baking.

Interestingly, when you remove external food sources, a large number of
epiphytic fungi and bacteria can still be found on the plant's surface,
suggesting that they must somehow be feeding directly from the plant.
Indeed, there is some research indicating that some plants intentionally release
compounds such as sugars, organic and amino acids, methanol, and various
salts along the surface. These nutrients would then attract the epiphytes that
live on the plant's surface.

Epiphytes are advantageous to a plant's survival, as they are provided with
enhanced protection against mold and other pathogens. Indeed, it is in the
best interest of the epiphytes to keep their host plants alive for as long as
possible [leaf surface sugars epiphytes].

More research is conducted every day into ways that yeasts can be used as
biocontrol agents to protect plants, the advantage being that these bio-agents
would be food-safe as the relevant strains of yeast are generally considered
harmless to humans. The yeasts would grow and multiply on the leaves,
essentially shielding them from other types of mold. This could be a potential
game changer for vineyards that suffer from mildew.

Such bio-agents could also be used to shield plants against the psychoactive
ergot fungus, which likes to grow in colder, more humid environments and
poses a significant problem for rye farmers.
Lawmakers have recently reduced the amount of allowed ergot contamination in
rye flour because it infects the grain and makes it unfit for consumption due
to its high toxicity to the liver. Yeasts could help to mitigate ergot contamination.

There is another interesting experiment performed by Italian scientists that
shows how crucial yeasts could be in protecting our crops. First, they made
tiny incisions into some of the grapes on a vine. Then, they infected the
wounds with mold. Some incisions were only infected with mold. Others were also
inoculated with some of the 150 different wild yeast strains isolated from the
leaves. They found that when the wound was inoculated with yeast, the grape
sustained no significant damage [yeasts biocontrol agent].


Intriguingly, there was also an experiment performed that showed how brewer's
yeast could function as an aggressive pathogen to grapevines. Initially, the
yeast lived in symbiosis with the plants, but after the vines sustained heavy
damage, the yeast became opportunistic and started to attack, even going so far
as to produce hyphae, the mycelium network normally associated with a fungus,
so that they could penetrate the tissue of the plants.

## Bacteria

The other most dominant microbial antagonists in your sourdough are bacteria.
In fact, they are so dominant that they outnumber the yeast in your dough
100 to 1. Whereas yeast provides leavening power, bacteria create the distinct
flavours for which sourdough has been named. These are due to the acidic
byproducts that result from bacterial feeding. As a bonus, these acids
can significantly increase the shelf life of sourdough
breads [shelflife acidity].


*Fructilactobacillus
    sanfranciscensis under the microscope.*


There are two predominant types of acid produced in sourdough bread: lactic and
acetic. In terms of flavor, lactic acid has clear dairy notes, while acetic
acid tastes of vinegar (of which it is, in fact, the primary ingredient!). These
acidic byproducts are produced by both *homofermentative* and
*heterofermentative* lactic acid bacteria.

*Homofermentative* means that, during fermentation, the bacteria produce
a single compound: in this case, lactic acid. *Heterofermentative*, on
the other hand, means that other compounds are also produced: in this case,
not only lactic acid, but also acetic acid, as well as ethanol and even some
carbon dioxide, two byproducts ordinarily associated with yeast. One quite
famous strain of lactic acid bacteria, *Fructilactobacillus sanfranciscensis*,
derives its name from the equally famous San Francisco style sourdough bread.
The first isolated culture came from a bakery in this city, hence the name.

Yeast and bacteria both compete for the same food source: sugar. Some scientists
have reported that bacteria consume mostly maltose, while yeast prefer glucose.
Others have reported that bacteria feed on the byproducts of yeast and vice
versa. This makes sense, as nature generally does a superb job of composting
and breaking down biological matter [lactobacillus sanfrancisco].

I have yet to find a proper source that clearly describes the symbiosis
between yeast and bacteria, but my current understanding is that they both
coexist and sometimes benefit each other, but not always. Yeast, for example,
tolerate the acidic environment created by the surrounding bacteria and are
thus protected from other pathogens. Meanwhile, however, other research
demonstrates that both types of microorganisms produce compounds that prevent
the other from metabolizing food—an interesting observation, by the way, as
it could help to identify additional antibiotics or
fungicides [mold lactic acid bacteria].

In the past, I've tried cultivating mushrooms and observed the mycelium
attempting to defend itself against the surrounding bacteria; both types of
microorganisms actively produced compounds to combat each other. And yet,
after a while, the fight seemed to reach a standstill, as the mycelium had
fully grown around the bacterial patch, preventing it from spreading further.
I imagine a similar scenario could be playing out in our sourdough starters,
although, given that the sourdough environment tends to be more liquid, this
fight would have to take place everywhere in the dough and not just in an
isolated patch. More research on this topic is required to get a better understanding of
the details of the relationship between yeast and bacteria.

One other interesting trait of sourdough bacteria worth mentioning is their
ability to break down and consume the proteins in your dough. If you've baked
sourdough before, chances are you've experienced this firsthand. You'll recall
from the *Enzymatic reactions* section that protease breaks down the
gluten network in your dough, resulting in a sticky mess if left unbaked for
too long. The bacteria, too, consume and break down the gluten in your
dough through a process called *proteolysis*.

This, to me, was a great riddle when I first started working with sourdough.
On the one hand, it makes the dough stickier. On the other, it makes the dough
more extensible and easier to work with. As the gluten is reduced, the dough
becomes easier for the microorganisms to inflate, allowing it to rise. This
could be likened to the level of effort required to inflate a thick rubber tire
versus a thin and fragile balloon. The latter would be easy to blow up with
your mouth, while the former would not.

Unsurprisingly, proteolysis is further accelerated by the protease enzyme
previously discussed, which aids in the breakdown of gluten into smaller,
more easily metabolized amino acids.

This, to me, is the amazing process of fermentation. When you eat sourdough
bread, you are not merely consuming flour and water but the end result of
complex biological processes accomplished by the bacteria and yeast. Because
of the added bacterial component, sourdough bread typically contains less
gluten than a pure yeast-based dough [proteolysis sourdough bacteria].
Furthermore, the homofermentative bacteria metabolize the ethanol produced by
the yeast and other heterofermentative lactic acid bacteria. In both cases,
most of the resulting compounds are organic acids. Every natural resource in
your sourdough bread is recycled by the microorganisms inside, which are all
trying to eat whatever is available for as long as possible, and with each
feeding, they become more adept at utilizing these resources.

Depending on which flavour profile you prefer, you can select for one organic
acid or another. Acetic acid production requires oxygen, and by depriving
your sourdough starter of it, you can boost the population of homofermentative
lactic acid bacteria. Over time they will become dominant and outcompete the
acetic acid-producing bacteria [acetic acid oxygen].

The optimal fermentation temperature of your lactic acid bacteria depends on
the strains you've cultured in your starter. Generally, they work best at the
temperature used to create your starter because you've already selected for
bacteria that thrive under that condition.

In one noteworthy experiment, scientists examined the lactic acid bacteria
found on corn leaves. They lowered the ambient temperature from 20–25°C to around
5–10°C and afterward observed varieties of the bacteria that had never been
seen before [temperature bacteria corn], confirming that there is, in
fact, a large variety of bacterial strains living on the leaves of the plant.

Incidentally, you could perform a similar experiment by kicking off a sourdough
starter at a lower temperature. In theory, the microbiome should adapt, as the
microorganisms that thrive the most at lower temperatures will start to become
dominant. It would be interesting to see if this could actively influence the
taste of the resulting bread.

One last footnote worth mentioning: Some sources say that fermenting at a
lower temperature can increase acetic acid production, while fermenting at a
warmer temperature can boost lactic acid production. I could not verify this
in my own tests. More research is needed on the topic.

---

[^1]: In a recent
study [milling commercial home mill comparison] tests have shown that
milling flour
at home with a small mill had no significant negative impact on the resulting
bread quality compared to milled flour from temperature-regulated large-scale
mills.

[^2]: For one
    interesting exception, skip ahead to the end of this section on
    page .



---


# Making a sourdough starter

> In this chapter you will learn how to make your
> own sourdough starter, but before doing so you will
> quickly learn about baker's math. Don't worry,
> it's a very simple way to write a recipe which
> is cleaner and more scalable. Once you get the hang
> of it you will want to write every recipe this way.
> You will learn to understand the signs indicating
> your starter's readiness, as well as
> how to prepare your starter for long-term storage.

## Baker's math


In a large bakery, a determining factor is how
much flour you have at hand. Based on the amount
of flour you have, you can calculate how many
loaves or buns you can make. To make it easy
for bakers, the quantity of each ingredient
is calculated as a percentage based on how much flour you have.
Let me demonstrate this with a small example from
a pizzeria. In the morning you check and you realize you
have around 1 kg of flour.
Your default recipe calls for around 600 g of water.
That would be a typical pizza dough, not too dry but
also not too wet. Then you would be using around 20 g
of salt and around 100 g of sourdough starter[^1].
The next day you suddenly have 1.4 kg of flour
at hand and thus can make more pizza dough. What do you do?
Do you multiply all the ingredients by 1.4? Yes you could,
but there is an easier way. This is where baker's math
comes in handy. Let's look at the default recipe with baker's
math and then adjust it for the 1.4 kg flour quantity.


| **Ingredient** |  | **Percentage** | **Calculation** |  |  |
| --- | --- | --- | --- | --- | --- |
| Flour | 1000 | 100% | 1000 of 1000 | is | 100% |
| Water | 600 | 60% | 600 of 1000 | is | 60% |
| Sourdough starter | 100 | 10% | 100 of 1000 | is | 10% |
| Salt | 20 | 2% | 20 of 1000 | is | 2% |

*An example table demonstrating how to
      properly calculate using baker's math*


Note how each of the ingredients is calculated as a percentage
based on the flour. The 100% is the baseline and represents the absolute
amount of flour that you have at hand. In this case that's
1000 g (1 kg).

Now let's go back to our example and adjust the flour, as we have
more flour available the next day. As mentioned the next day
we have 1.4 kg at hand (1400 g).


| **Ingredient** | **Baker's math** | **Calculated value** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Flour | 100% | 1400 | × | 1 | = | 1400 |
| Water | 60% | 1400 | × | 0.6 | = | 840 |
| Sourdough starter | 10% | 1400 | × | 0.1 | = | 140 |
| Salt | 2% | 1400 | × | 0.02 | = | 28 |

*An example recipe that uses
            1400 g as its baseline and is then calculated using
            baker's math.*


For each ingredient we calculate the percentage
based on the flour available (1400 g). So for the water
we calculate 60% based on 1,400. Open up your
calculator and type in 1400 × 0.6 and you have
the exact value in grams that you should be using.
For the second day, that is 840 g. Proceed to do the same
thing for all the other ingredients and you will know
your recipe.

Let's say you would want to use 50 kg of flour
the next day. What would you do? You would simply proceed
to calculate the percentages one more time. I like this
way of writing recipes a lot. Imagine you wanted to make
some pasta. You would like to know how much sauce you should
be making. Now rather than making a recipe just for you, a
hungry family arrives. You are tasked with making pasta
for 20 people. How would you calculate the amount of sauce
you need? You go to the internet and check a recipe and then
are completely lost when trying to scale it up.

## The process of making a starter


![A very active sourdough starter shown by the
      bubbles in the dough.](images/sourdough-starter-activity-indicators)

*A very active sourdough starter shown by the
      bubbles in the dough.*


Making a sourdough starter is very easy, all you need
is a little bit of patience. It is in fact so easy that it can be summarized
in a simple the flowchart The flour you should
use to bootstrap your starter is ideally a whole flour.
You could use whole-wheat, whole-rye, whole-spelt or
any other flour you have. In fact gluten free flours such
as rice or corn would also work. Don't worry, you can always
change the flour later. Use whatever whole flour you
already have at hand.


**Flowchart:** *The process of making a sourdough
      starter from scratch.*


Your flour is contaminated with millions of microbes. As explained
before in the chapter about wild yeast and bacteria, these
microbes live on the surface of the plant. That's why
a whole flour works better because you have more natural
contamination from the microbes you are trying to cultivate
in your starter. More of them live on the hull compared to the
endophytes living in the grain.

Start by measuring approximately 50 g of both flour and
water. The measurements don't have to be exact; you can use
less or more, or just eyeball the proportions. These
values are just shown as a reference.

Don't use chlorinated water when setting up your starter.
Ideally, you should use bottled water. In certain regions
like Germany, tap water is perfectly fine. Chlorine is added
to water as a disinfectant to kill microorganisms; you will
not be able to grow a starter with chlorinated water.

In this process, the hydration of your starter is 100%.
This means you're using equal amount of flour and
water. Stir everything together so that all the flour is
properly hydrated. This step activates the microbial spores
in your mixture, drawing them out of hibernation and
reviving them.
Finally, cover your mixture but make sure the covering is
not airtight. You still want some gas exchange to be possible.
I like to use a glass and place another
inverted one on top.

Now an epic battle begins, as visualized in
the figure. In one
study [yeasts biocontrol agent] scientists have identified
more than 150 different yeast species living
on a single leaf of a plant.
All of the different yeasts and bacteria are trying to get
the upper hand in this battle. Other pathogens such as mold
are also being activated as we added water. Only the strongest
most adaptable microorganisms will survive.


![A simple
      visualization of the microbial warfare that happens during the making of
      a sourdough starter. The wild spores on the plant and flour become
      activated the moment flour and water is mixed.  Only the most adapted
      flour-fermenting microbes will survive. Because of unwanted microbial
      fermentation it is advised to discard the feeding-leftovers of the first
      days. The surviving yeast and bacteria continuously try to outcompete
      each other for resources. New microbes have a hard time entering the
      starter and are eliminated.](images/sourdough-starter-microbial-war)

*A simple
      visualization of the microbial warfare that happens during the making of
      a sourdough starter. The wild spores on the plant and flour become
      activated the moment flour and water is mixed.  Only the most adapted
      flour-fermenting microbes will survive. Because of unwanted microbial
      fermentation it is advised to discard the feeding-leftovers of the first
      days. The surviving yeast and bacteria continuously try to outcompete
      each other for resources. New microbes have a hard time entering the
      starter and are eliminated.*


By adding water to the
flour the starches start to degrade. The seedling tries to
sprout but it no longer can. Essential for this process is the
amylase enzyme. The compact starch is broken down to more
digestible sugars to fuel plant growth. Glucose is what the
plant needs in order to grow. The microorganisms that survive
this frenzy are adapted to consuming glucose.

Luckily for us
bakers, the yeast and bacteria know very well how to metabolize
glucose. This is what they have been fed in the wild by the plants.
By forming patches on the leaf and protecting the plant from
pathogens they received glucose in return for their services.
Each of the microbes tries to defeat the other by consuming the
food fastest, producing agents to inhibit food uptake by others or by producing
bactericides and/or fungicides. This early stage of the starter
is very interesting as more research could possibly reveal
new fungicides or antibiotics.

Depending on where your flour
is from, the starting microbes of your starter might be different
than the ones from another starter. Some people have also reported
how the microbes from your hand or air can influence your starter's
microorganisms. This makes sense to a certain extent. Your
hand's microbes might be good at fermenting your sweat, but
probably not so good at metabolizing glucose. The contamination
of your hands or air might play a minor role in the initial epic
battle. But only the fittest microbes fitting the sourdough's
niche are going to survive.

This means the microorganisms knowing
how to convert maltose or glucose will have the upper hand. Or the
microbes fermenting the waste of the other microbes. Ethanol created
by the yeast is metabolized by the bacteria in your sourdough. That's
why a sourdough has no alcohol. I can confirm the role of aerial
contamination to a certain extent, when setting up a new sourdough
starter the whole process is quite quick for me. After a few
days my new starter seems to be quite alive already. This might
be due to previous contamination of flour fermenting microbes in
my kitchen.

Wait for around 24 hours and observe what happens to your starter.
You might see some early signs of fermentation already. Use your nose
to smell the dough. Look for bubbles in the dough. Your dough
might already have increased in size a little bit. Whatever
you see and notice is a sign of the first battle.

Some microbes have already been outperformed. Others have won the first
battle.  After around 24 most of the starch has been broken down
and your microbes are hungry for additional sugars. With a spoon take around
10 g from the previous day's mixture and place it in a new
container. Again—you could also simply eye ball all the quantities. It does
not matter that much. Mix the 10 g from the previous day with
another 50 g of flour and 50 g of water.

Note the ratio of 1:5. I very often use
1 part of old culture with 5 parts of flour and 5 parts of water.
This is also very often the same ratio I use when making a dough.
A dough is nothing else than a giant sourdough starter with slightly different
properties. I'd always be using around 100–200 of starter
for around 1000 g of flour (baker's math: 10–20%).

Homogenize your new mixture again with a spoon. Then cover
the mix again with a glass or a lid. If you notice the top of
your mixture dries out a lot consider using another cover. The
dried-out parts will be composted by more adapted microbes such as
mold. In many user reports, I saw mold being able to damage
the starter when the starter itself dried out a lot.

You will
still have some mixture left from your first day. As this contains
possibly dangerous pathogens that have been activated make sure you discard
this mixture. A rule of thumb is to begin keeping the discard,
the moment you made your first successful bread. At that point
your discard is long-fermented flour that is an excellent addon
used to make crackers, pancakes or delicious hearty sandwich
bread… I also frequently dry it and use it as a rolling agent
for pizzas that I am making.[^2]

You should hopefully again see some bubbles, the starter increasing
in size and/or the starter changing its smell. Some people give
up after the second or third day, because the signs might no longer
be as dominant as they were on day one. The reason for this lies in only a few
select microbes starting to take over the whole sourdough starter. The most
adaptable ones are going to win, they are very small in quantity and will
grow in population with each subsequent feeding. Even if you see no signs
of activity directly, do not worry, there is activity in
your starter at a microscopic level.

24 hours later again we will repeat the same thing again until
we see that our sourdough starter is active. More on that in the
next section of this book.

## Determining starter readiness

For some people the whole process of setting up a starter takes
only 4 days. For others it can take 7 days, for some even 20 days.
This depends on several factors including how good your wild microbes
are at fermenting flour. Generally speaking, with each feeding
your starter becomes more adapted to its environment. Your
starter will become better at fermenting flour. That's why
a very old and mature starter you receive from a friend might
be stronger than your own starter initially. Over time
your sourdough starter will catch up. Similarly, modern baking
yeast has been isolated like this from century old sourdough
starters.


**Flowchart:** *A flow chart showing you how to
      determine if your sourdough starter is ready to be used. Make sure to
      wait at least 6–12 after feeding your
      starter to check its readiness. To evaluate it, look at your starter's size
      increase, airy texture and take note of its smell.
      All three factors are important to properly evaluate your starter's activity level.
      An active starter is an important foundation for a successful dough fermentation*


The key sign to look at is bubbles that you see in your starter
jar. This is a sign that the yeast is metabolizing your
dough and creates CO₂. The CO₂ is trapped in your dough
matrix and then visualized on the edges of the container.

Also note the size increase of your dough. The amount the dough increases
in size is irrelevant. Some bakers claim it doubles, triples or quadruples.
The amount of size increase depends on your microbes, but also on
the flour that you use to make the starter. Wheat flour contains
more gluten and will thus result in a larger size increase. At
the same time the microbes are probably not more active compared
to when living in rye sourdough. You could only argue that
wheat microbes might be better at breaking down gluten compared
to rye microbes. That's one of the reasons why I decided to change
the flour of my sourdough starter quite often. I had hoped to create
an all-around starter that can ferment all sorts of different
flour[^3].

Your nose is also
a great tool to determine starter readiness. Depending on
your starter's microbiome you should notice either the smell
of lactic acid or acetic acid. Lactic acid has dairy yogurty notes.
The acetic acid has very strong pungent vinegary notes. Some
describe the smell as glue or acetone. Combining the visual clues
of size increase and pockets plus the smell is the best way
to determine starter readiness.

In rare events your flour might be treated and prevent microbe growth.
This can happen if the flour is not organic and a lot of biochemical
agents have been used by the farmer. In that case simply try again
with different flour. Ten days is a good period of time to wait before
trying again.

Another methodology used by some bakers is the so called *float test*.
The idea is to take a piece of your sourdough starter and place it
on top of some water, if the dough is full with gas it will float
on top of the water. If it's not ready, it can't float and will
sink to the bottom. This test does not work with every flour,
rye flour for instance can't retain the gas as well as wheat flour
and thus in some cases will not float. That's why I personally
don't use this test and can't recommend it.

Once you see your starter is ready I would recommend giving it
one last feeding and then you are ready to make your dough in the
evening or the next day. For the instructions on how to make your
first dough please refer to the next chapters (
and ) in this book.

If your first bread failed, chances are your fermentation hasn't
worked as expected. In many cases the reason is your sourdough starter. Maybe
the balance of bacteria and yeast isn't optimal yet. In that case a good
solution is to keep feeding your starter once per day. With each feeding your
starter becomes better at fermenting flour. The microbes will adapt more and
more to the environment. Please also consider reading the stiff sourdough starter
chapter in this book. The stiff sourdough starter helps to boost the
yeast part of your sourdough and balance the fermentation.

## Maintenance


**Flowchart:** *A full flowchart showing
      you how to conduct proper sourdough starter maintenance. You can use a
      piece of your dough as the next starter. You can also use left-over
      starter and feed it again. Choose an option that works best for your own
      schedule. The chart assumes that you are using a starter at a
      100% hydration level. Adjust the water content
      accordingly when you use a stiff starter.*


You have made your sourdough starter and your first bread. How do you perform
maintenance for your starter? There are countless different maintenance
methods out there. Some people go completely crazy about their starter and
perform daily feedings of the starter. The key to understanding how to properly
conduct maintenance is to understand what happens to your starter after you
used it to make a dough. Whatever starter you have left, or a tiny piece of
your bread dough can serve to make your next starter[^4].

As explained earlier your starter is adapted
to fermenting flour. The microbes in your starter are very resilient. They
block external pathogens and other microbes. That is the reason why, when
buying a sourdough starter, you will preserve the original microbes. It is
likely that they are not going to change in your starter. They are outcompeting other
microbes when it comes to fermenting flour. Normally everything in nature
starts to decompose after a while. However, the microbes of your starter have
very strong defense mechanisms. In the end, your sourdough starter can be
compared to pickled food. Pickled food has been shown to stay good for a very
long period of time [pickled foods expiration]. The acidity of your sourdough starter is quite
toxic to other microbes. The yeast and bacteria though have adapted to living
in the high-acid environment. Compare this to your stomach, the acidity
neutralizes many possible pathogens. As long as your starter has sufficient
food available it will outcompete other microbes. When the starter runs out of
food the microbes will start to sporulate. They prepare for a period of no
food and will then reactivate the moment new food is present. The
spores are very resilient and can survive under extreme conditions.
Scientists have claimed they found 250 million-year-old spores that are still
active [old spores]. While being spores
they are however more vulnerable to external pathogens such as mold.
Under ideal conditions though the spores can survive for a
long time.

But as long as they stay in the environment of your starter they live
in a very protected environment. Other fungi and bacteria have a hard time decomposing your left over starter mass.
I have seen only very few cases where the starter actually died. It is almost impossible
to kill a starter.

What happens though is that the balance of yeast and
bacteria changes in your starter. The bacteria is more fitted to living
in an acidic environment. This is a problem when you make another dough.
You want to have the proper balance of fluffiness and sour notes.
When a starter has hibernated for a long period, chances are that
you do not have a desirable balance of microbes.
Furthermore, depending on the time your starter hibernated you might only have
sporulated microbes left. So a couple of feedings will help to get your
sourdough starter into the right shape again.

The following are a couple of scenarios that will help you to conduct proper
starter maintenance, depending on when you want to bake the next time.

**I would like to bake again the next day:**
: Simply take whatever starter you have left and feed it again. If you depleted
all your starter you can cut a piece of your dough. The dough itself is
nothing different than a gigantic starter. I recommend a 1:5:5 ratio like
mentioned before. So take 1 piece of starter, feed with 5 parts of flour and 5
parts of water. If it is very hot where you live, or if you want to make the
bread around 24 hours later after your last feeding, change the ratio. In that
case I would go for a 1:10:10 ratio. Sometimes I don't have enough starter.
Then I even use a ratio of 1:50:50 or 1:100:100. Depending on how much new
flour you feed it takes longer for your starter to be ready again.

**I would like to take a break and bake next week:**
: Simply take your leftover starter and place it inside of your fridge. It will stay good
for a very long period. The only thing I see happening is the surface
drying out in the fridge. So I recommend drowning the starter in a little bit
of water. This extra layer of water provides good protection from the top
part drying out. As mold is aerobic it can not grow efficiently under
water [mold anaerobic]. Before using the starter again simply either stir
the liquid into the dough or drain it. If you drain the liquid you can use it
to make a lacto-fermented hot sauce for instance.

The colder it is the longer you preserve a good balance of yeast and
bacteria. Generally, the warmer it is the faster the fermentation process is,
and the colder it is the slower the whole process becomes.
Below 4°C the starter fermentation almost completely stops. The
fermentation speed at low temperatures depends on the
strains of wild yeast and bacteria
that you have cultivated.

**I would like to take a several months break:**
: Drying your starter might be the best option to preserve it in this case. As
you remove humidity and food your microbes will sporulate. As there is no
humidity the spores can resist other pathogens very well. A dried starter can
be good for years.

Simply take your starter and mix it with flour. Try to crumble the starter as
much as possible. Add more flour continuously until you notice that there is no
moisture left. Place the flour starter in a dry place in your house. Let it
dry out even more. If you have a dehydrator you can use this to speed up the
process. Set it to around 30°C and dry the starter for 12–20 hours. The next
day your starter has dried out a bit. It is in a vulnerable state as there is still a bit
of humidity left. Add some more flour to speed up the drying process. Repeat
for another 2 days until you feel that there is no humidity left. This is
important or else it might start to grow mold. Once this is done simply store the
starter in an airtight container. Or you can proceed and freeze
the dried starter. Both options work perfectly fine. Your sporulated starter
is now waiting for your next feeding. If available you can add some silica
bags to the container to further absorb excess moisture.

Initially, it would take about three days for my starter to become alive again
after drying and reactivating it. If I do the same thing now my starter is
sometimes ready after a single feeding. It seems that the microbes adapt. The ones
that survive this shock become dominant subsequently.

So in conclusion the maintenance mode you choose depends on when you want to bake next.
The goal of each new feeding is to make sure your starter
has a desired balance of yeast and bacteria when making a dough. There is no need to provide your
starter with daily feedings, unless it is not mature yet. In that case, each
subsequent feeding will help to make your starter more adept at fermenting
flour.

---

[^1]: This is my go to
pizza dough recipe. In Napoli modern pizzerias would use fresh or dry yeast.
However traditionally pizza has always been made with sourdough.

[^2]: Discarding starter when preparing
a new batch can be frustrating. With experience, bread-making
becomes more efficient, and excess discard is rarely produced. It is
possible to prepare just the right amount of starter
needed for bread dough. In fact, a fully depleted starter can even be revived
using a small portion of bread dough. Any leftover discard, rich in spores,
can also serve as a backup to create a new sourdough starter. Simply mix the
discard with a little flour and water, and it will spring back to life. That is a
great option if the starter was accidentally depleted. A practical approach
is to store all discard in a single jar in the fridge, adding new discard on
top as needed and using it whenever required.

[^3]: Whether this is working, I can't scientifically say.
Typically the microbes that have once taken place are very strong
and won't allow other microbes to enter. My starter has initially
been made with rye flour. So chances are that the majority of
my microorganisms are from a rye source.

[^4]: I very often use all my
starter to make a dough. So if the recipe calls for 50 of starter I make
exactly 50 starter in advance. This means I have no starter left. In that
case I would proceed to take tiny bit of the dough at the end of the
fermentation period. This piece I would use to regrow my starter again.



---


# Sourdough starter types

> In this chapter of the book we will have a closer look
> at different sourdough starter types, and their respective
> traits and usage. They are mostly characterized by their hydration
> level, and this will provide a trade-off between acidity, volume increase and
> the gluten level of your flour.

## Introduction


Depending on the flour you have at hand, the type of starter changes. With more
bacterial activity you have more gluten consumption of your microbes. So if
you want to bake a free standing loaf, you need a flour with more gluten. The
more gluten you have, the more of it can be broken down whilst still maintaining
dough integrity. If you live in a country where the climate to grow wheat
isn't ideal and you only have weaker flours, then a stiff sourdough starter
could be advised. The stiff sourdough starter will improve yeast activity and
reduce bacterial activity. If you are a chaser of a very sour bread and have a
very strong wheat flour then you can try to play with a liquid sourdough
starter. The key difference between all of the starters is how much water
is used in the starter. The regular starter has a 1:1 relationship of flour
to water. The liquid starter has a 5:1 water-to-flour ratio, and the stiff
starter has half as much water as flour, as summarized in
the table below.


|  |  |  | **Activity** |  |
| --- | --- | --- | --- | --- |
|  **Starter type** | **Hydration (%)** | **Flour type** | **Yeast** | **Bacterial** |
| Regular | 100 | Strong wheat | Balanced | Balanced |
| Liquid | 500 | Very strong wheat | Minimal | High |
| Stiff | 50–60 | All wheat | High | Low |

*A comparison of different
            sourdough starter types and their respective properties. The only
            difference is the amount of water (hydration) that is used when
            feeding the starter.*


You can change your starter type by just adjusting the feeding ratio of how
much flour and water you use. I frequently change my starter type from
regular to liquid and then back to a stiff starter. After changing the
environment of your microbes, apply feedings at the same ratio over a couple of
days so that they can adapt to the new environment. I typically see
changes after a single feeding, but I recommend 2 to 3 feedings, one feeding per
day, to see a stronger effect.


![Three different starter types
      next to each other. Note how the liquid starter is submerged in water.
      It has a hydration of 500% or more.  The regular starter
      has a hydration of around 100%, the stiff starter around
      50–60%.](images/sourdough-starter-types)

*Three different starter types
      next to each other. Note how the liquid starter is submerged in water.
      It has a hydration of 500% or more.  The regular starter
      has a hydration of around 100%, the stiff starter around
      50–60%.*


Your dough is generally just a big sourdough starter. So your starter is going
to adapt and regrow inside of your main dough. But you can influence the
properties that your starter carries over to your main dough. If you have more
bacterial fermentation, then your dough will also have slightly more bacterial
fermentation. If you have more yeast fermentation, then your main dough will
have slightly more yeast fermentation. This is important to know when you are
working with a more mature unfed starter.

Let's say your starter had last been
fed 48 hours ago. Chances are that your bacteria are very active while the
yeast could be dormant. In such a case you can skip feeding your starter
before making another dough. Just use a very tiny amount of starter. For
1 kg of flour I would take around 10 g of starter
(1% in terms of baker's
math). If my starter is very young and had just been fed 6 to 8 hours ago I might
end up going up to 20% of starter. As mentioned earlier,
remember that your dough is nothing
else other than a big starter. It will tremendously help you to figure out
your best next steps.

When using such a low inoculation rate (1%), you need to use stronger
flour when making wheat-based doughs. Your flour naturally breaks down due
to enzymatic activity. It might take 24 hours for the starter to re-grow
inside of your bread dough. At the same time, the enzymatic activity might
have caused your gluten to degrade significantly. While this is okay
when looking at your starter, your wheat-based dough will flatten
out during baking and no longer have the typical characteristics (fluffy crumb
structure). A stronger flour with more gluten is thus advised. It allows for
a longer fermentation before most gluten is broken down.

## Regular starter


![A regular sourdough starter at 100%
      hydration fed with rye flour.](images/sourdough-starter.jpg)

*A regular sourdough starter at 100%
      hydration fed with rye flour.*


The regular sourdough starter is made at a hydration of around 100%.
This means the starter has equal parts of flour and water. This is the most
common and most universal sourdough starter there is. The starter has a good
balance of yeast and bacteria. After a feeding, the volume of the dough
greatly increases. After it reaches a certain peak, it will start to collapse again.

The best way to judge whether the starter is ready is to look at signs such as
air pockets on the edges of your container. Also use the nose to evaluate the
smell of your starter. If you feel that the starter doesn't perform in a
desirable way, chances are that your yeast and bacteria ratios are off. In that
case frequent daily feedings using a 1:5:5 (starter:flour:water) ratio will
help.

A regular starter is a perfect choice to use when utilizing stronger wheat or spelt flours.
It also nicely works with rye, emmer or einkorn. If you only have a weak flour
at hand with less gluten, this starter might cause issues. As you tend to have
quite some bacterial activity, gluten is going to be broken down fast. When
using the starter, use around 1–20% starter based on the flour of your
dough.

Depending on the bacteria cultivated, a regular starter either has a lactic (dairy),
a vinegary (acetic) or mix of both flavor profiles. You can adjust your
starter's flavor by changing the type to a liquid starter.

## Liquid starter


![A liquid sourdough starter features a high level of
      water. The high water amount boosts lactic acid producing bacteria.
      After a while the liquid and flour start to separate. Bubbles on the
      side of the flour indicate that the starter is ready to be used.](images/sourdough-starter-liquid.jpg)

*A liquid sourdough starter features a high level of
      water. The high water amount boosts lactic acid producing bacteria.
      After a while the liquid and flour start to separate. Bubbles on the
      side of the flour indicate that the starter is ready to be used.*


**Flowchart:** *The process to convert your regular
      or stiff starter into a liquid starter. The whole process takes around
      3 days. The longer you maintain your starter at the suggested hydration
      level, the more adapted your microorganisms become. It is recommended to
      keep a backup of your original starter as the liquid environment will
      select anaerobic microorganisms. This boosts bacteria that create lactic
      acid rather than acetic acid. The resulting acidity will be perceived as
      milder. When beginning with a liquid starter your stiff starter will
      feature mild dairy notes. When beginning this process with a regular
      starter your created stiff starter will feature both dairy
      and vinegary notes.*


The liquid starter is made at a hydration of around 500%. This means
the starter has much more water than flour. The additional layer of water on
top of the flour changes the microbiome of your starter.

By introducing this layer of water, less oxygen is available throughout the
course of fermentation. This means that your starter will no longer be
producing acetic acid. The heterofermentative lactic acid bacteria will thrive
in this environment. This is a neat little trick to change your starter's
flavor profile from vinegary to lactic. Your starter is going to develop dairy
creamy notes. Interestingly, when changing the hydration again, your starter
is going to maintain the liquid starter flavor profile, but then benefit again
from enhanced yeast activity. The liquid starter conversion is irreversible.
By changing to a liquid starter you will permanently select a subset of
microbes that work better in the more liquid environment. So even after going
back to a regular or stiff starter the subset of microbes created by the
liquid conversion will remain. For this reason, it is recommended to keep a
backup of the starter before the liquid starter conversion.

To begin with the
conversion, simply take around 1 g of your starter, mix with 5 g flour and
25 g water. Stir everything together properly. After a few minutes the flour is
going to start settling in at the bottom of your jar. Repeat this process over
a few days. Shake the starter gently to see if you can see tiny CO₂ bubbles
moving in the liquid. This is a good sign that your starter is ready. Use your
nose to smell the starter. It should have a creamy dairy flavor note.

As you have more bacterial activity, this starter works best with a very strong
flour that can withstand a long fermentation period. Using this starter with a
weak wheat flour will not work. If you do not care about baking a freestanding loaf,
then you can easily use this starter together with a loaf pan.
This starter also works great when making a hearty pancake dough. To use it
I shake the starter container until I see all ingredients are homogenized.  Then
I use around 5% of it in terms of baker's math. So for 1000 g of flour
that's around 50 g of liquid starter. As it is very liquid you have to
include the 50 g in your liquid calculation. I typically treat the starter
directly as liquid in the recipes. So if the recipe calls for 600 g of water
and I use 50 g of starter, then I would proceed and only use 550 g of
water.

This type of starter is also an excellent mold combatant. As you are removing
oxygen from the equation, aerobic mold cannot properly grow. If your starter
has a mold problem then the liquid conversion could be the remedy. Take a
piece of your starter where you suspect mold growth. Apply the conversion
as mentioned before. The mold will likely sporulate as it runs out of food.
With each new feeding you are reducing the mold spores. The spores can no
longer reactivate as they cannot do so in the anaerobic conditions.

The liquid on top of your starter is an excellent resource that you could use
to make sauces. If you feel you would like to add a little bit of acidity,
drain the liquid part on your starter and use it. I have used it numerous
times to make lacto-fermented hot sauces.

## Stiff starter


![A stiff sourdough starter that I used to
      make a Stollen dough for Christmas. Note the bubbles on the edge of the
      container. The dough does not fall out of the jar. The moment
      the gluten structure breaks down due to fermentation the starter
      will ultimately fall in the jar.](images/sourdough-starter-stiff.jpg)

*A stiff sourdough starter that I used to
      make a Stollen dough for Christmas. Note the bubbles on the edge of the
      container. The dough does not fall out of the jar. The moment
      the gluten structure breaks down due to fermentation the starter
      will ultimately fall in the jar.*


The stiff starter is the driest of all the starters. It has a hydration of
around 50–60%. So for 100 g of flour you are using around
50–60 of water. If you can't mix flour and water because the
mixture is too dry you need to increase the water quantity. This is often
the case when using whole-wheat/rye flour to make your starter. The
more bran your flour contains, the more water your flour can absorb. The stiff
starter should have a comparable consistency to pasta or pizza dough. When
mixing the starter there should be no chunks of flour left. Test placing
the starter on your kitchen counter. When lifting it should slightly stick
to your counter's surface. This test indicates that you hydrated the flour sufficiently.
When the mixture is too dry, the fermentation speed is greatly reduced and
the starter will seem inactive. The starter should be much drier than a
regular starter, but also not too dry. Refer to
the figure for a visual example of the starter's
required hydration level.


![An image showing you a
      stiff starter that is too dry and one that is perfectly hydrated.  The
      starter shouldn't contain chunks of flour and slightly stick to your
      counter top. The starter in the picture is made with whole-wheat flour.](images/stiff-starter-dry-check.jpg)

*An image showing you a
      stiff starter that is too dry and one that is perfectly hydrated.  The
      starter shouldn't contain chunks of flour and slightly stick to your
      counter top. The starter in the picture is made with whole-wheat flour.*


**Flowchart:** *The process to convert your regular
      starter into a stiff starter. The whole process takes around 3 days. The
      longer you maintain your starter at the suggested hydration level, the
      more adapted your microorganisms become. The stiff starter boosts the
      yeast activity of your sourdough starter.  The guide uses a
      50% hydration level for the starter. If the dough is too
      stiff consider increasing this to 60%.*


In the stiffer environment the yeast thrives more. This means you will have
more CO₂ production and less acid production. In my tests this is a game
changer especially if you are using weaker gluten flours. The wheat flours in
my home country of Germany tend to be lower in gluten. For wheat to build gluten, warm conditions
are preferred [gluten development temperatures]. When following recipes
from other bakers, I could never achieve similar results. When following
timings my doughs would
simply collapse and become super sticky. Only when I started to buy more
expensive wheat flour my results did start to change. As not everyone can afford
these special baking flours and due to their limited availability, I stumbled upon the
stiff sourdough starter. I made several tests where I used the same amount of
starter and flour. I only changed the hydration between all the starters.
I would then proceed and place a balloon on top of each of the jars. The stiff
starter jar was clearly inflated the most. The regular starter
followed in second place. The liquid starter finished in third place with far less CO₂
production.


![A German Christmas *Stollen* made
      with a stiff starter instead of yeast.](images/stollen)

*A German Christmas *Stollen* made
      with a stiff starter instead of yeast.*


I then proceeded and bought a cheap low-gluten cake flour in my nearby supermarket.
This flour before had caused me massive headaches in the past. I made a sourdough bread
exactly how I would normally do—I had to reduce the hydration a bit as a low
gluten flour does not soak up as much water. Then I replaced the starter with
the stiff starter. The dough felt amazing and was suddenly able to withstand a
much longer fermentation period. The bread had great oven spring and tasted
very mild. I am still yet to find a proper scientific explanation why the yeast part of
the dough is more active. Maybe it is not. It could also be that the bacteria
is inhibited by the lack of water.

When making the stiff sourdough starter, start by using around 50%
water. If you are using a whole-wheat flour, or a strong flour consider going
up to 60%. All the ingredients should mix together very well. There
should be no crumbly flour left. This is a common mistake I have seen when
people tried to make the stiff starter. Yes it should be dry, but not to a
point where it is a brick of cement. If you have ever made a pasta dough, this
dough should feel exactly the same.

To evaluate whether your stiff starter is ready, look for a dome. Also look for
pockets of air on the sides of your container. Use your nose to smell the
starter. It should have a mild smell. It also tends to smell much more
alcoholic than the other starters.

When using a stiff starter, use around 1–20% starter in terms of
baker's math for your
dough. This depends on the ripeness of your starter.
In summer I typically use around
1–10% and in winter around 20%. This way you can
also control the fermentation speed. If it is very hot where you live, consider
lowering the starter amount to 1–5%. If it is very cold in your
area consider increasing the starter amount up to 30%.
Mixing the stiff starter can be a little bit annoying as it hardly homogenizes with
the rest of the dough. In this case, you can try to dissolve the starter in the
water you are about to use for your dough. This will make mixing a lot easier.


## Lievito madre or pasta madre

The *lievito madre*, also known as *pasta madre*, belongs to the
same category as the stiff sourdough starter. After conducting hours of
research, I could not find a difference between *pasta madre* and
*lievito madre*. Both terms seem to be used interchangeably in
literature.

In many recipes this starter is made directly
from dried or fresh fruits. You can also make a starter from leaves from your
garden. As described before, the wild yeast and bacteria consume the glucose
from the plants' leaves. All the options work. When making a starter directly
from dried fruits, you sometimes lack the bacterial part of the fermentation.
The acidity is very important in order to clean your starter from possible
pathogens. If you decide to make your starter from fruits, make sure it also
acidifies properly when making a dough. A tool such as a pH meter can be of
optimal help. Generally, the lower the pH, the higher the acidity. The acidity
should be below 4.2 to know that your starter produces sufficient acidity.

Some bakers cleanse the *lievito madre* in a bath of water. This is supposed to
remove excess acidity. In my own experiments I have not been able to confirm
this methodology. The acidity remains the same. The only reason this could
make sense is if you also tried to boost anaerobic microorganisms. However, then the
starter would need to remain in this environment for quite some time and not just
a few hours.

## Conclusion

Baking with sourdough is simple. It's just flour and water. When seeing a recipe
from an experienced baker you wonder, Wait, that's it? There is nothing more
to it? I feel that this might be the reason why some bakers have such complicated
feeding procedures. They resort to several feedings per day at a certain given ratio.
This makes the baker feel a little more elitist. Of course over time as
more and more people follow this procedure, it became a self fulfilling prophecy.
The more experienced you become, the higher the chances are that a bogus starter
feeding guide will reward you with beautiful results. The reason however is
not in the starter routine. The reason is that you understand the fermentation better
and become better at reading the signs of your dough.

If I had to choose one starter type I would go for the stiff starter. In many cases
it will provide you with consistently great results with little effort.
In my experience you can make any yeast-based dough and just replace
the yeast directly with the stiff sourdough starter. You will be able
to achieve even better results with the stiff starter.

Lastly, no matter which starter type you choose, you can control how sour
you want your dough to be. The longer you push the fermentation, the more
acidity is going to be piled up. The only difference is that for a given
volume increase, the stiff starter will produce the least acidity. So for a
volume increase of 100%, the liquid starter has produced the most acidity,
followed by the regular starter and then the stiff starter. If you wait long
enough, the stiff starter will have produced the same amount of acidity as the
other starters. But before doing so it will have also produced a lot more CO₂. If
you like the sour flavor, you have to push your fermentation longer. This also
means you either need to bake in a loaf pan or have a very strong gluten flour
that is able to withstand long fermentation times.



---


# Flour types

> In this chapter we will have a closer look at different flour types
> and their respective categorization. We will also look at common
> ways to distinguish different flours of the same type, this way you can more
> confidently purchase the flour you need.

The most basic flour type is a whole grain flour, in this case the whole seed has
been grounded to smaller pieces. Sometimes, depending on what you want to bake,
the hearty taste of the bran might not be desired. In this case you can use
whiter flours. Together with sieves, mills remove larger parts of the seed's
hull.  The seed already contains a pre-built germ from the plant waiting to be
activated. The whitest flour you can get is mostly just the starch part of the seed.
Depending on which layers are still present, different names are used to describe the
type of flour.


| **USA** | **UK** | {**Germany**} | {**France**} | {**Italy**} |
| --- | --- | --- | --- | --- |
| Cake | Soft flour | T405 | T45 | 00 |
| All purpose | Plain flour | T550 | T55 | 0 |
| Bread flour | Bread flour | T405 or T550 | T45 or T55 | 00 or 0 |
|  |  | T812 | T80 | 1 |
|  |  | T1050 | T110 | 2 |
| Whole | Whole | Vollkorn | T150 | Integrale |

*A comparison of how different types
            of wheat flour are labeled in different countries.*


In Germany, the ash content is used to describe the flours. The lab will burn
100 g of flour in the oven. Then afterwards the remaining ash is extracted
and measured. Depending on the quantity the flour is categorized. If the flour
is of type 405, then 405 of ash have remained after burning the
flour. The more hull parts the flour has, the more minerals remain, therefore the
higher the number, the closer the flour is to whole flour. The numbers are
slightly different between each grain type. Generally though, the higher the
value, the heartier the taste is going to be.


![An overview of a wheat kernel together
      with its content [wheat kernel].](images/wheat-kernel-overview)

*An overview of a wheat kernel together
      with its content [wheat kernel].*


If you compare different grain types, there are grains with high gluten, low gluten
and no gluten. Gluten is what enables bread to have its fluffy consistency.
Without gluten the baked goods wouldn't have the same properties. Managing
gluten makes the whole bread-making process more complex as more steps are involved.

A dough without gluten doesn't have to be kneaded as the role of kneading is
to create
the gluten bonds. The more you knead, the stronger they become. With low-gluten
and no-gluten flours, you only have to mix the ingredients together, making
sure you properly homogenize everything.

During fermentation
the gluten degrades as the microorganisms metabolize it. When too much gluten
has been converted your dough will no longer have the wheat-like structure previously
described. For no/low gluten flour your main focus is managing acidity, you do not
want the final bread to be too sour. Conversely you do not have to worry about
the gluten degradation, removing a huge headache from the equation.


| **Grain type** | **Homogenize** | **Knead** | **Stretch \ | Fold** | **Shape** |
| --- | --- | --- | --- | --- | --- |
| Spelt, Wheat ( 70%) | Yes | Yes | Yes | Yes |  |
| Rye, Emmer, Einkorn, Rice, Corn | Yes | No | No | No |  |

*An overview of different grain
          types and the steps involved in the respective bread making process.*


Because gluten has a special role, the rest of this chapter is dedicated to having a
closer look at different gluten flours and how to distinguish them. Like wheat
spelt contains significant amounts of gluten, so the same characteristics hold
true.

Several recipes call for wheat bread flour, but bread flour can refer to different types
of flour. It could be a T405 or a T550 in Germany—this is very often
classified incorrectly—the terms *strong* or *bread* flour in this case
refer to the properties of the flour. A bread flour is considered to have a
higher amount of protein and thus gluten. This flour is excellent when you
want to make a sourdough bread as your dough allows for a longer leavening
period. As described earlier, the gluten is consumed by your microorganisms.
The more gluten you have, the longer your dough keeps its integrity. If you wanted
to make a cake, you might want to use a flour with less gluten. The gluten binding
properties might not be desirable since the final cake could have a chewy texture.

In conclusion, not every T405, T45 or T00 flour is the same. Depending on the properties
of the plant they come from, the flours will have different properties. For that reason
some countries like Germany have introduced additional scales to evaluate the quality of the
wheat. The category *A* refers to good quality wheat that can be blended
with poorer qualities to improve the flour. The category *B* refers to
average wheat that can be used to create different baked goods. Category *C*
is used for wheat that has poor baking qualities. This could happen, for instance,
if the wheat already started to sprout and thus lost some of its desirable
baking properties. This type of wheat is typically used in animal feed or
as fermentable biomass for generators. Category *E* refers to *Elite* wheat. It's
the highest quality of wheat. This kind of wheat can only be harvested when the
wheat has grown under optimal conditions. You can compare this to a winery
that uses only the best grapes to make a reserve wine. Unfortunately, this is
usually not printed
on the packaging of the flour that you buy. You can look out for the protein
value as a possible indicator. However, large mills blend flours together to
maintain quality throughout the years. Blended flour is also not listed on
the packaging. It might be that bakeries extract gluten from some flour and
then mix it in order to create better baking flours.

In Italy the so-called
*W-value* has been introduced to better show how the flour will behave.
A dough is made, and then the resistance of this dough to kneading is measured.
The more gluten a flour has, the more elastic the dough is, and the more it will
resist kneading. A higher W flour will have a higher gluten content and allow for a longer
fermentation period. But at the same time, it is also harder for the microbes to
inflate the dough as there is more balloon material. To make an excellent fermented
product out of a high W flour you will need to have a long fermentation period.
The long fermentation period also means that your microbes will enrich
your dough with more flavor.


| **W-Value** | **Hydration (%)** | **Uses** | **Fermentation time** |
| --- | --- | --- | --- |
| 0–150 | 50 | Cookies | Very short |
| 150–250 | 50–60 | Cakes, Bread, Pizza | Short–Medium |
| 250–350 | 60–70 | Bread, Pizza | Long |
| 350+ | 70–90 | Bread, Pizza | Very long |

*An overview of different
            levels of W-values and the respective hydration and fermentation
            times.*


Generally, when aiming to
bake free standing sourdough bread, aim for a higher protein content. If the
gluten value is relatively low, your bread will collapse faster. Baking bread
is still possible, but it might be easier to use other techniques such as a
loaf pan, to consider skillet bread or flatbread.

An additional, rarely considered characteristic of good flour is the level of damage to the
starch molecules. This is a common problem when you are trying to mill your own wheat flours at
home. The chances are that your home mill is not able to achieve the same results
a larger mill can. The damaging of the starches is essential to improve the
properties of the dough. You will have better gelatinization and water
absorption with properly damaged starch [starch damage flour]. As more
starch is damaged, the surface area increases. This improves how water interacts with the flour.
This also provides a larger surface that your microbes can use to attack the molecules
and start the fermentation process.

I am still
yet to find a good way of milling my own wheat flour at home. Even after trying to
mill the flour 10 times with short breaks, I was not able to achieve the same
properties as with commercially milled flour. The doughs I would make felt
good, maybe a bit coarse. However, during baking the doughs would start to
de-gas quickly and turn into very flat breads. I have had great success though when
utilizing home-milled flour together with a loaf pan or as a pan bread. If you
have found great ways to work with home-milled flour, please reach out. The potential
of using home-milled flours is huge. It would enable even distant communities
to grow their own wheat and be able to produce amazing freshly baked bread.



---


# Bread types

> In this chapter you will learn about different bread types and their
> advantages and disadvantages.  You can also find very simple recipes for
> flatbread and pan loaf.  The former is probably the most accessible, least
> effort type of bread you can make, while the latter is a little more involved.
> Free standing bread has its own chapter, due to its increased complexity.

## Introduction


In this section we classify bread by its baking techniques. The appearance and
taste will of course be different, but you can get excellent bread with each
of them. Some breads will require investment and technique, as depicted in
the table below.  Flatbread is probably the most
accessible, least effort type of bread you can make. If you are a busy person
and/or don’t have an oven, this might be exactly the type of bread you should
consider.

|  | **Type of bread** |  |  |
| --- | --- | --- | --- |
|  | **Flat** | **Loaf pan** | **Free standing** |
| Cooking method | Pan, fire, barbecue | Oven | Oven |
| Working time | 3 min. | 5 min. | 60 min. |
| Flour types | All | All | Gluten flours |
| Difficulty | Very easy | Easy | Difficult |
| Cost | Low | Medium | High |

*An overview of different bread types
            and their respective complexity.*


## Flatbread


Flatbread is probably the simplest sourdough bread to make.
To make a flatbread no oven is required; all you need is a stove.


![An assorted selection of
      different flatbreads made with sourdough. From left to right:
      Wheat tortilla, rye, spelt and corn.](images/flat-breads-selection)

*An assorted selection of
      different flatbreads made with sourdough. From left to right:
      Wheat tortilla, rye, spelt and corn.*


This type of bread is super simple to make as you can skip
a lot of the technique that is normally required to make wheat doughs.
The flatbread can be made with all kinds of flours. You can even use
flour without gluten, such as corn or rice flour, to make the
dough. To make the flatbread a little more fluffy, you
can use a little bit of wheat flour. The developing gluten
will trap the gases. During baking, these gases will
inflate the dough.

Another trick to improve the texture of the flatbread is to
make a very wet dough. A lot of the water will evaporate
during the baking process and thus make the bread fluffier.
If your water content is very high, it will produce a
pancake-like consistency, as you can see in
the table below


|  | **Flat breads** | **Pancakes** |
| --- | --- | --- |
| Flour | 100 | 100 |
| Water | up to 100 (100%) | 300 (300%) |
| Sourdough starter | 5–20 (5–20%) | 5–20 (5–20%) |
| Salt | 2 (2%) | 2 (2%) |
| Bake when? | Dough increased 50% in size | Bubbles visible on surface |

*Flatbread or pancake recipe for 1 person.
            Multiply the ingredients to increase portion size.  Refer to the
            the relevant section
            "sec:bakers-math" to learn how to understand and
            use the percentages properly.*


For a full recipe including the process of making such a flatbread,   refer to
Subsection

### Flatbread framework


As explained above, if you are just getting started, making a flatbread is the
easiest way to start making great bread at home. With just a
few steps, you can stop buying bread forever. This works with
any flour, including gluten-free options.


**Flowchart:** *The process of making a flatbread is very
      simple, requiring very little effort. This type of bread is especially
      handy for busy bakers.*


This is my go-to recipe that I use to make bread whenever
I have little time or when I am abroad. You can choose
between two options:
1. A flatbread similar to a roti or naan bread
2. Sourdough pancakes.

To get started prepare your sourdough starter. If it has not been used for a very
long time, consider giving it another feed. To do so, simply take 1 g of your
existing sourdough starter and feed it with 5 g of flour and 5 g of water.
If you do this in the morning, your sourdough starter will be ready in the evening. The
warmer it is, the sooner it will be ready,  consider
using warm water if it is very cold where you live.


![A flatbread made with purely wheat flour. The
      dough is drier at around 60% hydration. The drier dough
      is a little harder to mix. As wheat contains more gluten, the dough
      puffs up during the baking process.](images/flat-bread-wheat)

*A flatbread made with purely wheat flour. The
      dough is drier at around 60% hydration. The drier dough
      is a little harder to mix. As wheat contains more gluten, the dough
      puffs up during the baking process.*


This way you should have around 11 g of sourdough ready in the evening. You will have
the perfect quantity to make a dough for one person. In case you want to make more
bread, simply multiply the quantities shown in
the table below.

Then in the evening simply mix the ingredients as shown in the table. Your dough
is going to be ready in the morning. It's typically ready after 6–12 hours. If
you use more sourdough starter it will be ready faster, conversely it will take
longer if you use less. Try to aim for a fermentation time of 8–12 hours as
by using your dough too soon, the flavor might not be as good. By using your
dough later it might become a little more sour. The best option is to
experiment and see what you personally like the most.

After mixing the ingredients together cover the container, this prevents the
dough from drying out and makes
sure no fruit flies get access. A transparent container will be helpful
when getting started. You can observe the dough more easily and see when
it is ready.


![An Ethiopian woman baking an *injera*
      made using teff flour.  The image has been provided by Charliefleurene
      via Wikipedia.](images/ethiopian-woman-checking-bread)

*An Ethiopian woman baking an *injera*
      made using teff flour.  The image has been provided by Charliefleurene
      via Wikipedia.*


If you used the flatbread option with less water, look at the size increase
of your dough. It should have increased at least 50% in size.
Also look out for bubbles on the sides of your container.

When using the pancake recipe, look out for bubbles on the surface of your dough.
In both cases use your nose to check the scent of your dough. Depending
on your sourdough starter's microbiome your dough will have
dairy, fruity, alcoholic notes or vinegary, acetic notes. Relying
on the smell of your dough is the best way to judge whether your
dough is ready or not. Timings are not reliable as they
depend on your starter and the temperature. If your dough
is ready too soon, you can now move it directly to the fridge and bake
it at a later, more convenient time. The low temperature will halt the fermentation
process[^1]
and your dough will last for several days. The longer you wait, the more sour the
bread is going to be. The fridge is a great option in case you want to
take the dough with you when visiting friends. People are going
to love you for the freshly baked flatbreads or pancakes. If you dare,
you can also taste a little bit of your raw uncooked dough. It is likely
going to taste relatively sour. I do this frequently to better evaluate the
state of my doughs.


![A sourdough pancake made with teff flour.
      The pockets come from evaporated water and CO₂ created by the
      microbes.  The image has been provided by Łukasz Nowak via Wikipedia.](images/injera-pancake-texture.jpg)

*A sourdough pancake made with teff flour.
      The pockets come from evaporated water and CO₂ created by the
      microbes.  The image has been provided by Łukasz Nowak via Wikipedia.*


If you are feeling lazy or don't have time, you could also use older sourdough starter
to make the dough directly without any prior starter feedings. Your sourdough starter
is going to regrow inside your dough. Remember that the
final bread might be a bit more on the sour side as the balance of yeast to
bacteria could be off. In the the table below
I recommended using around 5–20%
of sourdough starter based on the flour to make the dough. If you were to follow
this approach, just use around 1% and make the dough directly.
The dough is probably going to be ready 24 hours later, depending on the temperature.

If you want to make sweet pancakes, add some sugar and optional eggs to your dough
now. A good quantity of eggs is around one egg per 100 g of flour.
Stir your dough a little bit and it will be ready to be used. You'll
have delicious sweet savory pancakes, the perfect combination. By
adding the sugar now, you make sure that the microbes don't have
enough time to fully ferment it. If you had added the sugar
earlier, no sweet flavor would be left  12 hours later.

To bake your dough heat your stove to medium temperature. Add a little bit of
oil to the pan. This helps with heat distribution and ensures even cooking.
With a spatula or a spoon place your dough in the pan. If your dough
was sitting in the fridge, bake it directly. There is no need to wait for your
dough to come to room temperature. If you have a lid,
place it on your pan. The lid helps to cook your dough from the top.
The evaporating water will circulate and heat up the dough's surface. When
making a flatbread, make the dough around 1 thick. When using the
pancake option, opt for around 0.1–0.5 depending on what you
like.


![The crumb of a flatbread made with einkorn as flour.
      Einkorn is very low in gluten and thus does not trap as much CO₂ as
      a wheat based dough. To make the dough fluffier use more water or
      consider adding more wheat to the mix of your dough.](images/einkorn-crumb.jpg)

*The crumb of a flatbread made with einkorn as flour.
      Einkorn is very low in gluten and thus does not trap as much CO₂ as
      a wheat based dough. To make the dough fluffier use more water or
      consider adding more wheat to the mix of your dough.*


After 2–4 minutes flip over the pancake or flatbread. Bake it for the same
time from the other side. Depending on what you like, you can wait a little
longer to allow the bread to become a bit charred. The longer you
bake your bread, the more of the acidity is going to evaporate. If your
dough is a bit more on the sour side, you can use this trick to balance
out the acidity. This really depends on which flavor you are looking for.

When making a flatbread I recommend wrapping the baked flatbreads in a kitchen
towel. This way more of the evaporating humidity stays inside of your bread,
making sure your flatbreads stay nice and fluffy for a longer period after the
bake. A similar strategy is used when making corn tortillas.

You can safely store the baked flatbreads or pancakes in your fridge
for weeks. When storing make sure to store them in an airtight plastic bag so that
they do not dry out. If they dry out, spray them with some water and toast them.
They will be almost as good as when they were freshly baked.

Keep a little bit of your unbaked dough. You can use it to make the next
batch of bread or pancakes for the next day. If you want to bake a few days later, add
a little bit of water and flour and store this mixture in your fridge
for as long as you like[^2].

### Simple flatbread recipe


By following the steps outlined in this section,
you'll be introduced to a versatile bread that's perfect for a myriad of
culinary applications. Whether you're scooping up a savory dip,
wrapping a flavorful filling, or simply enjoying a piece with a drizzle
of olive oil, these flatbreads are sure to impress.

recipes/flat-bread.tex

## Loaf pan bread


Loaf pan bread is made using the help of a special loaf pan
or loaf tin. The edges of the pan provide additional support
for the dough to rise. Making a bread using a loaf pan requires
an oven.


![A freestanding bread and a wheat
      loaf pan bread. Both of them received a small incision before baking
      which helps to control how they open up.](images/loaf-pan-free-standing.jpg)

*A freestanding bread and a wheat
      loaf pan bread. Both of them received a small incision before baking
      which helps to control how they open up.*


After mixing your dough, you can place it directly into the loaf pan.
This makes the whole process simpler since you can skip steps such
as shaping the dough.

To make a great loaf pan bread with little work:

1. Mix the ingredients of your dough (gluten free works too)
2. Place into the loaf pan
3. Wait until your dough has roughly doubled in size
4. Bake in a non pre-heated oven for around 30–50 minutes

Knowing the exact baking time is sometimes a little challenging
as it might be that the outside of your bread is cooked but
the inside is still raw. The best way is to use a thermometer
and measure the core temperature. At around  92°C
(197°F) your dough is done. I generally bake loaf pan bread at
around  200°C (390°F), which is a little less
than my freestanding bread which I bake at  230°C
(445°F). That's because it takes a while for the dough
to bake properly inside the loaf pan. The edges don't heat up
as quickly. Then the top part of the dough is properly cooked, while
the inside isn't yet. When baking make sure to use steam
or simply place another equally sized loaf pan on top
of your loaf pan. This way you simulate a Dutch oven. The dough's
evaporating moisture will stay inside.

A good trick to make excellent loaf pan bread is to make a very
sticky dough. You can opt for a hydration of 90–100%, almost
resembling a default sourdough starter. Just like with flatbread,
the high humidity helps to make a more airy, fluffy crumb. The bread will
also be a bit chewier. This type of bread made with rye is my family's favorite
style of bread.  The hearty rye flavor paired with the sticky consistency really
makes an excellent sandwich bread.

To improve the structure you can also consider using around 50%
wheat flour in your mix. The gluten network will develop as your
dough ferments and allow for more gas to be trapped in the dough.

A common problem you will face when making a loaf pan bread is
the dough sticking to the pan. Use a generous amount of oil to grease
your pan. A nonstick vegetable oil spray can do wonders.
Don't clean your loaf pans with soap. Just use a kitchen towel
to clean them. With each bake a better patina forms, making your
pan more and more stick resistant.

What's amazing about this type of bread is that it works
with every flour. The overall time to work the dough is probably
less than 5 minutes, making it very easy to integrate
into your daily routine. Furthermore, loaf pans use the space
in your oven very efficiently. Using pans I can
easily bake 5 loaves at the same time in my home oven.
Normally I would need multiple baking sessions for
freestanding loaves.

## Free standing bread

A freestanding loaf is baked entirely without supporting
baking vessels in your oven. To make a freestanding loaf more steps
and tools are required.


![A freestanding sourdough bread. Note
      the incision known as an *ear* and the oven spring clearly
      distinguish this type of bread from flatbread and loaf pan bread.](images/free-standing-loaf.jpg)

*A freestanding sourdough bread. Note
      the incision known as an *ear* and the oven spring clearly
      distinguish this type of bread from flatbread and loaf pan bread.*


When using wheat, make sure to mix your dough enough to develop a gluten network.
Allow the dough to reach a certain size increase during the fermentation.
Afterward, divide and pre-shape the dough into the desired visual shape you
would like. Each shape requires a different technique. Sometimes achieving
the right shape can be challenging. Making a baguette, for instance,
requires performing more steps. Mastering this technique takes several attempts.

Once the dough is shaped, it is proofed again for a certain
period of time. Once the dough is ready, a sharp tool such
as a razor blade is used to make an incision into the dough.
This helps control how the dough opens up during the baking process.

All these steps require practice. Each of them has to be
performed perfectly, without mistakes.
But after baking you will be rewarded with a beautiful bread
with great taste and consistency.

There is a dedicated recipe and tutorial for this type of bread in the
ch:wheat-sourdough chapter.

---

[^1]: There are some exceptions. In some rare cases your starter
might also work at lower temperatures. You might have cultivated microbes that work best at
low temperatures. Nevertheless, fermentation
is always slower the colder it gets. A fridge really helps to preserve the state
of your dough.

[^2]: The starter will stay good for months. If you expect to
leave it longer, consider drying a little bit of your sourdough starter.



---


# Wheat sourdough


> In this chapter, you will learn how to make
> freestanding wheat sourdough bread.


![A freestanding sourdough bread
      next to bread made in a loaf pan.  Freestanding sourdough is considered
      the supreme discipline of sourdough bread by many bakers.](images/loaf-pan-free-standing.jpg)

*A freestanding sourdough bread
      next to bread made in a loaf pan.  Freestanding sourdough is considered
      the supreme discipline of sourdough bread by many bakers.*


Freestanding sourdough bread is my favorite
type of bread. It combines a great crunchy crust, superb
flavor, and a soft fluffy crumb. This is the type of bread
that is being inhaled by my friends and family. Unfortunately,
making this type of bread requires a lot more effort, patience,
and technique than other types of bread. You have to perfectly
balance the fermentation process. You cannot ferment for too
short and also not for too long. The techniques you need to
learn also require a bit more skill. It took me several attempts
to get this right. I faced several challenges: I had the wrong flour.
I didn't properly know how to use my oven.
When should I stop the fermentation? There is a lot of information
out there. I dug through most of it and have tried almost everything.
In many cases the information was wrong; in other cases, I found another
valuable puzzle piece. Aggregating all this
information was one of my main motivations to start `The Bread Code`.
My key learning was that there is no recipe that
you can blindly follow. You will always have to adapt the recipe
to your locally available tools and environment.

But do not worry. After reading this chapter you will know all the signs to
look out for. You will be able to read your dough.  You will turn into a
confident hobby baker who can bake bread at home, at high altitudes, at low
altitudes, in summer, in winter, at your friend's place, and even on vacation.
Furthermore, you will know how to scale your production from one loaf to
hundred loaves of bread.  If you ever wanted to open up a bakery, consider
this knowledge to be your foundation.

Mastering this process will enable you to make amazing bread
that tastes much better than any store-bought bread.

## The process


**Flowchart:** *The typical process of making a wheat-based sourdough bread.*


The whole process of making great sourdough bread starts with
readying your sourdough starter. The key to mastering
this process is to manage the fermentation process properly.
For this, the basis is to have an active and healthy
sourdough starter.

Once your starter is ready, you proceed to mix all the ingredients.
You want to homogenize your sourdough starter properly. This
way you ensure an even fermentation across your whole dough.

After a short break, you will proceed and create dough strength.
Kneading will create a strong gluten network. This is essential
to properly trap the CO₂ created during the fermentation.

Once you've kneaded, the bulk fermentation starts. It is called bulk fermentation
because you typically ferment multiple loaves together in one bulk.
Understanding when to stop this step will take some practice.
But nothing to worry about, you will learn the exact signs to look out for.

Once this is completed you need to divide your large blob of
dough into smaller pieces and pre-shape each piece. This allows
you to apply more dough strength and shape more uniform loaves.

The proofing stage follows where you finish the fermentation process.
Depending on your time you can proof it at room temperature or in the fridge.
Mastering proofing will turn your good loaf into a great loaf.

Lastly, you will finish the whole process by baking. You will learn different
options on how to properly steam your dough. This way your
dough will have a beautiful oven spring. During the second
stage of the baking process, you will finish building your crust.

All the steps rely on each other. You will need to get each of
the steps right to make the perfect bread.

## Readying your starter


The most crucial part of the bread-making process is your starter.
The starter is what starts the fermentation in your main dough.
If your starter is off, then your main dough is also going
to cause trouble during the fermentation. Your starter's
properties are passed on to your main dough. If your starter
doesn't have a good balance of yeast to bacteria, neither will your
main dough.


**Flowchart:** *The process to check
      your sourdough starter when making wheat-based doughs. In practice
      I frequently use a stiff sourdough starter. The stiff starter features
      enhanced yeast activity. In that case, you can use the same ratios as
      shown in the chart except for the water quantity. The stiff starter has
      a hydration of 50–60%. So you would have half the
      shown water quantities, i.e., if the chart shows 100 g of
      water, use 50–60 of water for your stiff starter.*


Generally, think of the dough you are mixing as a big starter with salt.
After mixing all the ingredients, you have a green field environment again.
The yeast and bacteria start to fight again to outcompete each other.
There is plenty of food available, and they all do their best to win.
Depending on the starter you mix into your dough, some of the microorganisms
might have an advantage over others.

The first option to achieve a good balance is to apply feedings.
If your starter hasn't been fed in a long period, the
bacteria dominate. This happens if your starter has been
sitting unused in the fridge, for instance. As more and more
acidity piles up, the environment is becoming more and more hostile
to the yeast. The lactic acid bacteria tolerate this environment
better. Your dough fermentation would be more on the
bacterial side with this starter. By applying a couple of
feedings, the yeast becomes more active. The older your
starter, the more acid resistant the yeast becomes. Initially,
I had to feed my starter 2–3 times to fix the balance. With my
more mature starter, one feeding seems to be enough to balance
the microorganisms.

Some people use a 1:1:1 ratio to refresh the starter. This would
be one part of the old starter (10 g for instance), 1 part of flour,
and one part of water. I think this is utter rubbish. As mentioned
your starter is a miniature dough. You would never opt for a 1:1:1 ratio to
make dough. You might use a maximum of 20% starter to
make dough. That's why I advocate using a 1:5:5 ratio or a
1:10:10 ratio depending on how ripe your starter is. As I almost
always use a stiffer sourdough starter due to its enhanced
yeast fermentation advantages (see the relevant section)
my ratio is never 1:5:5. My ratio would be 1:5:2.5 (1 part old starter,
5 parts flour, 2.5 parts water). If it is very warm where you live
you could opt for the aforementioned 1:10:5 or 1:20:10. This
way you slow down the ripening of your starter. You can also use this
trick to make starter feeding work with your schedule.
If your starter is typically ready in 6 hours but today you need it
ready later, simply increase how much flour/water you feed your starter.
These are all values that you need to experiment with on your own.
Every starter is unique and might behave slightly differently.

The second option at your disposal is the starter quantity that
you use to make the dough. As previously stated your starter
regrows inside of your main dough. While I would normally use
10–20% of starter based on the flour, sometimes I go
as low as 1% starter. This way the microorganisms have
more room to balance out while fermenting the dough. If my sourdough
starter has not been fed in a day, I might use 5% of sourdough
to make a dough. If I push this to 2 days without feedings,
I lower the starter amount even further. I would opt for the
previously mentioned 1% starter. If the food is very scarce,
your microorganisms will sporulate. They need to regrow again
from the spores they created. In this hibernation state, it takes
longer for them to become fully active again. I have tried
several times to make dough directly out of a dry starter.
I wasn't successful because the fermentation took too long.
The microorganisms had to regrow from spores and then begin
the fermentation. As explained earlier there is a limit to
fermentation times as your dough naturally breaks down.
Furthermore, you want your microorganisms to outcompete
other pathogens contained in the flour. The less starter
you use, the easier it is for them to reproduce. A strong
starter will outcompete other germs. While the method of
reducing the starter works, I recommend Option 1 more.
It will reliably create better bread. Option 2 is typically
what I use when I fed my starter in the morning but didn't
manage to make a dough in the evening. I don't want to feed
my starter again the next morning. I would like to make a dough
directly without waiting and thus use less of the very ripe starter.

Over time you will become more accustomed to your starter
and how it behaves. You will be able to read the signs of its
activity and judge its state.

## Ingredients

All you need to make great sourdough bread is flour, water, and salt. You
can of course add additional things to your dough such as seeds. I personally
enjoy the hearty taste of whole-wheat. Thus I like to add around
20–30% of whole-wheat flour to the mix. You could also
make this recipe with 100%
whole-wheat flour directly. In this case, look out for strong whole-wheat
flour that is made from flour with higher protein. If you don't like whole-wheat
you can omit the flour from the recipe. Simply replace the listed
quantity with bread flour. One thing to consider about whole-wheat
flour is its increased enzymatic activity. By adding some whole-wheat
flour you will speed up the whole fermentation process.

Especially when getting started I recommend using bread flour which
contains more gluten than all-purpose or cake flour. This is essential
when trying to bake a freestanding loaf with sourdough.

Find below an example recipe for one loaf including baker's math calculation:

- 400 g of bread flour
- 100 g of whole-wheat flour
- *Total: 500 g of flour*
- 300–450 of room temperature water (60% up to 90%). More on this topic in the next chapter.
- 50 g of stiff sourdough starter (10%)
- 10 g of salt (2%)

In case you want to make more bread simply increase the quantities based on
how much flour you have. Let's say you have 2000 g of flour available. The
recipe would look like this:

- 1600 g of bread flour
- 400 g of whole-wheat flour
- *Total: 2000 g of flour*, equaling 4 loaves
- 1200 g up to 1800 g of room temperature water (60 to 90%)
- 200 g of stiff sourdough starter (10%)
- 40 g of salt (2%)

This is the beauty of baker's math. Simply recalculate the percentages, and you
are good to go. If you are unsure about how this works, please check out the
full the relevant section which looks at the topic in detail.

## Hydration

Hydration refers to how much water you use for your flour. When
beginning to make bread, I always got this wrong. I followed a recipe from the
internet, and my dough never looked like the dough shown in the recipe.
The amount of water your flour requires is not fixed. It depends on the flour
you have.

When a seed gets into contact initially, the outer layers soak up the water.
That's why when using whole-wheat (still containing these layers) you have to
use a little bit more water.

By forming gluten strands, water is absorbed into your dough's gluten matrix.
The higher the protein value, the more water can be used.

Some bakers like to use highly hydrated doughs to create fluffier
bread[^1].
The reason for this
is the dough's improved extensibility. The wetter the dough, the easier it is
for the dough to be stretched. When you pull it, the dough will hold its
shape. In comparison, a very stiff (low hydration) dough will maintain its
shape for a longer period. To visualize this, think of your extensible
dough as a balloon. The stiff dough is like a car tire.
The yeast has a much harder time inflating the car tire compared to the balloon.
That’s because the rubber of the car tire is much less extensible.
It requires much more force to inflate the tire. For this reason,
an extensible dough will inflate more in the oven. The loaf will
be visually bigger and offer an airier more open crumb structure.

While this might sound great, the high hydration causes several side effects.

1. Your dough becomes more difficult to handle. Your dough will be stickier.
2. Your dough has to be kneaded for longer to build a proper gluten network.
3. During the fermentation your dough might become too extensible and lose some of the dough strength. To circumvent this, stretch and folds are applied compared to regular dough, requiring you to invest a lot more work.
4. Shaping becomes much more of a hassle as the dough is very sticky.
5. The dough can stick to the banneton a lot easier while proofing.
6. If you wait too long during proofing, the dough won't have enough strength left to pull upwards and will stay flat.
7. Generally, the higher the water content, the more bacterial fermentation you have. Thus a wetter dough will reduce gluten faster than a stiffer dough. This is why you have to start the fermentation with a sourdough starter in perfect shape. Bakers use a process called autolysis to shorten the main fermentation time to circumvent this.
8. The crumb, in the end, might be perceived as somewhat sticky. It still contains a lot of water. I love this crumb, but this comes down to personal taste.

To achieve a high-hydration dough, it is best to slowly add water to
your dough. Start with 60% hydration, then slowly add a bit more water. Knead
again until the water is absorbed. Repeat and add more water. As your dough
has already formed a gluten network, new water can be absorbed much easier.
You will be surprised by how much water your dough can soak up. This
method is commonly known as the bassinage method. More on that later.
By opting for this technique, I was easily able to push a low-gluten flour
to a hydration of 80%. This
is also my method of choice when making dough now. I keep adding water until
I can feel that the dough has the right consistency. As you bake more bread,
you will develop a better look and feel for your dough. When mixing
by hand this can be quite cumbersome. It is a lot easier when using a stand
mixer.

All in all, increasing hydration requires a lot of trial and error. There
is however one option that makes things easier and causes fewer headaches:
Slow fermentation. You get the same extensibility advantages the high hydration
offers by simply letting your dough ferment for a longer period.
Slowing the fermentation process is easy. Use less
sourdough starter or ferment in a cooler environment.

There are two reasons for the slow fermentation advantages.  As explained
earlier, both the protease enzyme and bacteria break down your gluten network.
So as fermentation progresses, your dough will automatically become more
extensible. This is because the rubber layers of your car tire are slowly
converted and eaten. Ultimately your car tire turns into a balloon that can
very easily be inflated. When waiting too long, the balloon will burst. You
will have no gluten left anymore, and your dough becomes very sticky. Finding
the sweet spot of enough rubber eating and not too much is what the perfect
wheat sourdough bread is about. But don't worry—after reading this chapter
you will have the right tools at your disposal.

The advantages of slow fermentation can be nicely observed when experimenting
with a fast-fermenting yeast dough (1% dry yeast based on flour). The
crumb of such a dough is never as
open as a dough made with sourdough. Furthermore, the protease enzyme
cannot do its job within such a short fermentation period.
Large industrial bakeries add active malt which contains a
lot more enzymes. This way the time required to make the dough is shortened. You
will most likely find malt as an ingredient in supermarket bread. It is a
great hack. The baked turbo fermentation bread will feature a relatively dense
and not fluffy crumb. That is because only very little gluten is broken down when
finishing the fermentation period in 1 hour. If you were to slow things down,
the dough would look completely different.
Try this again and use much less yeast. This is the
secret of Neapolitan pizza. Only a tiny bit of yeast is used to make the
dough. My default pizza recipe calls for around 150 of dry
yeast per \kg of flour. Give it a shot yourself the next time you
make a yeast-based dough. Try to push the fermentation to at least 8 hours.
The difference is incredible. You will have made bread with a much more
fluffy and open crumb. The flavor of the dough is drastically improved. Your
crust becomes crisper and features a better taste. This is because amylases have
converted your starches into simpler sugars which brown better during baking.
If you only learn one thing from this book, it is that slow fermentation is
the key to making great bread.

For this reason, my default hydration is much lower than the hydration of other
bakers. I prefer slower fermentation for my recipes.
The sweet spot for my default flour is at around 70% hydration.
Again, this is a highly subjective value that works for my flour.

If you are just getting started with a new batch of flour,
I recommend conducting the following test. This will help you to
identify the sweet spot of your flour's hydration capabilities.

Make five bowls with each 100 g of flour. Add different slightly
increasing water amounts to each of the bowls.

- 100 g of flour, 55 g of water
- 100 g of flour, 60 g of water
- 100 g of flour, 65 g of water
- 100 g of flour, 70 g of water
- 100 g of flour, 75 g of water

Proceed and mix the flour and water mixture until you see that there
are no chunks of flour left. Wait 15 minutes and return to your dough.
Carefully pull the dough apart with your hands. Your dough should be elastic, holding
together very well. Stretch your dough until very thin. Then hold it against a light.
You should be able to see through it. The flour-water mixture that breaks without
seeing the windowpane is your no-go zone. Opt for a dough with
less hydration than this value. You will know that your flour mix can go up to
 65% hydration, for instance. Use the leftovers of this experiment
to feed your starter.


![The window pane test allows you to see if you
      developed your gluten well enough.](images/window-pane-effect)

*The window pane test allows you to see if you
      developed your gluten well enough.*


From an economic perspective, water is the cheapest component in your bread
dough. When running a bakery, a higher hydrated dough will weigh more and have
lower production costs. The profit will be higher. This comes at the price
of increasing labor costs and more potential failures due to the enhanced
difficulty.

## How much starter?

Most bakers use around 20% sourdough starter based on the
flour weight.  I recommend going much lower, to around
5–10%.

By adjusting the amount of pre-ferment you can influence the time your dough
requires in the bulk fermentation stage. The more starter you use, the faster
this process is. The smaller the starter quantity, the slower. With a higher
quantity of starter, you are introducing more microorganisms to your main
dough. The higher this quantity, the faster the rate of fermentation in your
dough is.

The other factor influencing the rate of fermentation is the temperature of
your dough. The warmer the temperature, the faster the process; the colder, the
slower the process.

While food is available, the microorganisms will reproduce and increase in
quantity. The process is self-limiting: it stops when there is no
more food available. This can be compared to wine making where
the yeast ultimately sporulates and dies as ethanol levels increase. The ethanol creates an
environment that makes it impossible for other
microorganisms to join the feast. The same thing happens with the acidity
created by the bacteria. The high acidity slows the fermentation process and
prevents new microorganisms from entering the system.

Initially, your starter's properties are carried over to the main dough. Then,
as time progresses, the microorganisms adapt to the new environment. If your
starter is very bacterial then your main dough's fermentation will also be. You
end up with a dough that is not as fluffy as it could be. It will taste quite
sour, too sour for most people.

If you were to use an extreme value of around 90% starter based on your flour, there
would be very little room for the microorganisms to adjust in the main dough.
If you were to just use 1%, your microorganisms can regrow into a
desirable balance in the dough. Furthermore, you need to consider that a high value
of starter means a high inoculation with already fermented flour. As
mentioned earlier, enzymes break down the dough. This means the higher this
value, the more broken-down fermented flour you have. A too-long fermentation
always results in a very sticky dough that cannot be handled. The more
starter you use, the faster you will get to this point. If you were to use a
very little amount of starter, your flour might have naturally broken down
before the fermentation has reached the desired stage. You can observe this
when using a small quantity of around 1% sourdough starter. The small
amount of added microorganisms will not be able to reproduce fast enough
before the protease has broken down your dough completely.

As explained earlier the key to making great bread is a slow but not too slow
fermentation. Enzymes require time to break down your dough. Taking all this
into consideration, I try to aim for a fermentation time of around 8 to 12 hours. This seems to be
the sweet spot for most of the flours that I have worked with. To achieve this,
I use around 5% of sourdough starter in summer times
(temperatures around 25°C (77°F) in the
kitchen). In winter times I opt for around 10% up to
20% sourdough starter (kitchen temperature around
20°C (68°F)). This
allows me to use a sourdough starter that's not in perfect condition. As
explained earlier, your
bread dough is essentially a gigantic starter. The low inoculation rate allows
the starter to regrow inside your main dough into a desirable balance.
Furthermore, the enzymes have enough time to break down the flour. This also
allows me to skip the so-called autolysis step completely (more in the next section).
This greatly simplifies the whole process.

## Autolysis


Autolysis describes the process of just mixing flour and water and letting
this sit for a period of around 30 minutes up to several hours. After this
process is completed, the sourdough starter and salt are added to the
dough[^2].

The overall time that flour and water are in contact is extended. Thus you get the
beneficial enzymatic reactions that improve the taste and characteristics of the
dough. I do not recommend autolysis as it adds an unnecessary step to the
process. Instead, I recommend the fermentolysis technique which will be covered in the
next section of this book.

The effects of autolysis are very interesting. Try to mix just flour and
water and let that sit for a day. During the day, check the consistency of
your dough. Try and stretch the dough. If you dare, you can also taste the
dough throughout the day. With each hour, your dough will become
more extensible. It will be easier to stretch the dough. At the same time, your
dough will start to taste sweeter and sweeter. The protease and amylase enzymes
are doing their job. The same process is used when making oat milk. By letting
the mixture sit for some time, enzymes work on the oats. The taste is perceived as
sweeter and more appreciated. This process is further accelerated the more
whole-grain your flour is. The hull contains more enzymes. The gluten network
will ultimately tear, and your dough flattens out. For wheat sourdough, this is
your worst enemy. When this happens, your dough will become leaky and release
all that precious gas created during the fermentation. You need to find the
right balance of your dough breaking down just enough and not too much.

When you use a high inoculation rate of around 20% sourdough starter
your fermentation can be very quick. At 25°C it could be finished in as little as 5 hours.
If you ferment longer, your dough becomes leaky. At the same time, in
these 5 hours, the enzymes have not broken down the flour enough. This means
the dough might not be as elastic as it should be. Furthermore, not enough
sugars have been released and thus the flavor after baking is not good
enough[^3]. That's why bakers opt for autolysis. The autolysis starts the enzymatic
reactions before the microorganism fermentation begins. This way after 2 hours
of autolysis (an example) and 5 hours of fermentation the dough is in the
perfect state before beginning proofing.

When you try to mix your salt and starter into the flour/water dough you will
notice how cumbersome this is. It feels like you have to knead again from scratch
one more time. You will spend more time mixing dough.

For that reason, I am strongly advocating utilizing the fermentolysis approach
which greatly simplifies the mixing and kneading process.

## Fermentolysis


The fermentolysis creates the same advantageous dough properties the
autolysis creates without the headache of mixing your dough twice. You do this
by extending the fermentation time of your dough. Rather than doing a 2-hour
autolysis and 5-hour bulk fermentation you opt for an overall 7-hour
fermentation period.

To do this, you use less sourdough starter. A conventional recipe including the
autolysis step might call for 20% sourdough starter. Simply reduce this
value to 5–10%. The other option could be to place the dough in a colder
environment and thus reduce the speed at which your microorganisms replicate.


| S[table-format=2.0] S[table-format=2.1]@{}} | **Amount (%) for a starter** |  |
| --- | --- | --- |
|  **°C / °F** | **Recently fed** | **Starving** |
| 30 / 86 | 5 | 2.5 |
| 25 / 77 | 10 | 5 |
| 20 / 68 | 15 | 10 |

*A table visualizing how much sourdough
            starter to use depending on temperature and the starter's activity
            level.*


Based on my experience and my sourdough, my ideal bread always takes around 8
to 12 hours during bulk fermentation. Based on my availability throughout the
day, I use a higher or lower starter quantity. If I wanted to achieve a
completed fermentation in 8 hours, I would opt for a 10%
sourdough starter. If I wanted it to be ready in 12 hours, I would opt for
less starter, around 5%.  Simply mix all the ingredients and
your fermentation begins. The enzymes and microorganisms commence their work.
On a very warm summer day, the mentioned quantities no longer work. With a
10% starter, the same dough would be ready in 5 hours up to a
point of no return. Another additional hour would cause the dough to break
down too much. In this case, I would opt for 5% sourdough
starter to slow the whole process down to reach the 8 to 12 hour window again.
If it is very hot, I might use as little as 1% sourdough
starter[^4]. You have to play with the timings on your
own.  Rather than relying on timing though, I will show you a much better and
more precise approach by using a fermentation sample. This will be covered
later in this chapter.

Even for yeasted doughs, I no longer use autolysis. I just reduce the amount
of yeast that I am using. Opting for the fermentolysis will
save you time and simplify your bread-making process. As mentioned in previous chapters,
the secret to making great bread is a slow but not too slow fermentation.

## Dough strength

Dough strength is a fancy way to describe the bread-kneading process. As you wait and
knead, the gluten bonds in your dough become stronger. The dough
becomes more elastic and holds together better. This is the basis for trapping
all the gases during the fermentation process. Without the gluten network,
the gases would just diffuse out of your dough.


**Flowchart:** *The gluten development process for a wheat-based dough.*


It might sound odd, but the most important part of kneading is waiting. By
waiting you are allowing your flour to soak up water. This way the gluten
bonds of your dough form automatically and your dough becomes more elastic.
So you could be kneading for 10 minutes initially just to be surprised
that kneading 5 minutes and waiting 15 minutes has the same effect.

The gluten proteins glutenin and gliadin virtually instantly bond after being
hydrated. Disulfide bonds enable the longer portions of
glutenin to join with one another and form sturdy, extensible molecules.
Glutenins add strength, whilst the more compact gliadin proteins allow
the dough to flow like a fluid. Ultimately, the longer you wait, the more
your gluten network transforms into a web-like structure. This is what
traps the gases during the fermentation process [how does gluten work].


*A schematic
      visualization of automatic gluten development. The doughs are not
      kneaded, just initially mixed.  Note how dough strength deteriorates
      over time as enzymes break down the flour. The effect is accelerated for
      sourdough due to the bacteria's gluten proteolysis.*


The soaking process has to be extended the more whole-wheat flour is used.
The purpose of the wheat kernel's outer bran is to soak up water as fast
as possible. The enzymes become activated and start the sprouting process.
Because of this, less water is available for the gluten bonds to develop.
Either wait a bit longer or proceed and use slightly more water for
the dough.

This is the same principle that popular no-knead recipes follow. By making a less
hydrated dough and waiting your gluten network automatically forms. You still
have to mix and homogenize the ingredients. You wait a few minutes just to
find your dough having developed incredible dough strength with no additional
kneading[^5].

If you over-hydrate your dough at the beginning it becomes more difficult
for the gluten chains to form. The molecules are not as close together in
a wetter dough compared to a stiffer dough. It is harder for the molecules
to align and form the web structure. For this reason, it is always easier
to start with lower hydration and then increase the water quantity if needed.
This is also commonly known as the *Bassinage method*. The gluten
bonds have formed at the lower hydration and can then be made more extensible
by adding water and kneading again. This is a great trick to make
a more extensible dough with lower-gluten flour [bassinage technique].

When machine kneading a dough, opt for the same technique shown in
the flowchart.  Initially opt for a low
speed. This helps the homogenization process.
After waiting to allow the flour to soak up the water, proceed on a higher speed
setting. A good sign of a well-developed gluten network is
that your dough lets go of the container. This is because of the gluten's elasticity.
The elasticity is higher than the desire of the
dough to stick to the container.


![A schematic visualization
      of gluten development in sourdoughs with different kneading techniques.
      A combination of techniques can be utilized to achieve maximum dough
      strength.](images/dough-strength-sourdough)

*A schematic visualization
      of gluten development in sourdoughs with different kneading techniques.
      A combination of techniques can be utilized to achieve maximum dough
      strength.*


Generally, the more dough strength you create, the less sticky your dough is going to
feel. As the dough holds together, it will no longer stick to your hands as
much. This is a common problem beginners face. Sticky dough is frequently
the sign of a not well enough developed gluten network.


![A schematic visualization of how a rough
      dough surface creates more touch points compared to a smooth dough
      surface.  By touching the rough surface the dough will swell and get into
      contact with more areas of your hand.](images/dough-surface-touchpoints)

*A schematic visualization of how a rough
      dough surface creates more touch points compared to a smooth dough
      surface.  By touching the rough surface the dough will swell and get into
      contact with more areas of your hand.*


Kneading more is generally beneficial in almost all cases, as it results in a
stronger gluten network. However, when making soft milk breads, you might prefer
a more extensible dough from the start. In this scenario, excessive kneading
could lead to a chewier final bread, which is not desirable if you aim for a
fluffier texture. Achieving this fluffier dough can be accomplished by kneading
less. While this is an exception, properly kneading your wheat-based doughs
is generally advised.

When you use a stand mixer, you can run into the issue of kneading too much. This
is almost impossible in practice though. Even after kneading for 30 minutes on medium
speed, my doughs hardly ever were over-kneaded. The moment you knead
too much, the color of the dough can begin to change. You mostly
notice this, though, during baking. The resulting loaf looks very
pale and white. This is because mixing dough causes oxidation,
which is necessary for the development of gluten.
However, if the dough is mixed too much, the compounds that contribute
to the bread's flavor, aroma, and color may be destroyed, negatively
affecting the quality of the bread [oxidization dough].

The last step before beginning bulk fermentation is to
create a smooth dough ball. By making sure your dough's surface is
smooth, you will have fewer touch points when touching the dough.
See the figure for a schematic visualization
of how your hand touches a rugged and smooth dough.
With the smooth surface, your dough is going to stick less on your hands. Applying
later stretches and folds will be a lot easier. Without a smooth
surface, the dough becomes almost unworkable. Folding the dough later
becomes an impossible task. This is a frequent mistake I see many
new bakers commit.


![The transformation of a sticky dough
      blob to a dough with a smooth surface. The goal is to reduce surface
      touchpoints with your hands to make the dough less sticky when working
      it.](images/dough-ball-steps)

*The transformation of a sticky dough
      blob to a dough with a smooth surface. The goal is to reduce surface
      touchpoints with your hands to make the dough less sticky when working
      it.*


To make the dough's surface smooth, place your dough on a wooden board or
on your kitchen's countertop. Drag the dough with your palm over the surface.
A dough scraper could be used here for assistance.
Drag the dough towards you while making sure the top center of the dough stays in place.
It can help to gently place your second hand on top of the dough so that
the dough mass moves while retaining its orientation. Once the whole dough
is too close to the edge of the container/countertop, gently move it back
with two hands. By doing so, you are stretching the outer surrounding gluten layer.
For this reason, it is important to not use any flour during this process.
By using flour, you can no longer drag the dough over the surface and thus
you can't stretch the gluten. Always imagine you are touching something utterly sticky.
By doing so you will automatically try to touch the dough as little
as possible. Keep repeating the process until you see that the dough
has a nice smooth surface. The final dough should look like the dough
shown in the figure.

If your outer gluten layer tears, you have overstretched your dough. In
that case, take a 10-minute break, leaving your dough on the kitchen countertop.
This allows the gluten to re-bond and heal. Repeat the same process
and the damaged rugged areas should disappear.

The same dough-rounding technique is used later during
the pre-shaping process. After creating dough strength you
have all the time you need to practice rounding. Round the dough
as much as possible until it tears. Then wait the aforementioned 10 minutes and repeat.
Later, you don't have any room for error. Your technique has to be on point.
An over-pre-shaped dough can potentially not recover.

## Bulk fermentation


After mixing the starter into your dough, the next stage of
the process known as bulk fermentation begins. The term
*bulk* is used because in bakeries, multiple loaves are fermented
together in bulk. If you are a home baker, you might bulk
ferment a single loaf. The bulk fermentation ends when you
divide and pre-shape, or directly shape your final loaves or loaf.

The hardest part when making sourdough bread is controlling
the fermentation process. Bulking long enough but not too
long is the deciding factor for making great bread at home.
Even with poor shaping and baking techniques, you'll be able
to make excellent bread, solely by mastering the bulk
fermentation process.

With a too-short bulk, your crumb will be
perceived as gummy. Your crumb will feature large pockets of
air commonly referred to as *craters*. A too-long fermentation
results in the dough breaking down too much. The resulting
dough will stick to your banneton and spread while baking
into a pancake-like structure.

The key is to find the sweet spot between not too little
and not too much bulk fermentation. I'd always recommend pushing
the dough more toward a longer fermentation. The
flavor of the resulting bread is better compared to a pale
underfermented dough.


|  | **Fermentation** |  |  |
| --- | --- | --- | --- |
|  | **Too short** | **Too long** | **Perfect** |
| Crumb texture | Unbaked gummy areas towards the bottom of the bread. | Crumb can be perceived as gummy as most gluten broken down. | Crumb evenly baked. Crumb can be perceived as moist, but not gummy. |
| Alveoli | Overly large alveoli in the crumb "craters". | Many tiny alveoli equally distributed. | Alveoli evenly distributed, no "craters". |
| Taste | Pale neutral taste. | Strong acidic flavor profile. Acidity overweighs when tasting. | Balanced flavor profile, not too mild but also not too sour. Depending on starter vinegary or lactic notes. |
| Texture | Overall poor texture. | Good consistency, crumb is not as fluffy as it could be. | Great combination of  textures. |
| Oven spring | Vertical oven spring, mostly due to water evaporating and inflating the dough. | Very flat pancake like  structure after baking. | Great vertical oven spring. Dough grows more upwards rather than sideways. |

*The different stages of
            sourdough fermentation and the effects on crumb, alveoli, texture,
            and overall taste.*


The worst thing you can do when fermenting sourdough
is to rely on a recipe's timing suggestions. In 99%
of the cases, the timing will not work for you. The writer
of the recipe probably has different flour and a different
sourdough starter with different levels of activity. Furthermore,
the temperature of the fermentation environment might be
different. Just small changes in one parameter result
in a completely different timing schedule. One or two hours'
difference results in the dough not fermenting long enough, or
turning it into a gigantic sticky fermented pancake. This
is one of the reasons why the current baking industry prefers
to make solely yeast-based doughs. By removing the bacteria
from the fermentation, the whole process becomes a lot more
predictable. The room for error (as shown in
the figure) is much larger. The doughs
are perfect to be made in a machine.


**Flowchart:** *During the bulk
      fermentation, multiple doughs are fermented together in bulk.  A
      challenging aspect of homemade sourdough bread is to determine when this
      stage of fermentation is completed. This chart shows multiple available
      options to check on the bulk fermentation progress.*


Experienced bakers will tell you to go by the look and feel of
the dough. While this works if you have made hundreds of loaves,
this is not an option for an inexperienced baker. As
you make more and more dough, you will be able to judge
the dough's state by touching it.

My go-to method for beginners is to use an *Aliquot jar*.
The aliquot is a sample that you extract from your dough. The
sample is extracted after creating the initial dough strength.
You monitor the aliquot's size increase to judge the
level of fermentation of your main dough. As your
dough ferments, so does the content of your aliquot jar. The moment your
sample reached a certain size, your main dough is ready
to be shaped and proofed. The size increase you should
aim for depends on the flour you have at hand. A flour
with a higher gluten content can be fermented for a
longer period. Generally, around 80%
of your wheat flour's protein is gluten. Check your flour's
packaging to see the protein percentage. The actual size increase
value is highly variable depending on your flour composition.
I recommend beginning with a size increase of 25% and testing
up to 100% with subsequent bakes. Then identify a value
that you are happy with.


| **Flour protein content** | **Relative aliquot size increase** |
| --- | --- |
| 8–10% | 25% |
| 10–12% | 50% |
| 12–15% | 100% |
|  15% |  100% |

*Reference values for
            how much size increase to aim for with an aliquot jar depending on
            the dough's protein content.*


The beauty of the aliquot is that no matter the surrounding
temperature, you will always know when your dough is ready.
While the dough might be ready in 8 hours in summer, it could
easily be 12 hours in winter. You will always ferment your
dough exactly on point.


![An aliquot jar to monitor the dough's fermentation
      progress.  It took 10 hours for the dough to reach a 50%
      size increase.](images/aliquot-before-after)

*An aliquot jar to monitor the dough's fermentation
      progress.  It took 10 hours for the dough to reach a 50%
      size increase.*


While the aliquot sample has enabled me to consistently bake
great loaves, there are limitations to consider. It's crucial
to use a cylindrical-shaped container to properly judge
the dough's size increase. Furthermore, it is essential
to use room-temperature water when making your dough. If the
water is hotter, your aliquot, due to its smaller size,
will cool down faster. The aliquot will ferment more slowly
than your dough. Similarly, when you use too cold water,
your sample will heat up faster than the large dough mass.
In that case, your aliquot is ahead of your main dough. You
would probably stop the fermentation too early. Make sure
to keep the dough and aliquot close together. Some people even
place the aliquot in the same container. This makes sure that
both are in the same environment temperature. The aliquot
is also less reliable if your ambient temperature changes
a lot during the day. In that case, your aliquot will adapt
faster than your main dough. The readings will always be slightly
off. If you are making a large chunk of dough with more
than 10 kg of flour, the jar is also less reliable. The biochemical
reactions happening inside your dough will heat it.
The fermentation itself is exothermic which means
that it produces heat.

Another more expensive option is to use a pH meter
to monitor your dough's fermentation state. As the lactic
and acetic acid bacteria ferment, more acidity is piled
up inside your dough. The acidity value (pH) can be
measured using such a meter. The more acidity, the lower the pH
value of your dough. The pH scale is logarithmic, meaning
that each digit change will have a 10x increase in acidity.
A sourdough dough might begin fermenting at pH 6.0,
then shortly before baking has roughly pH 4.0. This means
that the dough itself is 10x times 10x (= 100x) sourer
than at the beginning. By using the meter, you can always
judge the state of your dough's acidification and then act
accordingly.

To use the pH meter successfully, you need to find pH values
that work for your dough. Depending on your starter,
water, and flour composition, the pH values to look out
for are different. A stronger flour with more gluten
can be fermented for a longer period. To find out
the pH values for your bread I recommend taking
several measurements while making your dough.

1. Measure the pH value of your sourdough starter before using it
2. Check the pH after mixing all the ingredients
3. Check the pH before dividing and pre-shaping
4. Check the pH before shaping
5. Check the pH of your dough before and after proofing
6. Check the pH of your bread after baking

If the bread you made turned out successfully with your values,
you can use them as a reference for your next batch. If the
bread didn't turn out the way you like, either shorten
the fermentation or extend it a little bit.


| **Step** | {**pH Value**} |
| --- | --- |
| Starter ready | 4.20 |
| Mixing | 6.00 |
| Dividing/preshaping | 4.10 |
| Shaping | 4.05 |
| Before proofing | 4.03 |
| After proofing | 3.80 |
| After baking | 3.90 |

*Example pH values for
            the different breakpoints of my own sourdough process.*


The beauty of this method is its reliability. Once you have found
out your good working values, you can reproduce
the same level of fermentation with each subsequent dough.
This is especially handy for large-scale bakeries that want
to achieve consistency in each bread.

While this method is very reliable, there are also certain
limitations to consider.

First of all the pH values that work for me likely won't work for
you. Depending on your own starter's composition of lactic
and acetic acid bacteria, your pH values will be different.
You can use the values shown in the table below
as rough ballpark figures. Regardless, you need to find values
that work for your setup.

Another limitation is the price. You will need to purchase
a high-tech pH meter, ideally, a meter featuring a spearhead
[^6].
This way you can directly poke the meter deep into the dough.
At the same time, automated temperature adjustments are a
feature to look out for. Depending on the temperature,
the pH value varies. There are tables you can use to
do the adjustment calculations. More expensive meters
have this feature built in. The pH meter loses accuracy
over time. For this reason, you need to frequently
calibrate it. The process is cumbersome and takes time.
Lastly, you need to carefully rinse the pH meter before
using it in your dough. The liquid surrounding the
head of your pH meter is not food-safe and thus should
not be eaten. I rinse the meter for at least one minute
before using it to measure my dough's fermentation stage.

The last method to judge the state of bulk fermentation
is to read the signs of your dough. The more bread you have
made, the more accustomed you will become to this process.
Look out for the dough's size increase. This can sometimes
be a challenge when your dough is inside a container.
You can help yourself by marking your container. Some bakers
even use a transparent rectangular bulk container. You
can use a pen to mark the initial starting point. From there
on you can nicely observe the size increase. Similar to the
mentioned aliquot sample, look out for a size increase that works
for your sourdough composition.


![A dough in a good state to
      finish bulk fermentation. Notice the tiny bubbles on the dough's surface.
      They are a sign that the dough is inflated well enough.](images/bulk-finished-dough)

*A dough in a good state to
      finish bulk fermentation. Notice the tiny bubbles on the dough's surface.
      They are a sign that the dough is inflated well enough.*


Look out for bubbles on the surface of your dough. They
are a good sign that your dough is inflated with gas. The
further you push the bulk fermentation the more bubbles
will appear. If you overdo this stage, the dough becomes leaky, and
the bubbles will disappear again.

Take note of the dough's smell. It should match the same
smell of a ripe starter shortly before collapsing. As mentioned
before, your dough is nothing but a gigantic starter. You
can also proceed and taste your dough. It will taste like
pickled food. Depending on the acidity you can judge how
far the dough is in the fermentation process. The final bread
will taste less sour. That's because a lot of acidity evaporates
during baking[^7].

When touching the dough, it should feel tacky
on your hands. The dough should also be less sticky
compared to earlier stages. If the dough is overly
sticky, you have pushed the fermentation too far.

If you pushed the bulk fermentation too far, you won't be able
to bake a freestanding loaf with the dough anymore. But don't
worry. You can move your dough into a loaf pan, or use parts
of the dough as the starter for your next dough. When using
a loaf pan, make sure it's properly greased. You might have
to use a spatula to transfer your dough. Allow the dough
to proof for at least 30 minutes in the loaf pan before
baking it. This makes sure that large cavities induced
by the transfer are evened out. You could push the proofing
stage to 24 hours or even 72 hours. The resulting
bread would feature an excellent, very tangy taste.


## Stretch and folds


![A dough where two sticky sides are being glued
      together using a stretch and fold. This process creates excellent dough
      strength.](images/dough-being-glued)

*A dough where two sticky sides are being glued
      together using a stretch and fold. This process creates excellent dough
      strength.*


In this section, you will learn all you need to know about stretching and
folding. You will learn when to stretch and fold and how to use this technique
to your advantage.

Stretching and folding is a set of techniques used by bakers during the bulk
fermentation stage. The process involves stretching the dough and then
folding the dough onto itself. Some recipes call for a single stretch
and fold, others for multiple.

The primary goal of this technique is to provide additional dough strength to
your dough. As shown in the figure there are
multiple ways to create dough strength[^8].
If you do not knead as much at the start, you can reach the same level of
dough strength by applying stretch and folds later. The more stretch and folds
you do, the more dough strength you add to your dough. The result will be a
more aesthetic loaf that has increased vertical oven spring.

Sometimes, if the dough is very extensible
and features very high hydration, stretching and folding is essential.
Without it, the dough itself would have too little dough strength and not
spring in the oven at all.

Another benefit of stretch and folds are their homogenization properties. By
folding the dough you are redistributing areas that are fermenting faster
than other areas. The heat in your dough is not the same in all areas.
The fermentation itself produces heat. For that reason, some of the areas in
your dough will ferment a little faster than others. This means that some
areas hold more gas and more acidity than others. Applying a stretch and fold
will redistribute heat, gas, and acidity. Some bakers also refer to this
process as crumb building. Careful folds ensure that your final dough's crumb
is not overly wild featuring large cavities. If you notice overly
large cavities in your final dough's crumb, then you might be able to fix that
by applying more stretch and folds[^9]. Please refer to the relevant section
"sec:debugging-crumb-structure" for more information on reading
your crumb.


![An overview of the steps involved to perform
      stretch and folds for wheat-based doughs.](images/stretch-and-fold-steps)

*An overview of the steps involved to perform
      stretch and folds for wheat-based doughs.*


The reason for the technique's popularity lies in its efficiency. By stretching
the dough outwards, you increase your dough's surface area. You then fold the
dough over, essentially gluing large areas of the dough together. Imagine a
piece of paper on which you place the glue. Then you fold the paper. Large areas
of the paper now stick together. Repeat the same process with more glue until
you have created multiple layers of paper and glue. This is the same thing that
happens to your dough. With only very few movements you have applied glue to your
dough.

To apply a stretch and fold first wet your hands with cold water. Watered hands
work wonders in reducing the dough's tendency to stick to your hands. Proceed and
carefully loosen the dough from the edges of your bulk container. Do this by
carefully placing your hand at the edge of the dough and pushing your hand
downwards on the container's walls. Once you have reached the bottom, drag the dough
a little bit inwards. The dough should stay in place and not move back to the
edge of your container. Try to be as swift as possible with this motion. The
slower you are, the more dough will stick to your hands. Repeat the same process
once all around your dough until the dough is free of your container's edges.
Wet your hands one more time and then carefully lift one side of the dough with
two hands placed in the center upwards. Make a fold in the center of the dough.
The upper smooth side needs to be placed on the bottom of the container. By doing
so, you will be gluing together the two sticky bottom sides. The top smooth
side should not be sticky in your hands, while the bottom rough surface should
tend to stick to your hands. Rotate the container and repeat the same thing
from the other side. Rotate the container 90 and then repeat the process
once again. Rotate the container another 180 in the same direction and
repeat the fold one last time. By doing so you have applied four folds in
total. Your dough should now stay in place and resist flowing
outwards[^10].

In theory, there is no limit to how often you can stretch and fold. You could
apply one every 15 minutes. If your dough has enough dough strength already,
applying additional folds is just a waste of time[^11]. If you apply a large number of consecutive folds, the
outer layer of gluten
will tear. In that case, you just have to wait for at least 5–10 minutes until
the gluten bonds heal and you can try again. When the gluten does not heal
anymore, chances are you have pushed the fermentation for too long. Likely
most of the gluten has broken down and you are already
in the decay stage shown in the figure.


![A dough during bulk fermentation that has
      flattened out. To improve its dough strength, a stretch and fold should
      be applied.](images/dough-requiring-stretch-and-fold)

*A dough during bulk fermentation that has
      flattened out. To improve its dough strength, a stretch and fold should
      be applied.*


Now, the reasonable amount of stretch and folds you should do greatly depends on how much you
kneaded initially and how extensible your dough is. A good recommendation is
to observe your dough in your bulk container. Once you see that the dough
flattens out quite a lot and spreads towards the edges of your bulk container,
you can proceed and apply a stretch and fold. For 95% of the doughs
that I am making, this is hardly more than once. I like to make overnight
doughs and in that case, I typically apply one stretch and fold directly after
waking up. Then the bulk fermentation might take another 2 hours before I proceed
with dividing and pre-shaping or directly shaping.

## Optional: Dividing and Preshaping

Dividing and pre-shaping is an optional step that is done
once your sourdough finishes with the bulk fermentation stage.
The step is required if you are making multiple loaves in one
batch. It is optional if you are making a single loaf.


**Flowchart:** *Dividing is only required when you are
      making multiple loaves in a single dough batch.*


The goal of dividing your dough into smaller pieces is to portion
your dough accordingly. This way you'll have multiple pieces of bread
which all weigh the same. For this reason, a scale is commonly
used to weigh the pieces of dough. If one piece of dough weighs
too little you can simply cut a bit more from your dough blob
to increase its weight.

When cutting the dough, try to be as concise as possible with your
movements. You don't want to unnecessarily damage your dough too much.
Quick movements with a knife or dough scraper help to prevent the
dough from sticking too much to your tools.


![The steps of dividing and preshaping your dough.](images/divide-preshape)

*The steps of dividing and preshaping your dough.*


I sometimes like to draw small lines with the dough scraper's edge
on the large dough mass before cutting it into smaller pieces.
This helps me to better plan where I want to do my incisions. When
I plan to make 8 loaves I try to use the lines to divide the dough
into 8 equally sized portions before cutting. If this is not precise enough,
you can use the aforementioned scale.

Now that you have cut your dough, the resulting chunks are not in an equal shape.
This is problematic for the next stage when you are shaping your dough.
The resulting loaves wouldn't look nice and even. You would probably
end up with areas that tear the moment you are shaping your dough.
You wouldn't start the whole proofing process on a good foundation. For that
reason, you need to pre-shape your dough.

Pre-shaping is done for several reasons:
- You divided your dough and require pre-shaping
- Your dough lacks dough strength. Pre-shaping will add more strength
- You want to even out the final loaf's crumb structure. By pre-shaping, the resulting crumb will look more even.

If you are making a single loaf from one dough batch the step is not required.
In that case, you can directly proceed with shaping, skipping this step.

The pre-shaping technique is the same as the process
the figure.  Whereas earlier you could tear the dough's
surface this could now result in a catastrophe.  For this reason, I recommend
practicing this step for as long as you need after kneading.  The gluten
network might be so extensible and degraded at this point that there is hardly
any room for error. The dough wouldn't come together again. The only way to
save such dough is to use a loaf pan.


![Drag the dough in the direction of the rough
      surface area. This way you minimize the movements required to complete
      the step.](images/preshape-direction)

*Drag the dough in the direction of the rough
      surface area. This way you minimize the movements required to complete
      the step.*


Pre-shape the dough as much as is needed to round up the top surface area. Try
to touch the dough as little as possible to reduce its ability to stick to
your hands. Drag the dough in the direction where you see a rough surface
area. In case you have too little space to drag the dough because it might
fall from the edge of your counter, simply lift it with a swift movement and
place it in a better position for pre-shaping. Please refer to
the figure for a visualization showing the
pre-shaping direction.

Try to set yourself a limit of movements to finish pre-shaping
a dough. Then you will be more conscious about each movement
you are performing. At the start you can try 5 movements,
iteratively reducing this to 3. The only reason for exceeding these
numbers could be if you on purpose want to even out the crumb
structure of your final loaves further.


![Baguette doughs resting after preshaping.](images/preshaped-dough)

*Baguette doughs resting after preshaping.*


Once you finished pre-shaping allow the dough balls to rest
on your counter for at least 10–15 minutes. Do not
cover the pre-shaped balls. By drying out the surface,
the following shaping step will be easier. The dried-out surface
will not stick to your hands as much. As
you tightened the dough's gluten you will need to
allow it to relax. Without a resting period, you wouldn't
be able to shape your dough into, for instance, a baguette-like structure.
The dough would resist each movement
always springing back into the previous shape. You
might have noticed this before, when making pizza dough. If you
don't wait long enough after balling the pizzas, it's impossible
to stretch the pizza. By waiting a few more minutes,
stretching becomes a lot easier. The dough will not resist
being transformed into the final shape that you like.

The aforementioned 10–15 minutes bench rest time depends
on how strongly you pre-shaped your dough. The more
you pre-shape the longer you need to wait. If your dough
resists a lot during shaping, extend this period up to 30 minutes.
If you wait too long, your dough's surface area can become too dry,
resulting in the dough tearing during shaping. As always, please
take these timings with a grain of salt and experiment in
your environment.

## Shaping


**Flowchart:** *A schematic visualization of the shaping process
      including checks for an overfermented dough.*


Shaping will give your dough the final shape before baking. After
completing shaping, your dough proceeds to the proofing stage and
will then be scored and ultimately baked.

There are countless shaping techniques. The technique to choose
depends on the type of bread you want to make. Some techniques
are gentler on the dough, making sure that the dough does not
degas. Other techniques are faster but degas the dough a little
more. The tighter you shape, the more evened out your final dough's
crumb structure will look. At the same time, a tighter shaping-technique
will improve your dough's strength. More strength will ultimately result
in more vertical oven spring.

The following instructions assume that you want to make a batard-style
bread featuring an oblong shape. Learning this technique
will provide you with a solid knowledge foundation that
can easily be extended to make bread rolls or baguettes.

Mastering the challenging shaping technique will likely take you
multiple attempts. You only have a single attempt per dough, though. If you
make a mistake, the final bread is likely not going to turn out as good
as it could. If this technique causes you a headache, I recommend making
a larger batch of dough and dividing and preshaping it into
smaller portions. Instead of making a large batard, practice making miniature
batard bread rolls.

### Apply flour to the dough's surface.


![A dough that has flour applied to its
      surface. This is the first step of the shaping process.](images/step-1-flour-applied)

*A dough that has flour applied to its
      surface. This is the first step of the shaping process.*


If you are only making one loaf out of your dough, apply flour
generously to the top layer of your dough. Rub the flour onto your
dough with your hands. Flip over your container. Wait a little bit
to allow the dough to release itself from the container. Proceed
with step 3.

If you divided and pre-shaped, apply flour generously to the dough's
top layer as well. With gentle hands spread the flour evenly across
the dough's surface. See the figure for a
visual representation of how your dough should look after coating
the surface.

### Flip the dough over


![A flipped-over dough. Note how the
      sticky side is facing you while the floured side is facing the
      countertop.  The sticky side is used as glue to hold the dough together.](images/step-2-flipped-over)

*A flipped-over dough. Note how the
      sticky side is facing you while the floured side is facing the
      countertop.  The sticky side is used as glue to hold the dough together.*


With gentle hands, carefully remove the dough from the surface. If
you possess a dough scraper, carefully tuck it under the dough with
rapid movements. Flip the dough over, making sure that the floured
areas are in contact with your hands. The non-floured bottom area that was
stuck to the counter is a no-touch zone. Try to avoid touching it
as it is rough and thus will stick to your hands.

Gently proceed and place the dough with the previously top-facing side
on your counter. The floured area is now on the surface, whereas the
sticky side is facing you.

### Make the dough rectangular


![A flipped-over dough. Note how the
      sticky side is facing you while the floured side is facing the
      countertop.](images/step-3-rectangular)

*A flipped-over dough. Note how the
      sticky side is facing you while the floured side is facing the
      countertop.*


You should be facing the sticky side of your dough now. Note how
the dough is currently round and not rectangular. The circular
shape will not be ideal when shaping the oblong batard.

For this reason, proceed and stretch the dough a little bit until
it has a more rectangular shape. While stretching, make sure to touch
the sticky side as little as possible. Place your hands on the bottom
floured side and the edge of the sticky side. With gentle hands,
stretch the dough until the shape in front of you looks rectangular.
Refer to the figure and compare
your dough with the shown dough.

### Fold the dough together


![The process of folding a batard. Note
      how the rectangle is first glued together and then rolled inwards to
      create a dough roll. Ultimately the edges are sealed to create a more
      uniform dough.](images/step-4-folding)

*The process of folding a batard. Note
      how the rectangle is first glued together and then rolled inwards to
      create a dough roll. Ultimately the edges are sealed to create a more
      uniform dough.*


Now that you have created the rectangular shape, your dough
is ready to be folded together. This only works because the side
facing you is sticky. Because of the dough's stickiness,
we can effectively glue it together, creating a very
strong bond.

You can practice this step with a piece of rectangular paper.
Once you mastered folding on paper you can easily apply
this to your real-life dough.

Make sure the batard is placed in front of you. Take the side
that faces you and fold it into the middle of the dough. Carefully
tuck it down so that it glues together with the sticky side.

Take the other side and fold it over the side you just folded.
Stretch the dough as much as possible towards you. Tuck it down
on the edge, creating your first glue layer.

Rotate the dough so that it is aligned lengthwise in front of you.
Rotate the dough inwards so that the seam side
now faces you.

Start to roll the dough inwards beginning at the top of the dough.
Keep rolling the dough inwards until you have created a dough roll.

Refer to the figure for a full visual
representation of the process.

If your dough does not hold its shape, chances are you have pushed
the fermentation too far. Most of the gluten has been degraded
and the dough won't be able to hold its shape. In this case,
the best option is to use a loaf pan to bake your bread. The
final bread will taste amazing but not offer the same texture
a freestanding bread would offer. Please refer to
the relevant section for more
details on how to properly read your dough's crumb structure.

### Sealing the edges

Your dough has finished shaping now. Sealing the edges
is an optional step. I like to do it because, in my opinion,
the final baked bread will look a little bit nicer without
any rough edges.

Gently pull together the swirl-like-looking edges of your dough
with two fingers. Rotate the dough and then repeat the same process
from the other side as well.

### Prepare for proofing


![The shaped dough is ready for proofing
      in the banneton. Note how the seam side is now facing you. The floured
      previous top side is facing downwards.](images/step-6-prepare-proofing)

*The shaped dough is ready for proofing
      in the banneton. Note how the seam side is now facing you. The floured
      previous top side is facing downwards.*


You should have a beautifully shaped dough in front of you now.
The proofing stage is about to start. To simplify later
scoring and to make sure your dough won't stick to your banneton,
apply another flour rub to the dough's surface. This
will dry out the surface and reduce the dough's tendency
to stick to everything.

For the coating, I recommend using the same flour you used
to make your dough. Rice flour is only recommended if you
want to apply artistic scoring patterns later. It is better
to use more flour than too little flour. Excess flour can be
brushed off later.

Once your dough has been coated, it is ready to be placed on your banneton.
If you do not have a banneton, you can use a bowl
with a kitchen towel inside.

The currently top-facing floured surface will be downwards-facing in your banneton.
By doing so the banneton can be flipped
over before baking, releasing the dough[^12].

Proceed and lift the dough with both hands from the counter.  Gently rotate it
once and then place the dough in your banneton for proofing[^13].
If you did everything right, then your dough should look somewhat similar to
the dough shown in the figure.  As the last
step of shaping, place a kitchen towel over your banneton or bowl and begin
proofing.

## Proofing

In bread baking, proofing refers to the final rise of dough before baking,
after it has been shaped into a loaf. The chemical reactions and processes
that occur during bulk fermentation and proofing are the same.

By shaping your dough, it has lost some of the air previously generated
throughout the bulk fermentation. The goal of proofing is to inflate
the dough again. A dough without proofing wouldn't offer the same texture
as a properly proofed dough. The proofed dough features a very fluffy
and soft crumb.

There are two proofing techniques. One strategy is to proof the dough
at room temperature whereas the other proofs the dough in the fridge.
Fridge-proofing is also commonly known as retarding.

Some bakers claim that cold-proofing improves the final flavor of the bread.
In all the loaves that I retarded I could not tell a difference
in terms of flavor for cold-proofed doughs. The microorganisms work
at a slower rate at colder temperatures. But I doubt that they alter
their biochemical processes. More research is needed on the topic
of retarding and flavor development.


**Flowchart:** *A schematic overview of the different steps of
      the sourdough proofing process. The proofing technique to choose depends
      on your availability and schedule.*


To me, the sole purpose of cold-proofing is its ability to allow you to better
manage the timing of the whole process. Assuming you finished shaping your
dough at 10 pm, chances are you wouldn't want to wait for another 2 hours to
proof the dough and then another hour to bake it. In this case, you can move
your dough directly to the fridge after shaping. Your dough will be proofing
overnight in the fridge. Then it can be baked at any time the following day
(there are a few exceptions; more on that later).  This is especially handy
for large-scale bakeries that use fridge-proofing extensively. Some of the
doughs are proofed a day before and placed in the fridge.  Early in the
morning, they can be baked directly out of the fridge. Within 2 hours they
will be ready to sell the first bread to morning customers. If throughout the
day more bread is needed, they simply take some proofed dough out of the
fridge and bake it. The time frame in which you can bake retarded dough is
big. It can be as little as 6 hours later up to 24 hours later.

Assuming you made an overnight dough and your dough is ready in the morning,
the situation might be different. You potentially want to bake the dough directly
for breakfast, or at lunchtime. In this case, you wouldn't want to proof the dough for
another 6 hours in the fridge. Room temperature-proofing is your technique
of choice.

To summarize, choose the technique that works for you depending on your
schedule and availability.

### Room temperature-proofing

The easiest and most reliable way to proof your dough is to proof the dough at
room temperature. It is my method of choice if my schedule allows it. This method
works great if you make an overnight dough and then proof it the next
morning.


![The finger poke test is a very reliable
      method to check if your dough has been properly proofed. If the induced
      dent is still visible one minute later, your dough can be baked.](images/step-13-finger-poke-test)

*The finger poke test is a very reliable
      method to check if your dough has been properly proofed. If the induced
      dent is still visible one minute later, your dough can be baked.*


The time it takes to proof your dough can be anything between 30 minutes and
3 hours. Rather than relying on timing, most bakers use the finger poke test.

Flour your thumb and gently press around 0.5–1 deep into the
dough.  Try this directly after shaping. You will notice that the created dent
will recover quickly. It will be gone again after one minute.

As you proceed with proofing, your dough will fill up with more gas. At the
same time, the dough will become more extensible. Once it starts to reach the
right amount of fluffiness and extensibility, the dent will disappear more
slowly.  Once the dough is ready for scoring and baking the dent should still
be visible after one minute of waiting.

I recommend performing the finger poke test once every 15 minutes throughout
the proofing stage. Realistically, based on my experience, proofing takes at least
one hour and can sometimes take up to 3 hours. Even at warmer temperatures proofing
has never been faster than an hour for me. As always please take my timings with
a grain of salt and experiment on your own.

Once I see that the dough is getting close to perfect proofing, I proceed and
preheat my oven. This way I don't overproof the dough. You would notice an
over-proofed dough when the dough suddenly becomes very sticky. At the same
time, the dough is likely to collapse during baking and will not spring back.
Generally, it is better to end proofing too early rather than too late.

### Cold-proofing (retarding)

The second proofing option is to place your dough inside the fridge for
proofing. This option is great if you do not want to bake the dough
within the next 3 hours.

The dough will initially proof at the same rate as the room temperature dough.
As the dough cools down the rate of fermentation slows. Ultimately at below
4°C (40F) the fermentation comes to a halt[^14]. The dough can rest in the fridge for up to 24 hours. In some
experiments, the dough was still good even 48 hours later. Interestingly,
there is a limit to fridge proofing. I can only explain this with continuous
fermentation activity at low temperatures.

The hard part is to judge when the dough is finished proofing in your fridge.
The previously mentioned finger poke test does not work on cold dough. Low
temperatures change the dough's elasticity. The dent from the poke test
will never recover.

For this reason, finding the best fridge-proofing time is best done
with an iterative approach. Begin with 8 hours on your first dough,
10 hours on the second, 12 hours on the third, and so on up to 24 hours.
As the temperature in your fridge is typically constant, you have an
environment in which you can rely on timings. Find the ideal proofing
time that works for you.

One additional consideration is the dough's core temperature before
placing it inside the fridge. The warmer your dough is initially
the longer it takes for the dough to cool down. This is an additional
variable to take into consideration when choosing the retarding time.
In summer times when my kitchen is hot, I choose a shorter fridge-proofing
time compared to winter times when the dough is colder.

A reliable way to ensure consistent proofing is to opt for using a pH
meter. By checking the amount of piled-up acidity you can ensure
each of your doughs has the right amount of acidity. Opt for an iterative
approach and check the pH for multiple proofing times. Find the pH
value that creates the best bread for you. Once you have identified
your perfect pH value you can resort to that number on all following
doughs. See the table below for some sample pH values
to follow.

## Scoring

Once your dough is done proofing, it's time to warm up your oven
to around 230°C (446°F). The next step is then
to proceed with scoring your dough.

Scoring is done for two reasons. There is functional and decorative
scoring. Functional scoring refers to making a small incision in the dough
through which it rises while baking. If the dough is not scored,
it would likely crack open at the weakest spots where you sealed
the dough after shaping. Decorative scoring can be used to apply
artistic patterns to your dough and make it more appealing. When
you want to apply artistic scoring, it is best to rub your dough
with additional rice flour before scoring. The white rice flour
greatly boosts the contrast of the scoring incisions and thus
makes the final pattern look more visually appealing.


![The ear is a characteristic that can be achieved on
      wheat sourdough when fermenting and scoring your dough with the perfect
      technique. It offers additional flavor and great texture when eating the
      bread.](images/the-ear)

*The ear is a characteristic that can be achieved on
      wheat sourdough when fermenting and scoring your dough with the perfect
      technique. It offers additional flavor and great texture when eating the
      bread.*


When using a banneton, the dough is flipped over and
placed on an oven rack, tray, stone, steel, or dutch oven. The pros
and cons of the different baking options are covered in the next chapter.
The dough's top side which was previously at the bottom of the
banneton should now be facing you.


![A loaf by Nancy Anne featuring an artistic
      scoring pattern.  The high contrast was achieved by rubbing the dough's
      surface with rice flour before baking. Her Instagram account
      `simply.beautiful.sourdough` is specialized to showcase beautiful
      artistic scoring patterns.](images/artistic-scoring)

*A loaf by Nancy Anne featuring an artistic
      scoring pattern.  The high contrast was achieved by rubbing the dough's
      surface with rice flour before baking. Her Instagram account
      `simply.beautiful.sourdough` is specialized to showcase beautiful
      artistic scoring patterns.*


The scoring cut is done at a 45 angle relative to the dough's
surface slightly off the dough's center. With the 45 angle cut
the overlaying side will rise more in the oven than the other side.
This way you will achieve a so-called *ear* on the final bread.
The ear is a thin crisp edge that offers intriguing texture
when eating. The thin edge is typically a bit darker after baking
and thus offers additional flavor. In my opinion, the ear turns
a good loaf into a great loaf.


![The 45 angle at which you score the
      dough is relative to the surface of the dough.  When scoring more towards
      the side, you have to adjust the angle to achieve the ear on your
      bread.](images/bread-scoring-angle)

*The 45 angle at which you score the
      dough is relative to the surface of the dough.  When scoring more towards
      the side, you have to adjust the angle to achieve the ear on your
      bread.*


The actual incision is done with a very sharp knife, or better, a razor
blade. You can use the razor blade directly or attach it to a chopstick.
The razor blade offers better flexibility than the sharp knife.
Regardless, the blade should be as sharp as possible. This way when cutting,
the dough is not torn and instead features a clean, non ragged incision.

To simplify scoring, your dough's surface must be dried out a little bit.
This way it is a lot easier to make the incision.
For this reason, it is crucial to rub your dough with a bit of flour
before placing it in the banneton. The dry flour will absorb some of the
moisture of the outer layers of your dough. This is especially important
when working with room temperature-proofed doughs. A cold-proofed dough
is a lot easier to score due to the dough's low viscosity. The room-temperature
dough is a lot harder to score. The scoring incision tears a lot
easier. With a ragged incision, the dough is not as likely to properly
rise in the oven. Chances are you will not achieve the previously mentioned
ear. For this reason, drying out the surface is especially important. Scoring
will become a lot easier.


![By applying flour to your dough's surface
      after shaping, the outer part of the dough dries out a little bit. This
      makes scoring a lot easier as the incision is less likely to tear.](images/dry-dough-surface)

*By applying flour to your dough's surface
      after shaping, the outer part of the dough dries out a little bit. This
      makes scoring a lot easier as the incision is less likely to tear.*


Scoring requires a lot of practice. For this reason, I recommend
practicing making the incision after creating dough strength. The dough
is going to be very wet and sticky. You can use a sharp knife or razor
blade to practice the technique. Wait a few minutes and then round
up the dough again. You can practice this for as long as you like
until you are happy with your technique. After proofing, you only
have a single chance to practice scoring. It's either hit or miss.

An additional trick that can help you to combine the benefits
of room temperature-proofing and easy cold-proofing scoring
is to place your dough in the freezer for 30 minutes before baking.
Once you notice your dough is almost done proofing, move it to the
freezer. The freezer will dry out the dough's surface even further
while also lowering its viscosity, making scoring easier.

Another interesting trick is to bake your dough for 30 seconds without steam.
The hot air will dry out the dough's surface even further and simplify
the scoring technique. Experiment with the timing to identify your personal
sweet spot.

---

[^1]: Sometimes it almost feels like a comparison of skill value
between bakers. The more water they can handle, the more skillful the baker.

[^2]: I have tested adding the salt at the start and end of the
autolysis process and could not notice a difference. Based on my current
understanding, the importance of adding salt later seems to be a myth.

[^3]: I have not seen studies yet looking at enzymatic speeds depending on
the temperature. But I assume the higher the temperature, the faster these
reactions. This goes up until a point when the enzymes break down under
heat.

[^4]: Please take these values with a grain of salt as they depend
    on your flour and your sourdough starter. These are values that you have
    to experiment with. After baking a couple of breads you will be able to
    read your dough much better.

[^5]: Give it a shot yourself. The automatic formation of gluten
networks is an amazing phenomenon that still fascinates me every time I am
making dough.

[^6]: Not every pH meter is suitable for measuring dough.
Please refer to the manual to make sure it is certified for
measuring the pH of liquid and semi-solid media. To receive
accurate pH readings further ensure that your pH meter
is properly calibrated.

[^7]: More on this topic later.
Just by baking longer and/or shorter, you can control
the tang of your final baked bread. The longer
you bake, the less sour the final loaf. The shorter,
the more acidity is still inside the bread. The resulting
loaf will be sourer.

[^8]: In fact I have seen many
    no-knead recipes calling for no initial kneading, but then applying
    stretch and folds during the bulk fermentation. The time required to do
    all the folds probably matches the initial kneading time required.

[^9]: In many cases these cavities can
also happen when a dough does not ferment enough. The crumb is commonly called
Fool's Crumb. Refer to the later Debugging Crumb Structures chapter of this
book to learn more about it.

[^10]: Please also refer to [stretch and fold technique] for a
video showing you how to best perform the technique.

[^11]: You could do it
just to better understand how the dough feels in your hands at different
fermentation stages.

[^12]: The same
applies when making other doughs such as baguette doughs. The floured
surface will always be downwards facing. The dough is then flipped over
once for baking.

[^13]: The seam
    side should now be facing you.  Some bakers like to seal the seam a little
    more. I did not notice that this improves the dough's strength. As far as
    I can tell, this only improves the visual appearance of the bottom side of
    the final loaf.

[^14]: The actual temperature
depends on the bacteria and yeast you cultivated in your sourdough
starter.



---


# Non wheat sourdough

> In this chapter you will learn how to make a basic sourdough bread
> using non-wheat flour, basically all flour except spelt.
> The key difference between wheat and non-wheat flour is
> the quantity of gluten, the former feature a high amount
> of gluten, while the non-wheat flours do not.

The whole process (see the flowchart) is a lot
easier: you mix the ingredients and wait for a certain period until the dough
has reached the level of acidity that you like.  Afterward, you shape the
dough or pour it into a loaf pan. After a short proofing period, the bread can
be baked. Due to the lack of gluten development, the final bread will feature
a denser crumb compared to wheat, as you can see in
Picture .


**Flowchart:** *A visualization of the
      process to make non-wheat sourdough bread.  The process is much simpler
      than making wheat sourdough bread. There is no gluten development. The
      ingredients are simply mixed together.*


For non-wheat flours—including rye, emmer, and einkorn—no gluten
development has to be done, meaning there is no kneading, no
over-fermentation, and no issues with making flat bread.  In the case of rye
flour, sugars called pentosans prevent gluten bonds from properly
forming [rye pentosans].


![A sourdough rye bread made using a loaf pan.
      The rye bread is not scored. The crust typically cracks open during
      baking.](images/final-bread)

*A sourdough rye bread made using a loaf pan.
      The rye bread is not scored. The crust typically cracks open during
      baking.*


This chapter will focus on making rye bread. The flour could
be replaced with einkorn or emmer based on your preference.

The following recipe will make you 2 loaves:


The sourdough starter can be in an active or inactive state. If it has been
at room temperature for a week with no feedings then it will be okay, same
if it has come right out of the fridge then still it will be no problem.
The dough is very forgiving.

If you follow the suggested quantities from the recipe you are making a
relatively wet rye dough. It's so wet that it can only be made using a loaf
pan. If you want to make a freestanding rye bread, consider reducing the
hydration to around 60%.


![For non-wheat dough the ingredients are mixed
      together. There is no need to develop any dough strength. This
      simplifies the whole bread-making process.](images/ingredients)

*For non-wheat dough the ingredients are mixed
      together. There is no need to develop any dough strength. This
      simplifies the whole bread-making process.*


Mix together all the ingredients with your hands, or opt for a spatula to
simplify things. Rye flour itself is very sticky and unpleasant to mix by
hand, the dough will stick a lot to your hands. If you use a stiff starter, it
could be easier to first dissolve it in the dough's water, then add the other
ingredients.


![Rye flour has a sugar molecule known as pentosan.
      These pentosans prevent the rye flour from building gluten bonds. As a
      result the dough never features an open crumb and is always very sticky
      when hand mixing.](images/sticky-hands)

*Rye flour has a sugar molecule known as pentosan.
      These pentosans prevent the rye flour from building gluten bonds. As a
      result the dough never features an open crumb and is always very sticky
      when hand mixing.*


The goal of the mixing process is simply to homogenize the dough, there
is no need to develop any dough strength. Once you see that
your sourdough starter has been properly incorporated, your
dough is ready to begin bulk fermentation.

You can bulk ferment the dough for a few hours up to
weeks. By extending the bulk fermentation time, you increase
the acidity the final loaf is going to feature. After around
48 hours, the acidity will no longer increase. This is because
most of the nutrients have been eaten by your microorganisms.
You could let your dough sit for longer, but it wouldn't alter the
final flavor profile by much.

I recommend waiting until the dough has roughly increased
by 50% in size. If you are daring, you can taste the dough to
get an idea of the acidity profile, it will likely taste very sour. However, a
lot of the acid will evaporate during the baking process, therefore the final
loaf will not be as sour as the dough you are tasting.


![The crumb structure of rye bread. By making a wetter
  dough, more water evaporates during the baking and thus the
  crumb tends to be a bit more open. Generally, rye
  bread is never as fluffy as wheat sourdough bread. The crust
  of this bread is a bit pale. The crust color can be controlled
  by baking the bread for a longer period.](images/crumb)

*The crumb structure of rye bread. By making a wetter
  dough, more water evaporates during the baking and thus the
  crumb tends to be a bit more open. Generally, rye
  bread is never as fluffy as wheat sourdough bread. The crust
  of this bread is a bit pale. The crust color can be controlled
  by baking the bread for a longer period.*


Once you are happy with the acidity level, proceed to dividing
and shaping your dough.  If you made a drier dough, use as much
flour as needed to dry the dough a little bit and form a dough ball.
There is no folding the dough. All you do is tuck it together
as much as is needed to apply the shape of your banneton.

Shaping might not be possible if you opt for the wetter dough. Carefully spread
the dough with a spatula in your greased loaf pan, wetting the spatula to make
this process easier. Spread it until the surface looks smooth and shiny.

For proofing, I recommend waiting around 60 minutes. An extended
proofing period does not make sense unless you want to further
increase the dough's acidity. The dough will not become fluffier
the longer you proof. With the short proofing period, however,
the dough will become a bit more homogeneous. This way the final
bread looks more uniform. The proofing period also allows the
dough to fully extend and fill the edges of the loaf pan. I also
like to move the dough to the fridge for proofing. The dough stays
good in the fridge for weeks. You can proceed and bake it at a
convenient time for you.

Once you are happy with the proofing stage, proceed and bake your dough
just like you'd normally do, more details can be found in
the relevant chapter. One challenging aspect
of using a loaf pan is to make sure that the center part of your
dough is properly cooked. For this reason, it is best to use a thermometer
and measure the internal temperature. The bread is ready once the internal
temperature reaches 92°C (197°F). I recommend
removing the bread from the loaf pan once it reaches the desired temperature,
then continue baking the loaf without the pan and steam. This way you achieve
a great crust all around your loaf, and can bake as long as you like until you
have achieved your crust color of choice. The darker, the more crunchy
the crust and the more flavor it offers. If you feel your dough might have
been overly acidic you can extend the baking time, as the longer you bake, the
more acidity will evaporate.

This is one of my favorite breads to bake which I eat on an
almost daily basis. The effort required to make bread like
this is much lower compared to a wheat-based dough. In some
cases, I extend the recipe and add additional sourdough discard
to the dough. You can add as much discard as you like. The resulting
bread will have a very complex but delicious flavor profile.



---


# Mix-ins

> In this chapter, you will learn about the fascinating world of sourdough
> mix-ins. Discover how these additions can elevate your bread, enhancing
> flavor, adding vibrant colors, and creating delightful textures that make
> each loaf a culinary masterpiece.


![These soft pull-apart sourdough
    buns have been made with the addition of pumpkin purée. The mashed pumpkin
    adds flavor and hydration to the dough.](images/pumpkin-sourdough)

*These soft pull-apart sourdough
    buns have been made with the addition of pumpkin purée. The mashed pumpkin
    adds flavor and hydration to the dough.*


A loaf of wheat sourdough has a very pure aesthetic. Good craftsmanship and
precision transform the ingredients into simple, but delicious food. With
mix-ins, the basic recipe can become the starting point for a whole world of
modifications to try and combine. Think of the loaf of bread as a blank canvas
to express yourself.

## Categories


![A popular method is to substitute part of the
          dough's water with another liquid, such as puréed pumpkin.  When
          incorporating the purée, add any extra water gradually, as the purée
          will release its own liquid into the dough over time.](images/pumpkin-on-flour)

*A popular method is to substitute part of the
          dough's water with another liquid, such as puréed pumpkin.  When
          incorporating the purée, add any extra water gradually, as the purée
          will release its own liquid into the dough over time.*


One approach to categorizing the mixins is to look at their respective shape.
However, the transition between these categories is somewhat fuzzy:

- Liquids: Integrate homogeneously into the dough, may replace some of or all of the water. Examples: Milk, butter, oil, spinach juice, tomato juice, eggs
- Powders: Integrate homogeneously into the dough, may replace some of the flour. Examples: Milk powder, semolina, cocoa, spices
- Small bits: Individually visible in the final loaf, small enough to distribute somewhat evenly throughout the dough. Examples: Seeds (wheat berries, rye berries, poppy seeds, sesame, pumpkin seeds, flax seeds), whole spices (coriander)
- Chunks: Larger pieces that will only be present in the occasional bite when eating a slice of your bread. Examples: dried tomatoes, chunks of cheese, chunks of chocolate

Another categorization approach looks at the changes to the bread:

- Flavor: Significantly changes the taste of the bread. Examples: rye flour, corn flour, spices, sugar.
- Color: Significantly changes the look of the bread. Examples: cocoa, squid ink, beetroot juice, tomato juice.
- Texture: Significantly changes the feeling in the mouth when eaten. Examples: Cheese (gummy), seeds (crunchy), olives (squishy chunks).

Many of the above-listed mix-ins can't be pinpointed to a single category. They
change multiple aspects of the final bread at the same time.


![In this case a combination of flax, sunflower and
    sesame was added to the dough. The seeds will slightly dehydrate the dough
    during fermentation and thus adding a bit more water
    (1–2%) is advised.](images/seeded-sourdough)

*In this case a combination of flax, sunflower and
    sesame was added to the dough. The seeds will slightly dehydrate the dough
    during fermentation and thus adding a bit more water
    (1–2%) is advised.*


Mix-ins affect the structure of the dough. One aspect is the impact on
hydration. Some mix-ins absorb a lot of water when added to the dough, so you
have to increase the amount of water to achieve the same dough consistency.
The other impact is on the gluten network. Bits and chunks disrupt the gluten
network and may reduce oven spring during baking. All of this depends on the amount of mix-ins
used. A good rule of thumb is to add 10–20% of the amount
of flour in most mix-ins, reduced to around 1–5% of the
amount of flour for spices.

An important factor is also the mix-in's behavior during baking. Particularly
chunks may bake differently than dough, and either melt (cheese) leaving holes
inside, or char when peeking through the crust (\eg vegetables). These
problems can be mitigated to some degree with the right preparation (\eg chopping
into smaller pieces, soaking dry ingredients in water or oil first,
or squeezing out excess moisture).

## Examples

The following is a list of common mix-ins and their peculiarities. They can be
combined depending on your preference.

### Flours
These are powders. Usually, you want to just replace some fraction of the
regular bread flour. Different flours change the taste of the bread and
usually moderately affect the color.


![Broa de milho is a traditional Portuguese bread
  made out of half rye and half corn flour.](images/broa)

*Broa de milho is a traditional Portuguese bread
  made out of half rye and half corn flour.*


- Whole wheat flour (substitute any amount, makes the bread taste more complex, nutty)
- Rye flour (very hearty, nutty, malty taste)
- Enzymatic malt (malty taste, improves enzymatic activity). The malt is a great addition when making quicker yeast-based doughs.
- Semolina (supports Mediterranean flavors)
- Cocoa (replace 10% of the flour for a black loaf, goes great with sweet toppings)
- Other non-wheat flours such as: Chickpea, corn, hemp, potato…{}

### Liquids

Instead of using water, you can substitute it with a different liquid,
affecting taste and texture.


![Dark hearty stouts work excellently as a water
  replacement when making sourdough bread. The resulting loaf features a
  hearty malty taste](images/beer-bread)

*Dark hearty stouts work excellently as a water
  replacement when making sourdough bread. The resulting loaf features a
  hearty malty taste*


- Beer
- Butter
- Buttermilk
- Cereal milk (the leftover milk from eating cereals)
- Coffee
- Eggs
- Fruit/vegetable juices (also see the relevant section)
- Milk (for sweet, soft breads)
- Milk alternatives such as: Almond, oat, soy…{}
- Mashed potatoes
- Mashed sweet potatoes. Bolo do caco is a typical bread from Madeira, made from 50% wheat flour and 50% mashed potatoes.
- Olive oil (Mediterranean)
- Other mashed vegetables such as: Beets, pumpkin…{}

### Colors

Some mix-ins will change the color and flavor of your bread. Common colorings
include:

- Activated charcoal powder (black)
- Beetroot juice (red)
- Blueberry juice (blue)
- Blue butterfly pea flower powder (blue)
- Carrot juice (orange)
- Pear juice (pink)
- Spinach juice (green)
- Squid ink (black)
- Strawberry juice (red)
- Tomato juice (red)

### Seeds and nuts
These are small bits, with some almost crossing into the chunk category. Some
seeds benefit from being boiled for about 10 minutes before adding them to the
dough.


![The Stollen is a traditional German sweet Christmas
    bread featuring a variety of mix-ins. The dough typically contains candied
    lemon, candied orange, and raisins. The mix-ins are soaked in rum before
    being added to the dough. While the stollen matures after baking (up to
    6 months) the candied ingredients release their aroma to the baked
    product.](images/stollen-close-up)

*The Stollen is a traditional German sweet Christmas
    bread featuring a variety of mix-ins. The dough typically contains candied
    lemon, candied orange, and raisins. The mix-ins are soaked in rum before
    being added to the dough. While the stollen matures after baking (up to
    6 months) the candied ingredients release their aroma to the baked
    product.*


- Cacao nibs
- Chia seed
- Chopped or whole nuts such as: Almonds, hazelnuts and walnuts
- Flaxseeds
- Hemp seed
- Poppy seed
- Pumpkin seed
- Sesame
- Sunflower seed
- Whole rye berries (boil 10 minutes)
- Whole wheat berries (boil 10 minutes)


![A sourdough bread made with half
      whole-rye flour and half rye berries. The berries are typically boiled
      for 10 minutes to allow them to soften a bit. When baking a loaf it is
      advised to use a thermometer to measure whether it is done baking. The
      final bread features a hearty tangy flavor and has a moist crumb.](images/seeds-bread)

*A sourdough bread made with half
      whole-rye flour and half rye berries. The berries are typically boiled
      for 10 minutes to allow them to soften a bit. When baking a loaf it is
      advised to use a thermometer to measure whether it is done baking. The
      final bread features a hearty tangy flavor and has a moist crumb.*


### Spices and flavor mix-ins
These are mostly powders or small bits.

- Blueberry skins (press through a sieve to remove juice), raw blueberries
- Browned onions
- Candied fruits such as: Lemon, orange, pineapple…{}
- Cinnamon
- Grated hard cheese such as: Gruyère, parmesan…{}
- Mediterranean herbs such as: Marjoram, oregano, rosemary, thyme…{}
- Miso
- Molasses
- Sugar
- Spices such as: Anise, fennel, cinnamon, coriander, cumin…{}
- Zests such as: Lime, Lemon, orange…{}

### Highlights
Mostly chunks, that add a big contrast and flavorful highlight to the basic
bread. Usually, you want to use only one (or a maximum of two) of these. The suggestions
can often be complemented by some flavor or flour mix-in.

- Chocolate chunks or drops
- Chunks of black garlic
- Chunks of cheese such as: Cheddar, feta…{}
- Cornflakes
- Dried fruits such as: Cranberries, dates, raisins…{}
- Olives
- Pickled pepperoni
- Sun-dried tomatoes (squeeze out the oil if using pickled ones, or soak dried ones in water)

### Combinations
A few combinations where multiple mix-ins complement each other:

- Butter and milk. Then add cinnamon and brown sugar before shaping
- Cheddar and pepperoni
- Cheddar and jalapeño
- Cocoa, cacao nibs, whole hazelnuts
- Cranberry and walnuts
- Semolina, Mediterranean herbs, olives, sun-dried tomatoes
- Tomato juice instead of water with 20% rye flour

## Techniques

Adding mix-ins to the dough is just the simplest approach. Add the mix-ins
directly when you knead the dough. After the first kneading wait for 30
minutes to see if the dough has enough or too much water. In the case of
whole-soaked berries (\eg rye or wheat) chances are that the berries will
release some water and make the dough wetter. In this case, you will want to
add a bit more flour to the dough to compensate for the high hydration.

### What is the best stage to
incorporate inclusions (seeds) into the dough?


You can include seeds directly at the start when mixing the dough. If you use
whole seeds such as wheat or rye kernels, soak them in water overnight and
then rinse them before adding them to the dough. This makes sure that they are
not crunchy and are soft enough when eating the bread. If you forgot to soak
them you can cook the seeds for 10 minutes in hot water. Rinse them with cold
water before adding them to your dough.

If you want to sweeten the dough, your best option is to add sugar during the
shaping stage. Sugar added too early in the process typically gets fermented
until none of it remains. Adjust your shaping technique a little bit and
spread your sugar mixture over a flattened-out dough. You can then roll the
dough together, incorporating layers of sugar.

### Adding before shaping


![A great technique is to add some of your mix-ins
      directly before shaping. In this case, a mixture of apples, cinnamon and
      brown sugar was applied. Proceed and roll the dough together. Afterward
      cut the roll into smaller pieces using a sharp knife, dough scraper or
      dental floss. Place each piece of dough next to each other in a greased
      bowl to allow them to be proofed.  Proceed and bake as you would
      normally do. The benefit of this technique is that the mix-ins will not
      be fermented. This is typically required in the case of sugar since you
      want the final baked goods to feature sweetness. If included upon
      initial mixing most of the sugar would be fermented and the bread would
      not taste sweet.](images/apple-swirl)

*A great technique is to add some of your mix-ins
      directly before shaping. In this case, a mixture of apples, cinnamon and
      brown sugar was applied. Proceed and roll the dough together. Afterward
      cut the roll into smaller pieces using a sharp knife, dough scraper or
      dental floss. Place each piece of dough next to each other in a greased
      bowl to allow them to be proofed.  Proceed and bake as you would
      normally do. The benefit of this technique is that the mix-ins will not
      be fermented. This is typically required in the case of sugar since you
      want the final baked goods to feature sweetness. If included upon
      initial mixing most of the sugar would be fermented and the bread would
      not taste sweet.*


Another approach is to lay the dough out flat after the bulk fermentation.
Then using a spatula spread your ingredient over the flat dough. Continue with
your regular shaping and/or roll up the dough. When creating a roll you can
use a sharp knife to cut the dough, dental floss works great too. Afterward,
place the tiny swirls in a container to let them proof and become fluffier.
This is an excellent way to add sweet mix-ins as the microbes will not ferment
them. When adding sugar to the initial dough it will be fermented and the
resulting dough will not taste sweet (depending on the fermentation duration).
This approach is excellent for garlic/cheese rolls, garlic/herb rolls, and
cinnamon rolls

### Covering the surface


![These are chop buns which are created by chopping
    up a retarded dough into smaller pieces before baking. Then each piece of
    dough is quickly dumped in water and then rolled in a bowl of seeds.
    Afterward, the dough is directly baked in the preheated oven. These
    coverings add superb additional flavor and can be adjusted depending on
    your preference. I love adding a mixture of sunflower, flax, and
    sesame seeds.](images/surface-seeds)

*These are chop buns which are created by chopping
    up a retarded dough into smaller pieces before baking. Then each piece of
    dough is quickly dumped in water and then rolled in a bowl of seeds.
    Afterward, the dough is directly baked in the preheated oven. These
    coverings add superb additional flavor and can be adjusted depending on
    your preference. I love adding a mixture of sunflower, flax, and
    sesame seeds.*


This works best for either powders or small bits. After shaping wrap your
coverings on the dough's surface. This works great too when covering your
banneton or loaf pan with seeds or oats. When using a loaf pan or banneton
these coverings also help to make the container stick less.

Another approach commonly used with buns is to wet the surface or dump the
dough in water. Afterward, dip the wet piece of dough into your bowl of
mix-ins.  This does not work for all mix-ins, as some can't handle the high
temperatures during baking and char. Most commonly done with seeds
(\eg sesame, oats, flax-seed).

### Swirled colors
Mix-ins that change the color of the dough bring the opportunity for even more
creativity by merging the dough before shaping.

Proceed and separate your base dough before adding a colorful ingredient. Bulk
ferment the dough in separate containers. Then Combine the two (or
more) differently colored doughs by laminating and stacking the colored sheets
of dough before the last folding, just before shaping. This way the colored
layers won't mix and the resulting dough will have differently colored and
tasting layers[^1].

---

[^1]: I once made an experimental dough by merging a wheat,
rye, spelt and einkorn dough into a single dough. The resulting dough was
layered featuring different colors, textures, and flavors.



---


# Baking

> Baking refers to the part of the process where you are loading your dough into
> the oven[^1].  Baking is typically done after
> your dough has gone through the bulk fermentation and proofing stage.  This
> chapter will review what happens to your dough during baking, as well as
> several techniques used to improve the final result.

## The process of baking
Once temperature starts to rise, the dough will go through several stages as
summarized in the table below.  As the dough heats up, the water
and acids in your dough start to evaporate. When baking a gluten based dough,
the bubbles in your dough start to expand.  The dough starts to vertically
rise, this is called oven spring.  Your bread starts to build a crust of
gel-like consistency, the crust is still extensible and can be stretched.


| **°C / °F** | **Stage** | **Description** |
| --- | --- | --- |
| 60 / 140 | Sterilization | The temperature is too hot for your microorganisms and they die. |
| 75 / 167 | Gel building | A gel builds on the surface persisting your dough's structure. It is still extensible and can spring in the oven. |
| 100 / 212 | Water evaporation | Water begins to evaporate and inflates your dough's alveoli. |
| 118 / 244 | Acetic acid evaporation | The vinegary tasting acid starts to evaporate, sourness decreases. |
| 122 / 252 | Lactic acid evaporation | The dairy tasting lactic acid begins to evaporate, sourness further decreases. |
| 140 / 284 | Maillard reaction | The Maillard reaction starts to deform starches and proteins. The dough starts browning. |
| 170 / 338 | Caramelization | Remaining sugars begin to caramelize giving your bread a distinct flavor. |

*The different stages that
            your dough undergoes during the baking process.*


At around  60°C (140°F) the microbes in your dough start to die.
There are rumors that until this happens the microbes produce
a lot of CO₂, resulting in the dough's expansion. However, this temperature
is reached quickly. Furthermore, stress makes the microbes
enter sporulation mode in order to focus on spreading genetics.
More research should be done here to validate or invalidate this
claim.

At  75°C (167°F) the surface of your dough turns into a gel. It
holds together nicely but is still extensible. This gel is essential
for oven spring as it retains the gas inside your dough.

At around  100°C (212°F) the water starts to evaporate out of your
dough. If this weren't the case, your dough would taste soggy and
doughy. The higher hydration your dough has, the more water your bread
still contains after the bake, changing its consistency.  As a result the
crumb is going to taste a bit more moist.

Another often undervalued step is the evaporation of acids.
At 118°C (244°F) the acetic acid in your dough
starts to evaporate.
Shortly after at 122°C (252°F) the lactic acid begins evaporating.
This is crucial to understand and it opens the door to many interesting
ways to influence your final bread's taste. As more and more water
begins to evaporate the acids in your dough become more concentrated.
There is less water but in relation you have more acids, therefore a shorter
bake will lead to a more tangy dough. The longer you bake the bread,
the more of the water evaporates, but also ultimately the acids will follow.
The longer you bake, the less sour your bread is going to be. By controlling
baking time you can influence which sourness level you would like to achieve.

It would be a very interesting experiment to bake a bread at different exact
temperatures. How would a bread taste with only evaporated water but
full acidity? What if you were to just completely get rid of the acetic
acid? How would the taste change?


*This
      chart shows how surface temperatures change using different steaming
      methods. In this case I used a Dutch oven and an apple as dough
      replacement. All the apples were coming from the fridge. The temperature
      was measured using a barbecue thermometer.  The more steam, the faster
      the apple's surface temperature increases.*


As the temperature increases further the crust thickens. The Maillard reaction
kicks in, deforming proteins and starches. The outside of your dough starts to
become browner and crisper, this process begins at
around 140°C (284°F)

Once the temperature increases even more to around 170°C
(338°F),
the caramelization process begins, the remaining sugars and the microbes which
did not convert yet start to brown and darken. You can keep baking
for as long as you like to achieve the crust color that you
like[^2].

The best method to know that your dough is done is to take
the temperature of your dough, you can use a barbecue thermometer
to measure it. Once the core temperature is at around 92°C
(197°F),
you can stop the baking process. This is typically not done though
as the crust hasn't been built yet[^3].

Once your dough has finished baking, it is ready to eat: your
dough has turned into a bread. At this
point, your bread is sterile as the temperature was too hot for
for the microorganisms to survive[^4].

## The role of steam
Steam is essential when baking as it helps to counter premature
crust building. During the first stage of the bake, the dough
increases in size as the water in your dough evaporates and pushes
the whole dough upwards.

Normally, under high heat a crust would form. Just like
if you were to bake vegetables in your home oven, at some point
they become darker and crisper. This is the same thing that
happens with your dough, and you want to delay this process
as long as possible until your dough no longer expands.
Expansion stops when most of the microbes have died and
the evaporating water no longer stays inside the alveoli.

The stronger the gluten network, the more gas can be retained
during the baking process. This gluten network at some point
loses its ability to contain gas as the temperature heats
up. The dough stops increasing in size. The steam plays
an important role as it condenses and evaporates on top
of your dough. The surface temperature is rapidly increasing
to around 75°C (160°F). At this temperature the
gel starts to build, and is still extensible and allows expansion.
Without the steam, the dough would never enter the gel stage,
but instead directly go to the Maillard reaction zone. You
want your dough to stay in this gel stage as long as possible
to achieve maximum expansion[^5].


![The second stage of the bake is done
      without steam to build a thicker, darker crust.](images/baking-process-stage-2.jpg)

*The second stage of the bake is done
      without steam to build a thicker, darker crust.*


When not steaming enough, you will notice that the scoring
incisions do not properly open up during the bake. They stay
closed as the dough is unable to push through the crust.
Another common sign, as you can see in the figure is
that you have larger pockets of air towards the crust of your dough. As the
dough increases vertically, expansion is halted by the crust. The pockets
of air converge into larger pockets as the pressure increases.
This can also happen when you are baking at too high a temperature.

The more you steam, the softer your dough's crust is. You will never
enter the Maillard and caramelization stage. This
is the reason why the source of steam is removed
for the second stage of the bake. No more expansion can
happen and you can focus on building a crust. If you
would like a soft crust, you can steam your dough all the
way.


![A submission by Karomizu showing a bread that
      has been baked at too high a temperature or with too little steam. Note
      the large pockets of air towards the crust. They are a typical
      indicator.](images/baking-too-hot)

*A submission by Karomizu showing a bread that
      has been baked at too high a temperature or with too little steam. Note
      the large pockets of air towards the crust. They are a typical
      indicator.*


## Building up steam

**Flowchart:** *A schematic visualization of the baking
      process using different sources of steam in a home oven.*


![My default home oven setup. The tray of rocks
  and tray on top of the rolls greatly improve the steaming capabilities. This way the bread can
  rise more during the initial stage of the baking process.](images/oven-example)

*My default home oven setup. The tray of rocks
  and tray on top of the rolls greatly improve the steaming capabilities. This way the bread can
  rise more during the initial stage of the baking process.*


![How steam builds in your oven
      using the later described inverted tray method.](images/baking-process-steam.jpg)

*How steam builds in your oven
      using the later described inverted tray method.*


### Dutch ovens


![An example of a dutch oven. Some are also
      made out of enameled cast iron, others are made out of clay and some
      feature a glass lid.  They all work similarly by entrapping some of the
      steam created during the baking process. The steamy environment allows
      the bread to rise further and thus have more oven spring and feature a
      fluffier crumb.](images/dutch-oven-example)

*An example of a dutch oven. Some are also
      made out of enameled cast iron, others are made out of clay and some
      feature a glass lid.  They all work similarly by entrapping some of the
      steam created during the baking process. The steamy environment allows
      the bread to rise further and thus have more oven spring and feature a
      fluffier crumb.*


**Flowchart:** *A visualization of the baking
      process using a dutch oven (DO). The dough is steamed for the first half
      of the bake and then baked without cover for the second half of the
      bake. The desired darkness and thickness of the crust depends on your
      personal preference. Some bakers prefer a lighter crust and others a
      darker.*


Dutch ovens are an ideal way to bake with a lot of
steam. They are not fully sealed. Regardless though,
as water evaporates from your dough, it will create a steamy
environment allowing your dough to rise. It
makes baking in a home oven very easy.

When using a Dutch oven, make sure to preheat it properly,
this way your dough will not stick to it. You can also
use additional semolina flour or parchment paper. Another
good trick is to spritz your dough with a bit of water.
To create more steam, you could also place a small ice cube
next to your main dough.

I have been using a Dutch oven myself for a long time. They
have issues though. They are relatively heavy. It is dangerous
to operate hot cast iron ovens. Especially when working with steam,
you have to be very careful. Furthermore,
they are expensive to buy. If your Dutch oven is made out
of cast iron you have to season it from time to time. This takes
time.

The biggest disadvantage, though, is
capacity. You can only bake a single piece of bread at a time,
as the size of the Dutch oven is limited.
In many cases, it makes sense to bake multiple
loaves in one go. It makes the whole process more
efficient as you have to knead less per loaf. The time it
takes to make one loaf is significantly reduced on average. Furthermore,
you don't require as much energy. You don't have
to preheat your oven twice for each loaf.

An additional disadvantage of Dutch ovens is the
need to move very hot and heavy cast iron[^6].
You will need to be very careful and ideally use
heat-resilient gloves when touching your Dutch oven.

Furthermore, some of the Dutch ovens come at a hefty
price tag. Especially for new bakers buying a Dutch oven on
top of other tools can be quite a hefty investment. For
this reason, I advocate the inverted tray method visualized
in the next section. In case you do not own an oven consider trying
the simple flatbread recipe which is baked in a pan. Please
refer to the relevant section for more details.


### Inverted tray method

The inverted tray method simulates a Dutch oven.
By placing another tray on top of your dough, the steam
created from the dough and water source stays
around your dough.


**Flowchart:** *A schematic visualization the
  inverted tray baking method that works great for home ovens.*


The biggest advantage of this method compared to the
Dutch oven is scalability. You can bake multiple loaves
at the same time. In my case that is around 2 freestanding
loaves and 4 loaves in a loaf pan.

For the inverted tray you will need the following tools:
- 2 trays
- 1 heat resistant bowl
- Boiling water
- Oven gloves
- (Optional) Parchment paper


![My home oven setup.](images/baking-example.jpg)

*My home oven setup.*


These are the steps to follow with the inverted tray method:
1. Preheat the oven to around 230°C (446°F) and preheat one of the trays.
2. Bring water to boil.
3. Place your loaves on a piece of parchment paper. You can also place each on a tiny piece of parchment paper. This makes loading the dough easier. If you don't have it or don't want to use it, you can opt for semolina flour. It helps to make the tray nonstick.
4. Take out your hot tray and place it on a cooling rack or on something else that is heat resistant.
5. Score your doughs.
6. Place your doughs on the hot tray.
7. Place the cold tray in your oven in an inverted position.
8. Move your hot tray including the loaves back to the oven.
9. Place the boiling water in the heat-resistant water bowl. I have added rocks to it, as it helps to improve the steam even further. This is optional.
10. Close the oven.
11. After 30 minutes remove the top tray. Also remove the bowl with water.
12. Finish baking your bread until you have reached your desired crust color. In my case this is another 15–25 minutes typically.

## Conclusions


| **Oven type** | **Plain (no tools)** | **Inverted tray** | **Dutch oven** |
| --- | --- | --- | --- |
| Gas | No | No | Yes |
| Convection (Fan always on) | No | No | Yes |
| Convection (Fan can be disabled) | No | Yes | Yes |
| Steam | Yes | Yes | Yes |

*An overview of different oven types and their
            different baking methods.*


Depending on your home oven, a different method
of steaming may be used. Generally most ovens
are made to vent out most of the steam during the
bake. They are typically not fully closed. During
baking you want to dry out whatever you are baking.
This is ideal if you are roasting vegetables and
want them to dry out. For baking though, this is
highly problematic. As described earlier, you
want there to be as much steam as possible.

If you are using a gas-based oven, the only option
is to utilize a Dutch oven. The same is true when you
are using a convection oven with a fan that
cannot be disabled. When using a convection
oven with a fan that can be turned off, you can
opt to use the cost-efficient inverted tray
method.

If you are in the luxurious
position of owning a steam oven, things are easier.
Just activate the steam function and you are
good to go. Placing an additional tray on top of your
dough during the bake helps to bake with indirect
heat. You remain in the gel zone longer and
will experience more oven spring.

---

[^1]: While some breads like flatbreads could also be baked on the
stove. This chapter focuses on the home oven.

[^2]: This really depends a lot on your personal preference.
Some people prefer a darker crust, others prefer a more pale crust.
It's better to build less crust than too much. You can always just
heat your bread in the oven one more time to continue building a
darker crust.

[^3]: The thermometer is
especially important when using a large loaf pan. It is sometimes
very hard to judge from the outside if the dough is done. I failed
many times and ended up having a semi baked dough.

[^4]: I wonder though
if a starter culture could be grown again from a slice of bread.
Under heat stress the microorganisms begin sporulating. Maybe
some of the spores survive the baking process and could be reactivated
later? If this works, you could use any store bought sourdough
bread as a source for a new starter.

[^5]: You can remove your
dough from the oven after 5 minutes to see the gel. You will notice
that it holds the dough's structure and it has a very interesting consistency.

[^6]: %
  Some of them can weigh up to 10 kg. Moving them is quite
  a tedious exercise. Especially if the cast iron is
  heated you have to be very concise with your movements.
  Despite doing my best I have a few scars on my
  hands and arms from operating the Dutch ovens.



---


# Storing bread

> In this chapter you will discuss different methods of storing your bread, each
> with their own pro and cons.  This way your bread can be best enjoyed at a
> later time.

A summary can be found in the table below, with details and
explanation in the rest of this chapter.

| **Method** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| Room temperature | The easiest option. Best for bread that is eaten within a day. Crust typically stays crisp when humidity not too high. | Bread dries out very quickly. |
| Room temperature in airtight container | Good for up to a week. | Bread needs to be toasted for crust to become crisp again. Catches mold more quickly |
| Fridge | Bread stays good for weeks. Can dry out a little bit when not using air-tight container. | Bread needs to be toasted. Requires fridge and energy. |
| Freezer | Bread stays good for years. | Requires thawing and then toasting. Requires freezer and energy. |

*A table visualizing the advantages
            and disadvantages of different bread storing options.*


## Room temperature

The most common method is to store your bread
at room temperature. After taking a slice of bread,
store your bread with the crumb facing side
downwards.

This method works great if you want to eat
your bread within a day. The crust stays
crisp and does not become soft[^1].
The biggest downside to this method is that
the bread becomes hard quickly. As time progresses,
more and more water evaporates from your dough's
crumb. Ultimately, the bread will become very hard
and impossible to eat. The more water you use
to make the bread, the longer the bread stays good.
A low-hydration recipe can dry out after 1–2 days;
a high-hydration bread needs 3–4 days to dry out.

Once your bread has dried out, you can run it under
tap water for around 10 to 15 seconds.
This water bath allows the
crumb's starch to absorb a lot of water. Proceed and
bake your bread again in the oven. The resulting loaf
will be almost as good as new again.

Another option for dried-out bread is to use it
to make breadcrumbs. These bread crumbs can be mixed
into subsequent loaves. They can also be used as
base ingredients for other recipes such as *Knödel*[^2].

## Room temperature in a container

Just like the previous option, you can also store your
bread inside a container. This could be a paper bag,
a plastic bag, or a bread storage box. The paper bag and
most bread boxes are not fully sealed, allowing some of
the air to diffuse out of the container. This also means that
the bread will slightly dry out.

When using a sealed bag such as a plastic bag, the bread
will retain a lot of moisture. The bread will stay good
for a longer period. However, at the same time, the crust
will also lose its crispness. Some of the water diffuses
into the bag and is then re-absorbed by the crust. If
you want the crisp crust, the best option is to toast your
bread.

Another problem with storage containers is natural
mold contamination. The moment your bread is taken out of
the oven it starts being contaminated with aerial mold spores.
The spores are microscopically small and are everywhere.
The mold spores grow best in a humid environment. By placing
your dough in a container you have created a mold paradise.
A plain yeast-based dough will start to mold within a few days
like this. The sourdough-based bread stays good
for a longer period as the acidity is a natural mold
inhibitor.

## Fridge

In my own experience storing bread inside the fridge
works well as long as you use a sealed container, even if some
sources say that the bread dries out inside of the
fridge [storing bread]. Supposedly the fridge
encourages liquid from the crumb to migrate to the bread's surface.

In my experience though, the trick is to use a sealable
container. With a sealable ziplock bag,
the excess humidity will stay in the bag and ensures
that the bread does not dry out as quickly. At room
temperature, this would cause your bread to mold. At
lower temperatures, the bread can stay good like this for
weeks. The crust however, will lose its crispness and
thus toasting is advised.

## Freezing

Another great option for long-term storage is to use
your freezer. Slice up the whole loaf and create portions
that you can consume within a day. Store each portion
in a separate container and place them inside your
freezer.

When you want to eat fresh bread, open one of the containers
in the morning and allow the bread to thaw over a few
hours. This is needed so you can easily separate the frozen-together
slices. Toast the slices in your toaster
or bake them in the oven until they have the crispness
that you like.

This option is great for very long-term storage. Personally
I like having a few slices of bread frozen as an emergency
backup when I have had no time to bake.

A 2008 study hints that there might be some health benefits to freezing and
toasting your bread. By doing so the starch molecules could become more
resistant to digestion and thus lower your body's blood sugar response by
almost 40% [freezing toasting bread].

---

[^1]: The higher the humidity in your room,
    the faster the crust will become soft.

[^2]: *Knödel* is an
    Austrian dish that uses old bread as a basis.
  Breadcrumbs and day-old bread are mixed with eggs, and sometimes
  spinach or ham are added. The batter is then boiled in salty water.



---


> You could consider this chapter as an FAQ about most problems faced by
> bakers, it should give you the debugging tools you need to analyze the
> situation.  You can then apply the appropriate measures and squash each
> *bug* one by one until you reach the perfect loaf.

## Starter
### My starter does not double in size

Some bakers call for the sourdough starter to double in size before using it.
The idea is to use the sourdough starter at peak performance to ensure a
balanced fermentation in the main dough.

The doubling in size metric should be taken with a grain of salt when judging
your starter. Depending on the flour you use to feed the starter, different
levels of its rising can be expected.  For instance, if you use rye flour then
only very little gas from the fermentation can be retained inside the starter.
In consequence, your sourdough starter will not rise as much. It could still
be in healthy shape. If you use wheat flour with less gluten, the starter will
not rise as much either. The reason is that you have a weaker gluten network
resulting in more gas dispersing out of your dough.

That being said, it is recommended that you develop your volume increase
metric. Your starter will increase in size and then ultimately lose structure
and collapse. Observe the point before it collapses.  This is the point when
you should use your starter. This could be a 50% volume
increase, 100% or 200%. It is always better to
use the starter a little bit too early rather than too late. If you use the
starter later, reduce the quantity that you use. If the recipe calls for a
20% starter quantity, use only 10% starter in
that case. Your starter will regrow in your main dough.

On top of relying on the size increase, start taking note of your starter's
smell. Over time you will be able to judge its fermentation state based on the
smell. The stronger the smell becomes, the further your dough has fermented.
This is a sign that you should use less starter when making the actual dough.

Please refer to
the relevant section "sec:readying-starter" for more
information on the topic.

### What's the best starter feeding ratio?

The best starter feeding ratio is commonly either 1:5:5 or 1:10:10.
In the case of 1:5:5 that's 1 part old starter,
5 parts flour and 5 parts water. If you are using a stiff starter,
use half the amount of water. So that's 1:5:2.5. Depending on when
you last fed your starter 1:10:10 might make more sense. If the starter
is old and hasn't been fed recently the 1:10:10 ratio is a better choice.
By reducing the starter inoculation ratio, you provide the microorganisms
with a cleaner environment. This way they can reproduce and regrow
into a more desirable balance to begin your dough fermentation.

Generally, think of your sourdough starter as a dough. Use the same
ratios you use for your bread dough for your starter. Your starter
should be trained in the same environment that you later use
for your dough. This way your starter is perfectly suited to
ferment the dough into which it is later inoculated.

The only exception to the 1:5:5 and 1:10:10 rule is the initial
starter set-up stage. For the first days during the starter-making
process there aren't enough microbes yet. So using a 1:1:1 ratio
can speed up the process.
### What's the benefit of using a stiff sourdough starter?

A regular sourdough starter has equal parts of flour and water
(100% hydration). A stiffer sourdough starter features a
hydration level of 50–60%.

The stiff sourdough starter boosts the yeast part
of your starter more. This way your gluten degrades
slower and you can ferment for a longer period. This
is especially handy when baking with lower gluten flours.

You can read more about the topic of stiff sourdough
starters in the relevant section.

### What's the benefit of using a liquid sourdough starter?

The liquid starter will boost anaerobic bacterial
fermentation in your starter. This way your starter
tends to produce more lactic acid rather than acetic
acid. Lactic acid is perceived as milder and more
yogurty. Acetic acid can sometimes taste quite
pungent. Acetic acid can be perfect when making
dark rye bread but not so much when making a fluffy
ciabatta-style loaf.

When converting your starter to a liquid starter you are
permanently altering the microbiome of your starter.
You cannot go back once you have eliminated acetic
acid-producing bacteria. So it is recommended to keep
a backup of your original starter.

A downside to the liquid starter is the overall
enhanced bacterial activity compared to yeast activity. This means the baked bread
will have more acidity (but milder). The dough will degrade
faster during fermentation. For this reason, you
will need to use strong high-gluten flour when using
this type of starter.

You can read more about the liquid starter in
the relevant section

### My new starter doesn't rise at all

Make sure that you use unchlorinated water.
In many areas of the world, tap water has
chlorine added to kill microorganisms. If that's
the case in your region, bottled spring water will
help.
You can also use a water filter with activated charcoal
which will remove the chlorine.
Alternatively, if you draw tap water into a pitcher or other
container and let it sit, loosely covered, the chlorine
should dissipate within 12–24 hours, and you have
the added advantage of automatically having
room-temperature water.

Make sure to use whole grain flour (whole-wheat, whole-rye, ).
These flours have more natural wild yeast and
bacterial contamination. Making a starter
from just white flour sometimes doesn't work.
Try to use organic unbleached flour to make
the starter. Industrial flour can sometimes
be treated with fungicides.

### I made a starter, it rose on day 3 and now not anymore

This is normal. As your starter is maturing, different
microorganisms are activated. Especially during
the first days of the process, bad microbes
like mold can be activated. These cause your
starter to rise a lot. With each subsequent
starter-feeding, you select the microbes that are best
at fermenting flour. For this reason, it is
recommended to discard the leftover unused starter
from the first days of the process. Later on, unneeded
starter amounts should never be thrown away. You can make
great discard bread out of it.

So just keep going and don't give up. The first big
rise is an indicator that you are doing everything
right. Based on my experience, it takes around 7
days to grow a starter. As you feed your starter
more and more, it will become even better at fermenting
flour. The first bread might not go exactly as you
planned, but you will get there eventually. Each
feeding makes your starter stronger and stronger.

### Liquid on top of my starter

Sometimes a liquid, in many cases black liquid, gathers on top
of your sourdough starter. The liquid might have a pungent
smell to it. Many people confuse this with mold. I have seen
bakers recommending to discard the starter because of this liquid.
The liquid is commonly known as *hooch*. After a while
of no activity the heavier flour separates from the water. The flour
will sit at the bottom of your jar and the liquid will stay on top.
The liquid turns darker because some particles of the flour weigh
less than the water and float on top. Furthermore dead microorganisms
float in this liquid. This liquid is not a bad thing; it's actively
protecting your sourdough starter from aerobic mold entering through
the top.


![](images/sourdough-starter-hooch)


Simply stir your sourdough starter to homogenize the hooch back into your
starter. The hooch will disappear. Then use a little bit of your sourdough
starter to set up the starter for your next bread.  Once hooch appears, your
starter has likely fermented for a long period of time. It might be very sour.
This state of starter is excellent to make discard crackers or a discard
bread. Don't throw anything away. Your hooch is a sign that you have a long
fermented dough in front of you. Compare it to a two year ripened Parmigiano
cheese.  The dough in front of you is full of delicious flavor.

### Fixing a moldy sourdough starter

First of all, making a moldy sourdough starter is very difficult.
It's an indicator that something might be completely off in your starter.
Normally the symbiosis of yeast and bacteria does not allow external
pathogens such as mold to enter your sourdough starter.
The low pH created by the bacteria is a very hostile environment
that no other pathogens like. Generally everything below a pH
of 4.2 can be considered food safe [food safe ph]. This
is the concept of pickled foods. And your sourdough bread
is essentially pickled bread.

I have seen this happening especially when the sourdough
starter is relatively young. Each flour naturally contains
mold spores. When beginning a sourdough starter, all
the microorganisms start to compete by metabolizing the
flour. Mold can sometimes win the race and outcompete
the natural wild yeast and bacteria. In that case simply
try cultivating your sourdough starter again. If mold reappears
again, it might be a very moldy batch of flour. Try a different
flour to begin your sourdough starter with.

Mature sourdough starters should not go moldy unless the conditions
of the starter change. I have seen mold appearing when the starter is stored
in the fridge and the surface dried out. It also sometimes forms on the
edges of your starter's container, typically in areas where no active
starter microorganisms can reach. Simply try to extract an
area of your starter that has no mold. Feed it again with flour and
water. After a few feedings, your starter should be back to normal.
Take only a tiny bit of starter: 1–2 are enough. They already
contain millions of microorganisms.

Mold favors aerobic conditions. This means that air is required in order
for the mold fungus to grow. Another technique that has worked for me
was to convert my sourdough starter into a liquid starter. This successfully
shifted my starter from acetic acid production to lactic acid production.
Acetic acid, similarly to mold, requires oxygen to be produced. After
submerging the flour with water, over time the lactic acid bacteria
outcompeted the acetic acid bacteria. This is a similar concept to pickled
foods. By doing this you are essentially killing all live mold fungi. You
might only have some spores left. With each feeding the spores will become
fewer and fewer. Furthermore, it seems that lactic acid bacteria produce
metabolites that inhibit mold growth [mold lactic acid bacteria].


![The
      interaction of lactic acid bacteria and mold fungi.
      In [mold lactic acid bacteria],
      mold+lactic+acid+bacteria et al.\ show how bacteria are
      producing metabolites that inhibit fungus growth.](images/fungi-lactic-acid-interactions)

*The
      interaction of lactic acid bacteria and mold fungi.
      In [mold lactic acid bacteria],
      mold+lactic+acid+bacteria et al.\ show how bacteria are
      producing metabolites that inhibit fungus growth.*


To pickle your starter, simply take a bit of your existing starter (5 g for
instance). Then feed the mixture with 20 g of flour and 100 g of water. You have
created a starter with a hydration of around 500%. Shake the mixture vigorously.
After a few hours you should start seeing most of the flour near the bottom
of your container. After a while most of the oxygen from the bottom mixture
is depleted and anaerobic lactic acid bacteria will start to thrive. Take a
note of the smell your sourdough starter. If it was previously acetic
it will now change to be a lot more dairy. Extract a bit of your mixture the
next day by shaking everything first. Take 5 g of the previous mixture, feed
again with another 20 g of flour and another 100 g of water. After 2–3
additional feedings your starter should have adapted. When switching back
to a hydration of 100% the mold should have been eliminated. Please note that
more tests should be conducted on this topic. It would be nice to really
carefully analyze the microorganisms before the pickling and after.

### My sourdough starter is too sour

If your sourdough starter is too sour it will cause problems during
the fermentation. Your fermentation will have more
bacterial activity than yeast activity. This means
you will likely create a more tangy loaf which isn't
as fluffy as it could be. The goal is to reach the right
balance: Fluffy consistency from the yeast and a great,
not-too-strong tang from the bacteria. This depends
of course on what you are looking for in terms of taste
in your bread. When making rye bread, I prefer to be more
on the tangy side for instance. When the described balance
is off, the first thing to check is your sourdough starter.

Note the smell of your starter. Does it smell very sour?
Taste a bit of your starter too. How sour does it taste?
Over time, every starter becomes more and more sour the longer
you wait. But sometimes your starter becomes sour too fast.
In this case apply daily feedings to your starter. Reduce
the amount of old starter that you use to feed. A ratio
of 1:5:5 or 1:10:10 can do wonders. In this case you would
take 1 part of starter (10 g) and feed it with 50 g of flour
and 50 g of water. This way the microorganisms start
the fermentation in a greenfield environment. This is
similar to the 10% starter or  20% starter
ratio that you use to make a dough. These days I almost
never use a 1:1:1 ratio. This only makes sense when you
are initially creating your starter. You want a sour
environment so that your microorganisms outcompete
potential pathogens. The acidic environment is toxic
to most pathogens that you do not want in your starter.

Another approach that can help is to convert your
sourdough starter into a stiff starter as
described in the relevant section.

### Why does my starter smell like vinegar or acetone?

Your sourdough starter has likely produced a lot of acetic acid.
Acetic acid is essential when creating vinegar. Once no additional
food is left some of your starter's bacteria will consume ethanol
and convert it into acetic acid. Acetic acid has a very pungent smell.
When tasting acetic acid, the flavor of your bread is often perceived
as quite strong.


*Oxygen is required to create acetic
      acid [acetic acid production].*


This is nothing bad. But if you would like to change
the flavor of your final bread, consider converting
your sourdough starter into a liquid starter. This will
help to prioritize lactic acid-producing bacteria.
Your flavor will change to dairy compared to vinegary.
You can't go back though. After the conversion your starter
will never go back to acetic acid production because you have
changed the tides towards primarily lactic acid fermentation.
I like to have a separate rye starter. In my experiments
rye starters tend to feature many acetic acid bacteria.
This starter is excellent when you want to make a very hearty,
strong-tasting bread. A pure rye bread tastes excellent when
made with such a starter. The flavor when taking a bite
is incredible. It nicely plays with soups as well. Just take
a bit of this bread and dip it in your soup.

### Why does my starter not float after using the float test?
The float test may not reliably determine your starter's readiness for dough
inoculation. While it's effective for wheat-based doughs, where ample gas gets
trapped in the gluten matrix, it's less reliable for non-wheat doughs. In non-
wheat doughs, the gas generated during fermentation tends to escape, causing
the starter to likely sink.

For more accurate assessments of your starter's readiness, watch for bubbles
at the container's edge and consider its aroma. A mature starter should emit a
mildly sour scent without being overly pungent.

## Dough
### Should I autolyse my dough?

In 95% of all cases, an autolysis
makes no sense. Instead I recommend
that you conduct a fermentolysis. You
can read more about the autolysis process in
the relevant section and
more about the topic of fermentolysis
in the relevant section.

The fermentolysis combines all the benefits
of the autolysis while eliminating disadvantages
such as having to knead the dough multiple times.

The autolysis only makes sense when you might
bake a fast-fermenting yeast-based dough with a
high yeast inoculation rate. But even in that
case you could just lower the amount of yeast
to fermentolyse rather than autolyse.

### My dough sample (aliquot) doesn't rise. What's wrong?

If you see that your dough rises in size but your aliquot doesn't, chances
are that both are fermenting at different speeds. This can often
happen when the temperature in your kitchen changes. The aliquot
is more susceptible to temperature changes than the main dough.
Because the sample is smaller in size, it will heat up or cool down
faster.

For this reason, you must use room-temperature water when
making your dough. By having the same temperature in both the sample
and your dough, you make sure that both ferment at the same rate.

If the temperature in your room changes significantly during the day, your
best option is to use a see-through container. Mark the container to properly
measure your dough's size increase.

Another option could be to use a more expensive pH meter to measure your
dough's acidity buildup. You can read more about different ways of managing
bulk fermentation in the relevant section.

### What's a good level of water (hydration) to make a dough?

Especially when starting to make bread, use lower amounts of water. This will
greatly simplify the whole process. I recommend using a level of around
60% hydration. So for every 100 g of flour use
around 60 g of water.  This ballpark figure will work for most
flours.  With this hydration, you can make bread, buns, pizzas, and even
baguettes out of the same dough.

With the lower hydration, dough handling becomes easier and you have more
yeast fermentation, resulting in lower over-fermentation risk.

### My dough completely tears after a long fermentation

Sometimes when touching your dough after a long fermentation
it completely tears apart. This could be for two reasons. It might
be that the bacteria completely consumed the gluten of your flour.
On the other hand, over time your gluten network automatically
degrades. This is the protease enzyme converting the gluten
network into smaller amino acids the seedling can use as
building blocks for its growth. This process starts to happen
the moment you mix flour and water. The longer your dough sits,
the more gluten is broken down. As the gluten holds the
wheat dough together, your dough will ultimately tear.


![My dough tearing after 24 hours of no activity.](images/tearing-dough)

*My dough tearing after 24 hours of no activity.*


In the picture  I experimented with
using a starter that has not been fed for 30 days at room temperature.
I tried to make a dough directly out of the unfed starter.
Typically after a long period
without feedings your microbes start to sporulate and go
into hibernation mode. This way they can survive for a long
period of time without extra feedings. Adding additional food
will activate them again. In this case the dough did not ferment
fast enough before the protease broke down the gluten. By activating
your microbes they will start to reproduce and increase in quantity
for as long as there is food available. But this process
in my case was not fast enough. After around 24 hours, the whole
dough just started to completely tear apart. The whole process was further
accelerated by my using whole-wheat flour. Whole-wheat
contains more enzymes than white flour.

To fix this, try to make sure that your sourdough starter is lively
and active. Simply apply a couple more feedings before
making your dough. This way your dough becomes ready to shape
before it has completely broken down.

## Bread
### My bread stays flat

A flat bread is in most cases related to your gluten
network breaking down fully. This is not bad; this
means you are eating a fully fermented food. However,
from a taste and consistency perspective, it might be
that your bread tastes too sour, or is not fluffy anymore.
Please also note that you can only make bread with
great oven spring when making wheat based doughs. When
starting with this hobby I always wondered why my rye
breads would turn out so flat. Yes, rye has gluten, but
small particles called *pentosans* (arabinoxylan and beta-glucan) [rye-defects].
They prevent the dough from developing a gluten network it can
with wheat. Your efforts will be in vain, and your dough will
stay flat. Only spelt- and wheat-based doughs have the capability
of retaining the CO₂ created by the fermentation.

In most cases something is probably off with your
sourdough starter. This very often happens when the starter
is still relatively young and isn't as capable of
fermenting flour. Over time your sourdough
starter is going to become better and better.
Keep your sourdough starter at room temperature
and then apply daily feedings with a 1:5:5 ratio.
This would be 1 part old starter, 5 parts flour,
5 parts water. This allows you to achieve a better
balance of yeast and bacteria in your sourdough.
Even better could be the use of a stiff sourdough
starter. The stiff sourdough starter boosts
the yeast part of your starter. This allows you
to have less bacterial fermentation, resulting
in a stronger gluten network toward the end
of the fermentation [stiff starter]. Please
also refer to the Subsection  where
I explained more about overfermented doughs. You can also
refer to the relevant section with more details on
making a stiff sourdough starter.

Furthermore, a stronger flour containing more gluten
will help you to push the fermentation further. This
is because your flour contains more gluten and will
take longer to be broken down by your bacteria. Ultimately,
if fermented for too long, your dough is also going
to be broken down and will become sticky and flat.

To debug whether the excess bacterial fermentation is the issue,
simply taste your dough. Does it taste very sour? If yes,
that's a good indicator. When working the dough, does it
suddenly become very sticky after a few hours? That's a
another good indicator. Please also use your nose to note
the smell of the dough. It shouldn't be too pungent.

### I want more tang in my bread

To achieve more tang in your sourdough bread, you have
to ferment your dough for a longer period of time.
Over time the bacteria will metabolize most of the
ethanol created by the yeast in your dough. The bacteria
mostly produce lactic and acetic acid. Lactic acid
is chemically more acidic than acetic acid but sometimes
not perceived as sour. In most cases a longer fermentation
is what you want. You will either need to utilize a loaf
pan to make your dough or use a flour that can withstand
a long fermentation period. A flour like this is typically
called a *strong flour*. Stronger flours tend
to be from wheat varieties that have be grown in more
sunny conditions. Because of that, stronger flours tend
to be more expensive. For freestanding loaves, I recommend
using a flour that contains at least 12% protein.
Generally, the more protein, the longer you can ferment your dough.

Another option to achieve a more sour flavor could be to
use a starter that produces more acetic acid. Based on my own
experience, most of my pure rye starters produced stronger acetic
notes. Chemically, the acetic acid isn't as sour, but when tasting
it will seem more sour. Make sure to use a starter that is at
a hydration of around 100%. Acetic acid production
requires oxygen. A starter that is too liquid tends to favor lactic
acid production because the flour is submerged in water. By submerging
the dough very little oxygen can pass through the water to the fermenting flour.
Because of this, only very little acetic acid can be produced. Over
time the acetic acid-producing bacteria will perish from your starter.


![A half-baked bread, known as *parbaked*.](images/parbaked-bread.jpg)

*A half-baked bread, known as *parbaked*.*


Another easier option could be to bake your sourdough
twice. I have observed this when shipping bread for my micro
bakery. The idea was to bake my bread for around 30 minutes
until it's sterilized, let it cool down and then ship it
to customers. Once you receive it, you just bake it again
for another 20–30 minutes to achieve the desired crust and
then you can eat it. Some of the customers reported a very sour
tasting bread. After investigating a bit more, it became
crystal clear. By baking the bread twice you don't boil off
as much acid during the baking process. Water
evaporates at around 100°C (212°F) while acetic
acid boils at 118°C (244°F) and lactic acid at
122°C (252°F). After baking for 30 minutes at
around  230°C (446°F) some of the water has
started to evaporate, but not all the acid yet. If you were to continue to
bake, more and more of the acid would start to evaporate. Now if you were to
stop baking after 30 minutes, you would typically have reached a core
temperature of around 95°C (203°F).  Your dough
would need
to be cooled down again to room temperature. The crust would
still be quite pale. Then a couple of hours later, you start
to bake your dough again. Your crust would become nice and
dark featuring delicious aroma. The aroma is coming from the
Maillard reaction. However, the core of your dough still won't
exceed the 118°C required to boil the acid. Overall, your
bread will be more sour. The enhanced acidity also helps
to prevent pathogens from entering your bread. The bread
will be good for a longer period of time. That's why
the concept of a delivery bakery works well with tangy sourdough bread.
In my own experiments, the bread stayed good for up to a week
in a plastic bag. This is much longer than a yeast-based dough that might
mold after just a few days[^1].

### My bread is too sour

Some people like the bread less sour as well. This
is personal preference. To achieve a less sour bread
you need to ferment for a shorter period of time.
The yeast produces CO₂ and ethanol. Both yeast and
bacteria consume the sugars released by the amylase enzyme
in your dough. When the sugar is depleted, bacteria starts to
consume the leftover ethanol by the yeast. Over time more
and more acidity is created, making a more sour loaf.

Another angle at this would be to change the yeast/bacteria
ratio of your sourdough. You can start the fermentation with
more yeast and less bacteria. This way, for the same given
volume increase of your dough, you will have less acidity.
A really good trick is to make sure that you feed your starter
once per day at room temperature. This way you shift
the tides of your starter towards a better yeast fermentation [more active starter].

To shift the tides even further, a real game changer
for me has been to create a stiff sourdough starter. The
stiff sourdough starter is at a hydration of around 50%.
By doing so your sourdough starter will favor yeast
activity a lot more. Your doughs will be more fluffy and less
sour for a given volume increase. I tested this
by putting balloons over different glass jars. I used
the same amount of flour for each of the samples.
I tested a regular starter, a liquid starter and a stiff
starter. The stiff starter by far created the most CO₂
compared to the other starters. As a consequence, the stiff
starter balloon was inflated the most [stiff starter]. You can read more
about the topic of stiff starters in the relevant section.

Another unconventional approach could be to add baking
powder to your dough. The baking powder neutralizes the
lactic acid and will make a much milder
dough [baking powder reduce-acidity].

### My bread flattens out when removing it from the banneton

After removing your dough from the banneton, your dough will always
flatten out a bit. That's because over time your gluten network
relaxes and can no longer hold the shape. However, during the course
of baking, your dough is going to increase in size and inflate again.

If your dough however flattens out completely, it's a sign that
you have fermented your dough for too long. Please refer to
Subsection
where I explain about overfermented doughs. Your bacteria
has consumed most of your gluten network. That's why your
dough fully collapses and stays flat during the bake. The
CO₂ and evaporating water will diffuse out of the dough.
A related symptom is that your dough sticks to the banneton.
When I starting baking I combated this with rice flour.
It worked for me but it might be a false find. Please refer to
Subsection  for more details on why
rice flour is not a good idea to manage sticky doughs.

These days I gently rub my
dough with a bit of non-rice flour before placing it in
the banneton. Now if the dough starts to stick to the banneton
while I remove it I resort to a drastic measure. I immediately
grease a loaf pan and directly place the dough inside. The loaf
pan provides a barrier and the dough can't flatten out as much.
The dough won't be as fluffy but it will be super delicious if you love tangy bread.

If you own a pH meter, take a note of your dough's pH before baking.
This will allow you to better judge your dough throughout
the fermentation process.

### My bread flattens out during shaping

Similarly to a dough flattening out after removing it from the banneton,
a flattened dough after shaping is also a possible sign of over-fermentation.

When you try to shape the dough, can you easily tear pieces from the dough?
If yes, you have definitely overfermented your dough. If not, it might just
be a sign that you have not created enough dough strength for your dough.
A ciabatta, for instance, is a dough that tends to flatten out a bit after shaping.

If your dough is not able to be shaped at all, use a greased loaf pan
to rescue your dough. You can also cut a piece of the dough and use it
as the starter for your next dough. Your sourdough dough is essentially
just a gigantic starter.

### My crust becomes chewy

Depending on which style of bread you are making a
thick crackly crust is sometimes desired. The crust
of your bread is created during the 2nd stage of the
baking process once the steaming source of your
oven has been removed. The dark colors are created by
the process known as *Maillard reaction* and then followed
by another process known as *caramelization*. Each
color of crust offers the taster a different aroma.

What happens quite often is that the crust becomes chewy after a day.
Sometimes when baking in the tropics with high humidity, the
crust only stays in this stage for a few hours. Afterwards
the crust becomes chewy. It's no longer as crisp compared
to the moment after baking. Your dough still contains moisture.
This moisture will start to homogenize in the final bread and
partially evaporate. The result is that your crust becomes chewy.

Similarly when storing your bread in a container or in a plastic
bag, your crust is going to become chewy. I have no fix for this yet.
I typically tend to store my breads in a plastic bag inside of my fridge.
This allows the moisture to stay inside of bread. When taking a slice
I always toast each slice. This way some of the crispness returns.
If you know of a great way, please reach out and I will update
this book with your findings.

troubleshooting/crumb-structures

## Misc
### Baking in the tropics

Depending on the temperature, your fermentation speed adapts.
In a warmer environment, everything is faster. In a colder
environment, everything is slower.

This includes the speed at which your sourdough ferments
the dough but also the speed of enzymatic reactions. The
amylase and protease enzymes work faster, making more
sugars available and degrading the gluten proteins.

At around 22°C (72°F) in my kitchen my bulk fermentation is ready
after around 10 hours. I use around 20% of sourdough
starter based on the flour. In summertime the temperatures
in my kitchen sometimes increase to
25°C (77°F). In that case
I reduce the sourdough starter to around 10%.

If I didn't do that, my fermentation would be done after
around 4–7 hours. The problem is that the dough is quite
unstable when fermenting at this high speed. This means
that you easily run into issues of over-fermentation.
Finding the perfect sweet spot between fermenting enough
and not too much becomes much harder. Normally you might
have a time window of 1 hour. But at the rapid speed it
might be reduced to a time window of 20 minutes. Now at
30°C (86°F), everything moves much faster. Your
bulk fermentation might be complete in 2–4 hours when using
10–20% starter. Proofing your dough in the fridge becomes
almost impossible. As your dough cools down in the fridge the fermentation
also slows down. However cooling the dough down from 30°C
to 4–6°C in your fridge takes much longer. Your
dough is much more active compared to a dough that starts at a temperature of
20–25°C. You might end up overproofing your dough if
you leave it overnight in the fridge.

That's why I recommend that you reduce the amount of starter
that you use in the tropics to around 1–5%
based on the flour. This will slow down the fermentation
process significantly and provides you a bigger window
of time. Try to aim for an overall bulk fermentation of at
least 8–10 hours. Reduce the amount of starter to get there.

When making dough, try to use the same water temperature
as your ambient temperature. Assuming that the temperature
will climb to 30°C try to start your dough
with 30°C water. This means that you can carefully rely on
a small fermentation sample (aliquot jar) that visualizes your fermentation
progress. To read more about this technique refer
to the relevant section.

The sample only works reliably if your dough temperature
is equal to your ambient temperature. Else the sample heats
up or cools down faster. So tread carefully when using
the sample in this case. It's always better to stop
the fermentation a little too early rather than too late.
Stretch and folds during the bulk fermentation
will help you to develop a better feel for
the dough. An expensive but possibly useful tool
could be a pH meter that allows you to perfectly
measure how much acidity has been created by the
lactic and acetic acid bacteria. In this case measure
the pH repeatedly and figure out a value that works
for your sourdough. In my case I tend to end bulk
fermentation at a pH of around 4.1. Please don't just
follow my pH value; it's very individual. Keep measuring
with different doughs to find out a value that works for you.

### My flour has low gluten content—what should I do?

You can always mix in a little bit of vital wheat gluten. Vital wheat gluten
is concentrated extracted gluten from wheat flour.

I recommend that you add around 5 g of wheat gluten for every
100 g of flour that you are using.

---

[^1]: Some of my first test customers however
reported that the bread was overly sour and not pleasant to eat at all.
When this happens to you, consider toasting the bread. Toasting
will boil off additional acidity.



---


## Debugging your crumb structure


The crumb structure of your bread provides insights into how well
your fermentation process has gone. You can also spot common flaws
arising from improper technique. This chapter will provide you with information
that you can use to debug your baking process.


*A schematic visualization of
      different crumb structures and their respective causes. The final bread's
      crumb is a key aspect to identify potential issues related to
      fermentation or baking technique.*


### Perfect fermentation


*The bread has a somewhat open crumb
      with areas featuring a honeycomb structure.*


Of course the perfect fermentation is debatable and highly subjective. To
me the perfect sourdough bread features a crisp crust paired with a fluffy,
somewhat open crumb. This is the perfect balance of different consistencies
when you take a bite.

Some people are chasers of a very open crumb, meaning you have large pockets
of air (alveoli). It's subjective whether that's the style of bread that you like;
however, to achieve it you need to ferment your bread dough perfectly.
It takes a lot of skill both in terms of mastering fermentation and technique
to achieve a crumb structure like that.

Personally, I like a bread like that, just with a slightly less wild crumb.
The style of crumb I like is called the *honeycomb crumb*. It's not too open, but
just enough open to make the bread very fluffy. To achieve the previously mentioned open crumb, you
have to touch your dough as little as possible. The more you interact with your
dough, the more you are degassing your dough. Excess touching of the dough
results in the dough's alveoli merging together. The crumb will not be as open.
That's why achieving such a crumb works best if you only ferment
one loaf at a time. Normally, if you have to pre-shape your dough,
you will automatically degas your dough a little bit during the rounding process.
If you skip this step and directly shape your dough, you will achieve a more open crumb.
A good rule of thumb is to not touch your dough for at least 1–2 hours before shaping,
to achieve as open a crumb as possible.


*A whole-wheat sourdough with an almost
      exclusive honeycomb crumb structure.*


Now this is problematic when you want to
make multiple loaves at the same time. Pre-shaping is essential as you are required
to divide your large bulk dough into smaller chunks. Without the pre-shaping
process, you would end up with many non-uniform bread doughs. This technique is
also used when making ciabattas. They are typically not shaped. You only cut the
bulk dough into smaller pieces, trying to work the dough as little as possible.
With pre-shaping you will converge your dough's alveoli into more of a honeycomb structure,
as large pockets of air will slightly merge. Similarly to the open crumb structure,
you also have to nail the fermentation process perfectly to achieve this crumb.
Too long a fermentation will result in gas leaking out of your dough while baking.
The honeycombs won't be able to retain the gas. If you ferment for too short a time,
there is not enough gas to inflate the structures. To me this is the perfect
style of crumb. As someone who appreciates jam, no jam will fall through a slice
of this bread compared to an open crumb.

### Overfermented


*A relatively flat dough that has
      many tiny pockets of air.*


When fermenting your dough for too long, the protease enzyme starts to
break down the gluten of your flour. Furthermore, the bacteria consume the gluten
in a process called *proteolysis* [raffaella di cagno].
Bakers also refer to this process as *gluten rot*.
The gluten that normally traps the CO₂ created
by the fermentation process of your microorganisms can no longer keep the
gas inside of the dough. The gas disperses outward resulting in smaller alveoli in your crumb.
The bread itself tends to be very flat in the oven. Bakers often refer
to this style of bread as a *pancake*. The oven spring can be compared
to bread doughs made out of low-gluten flour like einkorn.

Your bread will feature a lot of acidity, a really strong distinctive tang. From
a taste perspective, it might be a little bit too sour. From my own tests with family and
friends (n=15–20), I can say that this style of bread is typically
appreciated less. However, I personally really like the hearty strong taste.
It is excellent in combination with something
sweet or a soup.  From a consistency perspective, it is no longer as fluffy as it could be.
The crumb might also taste a little bit gummy. That's because it has been broken down a lot
by the bacteria. Furthermore, this style of bread has a significantly lower amount
of gluten [raffaella di cagno] and is no longer comparable to raw flour,
it's a fully fermented product.
You can compare it with a blue cheese that is almost lactose free.

When trying to work with the dough, you will notice that suddenly the dough feels
very sticky. You can no longer properly shape and work the dough. When trying to
remove the dough from a banneton, the dough flattens out a lot. Furthermore,
in many cases your dough might stick to the banneton. When beginning with baking
I would use a lot of rice flour in my banneton to dry out the surface of the dough a lot.
This way the dough wouldn't stick, despite being overfermented. However as it
turns out the stickiness issue has been my lack of understanding the fermentation
process. Now I never use rice flour, except when trying to apply decorative scorings.
Managing properly fermentation results in a dough that is not sticky.

If you are noticing, during a stretch and fold or during shaping, that your dough
is suddenly overly sticky, then the best option is to use a loaf pan. Simply take
your dough and toss it into a loaf pan. Wait until the dough mixture has increased
in size a bit again and then bake it. You will have a very good-tasting sourdough
bread. If it's a bit too sour, you can just bake your dough for a longer period
of time to boil away some of the acidity during the baking process. You can also use
your dough to set up a new starter and try again tomorrow. Lastly, if you are hungry,
you can simply pour some of your dough directly into a heated pan with a bit of
oil. It will make delicious sourdough flatbreads.

To fix issues related to over-fermentation, you need to stop the fermentation process
earlier. What I like to do is to extract a small fermentation sample from my dough.
Depending on the volume increase of this sample, I can mostly judge when my fermentation
is finished. Try to start with a 25% volume increase of your
main dough or sample.  Depending on how much gluten your flour has, you can
ferment for a longer period of time.  With a strong flour featuring a
14–15% protein, you should be able to safely ferment
until a 100% size increase. This however also depends on your
sourdough starter's composition of yeast and bacteria. The more bacterial fermentation,
the faster your dough structure breaks down. Frequent feedings of your sourdough
starter will improve the yeast activity. Furthermore, a stiff sourdough starter
might be a good solution too. The enhanced yeast activity will result in a more fluffy
dough with less bacterial activity. A better yeast activity also will result
in less acidity in your final bread. If you are a chaser of a very strong tangy
flavor profile, then a stronger flour with more gluten will help.

When retarding sourdough (cold-proofing in the refrigerator), temperature plays a
pivotal role in fermentation rates.  As the dough chills in the refrigerator,
fermentation decelerates. Starting the retarding process at a warmer
temperature means this deceleration takes longer.

For instance, a dough that's ideal after 8 hours of retarding might be ready in
merely 4 hours if it began at a higher temperature. Thus, it's crucial to
experiment and determine the optimal retarding duration for your specific
conditions. Conversely, if the dough starts colder, fermentation halts more
rapidly in the refrigerator. In such scenarios, allowing the dough to proof at
room temperature briefly before refrigerating can be beneficial.

### Underfermented


*A dense dough featuring a gummy, not fully
      gelatinized area.  The picture has been provided by the user
      *wahlfeld* from our community Discord server.*


This defect is also commonly referred to as *underproofed*. However underproofed
is not a good term as it only refers to having a short final
proofing stage of the bread-making process.
If you were to bake your bread after a perfectly-timed bulk fermentation stage,
the result will not be underproofed even if you skipped the proofing stage entirely.
Proofing will make your dough a bit more extensible and allows your sourdough
to inflate the dough a bit more. When faced with an underfermented bread, something
went wrong earlier during the bulk fermentation stage, or maybe even
before with your sourdough starter.

A typical underfermented dough has very large pockets of air and is partially
wet and gummy in some areas of the dough. The large pockets can be compared
to making a non-leavened wheat or corn tortilla. As you bake the dough in your pan,
the water slowly starts to evaporate. The gas is trapped in the structure of the dough
and will create pockets. In case of a tortilla, this is the desired behavior.
But when you observe this process in a larger dough, you will create several
super alveoli. The water evaporates, and the first alveoli form. Then at some point,
the starch starts to gelatinize and becomes solid. This happens first inside of the pockets
as the interior heats up faster compared to the rest of the dough. Once all the starch
has gelatinized, the alveoli holds their shape and no longer expand. During this
process other parts of the bread dough are pushed outwards. That's why an underfermented
dough sometimes even features an ear during the baking process. This
is also commonly referred to as a *fool's crumb*. You are excited about an ear which
can be quite hard to achieve. Plus you might think you finally created some big pockets
of air in your crumb. But in reality you fermented for too short a period
of time.


*A typical example of a fool's crumb
      featuring an ear and several overly large alveoli. The picture has been
      provided by Rochelle from our community Discord server.*


In a properly fermented dough, the alveoli help with the heat transfer throughout the dough.
From within the many tiny fermentation-induced pockets, the starch gelatinizes. With
an underfermented dough, this heat transfer does not properly work. Because of that
you sometimes have areas which look like raw dough. Bakers refer to this as a very
gummy structure sometimes. Baking your dough for a longer period of time would also properly
gelatinize the starch in these areas. However, then other parts of your bread
might be baked too long.

To fix issues related to under-fermentation, you simply have to ferment your dough
for a longer period of time. Now, there is an upper limit to fermentation time
as your flour starts to break down the moment it is in contact with water. That's why it
might be a good idea to simply speed up your fermentation process. As a rough
figure, I try to aim for a bulk fermentation time of around 8–12 hours typically.
To achieve that you can try to make your sourdough starter more active.  This can be done
by feeding your starter daily over several days. Use the same ratio as you would
do for your main bread dough. Assuming you use 20% starter
calculated on the flour, use a 1:5:5 ratio to feed your starter. That would be
10 g of existing starter, 50 g of flour, 50 g
of water for instance.  To boost your yeast activity even more, you can
consider making a stiff sourdough
starter. The bacteria produces mostly acid. The more acidity
is piled up, the less active your yeast is. The stiff sourdough starter
enables you to start your dough's fermentation with stronger yeast activity
and less bacterial activity.

### Not enough dough strength


*A very flat bread without enough dough strength.*


When a dough flattens out quite a lot during the baking process, the chances are
that you did not create enough dough strength. This means your gluten matrix
hasn't been developed properly. Your dough is too extensible and flattens out
mostly rather than springing upwards in the oven. This can also happen if you
proofed your dough for too long. Over time the gluten relaxes and your dough
becomes more and more extensible. You can observe the gluten relaxing behavior
too when making a pizza pie. Directly after shaping your dough balls, it's
very hard to shape the pizza pie. If you wait for 30–90 minutes stretching
the dough becomes a lot easier.

The easiest way to fix this is probably to knead your dough more at the start. To simplify
things consider using less water for your flour too. This will result in a more elastic dough
right away. This concept is commonly used for no-knead style sourdough.  Alternatively, you
can also perform more stretch and folds during the bulk fermentation process. Each
stretch and fold will help to strengthen the gluten matrix and make a more elastic dough.
The last option to fix a dough with too little dough strength is to shape your dough tighter.

### Baked too hot


*A bread with very large alveoli close to the crust.*


This is a common mistake that has happened to me a lot. When you bake your dough
at too high a temperature, you constrain your dough's expansion. The starch
gelatinizes and becomes more and more solid. At around
140°C (284°F) the Maillard reaction starts to
completely thicken your bread dough's crust. This is similar to baking your
bread dough without steam. As the internal dough's temperature heats up,
more and more water evaporates, gas expands and the dough is being pushed upwards.
Once the dough reaches the crust, it can no longer expand. The alveoli merge
into larger structures close to the surface of the dough. By baking too hot,
you are not achieving the ear which adds extra flavor. Furthermore, by restricting
it's expansion, the crumb will not be as fluffy as it could be.

If you have an extensible dough with high hydration, baking too cold will result
in the dough flattening out quite a lot. The gelatinization of the starch is
essential for the dough to hold its structure. After conducting several
experiments, it seems that my sweet spot for maximum oven spring seems to be
at around 230°C (446°F). Test the temperature
of your oven, because in several
cases the displayed temperature might not match the actual temperature of your
oven [too hot baking]. Make sure to turn off the fan of your oven. Most
home ovens are designed to vent the steam as fast as possible. If you can not
turn the fan off, consider using a Dutch oven.

### Baked with too little steam


![One of my earlier breads that
      I baked at a friend's place where I couldn't steam the dough properly.](images/no-steam)

*One of my earlier breads that
      I baked at a friend's place where I couldn't steam the dough properly.*


Similar to baking too hot, when baking without enough steam, your dough's crust
forms too quickly. It's hard to spot the difference between the two mistakes.
I typically first ask about the temperature and then about the steaming technique
to determine what might be wrong with the baking process. Too little steam can
typically be spotted by having a thick crust all around your dough paired
with large alveoli towards the edges.

The steam essentially prevents the Maillard reaction from happening too quickly
on your crust. That's why steaming during the first stages of the bake is so important.
The steam keeps the temperature of your crust close to around
100°C (212°F). Achieving steam
can be done by using a Dutch oven, an inverted tray and/or a bowl of boiling water.
You might also have an oven with a built-in steam functionality. All the methods work,
it depends on what you have at hand. My default go-to method is an inverted
tray on top of my dough, paired with a bowl full of boiling water towards the bottom
of the oven.


![An apple with 2 probes
      to measure ambient and surface temperatures of several steaming
      techniques in a Dutch oven.](images/apple-experiment-temperatures)

*An apple with 2 probes
      to measure ambient and surface temperatures of several steaming
      techniques in a Dutch oven.*


Now there can also be too much steam. For this I tested using a Dutch oven paired with large ice
cubes to provide additional steam. The temperature of my dough's surface would directly
jump close to 100°C. The steam contains more energy and thus through convection
can heat up the surface of your dough faster. I tested this by putting an apple inside
a Dutch oven and measuring its surface temperature using a barbecue thermometer.
I then changed the steaming methods to plot how quickly the temperature
close to the surface changes. I tested an ice cube inside of a preheated
Dutch oven, a plain preheated Dutch oven, a preheated Dutch oven with spritzes
of water on the apple's surface and a non-preheated Dutch oven where I would only preheat
the bottom part. The experiment then showed that the ice-cube method would heat up
the surface of the apple a lot quicker. When replicating this with a bread dough,
I would achieve less oven spring.


*A chart showing how
      the temperature of the apple's surface changes with different
      steaming techniques.*


*This figure shows
      how the ambient temperatures inside of the Dutch oven change depending
      on the steaming technique that is used.*


Generally though, achieving too much steam is relatively challenging. I could only
make this mistake when using a Dutch oven as the steaming method paired with relatively
large ice cubes. After talking with other bakers using the same Dutch oven, it seems
that my ice cubes (around 80 g) were 4 times as heavy as the ones
other bakers would use (20 g).



---


# Glossary


> This glossary provides definitions and explanations for terms frequently
> used in bread making. Understanding these terms is essential for both
> novice and experienced bakers aiming to master the art and science of
> bread making. The glossary is arranged alphabetically for easy reference.

**Acetic Acid**
: A type of organic acid produced by hetero fermentative lactic
acid bacteria and acetic acid bacteria during fermentation. It gives sourdough bread
its characteristic tangy flavor and helps to preserve the bread by lowering its pH.
The flavor of acetic acid has a more vinegary profile.

**Aliquot jar**
: A small piece of dough extracted after creating initial
dough strength.  The aliquot jar is used to monitor the dough's fermentation progress.
It's important to ensure the dough's water temperature in the aliquot matches
your room temperature for accurate readings. Be mindful that the aliquot
jar may not be as effective if there are significant temperature
fluctuations in your kitchen. This is because the small dough sample in
the aliquot can heat up or cool down faster than the main dough mass,
potentially impairing its ability to accurately monitor fermentation.
It's crucial to use a cylindrical-shaped aliquot container to properly judge
the dough's size increase.

**All Purpose Flour**
: A general flour that’s balanced to make breads and also
cakes. In Germany this is type 550.

**Alpha-amylase**
: A type of amylase that breaks down starch molecules into
shorter fragments, producing maltose and some glucose.

**Alveograph**
: A device used primarily in the evaluation of wheat flour's
baking quality. The alveograph assesses the dough's rheological properties,
particularly its extensibility and resistance to extension, by inflating a piece
of dough like a balloon until it bursts. The resulting chart, or *alveogram*,
displays a curve that represents the balance between the dough's elasticity and
extensibility. Specific parameters derived from the curve, such as the P (pressure
required to inflate the dough) and L (extensibility of the dough), provide invaluable
insights to bakers and millers regarding the flour's potential performance in
bread-making. By analyzing the alveogram, professionals can make informed decisions
about the suitability of a flour for certain baking applications, as well as
potential blending needs with other flours.

**Alveoli**
: (singular Alveolus) The little pockets that form the crumb,
formed by the gluten matrix trapping carbon dioxide.

**Amylase**
: An enzyme that breaks down starches into simpler sugars, facilitating
the fermentation process in beer and bread making. When making beer the temperature
of the brew is kept for extended periods at certain temperatures to ensure that most
starches are broken down to sugars. These sugars are then consumed by the microbes
during the fermentation process.

**Autolyse**
: A process where flour and water are mixed and then left to rest
before adding other ingredients. This activates enzymes such as amylase and protease.
By doing so the bulk fermentation time is shortened and the final loaf will have
better properties. The browning of the loaf becomes better and the crumb fluffier.
An autolyse is recommended when using a high percentage of starter to inoculate the
dough (> 20%). An alternative easier approach can be the fermentolyse.

**Bacteria**
: Unicellular microorganisms that exist in diverse forms and
habitats. They play crucial roles in various natural processes, especially in food
preparation like sourdough fermentation. Lactic and acetic acid bacteria, in particular,
are pivotal in the sourdough process, contributing to its distinct taste and texture.
Some bacteria are beneficial, aiding in digestion or producing vitamins, while others
can be harmful and cause diseases.

**Baker’s Math**
: Baker’s math is a ratio based system of sharing recipes,
making them easily scalable. It’s based on the total weight of the flour in a formula,
where each ingredients weight is divided by the flours weight to give a percentage.
For 500 g of flour you could be using 60% of water (300 g),
10% of starter (50 g) and 2% of salt (10 g).

**Baker’s percentage**
: See Baker’s math.

**Baking**
: The final, transformative step in bread making wherein dough is
exposed to high temperatures, causing a series of chemical and physical reactions
that result in a finished loaf of bread. During the baking stage:

1. *Yeast Activity & Oven Spring:* In the initial phase of baking, the temperature inside the dough rises, increasing yeast activity. This results in rapid carbon dioxide production, leading to what bakers refer to as *oven spring*, or the rapid rise of the loaf.
2. *Protein Coagulation:* As the temperature continues to climb, the proteins in the dough, primarily gluten, begin to coagulate or set, which gives the bread its structure.
3. *Starch Gelatinization:* Starches absorb water and swell, eventually gelatinizing. This process contributes to the crumb structure of the bread.
4. *Caramelization & Maillard Reaction:* The crust of the bread browns due to two primary reactions: caramelization of sugars and the Maillard reaction between amino acids and reducing sugars. This not only affects the appearance but also imparts a distinctive flavor and aroma to the bread.
5. *Evaporation of Acids:* Some acids produced during fermentation evaporate at certain temperatures during baking. This evaporation can influence the final flavor profile of the bread, making it less tangy than the unbaked dough. By extending the baking time the acids become less concentrated and the dough can lose some of its tang.
6. *Moisture Evaporation:* Water in the dough turns to steam and begins to evaporate. The steam contributes to the oven spring and also helps in gelatinizing the starches.
7. *Crust Formation:* The outer layer of the dough dries out and hardens to form a crust, which acts as a protective barrier, keeping the inner crumb moist.

**Banneton**
: A wicker basket used to shape and support dough during its final
proof. The bannetons are typically made out of rattan or wood pulp. An alternative
DIY solution is to use a bowl with a kitchen towel inside. While resting inside of
the banneton the dough’s surface dries out and becomes easier to score before baking.

**Bassinage method**
: A bread making technique involving the staged addition of water
to the dough. Initially, the dough is mixed to a lower hydration level,
allowing gluten bonds to form more effectively. Once these gluten structures
are established, additional water is gradually incorporated through further
kneading. This method enhances the dough's extensibility, especially beneficial
when working with lower-gluten flours. By employing the bassinage method,
bakers can achieve a dough that is both strong and extensible.

**Bench Rest**
: A short resting period given to the dough after preshaping
allowing the gluten to relax a little bit and making shaping easier. Most people
bench rest for 10 minutes up to an hour. The bench rest becomes especially important
when making pizza doughs. Without an extended bench rest the dough is too elastic and
can not be shaped.

**Beta-amylase**
: An enzyme that further breaks down the starch fragments
produced by alpha-amylase into maltose.

**Bread Flour**
: A flour that is perfect for sourdough bread making. It features
a higher amount of gluten and can thus ferment for a longer period of time.

**Brühstück**
: A German baking technique similar to a scald. It translates as
*boil piece*. Hot or boiling water is poured over whole grain flour or crushed grains,
then cooled and mixed with the main dough. This process helps in moisture retention
and can enhance the flavor and texture of the final bread. Also see *scald*.

**Bulk Fermentation**
: The initial rising period after mixing all the
    ingredients.  The dough is typically allowed to rise until it increases to
    a certain volume. The volume of increase depends on the flour that is
    used. When baking with wheat flour the gluten amount of the flour is the
    deciding factor. The more gluten your flour has (protein) the longer you
    can bulk ferment. A longer bulk fermentation improves the flavor and
    texture of the final bread. It becomes tangier and fluffier. You can aim
    for a 25% size increase of your dough and then slowly
    increase this to find your flour's sweet spot. This is highly dependent
    from flour to flour. When using low gluten flour like rye you need to be
    careful as the longer fermentation can create a too sticky dough which
    collapses and does not hold its shape anymore.

**Cake Flour**
: Cake flour is a light, finely milled flour with a lower
    protein content than all-purpose flour. It's ideal for tender baked goods
    like cakes, cookies, and pastries.

**Coil fold**
: A special stretch and folding technique. The coil fold is
very gentle on the dough and is thus excellent throughout the bulk fermentation.
By applying the coil fold the dough strength is improved by minimizing damage
to the dough structure.

**Crumb**
: The inner texture of the bread, which is characterized by the size,
shape, and distribution of the holes (or *alveoli*). It's what's inside once you slice
a loaf of bread open. A *tight crumb* refers to bread with small, evenly distributed
holes, while an *open crumb* has larger, more irregular holes.

**Diastatic Malt**
: Malted grain that has been dried and then ground into a powder.
This malt contains enzymes that can break down starches into sugars, which can be
beneficial in the fermentation process for bread. When added to dough, it can improve
the bread's flavor, color, and shelf life.

**Discard**
: The portion of sourdough starter that is removed and not fed when
maintaining the starter. This is often done to prevent the starter from becoming too
large and unmanageable. Discard can be used in various recipes or thrown away.

**Dividing**
: The process of breaking the dough mass into smaller pieces,
typically to shape into individual loaves or portions.

**Dough Hydration**
: Expressed as a percentage, it's the amount of water in a
dough relative to the amount of flour. A higher hydration dough will be wetter and
stickier, while a lower hydration dough will be firmer. For example, a dough
with 500 g of flour and 375 g of water has a hydration of
75%

**Dough Strength**
: Refers to the dough's resilience, elasticity, and structure.
A strong dough can be stretched without tearing and holds its shape well. This is
largely influenced by the flour's protein content and the development of the gluten
network.

**Dutch Oven**
: A heavy-duty pot with a tight-fitting lid, often made of cast
iron. It's used in baking to trap steam during the initial phase of baking, helping
to create a crusty exterior on bread.

**Elasticity**
: A property of dough that describes its ability to return to
its original shape after being stretched or deformed. It's influenced by the flour's
protein content and the development of the gluten network.

**Extensibility**
: Refers to the dough’s ability to be stretched or extended
without tearing. It's the opposite of elasticity and is desirable in certain types
of breads, like ciabatta, that have a more open crumb structure.

**Feed**
: The act of adding fresh flour and water to maintain a sourdough
starter. Regular feeding keeps the starter active and healthy.

**Fermentation**
: The metabolic process by which microorganisms such as yeast
and bacteria convert carbohydrates (like sugars) into alcohol or acids. In bread
making, this produces carbon dioxide which causes the dough to rise.

**Fermentolyse**
: Using a small amount of starter to slow fermentation.
It's a method where fermentation and autolyse are combined. Typically around 10%
of starter is used for the fermentolyse. The flour, water and starter are mixed
together. By adding the starter early the dough becomes more extensible and easier
to handle.

**Finger poke test**
: The finger poke test is a simple yet effective way to
check if your sourdough bread is ready to bake. After the final rise, lightly
flour your finger and gently press about half an inch into the dough.
If the dough springs back slowly and leaves a slight indentation, it's perfect
and ready for the oven. If it springs back quickly, it needs more time to rise.
However, if the dough collapses or doesn't spring back at all, it may be
over fermented.

**Float test**
: The float test is a technique for assessing the readiness
of a sourdough starter. To perform this test, take a small sample of
your starter and gently place it in a glass of water. The outcome
of this test can provide insights into your starter's fermentation stage.

- **** : *Positive result:* If your starter effortlessly floats on the surface of the water, it's a clear indication that it has reached its peak of fermentation and is ready to be used as a leavening agent in your dough. This buoyancy is a result of the carbon dioxide gas produced during the active fermentation process. **** : *Negative result:* Conversely, if your starter sinks to the bottom of the glass, it suggests that it's not quite ready yet. This indicates that the fermentation process has not progressed sufficiently for optimal leavening power.

It's worth noting that while the float test is a reliable indicator
for wheat-based sourdough starters, it may not be as effective for non-wheat
starters. This is because the gas generated during fermentation in non-wheat
starters tends to escape more readily, making it less buoyant. For non-wheat
starters, a more accurate approach involves observing the presence of
bubbles in your starter jar and assessing its aroma. A mature starter should
emit a mildly sour, but not overly pungent, scent.

**Fool’s Crumb**
: A term used to describe a crumb structure that has several
large pockets or holes, rather than an even distribution of smaller holes. This
isn't necessarily a desired feature, as it can indicate uneven fermentation or
improper shaping techniques.

**Gluten**
: A protein complex formed from gliadin and glutenin, found in wheat
and some other grains. It provides elasticity and strength to the dough when
properly aligned and developed. During the course of the bulk fermentation much of
the gluten is degraded by the protease enzyme and lactic acid bacteria.

**Homogenizing**
: The act of creating a consistent and uniform mixture. For
flours like einkorn and rye, where gluten alignment isn't the main goal, kneading
ensures that the dough achieves this homogeneous consistency.

**Hooch**
: A liquid layer that sometimes forms on top of a sourdough starter.
It's an indication that the starter is hungry and needs feeding. It acts as a
barrier shield and prevents the starter from catching mold. It can be mixed right
back into the starter or extracted to make hot sauces.

**Kneading**
: The manual or mechanical process of working dough to develop gluten
in wheat and spelt-based breads, or to homogenize the dough mass in flours like
einkorn or rye.

**Kochstück**
: When making a Kochstück, the flour or grains are heated
together with the fluid. The mixture needs to be stirred while heating up
to prevent clumping and burning it.

**Lactic Acid**
: Another organic acid produced by lactic acid bacteria during
fermentation. It imparts a mild tangy yogurty flavor to sourdough bread and, along
with acetic acid, contributes to the bread's overall acidity.

**Levain**
: See Sourdough starter.

**Maillard Reaction**
: The Maillard reaction is one of the causes of food browning
during cooking. The reaction occurs between reducing sugars and amino acids, and
depending on the initial reactants and cooking conditions can produce a wide variety
of end products with different tastes and aromas. Maillard reactions occur readily
above 150, although will still occur much more slowly below that
temperature. Optimal reaction rate occurs between pH 6.0 to pH 8.0,
although it favors alkaline conditions.

**Maltose**
: A sugar produced from the enzymatic breakdown of starch by amylases.
It's a primary food source for yeast during fermentation.

**Non-diastatic Malt**
: Malted grain that has been dried at higher temperatures,
deactivating its enzymes. It's used primarily for flavor and color in bread making.
Amylase and protease become degraded at temperatures higher than 50°C.

**Oven Spring**
: The rapid rise of the dough in the oven during the early stages
of baking due to the expansion of trapped gases and water.

**Over Fermenting**
: A common problem when making wheat or spelt doughs. When the
dough is fermented for too long most of the gluten in the dough is broken down. The
resulting dough is very sticky. The final bread will be very flat and lose some of its
typical texture. The crumb structure features many tiny pockets of air. A lot of the
trapped gasses can diffuse out of the dough during baking. If you notice this during
bulk fermentation it is advised to place the loaf inside of a loaf pan and then bake
it after a 30 to 60 minute rest.

**Over Proofing**
: The same as over fermenting, however happening during the
proofing stage.

**pH**
: A measure of the acidity or alkalinity of a solution. The pH scale
ranges from 0 to 14, where a pH value of 7 is neutral. Solutions with a pH value below
7 are acidic, while those with a pH above 7 are alkaline or basic. Fermented
foods with a pH below 4.2 are generally considered foodsafe. A pH meter can be
used to monitor your sourdough bread's fermentation progress.

**P/L Value**
: A critical parameter derived from the alveograph test, the P/L
value represents the ratio of the dough's tenacity (P) to its extensibility (L).
Specifically:

- **** : *P (Pressure)* refers to the pressure required to inflate the dough during the alveograph test. It indicates the dough's resistance to deformation or its strength. **** : *L (Length)* represents the extensibility of the dough, or how far it can be stretched before tearing.
The P/L ratio provides insights into the balance between the dough's elasticity and
extensibility:
- **** : *Low P/L Value* indicates a dough that is more extensible than resistant. This means the dough can be stretched easily, making it suitable for certain products like pizza or ciabatta. **** : *High P/L Value* suggests a dough that has more strength than extensibility. Such a dough is more resistant to deformation, which can be preferable for products that require good volume and structure, like certain types of bread.
The P/L value helps bakers and millers determine the suitability of a flour for
specific baking applications. Adjustments in flour blends or baking processes might
be made based on this ratio to achieve desired bread characteristics.

**Preferment**
: A mixture of a proportion of the doughs ingredients which is
allowed to ferment before being added to the final bread dough. These can include
sourdough, poolish, biga, pâte fermentée, or a general sponge.

**Preshaping**
: When dividing your large dough mass into smaller portions you end
up having non-uniform pieces of dough. This makes shaping much harder because the
resulting shaped dough will not be uniform. For this reason bakers drag the tiny dough
pieces over the surface of the counter to create more uniform looking dough balls.

**Proof**
: The final rise of the shaped dough before baking.

**Protease**
: An enzyme that breaks down proteins, including gluten, into smaller
peptide chains and amino acids. In the context of bread making, protease activity can
both benefit and challenge bakers. Moderate protease activity can make dough more
extensible, which can be helpful in some bread-making processes. However, excessive
protease activity can weaken the gluten network, leading to doughs that are slack,
sticky, and challenging to handle, and may result in breads with poor volume and
structure. Factors such as fermentation time, dough temperature, and the source of the
flour can influence protease activity in bread doughs. In sourdoughs, longer
fermentation times, particularly at warmer temperatures, can lead to higher protease
activity, as the acidic conditions activate cereal proteases. Flour from sprouted
grains or malted grains can have higher protease activity due to the sprouting or
malting process. Understanding and controlling protease activity is crucial in
achieving desired bread quality and handling characteristics.

**Pullman Loaf**
: A type of bread loaf characterized by its perfectly
    rectangular shape and soft, fine crumb. It is baked in a special lidded
    pan called a Pullman pan or *pain de mie* pan. The lid ensures that
    the bread rises in a perfectly straight shape, without the domed top
    characteristic of other bread loaves. Pullman loaves are often sliced very
    thin and are popular for making sandwiches.

**Retarding**
: The process of slowing down fermentation during the proofing
stage by placing the dough in a colder environment, typically a refrigerator. This aids
bakers in scheduling, allowing them to have more control over when to bake their breads,
especially in large-scale bakeries where timing is essential to serve freshly baked bread
to early morning customers. While scheduling is the main reason, some bakers also assert
that retarding can enhance the bread's overall flavor profile. Also known as
fridge-proofing.

**Rye**
: A type of grain used in baking. Due to its low gluten content, breads
made solely from rye flour tend to be dense. However, rye has a unique flavor and
many health benefits, so it's often combined with wheat flour in baking. Pure rye
breads are typically made with a sourdough process to help the dough rise.

**Scald**
: A method where boiling water is poured over flour, grains, or other
ingredients and then allowed to cool. In baking, this process can gelatinize the
starches in the flour or grains, resulting in a dough that retains moisture better,
provides a softer crumb, and potentially extends the bread's shelf life. Additionally,
scalding can help inactivate certain enzymes which can be detrimental to the dough's
quality. The scalding technique can also enhance the overall flavor and aroma of
the bread, bringing out more pronounced grainy notes and reducing bitterness
sometimes found in certain whole grains.

**Scoring**
: Cutting the surface of the bread dough before it's baked. This
allows the dough to expand freely in the oven, preventing it from bursting in
unpredictable ways. It also provides a controlled aesthetic to the finished loaf.

**Sift**
: To pass flour or another dry ingredient through a sieve to
    remove lumps and aerate it.

**Soaker**
: A mixture of grains or seeds with water that is left to soak overnight (or for a
specified amount of time) before being incorporated into bread dough. This helps to
soften and hydrate the grains or seeds (sesame, pumpkin, ), making them
easier to integrate into the dough and
providing a moister crumb in the finished bread.

**Sponge**
: A type of preferment, a sponge is a wet mixture of flour, water, and
yeast that is allowed to ferment for a certain period before being incorporated into
the final dough.

**Starter**
: A fermented mixture of flour and water containing a colony of
microorganisms including wild yeast and lactic acid bacteria. It's used to leaven
bread.

**Straight Dough**
: A bread-making method where all ingredients are mixed
together at once, without the use of a preferment.

**Stretch and Fold**
: S&F is a technique used during the bulk fermentation phase
to strengthen the dough and help align the gluten structure. Instead of traditional
kneading, the dough is gently stretched and then folded over itself. This process is
typically repeated multiple times throughout bulk fermentation.

**Tangzhong**
: A Chinese technique for bread-making, similar to the
Japanese yudane method. It involves cooking a small portion of the flour
with water (or milk) to create a slurry or roux. This process, which can be seen as a
variant of scald, gelatinizes the starches in the flour, resulting in breads
that are softer, fluffier, and have improved moisture retention. Once cooled, the
Tangzhong is mixed with the remaining ingredients to produce the final dough.

**Tight Crumb**
: Refers to a bread crumb (the soft inner part of the bread) that
has small, uniform air holes.

**Wild Yeast**
: Naturally occurring yeast, present in the environment and on the
surface of grains, used in sourdough fermentation as opposed to commercial yeast.
There’s wild yeast on almost any surface of plants. The wild yeasts live in symbiosis
with the plant providing a shield against pathogens and receiving sugars from the
photosynthesis of the plant in return. When the plant becomes weak the wild yeasts
can become parasitic and consume the host.

**W-Value**
: A parameter representing the strength of flour in terms of its
baking quality. The W-value, derived from the Chopin Alveograph test,
measures the energy required to blow a bubble with the dough until it bursts.
It is a direct indicator of the flour's ability to withstand the fermentation
and baking processes. A higher W-value typically indicates a stronger
flour, suitable for breads with high volume and longer fermentation times.
Conversely, a lower W-value suggests a weaker flour, better suited for
products requiring less structure, like cakes and pastries.

**Yeast**
: Microorganisms that ferment the sugars present in the dough, producing
carbon alcohol, carbon dioxide and heat; thereby causing the dough to rise.

**Yudane**
: A Japanese method of bread-making which involves the preparation
of a starter by mixing boiling water with bread flour in a specific ratio, typically 1:1
by weight. After mixing, the paste is left to cool to room temperature and then
refrigerated overnight. The next day, it is combined with the remaining ingredients
to make the dough. The Yudane method, essentially a type of scald, helps in
improving the texture of the bread, making it softer and fluffier while also enhancing
its shelf life.



---

