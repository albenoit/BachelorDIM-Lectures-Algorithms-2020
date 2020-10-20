import pika
import config
import os
import time

def simple_queue_publish(message, concurrency):
    '''
    Function to send message with CLOUDAMPQ
    Parameters :
        message: the message to sent,
        concurrency: parameter to set persistent message option
    '''
    #configuration
    url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    #connexion
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    if(concurrency == False):
        channel.basic_publish(exchange='logs',
                            routing_key='presentation',
                            body=message)
    else :
        i = 0
        while(i <= 50):
            message = 'Message %r envoyé' % i
            channel.basic_publish(exchange='logs',
                            routing_key='presentation',
                            body=message,
                            properties=pika.BasicProperties(
                                delivery_mode=2, #make persistent message
                            ))
            i = i + 1
            time.sleep(1)


    print(("  Sent %r" % message))
    connection.close()