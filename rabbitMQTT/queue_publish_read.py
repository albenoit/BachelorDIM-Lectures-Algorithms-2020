# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika
import os
import config
import argparse


"""
Created on Tue Oct 13 13:55:37 2020

@author: fuchsca
"""

parser = argparse.ArgumentParser(description = 'How to')
parser.add_argument('-read',action='state_true()')
parser.add_argument('-concurrency');
FLAGS = parser.parse_args();
print('flags');


#Connecting

url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQPchannel = connection.channel()
channel = connection.channel()

#Sending

nomMessage = "MonMessage"
corpsmessage = "je mange un poisson"
channel.queue_declare(queue=nomMessage)
channel.basic_publish(exchange='',
                      routing_key=nomMessage,
                      body=corpsmessage)
print(" [X] Sent " + corpsmessage)

#Reception
counter = 0
def callback(ch, method, properties,body) :
    
    
    global counter
    counter = counter + 1
    
    print(" [X] Received %r" %body + "il y a eu %r messages" %counter)
    
channel.basic_consume(queue=nomMessage,
                      on_message_callback=callback,
                      auto_ack=True)

#res = channel.queue_declare(
#        callback=on_callback,
#        queue=nomMessage,
#        durable=True,
#        exclusive=False,
#        auto_delete=False,
#        passive=True)
#
#print ("Messages in queue %r" (res.method.message_count))

print("il y a eu %r messages" %counter)
print(' [*] Waiting for messages. To Exit press CTRL + C')
channel.start_consuming()

connection.close()




