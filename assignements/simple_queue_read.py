# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:56:03 2020

@author: tapiev
"""

import pika 



count = 0
f = open("P:\\Git_algo\key.txt", "r")
connec_string = f.read()
print(connec_string)
connection = pika.BlockingConnection(pika.URLParameters(connec_string))
channel=connection.channel()
channel.queue_declare(queue='gigadurable',durable=True)
channel.basic_qos(prefetch_count=1)
def callback(ch,method,properties,body):
    print(" [x] Received %r" % body)
    global count
    count +=1
    print("number of received event : " + str(count))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

channel.basic_consume(queue='gigadurable',
                      on_message_callback = callback,
                      auto_ack=False)
print(' [*] Waiting for messages. o exit press CTRL+C')
channel.start_consuming()