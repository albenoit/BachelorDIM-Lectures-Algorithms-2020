import argparse
import pika
import os
import config
import time
import sys
import json

"""
    File to connect and publish some message with CLOUDAMPQ
    Arguments:
        -read: parameter to switch in reader mode
        -message: parameter to add the message to publish in publish mode
        -concurrency: parameter to set persitent mode in publish mode 
                    and acknowledging in read mode
    """

counter = 0
subscribers = []

parser = argparse.ArgumentParser()
parser.add_argument("-signin", action="store_true")
parser.add_argument("-read", "-r", action="store_true")
parser.add_argument("-message", "-m", type=str)
parser.add_argument("-user", "-u", type=str)

args = parser.parse_args()

# configuration
url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange="caramail", exchange_type="direct")

user = args.user if args.user else connection.close()


def callback(ch, method, properties, body):
    global counter
    global subscribers

    counter = counter + 1
    print(" [x] Reveived %r" % body)
    print(" Route = %r" % method.routing_key)
    print(" Prop = %r" % json.dumps(method.__dict__))
    print(" CH = %r" % ch)


if args.signin:
    message = input("Enter your presentation :")
    message = args.user + "," + message
    channel.basic_publish(
        exchange="caramail",
        routing_key="presentation",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make persistent message
        ),
    )
elif args.read == False:
    if args.message:
        message = args.user + "," + args.message
        channel.basic_publish(
            exchange="caramail",
            routing_key="posts",
            body=message.encode("utf-8"),
        )
    else:
        print("Aucun message passé en paramètre. Action annulée.")

else:
    result = channel.queue_declare(queue="", exclusive=False)
    queue_name = result.method.queue  # get the reader specific queue name

    channel.queue_bind(exchange="caramail", queue=queue_name, routing_key="posts")

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=False
    )
    print(queue_name)
    print((" [*] Reading %r queue." % queue_name))
    print((" [*] Waiting for messages. To exit press CTRL+C"))
    # if(sleep != False):
    #         print('Running with sleep mode with 5 sec timer')
    channel.start_consuming()


connection.close()