# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika

"""
Created on Tue Oct 13 13:47:56 2020

@author: fuchsca
"""

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                              rounting_key='hello',
                              body='Hello World!')
print(" [X] Sent 'Hello World!'")
connection.close()