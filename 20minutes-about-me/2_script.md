Hello everyone,

This is the second video of the series '20 minutes about me'. In this video, I will share my experiences about knowledge graph and large language models, aka ChatGPT. 

As I have explained that I am doing this is to let potential collaborators, investors, and recruiters know more about me. I believe it is important to know a person's value, expertise, and vision before deciding to work together.


The theme of this video is about knowledge graph and large language models, which is big part of my current research. 

Now, let's have a look at the roadmap of this video. First, I will give some examples of showing halluciative behaviors of ChatGPT. Then I will explain why it happens like this. After that, I will explain how knowledge graph could address this issue. Finally, I will explain why I fell in love with knowledge graph. 


I hope you will enjoy this video. Let's get started. It has been well known that large language models, such as ChatGPT, have the capability to generate human-like text. However, it is also well known that these models sometimes generate hallucinative text.

Let's check some examples. 

In this example, I asked ChatGPT a question: what is H01M 10/06 in patent classification? ChatGPT gives some answers. If you are not patent expert, you may think the answers are correct. But if you are patent expert, you will find that the answers are wrong. In this example, the model I am using is gpt-3.5-turbo.


Before we go for the next example, let me explain what is CPC classification. CPC classification is a patent classification system. It is used by patent offices to classify patent documents. Say, you created a new technology like the one shown on the screen. After submitting the patent application, the patent office will assign a CPC classification to your patent. This classification is used to search for similar patents. In this case, it will be H04M, which is a classification for telecommunication.


Now, say you got this invention, which is an electric battery. The patent office will assign a CPC classification to your patent. In this case, it will be H01M, which is a classification for batteries. And sub-classification 10/06 is for lead-acid batteries.


However, when we ask ChatGPT what is H01M 10/06, it told us that it is a classification for battery, but did not tell us it is for lithium batteries. This is a halluciative behavior. If you read the text, you can see it gives you some extra information, which is useless.


You may argue that GPT-4 will perform better. But when I tried GTP-4-turbo, it still gives some wrong information. And some of the information is even misleading.

I tried several times with different models, but the results are similar. This is a common issue for large language models.

In this round, GPT says that H01M 10/06 is lithium battery. But it is not. It is lead-acid battery. This is a halluciative behavior. I tried it again, but the result is still wrong.


Why LLMs have halluciation issue?


Before I answer this question, let's review some basic concepts about linear regression. Whether it is linear regression or transformer model, they all try to estimate parameters of a function by doing some optimization. The difference is that linear regression is a simple model, while transformer model is a complex model. However, the process is same:

- they need to fit with data
- use optimization to find the best parameters

Therefore, both linear regression and transformer models are probabilistic models. This means they behave stochastically. 

When we ask a question to a transformer model, it will give us an answer based on the probability distribution of the answers. The answer with the highest probability will be selected. Therefore, it has a chance to give us a wrong answer. This is why we see the halluciative behavior of ChatGPT.

Because large language models have to find their parameters in different probability space and distribution, they have to make some trade-offs. When they are doing prediction or generation, each token follows the path that is shaped by maxium likelihood estimation. Therefore, jumping around in the probability space is inevitable. This is why we see the halluciative behavior of ChatGPT.


So, people in the community are aware of this issue. How could we solve this problem?


The industry has spent lots of investment and energy on RAG, which means
retreval-augmented generation. The idea is to use documents or data as gound truth to guide the generation process. There are many packages are doing this, I will not go into details here.

Recently, microsoft published a research paper called GraphRAG. The idea is to use knowledge graph to guide the generation process. The results are promising. 


Now, I will explain how knowledge graph could address this issue.

If we come back to the first example. I have asked ChatGPT what is H01M 10/06. When you go to google the official answer, you will find that it is a classification for lead-acid batteries like the document shown on the screen.

The reason we see many 'wound' words from GPT's answer is that this document has many text about batteries and some of them are discussing topics realted to 'wound'. I used the search function to see the frequency of the word 'wound' in the document. 

When you zoom in, you can see the frequency of the word 'wound' around the true answer is very high. This is why ChatGPT gives us the wrong answer.

This image shows the answer from ChatGPT. You can see that it talks about 'wound' a lot. Therefore, one has to be careful when using ChatGPT to generate text.


Okay, lots of complaints about ChatGPT. How could we solve this problem? We can use knowledge graph to guide the generation process. 

This table gives the answer of 'H01M 10/06' from the knowledge graph query. You can see that it is a classification for lead-acid batteries. The answer is correct because this is the official answer from the patent office. 

What we are doing here is that we use the SPARQL query to get the answer from the knowledge graph. Here I show you the query and results. 


I will not go into details about how to build a knowledge graph. In general, you need to build up the ontology and map the data to the ontology as it is shown on the screen.

In this case, we are transforming the hierachy of the patent classification into a graph. 



When we combine the knowledge graph with ChatGPT, we basically feed the knowledge graph to ChatGPT. When ChatGPT generates text, it will refer to the knowledge graph to make sure the answer is correct.

Therefore, knowledge graph is very useful to address the halluciative behavior of ChatGPT. Here I give the another example, which is a medical knowledge graph. 


This figure shows the pros and cons of both knowledge graph and ChatGPT. I will not go into details here. But you can see that knowledge graph is very useful to address the halluciative behavior of ChatGPT.


Now, let me share why I fell in love with knowledge graph.


When I start to work as a data scientist, I was very keen to learn all kinds of technology in the data science community, such as common ETL tools, machine learning algorithms, and big data technologies. However, technology is only part of the story.

If we look at the big picture, technology is probably only one third of the story. Good management from human beings is another third. The last third is about integrating common automation tools and AI technologies with the business. To do this, knowledge graph plays a big role.


By the way, most people learn to do data-driven projects with data models, such as the one shown on the screen. However, when you have a large amount of data, you will find that it is very hard to manage the data models. So many relationships and so many attributes, I found it hard to manage them. I prefere to use knowledge graph to manage the data, especially for the complex data models.


Peole have already used knowledge graph in many industries, such as finance, healthcare, and e-commerce. Here I show you some examples.

The first one is called spoke, which is a knowledge graph for biomedical data. 


The second one is from swiss personalized health network. They use knowledge graph to integrate data from different sources.

The third one is from IDTA, they use knowledge graph to build up digital twin for the industry.


I will not go on and on about the examples. Since I appreicate the power of knowledge graph, I will record a series of videos to share my experiences about knowledge graph and to teach semantic web technologies. 

With my 10 years of experience in data science, I believe I can help you to build up your knowledge graph in a more efficient way.


Before I finish this video, I want to share a paper which I found very useful. The paper is called 'Unifying Large Language Models and Knowledge Graphs'. This paper gives a good roadmap on how to combine large language models with knowledge graphs. I highly recommend you to read it.


Okay, that's all for this video. I hope you enjoy it. If you have any questions, please feel free to ask me. I will be happy to answer your questions.