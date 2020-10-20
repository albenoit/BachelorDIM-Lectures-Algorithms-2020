# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:53:05 2020

@author: cuvellin
"""
import pika

count_publish = 0
def publish(channel, queue_name: str):
    '''
    publish and show the message write in the body params with incremental number
    
    Parameters:
        channel
    Return:
        void
    '''
    global count_publish
    count_publish += 1 
    exchange=''
    if queue_name == 'task_queue':
        exchange='logs'
    
    channel.basic_publish(exchange=exchange,
                          routing_key=queue_name,
                          body='Hello Word!',
                          properties=pika.BasicProperties(
                                  delivery_mode = 2
                             )
                          )
    print(" [" + str(count_publish) + "] Sent 'Hello World !'")