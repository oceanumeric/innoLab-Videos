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
