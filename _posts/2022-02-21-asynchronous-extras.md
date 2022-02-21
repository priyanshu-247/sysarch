---
toc: true
layout: post
description: Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
categories: [markdown]
title: Asynchronous Basics
# image: images/post_img/post1.png
comments: true 
hide: true
---

Note: Threaded programs allow you to create multiple, parallel paths of execution that all share the same memory space. This is both an advantage and a disadvantage. Any memory shared between threads is subject to one or more threads trying to use the same shared memory at the same time. This can lead to data corruption, data read in an invalid state, and data that’s just messy in general.

In threaded programming, the context switch happens under system control, not the programmer. The system controls when to switch contexts and when to give threads access to shared data, thereby changing the context of how the memory is being used. All of these kinds of problems are manageable in threaded code, but it’s difficult to get right, and hard to debug when it’s wrong.
