---
marp: true
theme: tech2
paginate: true
math: katex
---


# The ChatGPT Advantage: Leveraging Free Agents for Success


Fei Wang (Michael) :heart: AI and many other things

HyperGI

Github: [oceanumeric](https://github.com/oceanumeric)



<img class="landing-img" src="../images/michael.png">

---


# I developed several agents to assist me with my daily work (not like the way you think 🐬)

## Now I'm going to show you how I did it 

> Make your agents be measurable

> It is tricky but everyone can do it too

<img class="landing-img" src="../images/michael.png">


---

![bg fit](./images/multi-agents-demo.png)


---

# Before we start, let me show you how to set up the above environment

# Lab Session


---

# Roadmap

- Understand how GPTs were trained by doing a simple experiment with [DALL-E](https://labs.openai.com/)

- Try 'Strategic Planning' with ChatGPT

- Try 'Data Extraction Specialist' with ChatGPT
    - Here you will learn what ChatGPTs are really good at
    - You will also learn a secret weapon that makes ChatGPTs be more powerful
        - **function calling** ❤️

- Try 'Rank Search Results' with ChatGPT
    - Here you will learn a framework to do prompt engineering _in a scientific way_ 



--- 

# We all know: GPTs are trained with a lot of data

> ~50TB of data


<img style="width:60%" src="../ai-duckdb/images/im7.png">


---

# ~50TB of data means what?

- My laptop is 6 years old
    - I used for all kinds of work
- 108GB Documents (not all of them are generated by me)
- 50TB = 50,000GB
    - $50,000 / 108 \approx 463$ people working for 6 years
    - $463 \times 6 \approx 2,778$ years of work by one person

<img style="width:60%" src="./images/data-on-my-laptop.png">


---

# ~50TB of data means what?

- High quality of data collected from the Internet

- Structured data collected from the Internet

> Knowing how they collected the data and what kind of data they collected is important


---

# Cai Guo-Qiang

![bg right](https://caiguoqiang.com/wp-content/uploads/2019/01/skyladder-netflix_ltr.jpg)


---

<iframe width="960" height="500" src="https://www.youtube.com/embed/lLTT8ogRf50?si=ncvxb-GdDxje84Vy&amp;start=15" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

![bg fit](./images/caiguoqiang.png)


---


Small Temple in a Fishing Village
1975 [ca.]
*Watercolor on paper*
15.9 x 25 cm


![bg right](./images/cgq1.png)


---

![bg fit](./images/dalle-instruction.png)


---

![bg fit](./images/dalle1.png)


---

![bg fit](./images/dalle2.png)


---

![bg fit](./images/dalle3.png)



---

![bg fit](./images/combined.png)


---

# ~50TB of data means what?

- High quality of data collected from the Internet
    - with very `good labels`
    - in terms of quality
        - for images - resolution, etc.
        - for text - grammar, etc



---

# ~50TB of data means what?

- High quality of data collected from the Internet
    - with very good labels

- Structured data collected from the Internet
    - knowledge graph
    - things are mapped to each other
        - images to text
        - problems to solutions
            
            

---


![bg contain](./images/stackoverflow.png)


---

# Why knowing this will help us?

- this will help us to know how to feed the data to the GPTs
    - how to prepare the data
    - how to make the data structured
    - how to make the data high quality





---

# Let's do a simple experiment with ChatGPT


<img class="landing-img" src="../images/michael.png">


---

# Strategic Planning

```
# Prompt

You are a master of doing strategic planning.
Your goal is to help your client to get the best plan 
and executable actions to achieve the client's goal 
as well as possible. 

If the client's is goal is not very clear, 
help the client to refine the goal too.
```


---

# Lab Session


--- 

# This kind of strategic planning is still too abstract

- It could guide us some directions
- But, you will not feel that you are being empowered

<br>

> RULE NO.1: Avoid using ChatGPT to answer general questions (or big questions)

<br>

- `You can consult with it but don't rely on it`


---

# Let's do another experiment with ChatGPT

## Data Extraction Specialist

<img class="landing-img" src="../images/michael.png">

---

# Data Extraction Specialist

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


--- 

# Lab session (without function calling)


---

# Function Calling (one of the secret weapons)

![bg right](https://miro.medium.com/v2/resize:fit:1358/1*R7SsR-EipK9BmVK3yX4_rQ.png)


---

# Function calling

- It is a feature to make ChatGPTs be more powerful
    - Very handy for doing data extraction
    - It structures the data very well
    - You need to know `json` format a little bit
        - Do not be scared, it is very easy
        - It is just a nested dictionary

```js
{
    "agent_name": "data_extraction_specialist",  // string
    "creator": "Michael",
    "version": [{"2021-12-01": "v1.0.0"}, {"2021-12-02": "v1.0.1"}]  // array 
}
```


---

# Function calling


```js
{
  "name": "extract_address",
  "parameters": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of company"
      },
      "address": {
        "type": "string",
        "description": "The address of the company"
      },
      "country": {
        "type": "string",
        "description": "The located country of the company"
      }
    },
    "required": [
      "company_name",
      "address",
      "country"
    ]
  },
  "description": "Extract the address from the website"
}
```

---

# Function calling

## Format matters a lot

- Start with the example provided by OpenAI

- Define the structure of the data (whatever you want)

> Remember to save after editing the function calling ⚠️


---

# Lab Session: Function Calling


---

```js
{
  "name": "extract_contacts",
  "parameters": {
    "type": "object",
    "properties": {
      "country_phone_code": {
        "type": "number",
        "description": "The country phone code of the company"
      },
      "email": {
        "type": "string",
        "description": "The email of the company"
      }
    },
    "required": [
      "country_phone_code", "email"
    ]
  },
  "description": "Extract the contact information from the website"
}
```

---


[OpenAI Cookbook](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)

```python
functions = [
  {
    "name": "extract_address",  # ....
  }
]
prompt = """You are a Data Extraction Specialist..."""
def my_function(input_data):
  completion = client.chat.completions.create(
          model="gpt-4",
          messages=[
              {"role": "system", "content": prompt},
              {
                  "role": "user",
                  "content": f"your data input {input_data}",
              },
          ],
          functions=functions,  # this is how you use it
          function_call='auto'
      )
  return completion.choices[0].message.model_dump_json()  # result
```

---

# Why does ChatGPT love json format?

## Another secret I will share with you now :)

![bg right:40%](https://upload.wikimedia.org/wikipedia/en/3/34/Fantastic_Beasts-_The_Secrets_of_Dumbledore.png)


---

![bg fit](https://miro.medium.com/v2/resize:fit:1400/0*2iFIzmhNNBa-AMe-.png)


---

# This is not made for children

![bg right](https://www.myfashionlife.com/wp-content/uploads/2009/12/rosie.jpg)


---

# Lab Session (what kind of data LinkedIn collects from you)



---

# Welcome to Schema.org


> Founded by Google, Microsoft, Yahoo and Yandex, Schema.org vocabularies are developed by an open community process, using the public-schemaorg@w3.org mailing list and through GitHub.

<br>

- [Person](https://schema.org/Person)
- [Organization](https://schema.org/Organization)
- [Health/medical](https://schema.org/docs/meddocs.html)


---

# ~50TB of data means what?

- High quality of data collected from the Internet
    - with very good labels
    - with very good quality
        - for images - resolution, etc.
        - for text - grammar, etc
- Structured data collected from the Internet

<br>

> Takeaway: json format works very well with ChatGPTs



---

# See How LinkedIn Uses My Data

# Lab Session


---

# Inferences About You 

- `career inference`
    - `people leader`
- `age inference`
    - `25-34`
    - based on your education and experience

![bg right:40%](./images/linkedin-data.png)


--- 

# Will I stop using LinkedIn?

- No, I will not stop using LinkedIn
    - I will use it more often


> The above text is generated by ChatGPT after typing `No`...


--- 

# Will I stop using LinkedIn?

> Society as an interactive process

- The faster information flows, the faster society evolves
    - Trial and error
- Let's iterate faster
    - You give me your data
    - if I used it well, you will be happy
    - if I used it badly, punish me as you wish


---

# Also, there are people who want to share their data, like me 😎

<img class="landing-img" src="../images/michael.png">


---

# Like her (for educational purpose only)

<img width="90%" src="./images/gmx-model.png">


---

# Anyway, you got the POINT (or POINTS)

![bg right](./images/instagram-model2.png)


---

# Like her 

<img width="90%" src="./images/public-figure.png">


---

# Let's summarize what we have learned so far

- GPTs are trained with a lot of data

- Knowlge graph as a map between different data

- Avoid using ChatGPT to answer general questions (or big questions)

- Function calling is a secret weapon for extracting information you want

- json format works very well with ChatGPTs

- schema.org is a good place to find the structure of the data


---

# Hey, Greta Thunberg, if you are watching this video

<img style="width:50%" src="./images/male-models.png">


--- 

# You learned a lot today

## One more Lab Session


---

# Rank Search Results

- A relative hard task for ChatGPT

- You will learn a framework to do prompt engineering _in a scientific way_

- You will also learn how to design a `data strategy` for your ChatGPTs


---

# Rank Search Results

## Problem setting

> I notice a company called `watershed`, a software platform to help businesses to reduce their carbon footprint comprehensively. I want to know more about it.


---

![bg contain](https://watershed.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmeasure.ec4d22be.png&w=3840&q=75)


---

# I want to find how they did it

## Of course, I googled it

- Selected `30` results from Google
- Each of them is a `json` object



---

```js
{
"date": ["2024-01-16"],
  "query": ["how watershed help firms to reduce carbon emissions"],
  "results": [
        {
        "result_idx": 1,
        "title": "Watershed — The enterprise climate platform",
        "link": "https://watershed.com/",
        "snippet": "Watershed is the enterprise climate platform.
        Measure your carbon footprint, report your results,
        and take action to reduce your emissions — starting now."
        },
        // ... many more results upto 30
    ]
}
```

---

# I want ChatGPT to help me to select the best results that fit my needs

> 🧐 how could ChatGPT know what I want?

> Prompt Engineering 🦾


---

# Lab Session


---

# Prompt Engineering

> What is prompt engineering?

[ChatGPT Answer](https://chat.openai.com/share/d2a0f20c-f23a-4ed0-be3a-e393184b8b8a)

> Too long to uninstrucive

```
# my answer

It is not command engineering. It is prompt engineering.
```


---

# Command V.S. Prompt

> Command: `Do this!` or `Give me the best results!`

> Prompt: `I have this..., they are organized in this way..., now arrange them based on the number of relevant keywords that fit my needs`


---

# Introudcing HyperGI's Prompt Engineering Framework

- Classify all you tasks into the following categroies:

   1. `write` (or `generate`)
   2. `extract` (or `retrieve`)
   3. `rank` (or `sort`)

  
---

# Introudcing HyperGI's Prompt Engineering Framework

<img style="width:60%" src="https://pythoncoursesite.files.wordpress.com/2017/01/input_output.gif">


---

# Introudcing HyperGI's Prompt Engineering Framework

> Let's say we have a simple input `I booked a flight from New York to London`

- `write` (or `generate`): _I booked a flight from New York to London_ `I am planning to stay in London for 3 days.`
- `extract` (or `retrieve`): _I booked a flight from New York to London_ `places: New York, London`
- `rank` (or `sort`): _I booked a flight from New York to London_ `A flight was booked from New York to London`


---

# Introudcing HyperGI's Prompt Engineering Framework

- Write and Extract are easy to understand
  - most effective way is to give examples (good examples)
  - brainstorming together with ChatGPT is a good way to get good examples
  - `function calling` is a good way to structure the data

- Rank is a little bit tricky
  - You need to understand the data well
  - You need to know how to design a good prompt


---

# People always want the best results

> But, what is the best? (rank or sort)

<br>

<img style="width:50%" src="https://afteracademy.com/images/comparison-of-sorting-algorithms-banner1-b8ab06536245c4da.png">




---

# Best as subjective

![bg right:40%](https://www.refinery29.com/images/11525994.jpg)


---

# Best as subjective

![bg right:40%](https://s.yimg.com/ny/api/res/1.2/y9OOymNr4JEAr4g.aiETAg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTk2MA--/https://media.zenfs.com/en/fashionista_850/b91b7f6670984781f803ad9d10363a7f)


---

# But 'best' could be objective


> For the best as objective, design the metric first


---

# Best as objective

<img style="width:93%" src="https://www.azquotes.com/picture-quotes/quote-you-can-t-manage-what-you-don-t-measure-peter-drucker-86-73-61.jpg">



---

# Lab Session (Rank Search Results with A Metric)

- [fei.wany@hypergi.com]() : Europe
- [christian.huening@hypergi.com]() : US


> Contact us if you want to know more about HyperGI's Prompt Engineering Framework. We also develop and deploy customized ChatGPTs and multi-agent systems for our clients.


<img class="landing-img" src="../images/michael.png">


---

# Knowing the data well is important

- You need to know what kind of data you have

- Know how to label or describe the data

- Then you can organize the data in a way that ChatGPTs can understand


---

# Maybe learning a little bit about 'sorting algorithms' is helpful

- Give you a sense of how to design a good prompt

- Give you the language that you can instruct ChatGPTs to do the sorting

- [Design and Analysis of Algorithms](https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp) from MIT


---

# If no time to learn, just use the following principle

```
# What is decision making?
```

> Decision making is the process of selecting a course of action from among `multiple alternatives` to achieve a desired outcome or solve a problem. It involves evaluating various options, considering their potential consequences, and `choosing the most suitable or optimal solution` based on `a set of criteria, goals, or values`. Decision making is a fundamental aspect of human cognition and is applicable in various contexts, including personal, professional, and organizational settings.


---

# Decision Making as a Sorting Problem

- `multiple alternatives` $\rightarrow$ `many choices`
- `choosing the most suitable or optimal solution` $\rightarrow$ `best choice`
- `a set of criteria, goals, or values` $\rightarrow$ `metric`



---

# Programs =  Data Structures + Algorithms

- Structure your data well
- Design a good prompt

![bg right:40%](https://upload.wikimedia.org/wikipedia/en/9/90/Algorithms_%2B_Data_Structures.jpg)



---

<br>

# See you next time 


![bg right:53%](https://static.vecteezy.com/system/resources/thumbnails/008/873/599/original/subscribe-and-reminder-button-animation-on-black-channel-animated-background-click-internet-media-online-social-stream-streaming-views-youtube-free-video.jpg)

<img class="landing-img" src="../images/michael.png">