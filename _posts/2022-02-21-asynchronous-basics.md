---
toc: true
layout: post
description: Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
categories: [markdown]
title: Asynchronous Basics
comments: true 
---

# Asynchronous Basics

Before we dewel into async basic, lets understand the sync code behaviour.

### Sync 
It execute one step a time. Even with all conditional branching, loops and function calls. we can still think in terms of code that a single step at a time. when each step is completed, the program moves to next one.

### Real Example 
Lets think "techie [our bot]" needs to send message to 100 bot friends for special bot get together. Each bot friends reply with different time delay. So on an average each take 30 miliseconds to reply. The "techie [our bot]" as being superfast bot in these bot society with heavy resource hardware and updated software [As we take care of our bot a lot], it replys in 0.5 miliseconds. As this is non-working day, techie decide to send message and wait for other bot to accept/reject invitations, so time taken would be 30.5 milisecods with each bot. this would lead to total time of 30.5 * 100 = 3050 miliseconds (lazy converter, it will take time to convert into seconds). 

Now Scenario has been changed as this would be going to very rough day for techie [bcz our team is on trip, everyone is enjoying !!!]. As techie seeing us ignore, decide to have party with bot friends after works. But it seems as of tight **Process Schedule", techie don't have 3050 miliseconds to send invitation. What to do now !!!. 
On **thinking** techie decided to take approach of async way, secretly our one of team member taught this to techie.
Let us see what has been taught to techie secretly.

**[confidential notes started !!]**

Asynchronous program behave differently, it will take one execution step a time. Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.

This means that the program will move on to future execution steps even though a previous step hasn’t yet finished and is still running elsewhere. This also means that the program knows what to do when a previous step does finish running.

Asynchronous programming techniques allow programs to take advantage of relatively slow IO processes by freeing the CPU to do other work.

homework techiniques for techie : polling interval, threading way, context-switching, blocking code & non-blocking code.

**[confidential notes ended !!]**


### we need to first look at techie sync code for bot invitation.

```
import queue
import random
import time 

# create random status behaviour for bots
def random_status(bot_info):
    status = ['online','offline','busy']
    for info in bot_info:
        info['status'] = random.choice(status)
    return bot_info

# create random respone delay behaviour for bots
def random_response(info):
    delay = 5
    response = random.choice(['accept','reject' 'on sick leave'])
    if info['status'] == 'busy':
        delay += random.randint(1,5)
    time.sleep(delay)
    return response, delay 

def imp_message(imp_queue):
    if imp_queue.empty():
        print("No special attention needed.")
    else: 
        while not imp_queue.empty():
            info = imp_queue.get()
            print("Hi {0},Get well soon !!".format(info['name']))

def invite(invite_queue, imp_queue):
    total_time = 0
    if invite_queue.empty():
        print("No new invitation to make.")
    else:
        while not invite_queue.empty():
            info = invite_queue.get()
            print(info)
            respone, delay = random_response(info)
            if respone == 'on sick leave':
                imp_queue.put(info)
            total_time += delay
            print("time taken to get response: {0} millisecond".format(delay))
    print("time taken in {0} millisecond to complete invitaiton".format(total_time))
    


def main():
    bot_info = [
        {"name": "Smart Bot"},
        {"name": "Volter Bot"},
        {"name": "Fintech Bot"},
        {"name": "Pepper Bot"},
        {"name": "CloudBot"}
    ]
    bot_info = random_status(bot_info)
    invite_queue = queue.Queue()
    imp_queue = queue.Queue()
    imp_queue.put({"name":"Pretbot"})
    for info in bot_info:
        invite_queue.put(info)
    # sync task for invitation and special message.
    invite(invite_queue,imp_queue)
    imp_message(imp_queue)

if __name__ == "__main__":
    main()

```















































