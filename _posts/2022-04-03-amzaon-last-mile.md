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


# problem 2 



```
def party(guest,total_candle,time_burn,atleast_candle):
    temp = 0 
    while len(guest) > 0:
        t = guest.pop(0)
        if t < temp:
            print(t,guest,total_candle)
            continue
        else:
            temp = t + time_burn 
            total_candle -= atleast_candle
            
        if total_candle < 0:
            print("not possible")
            return 
        print(t,guest,total_candle)
            
guest = [5, 7, 9, 10, 12,18,30,50,56,78,85,87,89]
total_candle = 15
time_burn = 5
atleast_candle = 2
party(guest,total_candle,time_burn,atleast_candle)
```
```

import math 
def party(guest,total_candle,time_burn,atleast_candle):
    temp = 0 
    prev = 0
    while len(guest) > 0:
        t = guest.pop(0)
        if t < temp:
            print(t,guest,total_candle)
            continue
        else:
            dark_candle = math.ceil((t - prev)/time_burn)
            temp = t + time_burn 
            total_candle -= atleast_candle
            total_candle -= dark_candle
        prev = t
        if total_candle < 0:
            print("not possible")
            return 
        print(t,guest,total_candle)
            
guest = [5, 7, 9, 10, 12,18,30,50,56,78,85,87,89]
total_candle = 15
time_burn = 5
atleast_candle = 2
party(guest,total_candle,time_burn,atleast_candle)
```













You are employed as an Azure DevOps Engineer, and your company wants to run their microservices applications on containers. This is to prevent managing of nodes in VM scale sets and paying for infrastructure which may go unused. The company decides to use virtual nodes with managed container instances. You have to create Azure Container Instances with the following configurations. i) Kubernetes Service: Region: East US, Node size: Standard Ds2 v2, Node count: 1, Integrations -> Container monitoring: Disabled. ii) Container instance: Region: East US, Image source: Quickstart images, Container image: mcr.microsoft.com/azuredocs/aci-helloworld (Linux), Size: 2 vcpus, 4 GiB memory, 0 gpus. iii) App Services: Runtime Stack: .NET Core 3.1 (LTS), Operating System: Windows, Region: East US, Size: F1 Shared infrastructure, 1 GB memory. iv) Batch Account: Region: East US.