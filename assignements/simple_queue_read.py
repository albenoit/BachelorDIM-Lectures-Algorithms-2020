# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:00:26 2020

@author: cuvellin
"""
count = 0

def callback(ch, method, properties, body):
    global count
    count += 1
    print(" [" + str(count) +  "] Received " + str(body))
      

def read(channel):
    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)
    
    print(' [*] Waiting for messages:')
    channel.start_consuming()