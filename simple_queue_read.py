# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:06:29 2020

@author: polletb
"""

from decouple import config 

AMQP_URL = config('AMQP_URL')