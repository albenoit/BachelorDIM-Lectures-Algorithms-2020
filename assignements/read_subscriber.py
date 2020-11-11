# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:55:46 2020

@author: tapiev
"""

import pika 
    

f = open("P:\\Git_algo\key.txt", "r")
connec_string =f.read()
f.close()
messagetext ="yo"

connection = pika.BlockingConnection(pika.URLParameters(connec_string))
channel=connection.channel()

channel.exchange_declare(exchange='logs',
                          exchange_type='fanout')
result = channel.queue_declare(queue='',exclusive = True)


connection.close()
