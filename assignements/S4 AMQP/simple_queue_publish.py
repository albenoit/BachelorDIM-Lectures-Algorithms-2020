# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:03:45 2020

@author: vibertvg
"""


def simple_queue_publish(channel, connection): 
    """
    Function who write the messages and send it to queue
    Parameters:
        channel : channel to send
        Connetion: connect to queue
    Returns:
        return sending message hello world
    """
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
