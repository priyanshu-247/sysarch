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