# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:45:06 2020

@author: ceriatik
"""

import pika
import myKeysCloudAMQP
import os

amqp_url= myKeysCloudAMQP.cloud_amqp_key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)

count = 0
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_qos(prefetch_count=1)

"""
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)
"""

def callback (ch, method, properties, body):
    print("[x] Received %r" % body)
    global count
    count += 1
    print("[x] Message Processed, acknowledging (o delete message from the queue)")

channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
channel.start_consuming()
