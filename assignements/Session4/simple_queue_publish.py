import pika
import config
import os

def simple_queue_publish(message, concurrency):
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
    if(concurrency == False):
        channel.basic_publish(exchange='',
                            routing_key='presentation',
                            body=message)
    else :
        i = 0
        while(i <= 50):
            message = 'Message %r envoyé' % i
            channel.basic_publish(exchange='',
                            routing_key='presentation',
                            body=message,
                            properties=pika.BasicProperties(
                                delivery_mode=2, #makepersistent message
                            ))
            i = i + 1

    print(("  Sent %r" % message))
    connection.close()