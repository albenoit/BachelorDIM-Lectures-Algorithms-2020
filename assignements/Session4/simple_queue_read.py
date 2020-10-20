import pika
import config
import os
import time

counter = 0

def simple_queue_read(concurrency, sleep):
    '''
    Function to received and print in console 
    some message with CLOUDAMPQ
    Parameters:
        concurrency: parameter to set acknowledging
    '''

    #configuration
    url = os.environ.get('CLOUDAMQP_URL', config.amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    #connexion
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')

    def callback(ch, method, properties, body):
        global counter
        counter = counter + 1
        print(" [x] Reveived %r" % body)
        print('%r messages received' % counter)
        if(concurrency != False):
            print(' [x] Message Processed, acnowledging (to delete message from the queue)')
            ch.basic_ack(delivery_tag= method.delivery_tag)
        
        if(sleep != False):
            time.sleep(5)
        

    channel.basic_consume(queue='presentation', on_message_callback=callback, auto_ack=False)

    print((" [*] Waiting for messages. To exit press CTRL+C"))
    if(sleep != False):
            print('Running with sleep mode with 5 sec timer')
    channel.start_consuming()