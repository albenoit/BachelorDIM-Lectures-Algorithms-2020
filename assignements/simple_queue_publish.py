# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pika 
import argparse
    
parser = argparse.ArgumentParser()
parser.add_argument('-m')
parser.add_argument('-concurrency', action='store_true')
args = parser.parse_args()

message = args.m
concurencebool = args.concurrency

f = open("P:\\Git_algo\key.txt", "r")
connec_string =f.read()
f.close()
messagetext = "hello"
if message != "" and message != None :
    messagetext = message

connection = pika.BlockingConnection(pika.URLParameters(connec_string))
channel=connection.channel()
channel.queue_declare(queue='hello')
if concurencebool :
     channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(messagetext),
                      properties=pika.BasicProperties(delivery_mode=2))
     print("la concu est dure ")
else:
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=str(messagetext))
print("[x] Sent "+str(messagetext))
connection.close()
