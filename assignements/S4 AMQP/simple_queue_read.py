# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:14:44 2020

@author: vibertvg
"""
count = 0

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))
  global count
  count = count +1
  print(count)


def simple_queue_read(channel, connection):
    channel.basic_consume('hello',
                      on_message_callback=callback,
                      auto_ack=True)
    print(' [*] Waiting for messages:')
    channel.start_consuming()
    