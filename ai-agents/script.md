
# Script for ai-agents video

## Introduction

Hello everyone, welcome to my channel. This is michael a michine learning engineer
from HyperGI. Today I want to show you how to leverage free agents
for your work, so you can use ChatGPT more efficiently.


## slide 2 

I have been developing agents and testing the capacity of ChatGPT for a while
ever since it has been released. I have been using it for my work and I found it very handy, especially when multiple agents are working together.

Now, I am going to show you how to use it for your work. BTW, many people have
talked about this on the youtube, but I think I have a different perspective and
I want to share with you.

Some parts are tricky but I think everyone can learn it.


## slide 3

This is the showcases for multiple agents I have experimented with. It is 
from the OpenAI's playground console. You can see  that there are several 
agents there with different ids  and indstructions. 


## slide 4

Before we start, I want to show you how to set up the environment.


## slide 5

Here is the roadmap for this video. First, we will try to understand
how GPTs were trained by doing a simple experiend with Dall-E. Then we will
try to build a strategic planning agent. After that, we will build a 
data extraction specialist with ChattGPT. Here you will learn what
ChatGTPTs are really good at. You will also learn a
secret weapon to make ChatGts be more powerful. It is called function
calling (the feature I love the most from OpenAI). Finally, we will
try to build an agent that could help us to rank the search results. Here
you will learn a framework to do prompt engineering in a scientific way. 


## slide 6

If you have watched my previous video, you will know that I have explained
the size of the data that OpenAI used to train GPTs. Here is the image.
It shows the scale of the data. It is huge.


## slide 7

Now, let's do another calcuation so we could understand how big the data is. My laptop is around 6 years old now. I used for all kinds of work. I have around 108GB documents
saved on my laptop. 50TB is around 50 thousand GB. Assuming the data quality is same,
you can think of 50TB is around 463 people working for 6 years to generate that much data or one person working for 2778 years. It is a huge amount of data.


## slide 8

But it is not just quality, it is also about the diversity of the data and quality of the data. They collected high quality of data all over the internet and structured it in a way that is easy for the model to learn.

Knowing how they collected the data and what kind of data they collected is very important as will help us to understand how to use the model and how to build agents that could work with the model.


## slide 9

Okay, now let me use an example to show you why data matters a lot and knowing the 
structure of the data matters a lot. Here is an example. This is one of artists I like a lot, his name is called Cai Guo-Qiang. Netflix has a documentary about him. I highly recommend you to watch it. It is very inspiring, it is called 'Sky Ladder'.


## slide 10

Here is the trailer of the documentary. He mainly uses the fireworks to create art. you can have a look at after this video. 


## slide 11

Now, let's choose one of his paintings adn see how Dall-E could generate it. Here you can see I chosed this one from this website.


## slide 12

The title is 'small template in a fishing village'. With extral description 'watercolor on paper'. Now, let's see how Dall-E could generate it.



## slide 13

I copy the title and paste it to Dall-E. 


## slide 14

Here is the result. It is not bad. It is not exactly the same but it is very close.


## slide 15

If we add 'in the style of Cai Guo-Qiang', it will generate something different. 


## slide 16

Now, if we add 'watercolor on paper', it gets interesting. It is not exactly the same but it is close.


## slide 17

As you can see, they have the same style now. 


## slide 18

So, 50TB data is not just about the size of the data, it is also about the quality of the data. High quality means that data is structured with very clear labels. Other factors such as resolution of images, grammar of the text, etc. are also important.


## slide 19

Those data are not just random data. They are structured in a way that could be used to build up a knowledge graph. Things are mapped to each other in a way that is easy for the model to learn.


## slide 20

Let's say this example. Here is the Q&A from stackoverflow. You have questions for all kinds of topics and you also have answers for those questions. Most importantly, you have people voting for the best answers. Those data are structured in a way that is easy for the model to learn.


## slide 21

Why knowing this will help us? Because we can use this knowledge to build agents that could work with the model. With those information in mind, you will know

- how to prepare the data
- how to make the data structured
- how to make the data high quality


## slide 22

Let's do some experiment with ChatGPT.


## slide 23

Here we will build a strategic planning agent. The agent will help us to plan our work.

This is the prompt. 


```
# Prompt

You are a master of doing strategic planning.
Your goal is to help your client to get the best plan 
and executable actions to achieve the client's goal 
as well as possible. 

If the client's is goal is not very clear, 
help the client to refine the goal too.
```

## slide 24

As we have did together in our lab session. This kind of strategic planning is 
still too abstract. It could give us some directions but you will
not feel that you are being empowered. 

Therefore, rule no. 1: avoid using ChatGPT to answer very general questions.


You can concult with it but don't rely on it.


## slide 25

Now, let's another experiement with ChatGPT. This time we will build a data extraction specialist. The agent will help us to extract data from the internet.


## slide 26

Here is the prompt.


```
You are a Data Extraction Specialist is 
responsible for retrieving specific data points 
from various sources based on user requests. 
You can fetch specific data points from different 
sources as per user requests depending on the specific 
context or industry. 

You are now hired as a helpful assistant for helping you 
clients at HyperGI.
```


## slide 27

Now, let's do lab session without using the function calling feature to see how it works.


## slide 29

As you can see from the lab, without the function calling feature, you have to structure your information mannually. It is not very efficient.


## slide 30

Function calling is a feature that makes ChatGPT very powerful. It structures the data very well. It follows the json format. For those who have not used json before, it is a very simple format. It is just a key-value pair. Don't be scared by it. It is very easy to use. I have another example to show you how to use it on the screen.


## slide 31

Let's review the structure of the function calling feature. You need function name,
parameters, and properties and requirements. Just follow the format and you will be fine.

## slide 32

As you have seen from the lab, sometimes we miss the format, it will not work. So, you need to be careful with the format.



## slide 33, 34, 35

Please do more labs to get familiar with the function calling feature. It is very powerful. And I also put python code on the screen so you can see how to use it in python. Read OpenAI's Cookbook for more details.


## slide 36

But why does ChatGT love json? Here is another secret I will share with you. 


## slide 37

Btw, if you ever uploaded some videos to youtube, you will notice that youtube will ask you whether this video is for kids or not. 


## slide 38

Since this video is not made for children, I could show you the secret. 



## slide 40

After knowing big players like LinkedIn organize my data so well. I want you know other organization called scheme.org. This organization was founded by Google, Microsoft, Yahoo, and Yandex. They have been working together to organize the data
on the internet. They standarlized the data format on the internet. They have been working on it for a long time. So, your data is well collected and well organized.


## slide 41

I hope know you understand better what does high quality 50TB data mean. I mean I have several master degrees and the data reviewed by me should be high quality. And they use it for free. Fair game 101. 

The takeway is that ChatGPT works very well with json format. 


## slide 42

Let's check closely how linkedin used my data. 


## slide 43

Here is the list of files they have collected and organized. Linkedin also did some career inference for me. They think I am a people leader. I am not sure how they did it. But I think it is very interesting. They also did the age inference for me saying that I am 25 to 34 years old based on my education and experience. 


## slide 44

But, will I stop using Linkedin, probably not.


## slide 45

I see our society as an interaction process, the faster informatino flows ,the faster society evolves. It is kind of trial and error process but with certain rules.


## slide 46

Also, there are people who want to share their knowledge and experience with others. Like me, 


## slide 47

Or like here. This image is only for eudcation purpose. to explain it to you what is instagram and how it looks like. 


## slide 48

Anyway, you got the point.


## slide 49

this slide was added later as I noticed that she put her instagram account as 'public figure'. so, you got the point.

## slide 50

Let's summarize what we have learned so far. 


- GPTs are trained with a lot of data

- Knowlge graph as a map between different data

- Avoid using ChatGPT to answer general questions (or big questions)

- Function calling is a secret weapon for extracting information you want

- json format works very well with ChatGPTs

- schema.org is a good place to find the structure of the data


## slide 51

By the way, to balance the gender ratio, I have to put more points in my slides. This guy is very environmental friendly as he does not need to wear the t-shirt. I am so jealous of him.


## slide 52

Okay, you have learned a lot today. Now, let's do another experiment with ChatGPT. This time we will build an agent that could help us to rank the search results. Here you will learn a framework to do prompt engineering in a scientific way.