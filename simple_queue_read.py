# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:06:29 2020

@author: polletb
"""
compteur = 0

def callback(ch, method, properties, body):
  global compteur
  print(" [" + str(compteur) + "] Received " + str(body))
  compteur = compteur + 1


def read_queue(channel):
    channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

    print(' [*] Waiting for messages:')
    channel.start_consuming()




