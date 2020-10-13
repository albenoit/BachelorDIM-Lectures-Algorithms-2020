# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika

"""
Created on Tue Oct 13 13:55:37 2020

@author: fuchsca
"""


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')