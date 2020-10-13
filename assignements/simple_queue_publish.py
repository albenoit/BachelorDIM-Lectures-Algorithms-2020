# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:53:05 2020

@author: cuvellin
"""


def publish(channel):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello Word!')
    print(" [x] Sent 'Hello World !'")
