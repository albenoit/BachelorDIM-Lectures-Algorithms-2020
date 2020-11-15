import argparse
import pika
import os
import config
import time
import sys
import json

"""
    File to connect, read adn response in rpc_queue some message with CLOUDAMPQ
    Methods:
        on_request: callback method on receive message. Send response to the server with correlation_id
"""
# configuration
url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="rpc_queue")


def on_request(ch, method, props, body):

    print(" [*] Received request ==> %r" % body.decode("utf-8"))
    response = "Fine and you?"

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
