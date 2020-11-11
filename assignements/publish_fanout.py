# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:37:03 2020

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
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=str(messagetext))

connection.close()
