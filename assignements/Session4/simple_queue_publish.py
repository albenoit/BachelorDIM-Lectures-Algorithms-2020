import pika
count=0
def simple_queue_publish(channel, connection,name_queue):
    '''
        publish all messages
        Parameters:
            channel, connection
        Returns:
            void
        Raises:
            no raise
    '''
    global count
    count +=1
    if (name_queue == 'task_queue'):
        exchange='logs'
    else:
        exchange=''
    channel.basic_publish(exchange=exchange,
                          routing_key=name_queue,
                          body='Hello World!',
                          properties=pika.BasicProperties(
                              delivery_mode = 2,
                          ))
    
    print(" [" + str(count) + "] Sent 'Hello World!'")
    connection.close()