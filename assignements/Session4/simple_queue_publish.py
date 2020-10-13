def simple_queue_publish(channel, connection):    
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

    print(" [x] Sent 'Hello World!'")