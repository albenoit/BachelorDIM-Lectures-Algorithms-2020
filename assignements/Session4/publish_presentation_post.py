import argparse
import pika
import os
import config
import time

"""
    File to connect and publish some message with CLOUDAMPQ
    Arguments:
        -read: parameter to switch in reader mode
        -message: parameter to add the message to publish in publish mode
        -concurrency: parameter to set persitent mode in publish mode 
                    and acknowledging in read mode
    """

parser = argparse.ArgumentParser()
parser.add_argument("-signin", action="store_true")

args = parser.parse_args()

# configuration
url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange="caramail", exchange_type="topic")


if args.signin:
    message = input("Enter your presentation :")
    channel.basic_publish(
        exchange="caramail",
        routing_key="presentation",
        body=message,
    )
else:
    message = input("Enter your message :")
    channel.basic_publish(
        exchange="caramail",
        routing_key="posts",
        body=message,
    )

connection.close()