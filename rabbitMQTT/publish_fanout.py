# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:53:22 2020

@author: fuchsca
"""

# -*- coding: utf-8 -*-
#!/usr/bin/en python
import pika
import os
import config
import argparse

"""
Created on Tue Oct 13 13:47:56 2020

@author: fuchsca
"""

parser = argparse.ArgumentParser(description = 'Currency')
parser.add_argument('-concurrency');
url = os.environ.get('CLOUDAMQP_URL',config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 600

connection = pika.BlockingConnection(params) # Connect to CloudAMQPchannel = connection.channel()
channel = connection.channel()
nomMessage = "task_queue"
#corpsmessage = input('Entrez un message : ')
corpsmessage = 'TestMessage'

channel.exchange_declare(exchange='logs',exchange_type='fanout')

for i in range(1,10) :
    
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=corpsmessage,
                          properties=pika.BasicProperties(delivery_mode = 2,) # make message persistent
                        )
    print(" [X] Sent " + corpsmessage)


connection.close()