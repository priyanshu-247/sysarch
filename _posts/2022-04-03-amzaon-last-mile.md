---
toc: true
layout: post
description: coding challenge 2022
categories: [markdown]
title: Amazon last mile challenge
# image: images/post_img/post1.png
comments: true 
hide: false
---

# problem 1

Load balance the job on n number of processor where k is number of processor to be executed on these processor 

```
from heapq import heapify, heappush, heappop
def loadbalance(job,k):
    heapify(job)
    while k > 0:
        loc_min = heappop(job)
        heappush(job,loc_min+1)
        k -= 1
    print(job)

loadbalance([2,4,3],100)
```

