# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:47:52 2020

@author: derbaghc
"""

"""
import config
import pika 
import os 

url = os.environ.get('CLOUDAMQP_url', config.keyAMQP)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(pika.URLParameters(config.keyAMQP))
channel = connection.channel()
"""
import pika 

'''
Fonction qui envoie un message à un exchange
params : channel, queueName, connection 
return : print le message envoyé 
'''
def publish(channel, queueName, connection):
    channel.basic_publish(exchange='logs', 
                          routing_key='',
                          body='Hello World',
                          properties=pika.BasicProperties(
                                  delivery_mode = 2 
                          ))
    print(" [X] Sent 'Hello World!'")
    connection.close()

'''
Fonction qui envoie un message à une queue en divisant les tâches 
params : channel, queueName, connection
return : print le message envoyé
'''
'''
def publish(channel, queueName, connection):
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body='Hello World',
                          properties=pika.BasicProperties(
                              delivery_mode=2
                          ))
    print(" [X] Sent 'Hello World!'")
    connection.close()
'''
