# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:48:25 2020

@author: derbaghc
"""
"""
import config
import pika
import os


url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
"""

'''
Fonction qui se lance à la réception d'un message et qui stocke le message pour éviter les pertes
params : ch (channel), method, properties, body
return : stocke le message  
'''
def callback(ch, method, properties, body):
    print(" [X] Received %r" %body)
    # TODO process the message
    print(" [X] Message Processed, acknowledging (to delete message from the queue)")
    ch.basic_ack(delivery_tag = method.delivery_tag)


'''
Fonction qui attend l'arrivée des messages (consumer)
params : channel, queueName
return : print l'attente des messages
'''
def consume(channel, queueName):
    channel.basic_consume(queue=queueName,
                          on_message_callback=callback,
                          auto_ack=False)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()