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

# Principle I: The value of information is context wise


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
        - not relevant



---

# How to measure the context?
  
- Context in the airline industry: very valuable

> Context is rich; ✈️⛑👨‍👩‍👦💸...

- Context in the homeoffice worker: not valuable

> Context is not that rich; 🏡👨‍💻🪑


---


![bg contain](./images/war-and-peace.png)





---

# Strategy II: To measure the context is to measure the number of relevant entities and degree of relevance (relations)


[ChatGPT's Answer](https://chat.openai.com/share/a3f1b0b1-48f9-4ba4-a5c6-6ac22eb84a50)



---

# Recap

- Principle I: The value of information is context-wise
- Strategy I: To sell information is to construct (or sell) context
- Principle II: Context is linked information (Entitites + Relations)
- Strategy II: To measure the context is to measure the number of relevant entities and degree of relevance (relations)


---

![bg contain](./images/summary1.png)


---

# How does ChatGPT (LLM) understand the context?

- Entities (easy, just store the information in the database)
- Relations (hard, need to learn from the data)



---

# How to measure the degree of relevance?

- we can assign a score (or weight) to each relation
    - the higher the score, the more relevant the relation is
    - the lower the score, the less relevant the relation is


---

![bg contain](./images/degree-of-relevance-1.png)



---

![bg contain](./images/word-embeddings2.png)


---


<iframe width="960" height="500" src="https://www.youtube.com/embed/8-Ymdc6EdKw?si=14eQukFU90KTAiM5&amp;start=35" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


---

<iframe width="960" height="500" src="https://www.youtube.com/embed/Rp3A5q9L_bg?si=jisfi0Vxj-52Yzad&amp;start=1992" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


---

# Human vs AI (complementary to each other)


| | Human | AI |
|---|---|---|
|context | we understand the context | AI understands the context _partially_ |
| memory | strore information in the brain | store information in the database |
| reasoning | intuition and logic | algorithms |
| shortcoming | limited memory and processing power | limited understanding of the context |
| advantage | creativity and flexibility | scalability and efficiency |

