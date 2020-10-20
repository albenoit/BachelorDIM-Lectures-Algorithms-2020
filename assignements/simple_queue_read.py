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
    ch.basic_ack(delivery_tag=method.delivery_tag)
      

def read(channel, queue_name: str):
    '''
    Read all new messages
    
    Parameters:
        channel
    Return:
        void
    '''
    if queue_name == 'task_queue':
        channel.exchange_declare(exchange='logs',
                             exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        
        channel.queue_bind(exchange='logs',
                          queue=queue_name)
    
    channel.basic_consume(queue_name,
                          callback,
                          auto_ack=False)
    
    print(' [*] Waiting for messages:')
    channel.start_consuming()