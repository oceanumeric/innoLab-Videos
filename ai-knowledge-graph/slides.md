---
marp: true
theme: rose-moon
paginate: true
math: katex
---


# From the Value of Information to the Value of AI

## Data and AI Strategy at HyperGI

<br>

Fei Wang (Michael) :heart: AI and many other things

HyperGI

Github: [oceanumeric](https://github.com/oceanumeric)



<img class="landing-img" src="../images/michael.png">

---


# Roadmap

- A framework for navigating in the information and AI age
    - Three fundamental questions



---

# Q1 - Why do we need information?

- Human beings are information-driven animals
    - our brain is a complex information processing system
    - we reply on information to make decisions
    - we are curious about the world

<br>

> In the business world, many important decisions are made based on information.


---

# Q2 - Is it always beneficial to have more information?

- tricky? 🧐
- what is the value of the information?
- What is the cost of getting the information?


<br>

> Both the value and the cost of information are context-dependent.


---

# Q2 - Examples

- It will rain tomorrow ⛈
    - Cost: almost zero
    - Value: depends
        - for airline industry: high
        - for a homeoffice worker: low

- In the war, the enemy is going to attack tomorrow
    - Cost: high
    - Value: high


--- 

# Principle I: The value of information is context-wise


---

# Strategy I: To sell information is to construct (or sell) context


---

# Some examples

<iframe width="960" height="500" src="https://www.youtube.com/embed/8Nvf4BteCR4?si=5rEMXSFqnYbFP2JS&amp;start=269" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


---

# Q3 - What is context and how to measure it?

- Context is the background information that is needed to interpret the information
    - what is the background information?
    - Can AI understand the context?

<br>


---

# Can AI understand the context?

## Yes

- The following example shows that AI can understand the context

<br>

```
> Here is a job title: data scientist, give me a short-bio that
could be used for a resume

ChatGPT: A dedicated and results-oriented data scientist
with [X years] of experience in leveraging advanced
analytics techniques to extract insights and
drive strategic decision-making.
Proficient in statistical analysis, ....
```


---

# Can AI understand the context?

## Yes or No

<br>

![tina-conservation](./images/tina-conversation.png)

---

# Can AI understand the context?

## Yes or No

<br>

```
> Do you know this website: https://www.thalia.de/,

ChatGPT: Yes, I'm familiar with Thalia.de. Thalia is a
German-based chain of bookstores and online retailer
specializing in books, e-books, music, movies, and more.
Thalia.de offers a wide range
```


---

# Can AI understand the context?

## Yes or No


<br>

```
> Do you know this website: https://www.jaeger-birkenau.de/

ChatGPT: I'm sorry, but I couldn't find any information
on "https://www.jaeger-birkenau.de/".
It seems to be a specific website, but without 
more context, I can't provide details about its content or purpose.
```


---

# What is the context?

- Context is just linked information
    - ChatGPT knows Thalia.de because
        - first, it is in its training data (database)
        - second, it is linked to other information (such as bookstores, online retailer, books, e-books, music, movies, etc.)
    - I didn't know the Thalia.de because
        - I did not store this information in my brain

- Therefore, we can say that

> Context = Entitites + Relations


---

# Principle II: Context is linked information (Entitites + Relations)


---

# Why context matters?

- Context is the key to understand the information
    - without context, information is meaningless
    - with context, information is valuable


---

# Recap

- Principle I: The value of information is context-wise
- Strategy I: To sell information is to construct (or sell) context
- Principle II: Context is linked information (Entitites + Relations)

<br>

> How could we measure the context? Why it matters?



---

![bg contain](./images/context-logic.png)


---

# How to measure the context?

- Tomorrow is going to rain
    - Context: weather, location, time, etc.
    - Context in the airline industry: very valuable
        - very relevant to the business
    - Context in the homeoffice worker: not valuable
        - not relevant to the business


---

# Strategy II: To measure the context is to measure the degree of relevance


[ChatGPT's Answer](https://chat.openai.com/share/a3f1b0b1-48f9-4ba4-a5c6-6ac22eb84a50)



---

# How could we measure the degree of relevance?


|Method | Algorithm (inluding AI) can do | Human can do |
|:---|:---:|:---:|
|Contextual Analysis | :heavy_check_mark: | :heavy_check_mark: |
|Comparsion | :heavy_check_mark: | :heavy_check_mark: |
|Scoring System | :heavy_check_mark: | :heavy_check_mark: |
|Expert Opinion| :x: (it depends) | :heavy_check_mark: |

<br>

> BUT, the above table does not give us a clear answer to the question: How to measure the degree of relevance?


---

# How could we measure the degree of relevance?


| Search Engine + AI | Human |
|:---|:---|
| need to work out the algorithm | need to talk with experts |
| need to collect data | need to think and understand |
| need to put it into a context | need IQ and EQ |