# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:56:30 2020

@author: polletb
"""
import time
sleep = None

def callback(ch, method, properties, body):
    '''
    Callback for read message
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
    '''
    print(" [" + str(method.delivery_tag) + "] Received " + str(body))
    if sleep:
        time.sleep(2)

def read_queue_fanout(channel, queueName:str, sleepValue:str):
    '''
    Read RabbitMQ Advanced Message Queuing with Pika
    Parameters:
            check official documentation : https://pika.readthedocs.io/en/stable/
            queueName: str
            sleep: str
    '''
    global sleep
    if sleepValue:
        sleep = True
    channel.basic_consume(callback,
                      queue=queueName,
                      no_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()