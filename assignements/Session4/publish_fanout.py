import pika
import config
import os
import time

"""
Function to send message with fanout mode
"""
# configuration
url = os.environ.get("CLOUDAMQP_URL", config.amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

# connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange="posts", exchange_type="fanout")

ti = 1
while ti < 50:
    message = "Test d'envoi de message avec fanout exchange mode ==>%r" % ti
    channel.basic_publish(
        exchange="posts",
        routing_key="",
        body=message,
    )
    print((" Sent %r" % message))
    print((" Sent %reme message" % ti))
    ti = ti + 1
    time.sleep(5)


connection.close()