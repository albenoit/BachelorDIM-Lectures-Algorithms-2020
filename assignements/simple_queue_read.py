# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:00:26 2020

@author: cuvellin
"""
count_read = 0

def callback(ch, method, properties, body):
    '''
    Show each message with incremental number
    
    Parameters:
        ch, method, properties, body
    Return:
        void
    '''
    global count_read
    count_read += 1
    print(" [" + str(count_read) +  "] Received " + str(body))
      

def read(channel):
    '''
    Read all new messages
    
    Parameters:
        channel
    Return:
        void
    '''
    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)
    
    print(' [*] Waiting for messages:')
    channel.start_consuming()