import pika
import config
import os

def simple_queue_publish(message):
    '''
    Function to send message with CLOUDAMPQ
    Parameters :
        message: the message to sent
    '''
    #configuration
    url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    #connexion
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    channel.basic_publish(exchange='',
                            routing_key='presentation',
                            body=message)

    print(("  Sent %r" % message))
    connection.close()