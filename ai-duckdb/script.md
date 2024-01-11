# Script for my video

## Slide 1

Hello, My name is michael and I am a machine learning engineer
and AI practitioner. Today I am going to talk about DuckDB and
how it can be used for AI and why you should care.

## Slide 2

If you are following the news, you might have heard about the
the lawsuit against OpenAI from NewYork Times. The Times 
sues OpenAI and Microsoft Over AI Use of their copyrighted work. 

## Slide 3

Many organizations are now thinking that they should go to 
the court with OpenAI. 

## Slide 4

Of course, OpenAI claims NY Times copyright lawsuit is
without merit.


## Slide 5

With all the money they have, OpenAI probably can afford
to hire the best lawyers in the world. So, in the end,
they either win or settle the case by paying some money.

## Slide 6

The lawsuit is all about the data. To train the AI model,
OpenAI used the data from NY Times. A GPT-3 model was
trained with around 45 TB of text data from all over the
internet.


## Slide 7

To prevent OpenAI from using their data, many organizations
have added a new line into their 'robots.txt' file, which 
disallows OpenAI from crawling their website.


## Slide 8

What does 45 TB of text data mean? 


## Slide 9

If you look at the following image, you can see that 
45 TB of text data is a lot. 1PB is 1024 TB, which is
around 1 million GB.


## Slide 10

Let's image 1 byte is 1 cubic millimeter. Then the following
image shows the comparison between 100kb and 1Tb. I hope this gives 
you a better idea of how big 45 TB is.

## Slide 11

To train the GPT-3 model, OpenAI has to use a large
cuslter of GPUs. The following videos explains how
they did it. Here is the video that explains how
they did it.

## Slide 12

After OpenAI released the GPT-3 model, many people asked why other big firms like Google
did not release their similar products.

## Slide 13

The answer is simple. It is not easy to train a GPT-3 model. Havig data is not part of the
problem. I think there are many tricks that OpenAI used to train the GPT-3 model. Of course,
it must be a hard engineering work.

I have been testing other chatbots from Google and meta, they are not as good as OpenAI's.

## Slide 14

Ever since ChatGPT was released, many things have changed. Many people are trying to build
their own GPT-3 model.

## Slide 15

But, it is not easy to train a GPT-3 model. What do I mean by that? Let's say I want to build a
mini ChatGPT model. Intead of using 45TB of data, I will use 45GB of data and I will use only
goodreads.com data as I don't want to get sued by NY Times.


## Slide 16

If the square box is OpenAI, then that 
small dot would be me who is using 45GB of data to train a GPT-3 model instead of 45TB.

## Slide 17

Here is my hardware, which is a 32 core CPU and 32GB of RAM and 2 GPUs.

## Slide 18

To build a mini ChatGPT model, I need to first collect the data. Here, I choose to collect
text from goodreads.com.

## Slide 19

After collecting the data, we need to clean 
and process the data. This is a very important step. If you don't do it right, you will
get a bad model.

## Slide 20

Then, we will train the mode, deploy the model and maintain the model.

## Slide 21

Now, I have done the collection


## Slide 22

As it is shown in this animation, where I 
got all those book information from goodreads.com.

## Slide 23

In the end, I got around 2.36 million books
with 29 columns, such as author, title, rating, etc. The size of the data is around 1.9GB compressed and around 8GB uncompressed.

## Slide 24

I also collected 15.7 million reviews from goodreads.com, which is around 7GB compressed and 30GB uncompressed. As you can see, each book could have many reviews.

## Slide 25

Okay, now we have the data, let's just read in the data with pandas and see how it goes.

It turned out that my computer crashed when I am using pandas to read in the data as pandas is not designed to handle large data.

## Slide 26

See, this just one chanllenge when you are trying to build a GPT-3 model.

## Slide 27

After doing some research, I found some firms could provide cloud service for big data processing and model training, such as this one. 

## Slide 28

But it still costs me around 500 dollars, so not for me. 

## Slide 29

Then, I found DuckDB, which is a free and open source database. It is designed to handle big data.

## Slide 30

I am very happy to find DuckDB. It is very easy to use. I just need to install it and then I can use it right away.

## Slide 31

Let's see how duckdb could handle the data. For 1.94gb compressed and 8gb uncompressed data, it only takes 6 seconds to read in the data with my limited hardware.

## Slide 32

Let me say that again, it only takes 6 seconds for around 8GB data. 

## Slide 33

And if you profile the memoery usage, actually it only takes around 1.5GB of memory to read in the data.

## Slide 34

That is called true kongfu.

## Slide 35

Duckdb Can process upto 300GB of data on a single machine.

## Slide 36

Now, with my hardware, finally I can build my mini ChatGPT model. 

## Slide 37

But before I do that, I checked the data 
and had a look at the top 10 books with the most reviews.

## Slide 38

One book got my attention, which is called "Fifty Shades of Grey". It has more than 100 thousand reviews.

## Slide 39

So, maybe I should read this book first before I build my mini ChatGPT model.

## Slide 40

Okay, enough talking about fifty shades of grey. Let's get back to the topic.

why should you care about DuckDB? You should care about DuckDB because it will save you a lot of time and money.

## Slide 41

We all know only big firms have big data. Even at google, 90% of all analytics queries are less than 1TB.

## Slide 42

If we check this image again, and you should realize that most of firms sit in the small cube, which is aound 1TB. That small dot is still me :)

So, if you date is not that big, you probably
do not need cloud service. You can just use DuckDB to handle your data.

## Slide 43

In 2022, Davbid Hansson the founder of Ruby on Rails, wrote an artical called 'why we are leaving the cloud'. In that artical, he said that they are leaving the cloud because they can save a lot of money.

## Slide 44

How much money can you save? Roughly speaking, you can save 7 million dollars over five years if you are midsize company.

## Slide 45

So, with the modern datastack, having duckdb doing in-process analytics and postgresql doing the rest, you can do lots of things with spending less money without or with less cloud service.

## Slide 46

THis is why you should care about DuckDB and how I love duckdb now. 

## Slide 47

Here is the list of resources that I used in this video. So, hapy coding and zoom in to see 
what I am searching on google.

See you next time and please subscribe to my channel or give me a like if you like this video.