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

## Databse 

We can server *multiple concurrent* request using horizontal scaling <br>
Multiple request will lead to *lots of read/write request* to database which eventually lead to <mark style="background-color:SlateBlue;color:white">slowness</mark> of app.

<mark style="background-color:Tomato;color:white"> How to solve data read/write issue? </mark>
<ul>

<li> 

### Path 1
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

### Path 2
Switch to NOSql, now joins will need to be done in your app. <br>
Sooner  your db request will again be slower & slower. <br>
you will need to introduce <mark style="background-color:SlateBlue;color:white">Cache</mark> .
</li>
</ul>