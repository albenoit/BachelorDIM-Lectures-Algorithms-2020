# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:52:37 2020

@author: polletb
"""

def publish_queue(channel, connection):    
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    
    print(" [x] Sent 'Hello World!'")
    

#publish_queue()