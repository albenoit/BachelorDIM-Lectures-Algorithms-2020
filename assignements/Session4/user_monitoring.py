import pika
import config
import os
import time
import sys
import json

counter = 0
subscribers = []
descriptions = []

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
    global descriptions

    body = body.decode("utf-8")
    body = body.split(",")

    if body[0] in subscribers:
        descriptions[subscribers.index(body[0])].append(body[1])
    else:
        subscribers.append(body[0])
        descriptions.insert(subscribers.index(body[0]), [body[1]])

    counter = len(subscribers)
    print("Il y a %r utilisateurs dans le channel." % counter)

    if counter != 0:
        for i, user in enumerate(subscribers):
            print("-------------------------")
            print("Nom : %r" % user)
            print("Description : ")
            for desc in descriptions[i]:
                print(desc)
            print("")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print((" [*] Reading %r queue." % queue_name))
print((" [*] Waiting for messages. To exit press CTRL+C"))
# if(sleep != False):
#         print('Running with sleep mode with 5 sec timer')
channel.start_consuming()