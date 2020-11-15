import pika
import config
import os
import time
import sys
import json

counter = 0
subscribers = []

# configuration
url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange="caramail", exchange_type="direct")
# channel.basic_qos(prefetch_count=1)

result = channel.queue_declare(queue="", exclusive=False)
queue_name = result.method.queue  # get the reader specific queue name


channel.queue_bind(exchange="caramail", queue=queue_name, routing_key="presentation")


def callback(ch, method, properties, body):
    global counter
    global subscribers

    if method.consumer_tag in subscribers:
        subscribers.index(method.consumer_tag)
    else:
        subscribers.append(method.consumer_tag)

    counter = counter + 1
    print(" [x] Reveived %r" % body)
    print(" Route = %r" % method.routing_key)
    print(" Prop = %r" % json.dumps(properties.__dict__))
    print(" CH = %r" % ch)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print((" [*] Reading %r queue." % queue_name))
print((" [*] Waiting for messages. To exit press CTRL+C"))
# if(sleep != False):
#         print('Running with sleep mode with 5 sec timer')
channel.start_consuming()