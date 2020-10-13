# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:06:29 2020

@author: polletb
"""


def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

def read_queue(channel, connection):
    channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
    




