# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:06:29 2020

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


def read_queue(channel, queueName:str, sleepValue:str):
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
    channel.basic_consume(queueName,
                      callback,
                      auto_ack=False)

    print(' [*] Waiting for messages:')
    channel.start_consuming()




