---
marp: true
theme: tech1
paginate: true
math: katex
---


# Here is my presentation


<img class="landing-img" src="../images/michael.png">

---

# This is the first slide and the title

## this is the second title

hello


```python
@profile
def read_json():
    start = time.time()
    duckdb.read_json("./data/goodreads_books.json.gz").show()
    end = time.time()
    print(end - start)  

if __name__ == "__main__":
    read_json()  # 6 seconds for around 8GB data (1.94 GB compressed)
```



---

# The second slides 


```js
// Using require
const hljs = require('highlight.js');

// Using ES6 import syntax
import hljs from 'highlight.js';
```

---

# Why it is so hard to build a functional AI product?

## Let's say I want to build a `mini` ChatGPT

- Instead of using 45TB of data, I will use 45GB of data
- Instead of gathering all text everwhere, I will only use the text from `Goodreads`


---


<!-- _class: math -->

$$
\begin{aligned}
\mathcal{L}(\theta) &= \sum_{i=1}^{N} \log p(x_i | x_{<i}, \theta) \\
&= \sum_{i=1}^{N} \sum_{t=1}^{T_i} \log p(x_{i,t} | x_{i,<t}, \theta)
\end{aligned}
$$


---

> this is the code block

- [hue color](https://www.happyhues.co/palettes/4)



