---
toc: true
layout: post
description: Scalable Service results in increased performance in a manner proportional to resource added.
categories: [markdown]
title: Scalibility Basics
---
# Scalibility Basics

## Clone

### First *Golden Rule* of Scalibility

Every server contains exactly `SAME CODEBASE` and `DON NOT STORE` any user-related data, like session or profile picture, on local disk or memory.

<mark style="background-color:Tomato;color:white"> where to store userdata? </mark>

> userdata needs to be stored in a centralized data store <br> which is accessible to all your app server.

<br>

## Database 

We can server *multiple concurrent* request using horizontal scaling <br>
Multiple request will lead to *lots of read/write request* to database which eventually lead to <mark style="background-color:SlateBlue;color:white">slowness</mark> of app.

<mark style="background-color:Tomato;color:white"> How to solve data read/write issue? </mark>
<ul>

<li> 
<h3>Path 1</h3>
Do Master Slave Replication <br>
(Read from slave, write to master)<br>
Upgrade master server by adding more RAM.
<ul>
<li>Sharding</li>
<li>Denormalization</li>
<li>Sql Tunning</li>
</ul>

</li>

<li>
<h3>Path 2</h3>
Switch to NOSql, now joins will need to be done in your app. <br>
Sooner  your db request will again be slower & slower. <br>
you will need to introduce <mark style="background-color:SlateBlue;color:white">Cache</mark> .
</li>
</ul>

## Cache 

`when to use cache `: user have to suffer slow page request when a lot of data is fetched from database.<br>
With "Cache" means `IN-MEMORY` like memcached or redis.

<ol>There are two patterns of caching data
<li>Cached Database Queries</li>
<li>Cached Object<br>
<mark style="background-color:MediumSeaGreen;color:white">Idea of objects to cache</mark>

- User Session
- Fully Rendered Blog Articles
- Activity Streams
- User <-> Friend Relationships

</li>
</ol>


## Asynchronism

`Please wait a while situations`

### Async #1 
    The First way of aysc processing is the pre build the content and serve when request arrive.

This paradigm used to serve dynamic content page of a website are prebuid <br>
and locally stored as static website on every change often these computing <br>
are done on a regular basis, maybe a scirpt which is called every hour by a cronjob. <br>
the static website are stored in <b>cloud object storage</b>.

### Async #2 
    The Second way of async processing is the system request the heavy computing task, put it in job queue and free the system to do other task and let notify system when it's done.

User come & start a very heavy computing task `such as order product online`, so frontend website sends a job onto a job queue & immediately signals back to the user. the job queue is constantly checked by a bunck of workers for new job, the worker do work and signal work done to frontend.

---

We have come to end of blog, Please let us know for any suggestions and queries in comment box.<br>

<b> Stay tunned . Amazing Work Comming Soon <b>

