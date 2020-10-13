import pika
import os
import keys

def sendMessage(message):
    url = os.environ.get('CLOUDAMQP_URL', keys.amqpkey)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    try:
        message
    except NameError:
        message = "Hello World!"

    # publish
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    channel.basic_publish(exchange='',
        routing_key='presentation',
        body=message)

    for i in range(0, 230):
        channel.basic_publish(exchange='',
        routing_key='presentation',
        body=message)

    print(" [X] Send '"+message+"'")
    connection.close()