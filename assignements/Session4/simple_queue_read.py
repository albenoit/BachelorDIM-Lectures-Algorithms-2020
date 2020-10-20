count=0
def callback(ch, method, properties, body):
  '''
        show each message
        Parameters:
            ch, method, properties, body
        Returns:
            void
        Raises:
            no raise
    '''
  global count
  count +=1
  print(" [" + str(count) +"] Received " + str(body))
  ch.basic_ack(delivery_tag = method.delivery_tag)


def simple_queue_read(channel, connection,name_queue):
  '''
        read all messages
        Parameters:
            channel, connection
        Returns:
            void
        Raises:
            no raise
  '''
  
  if(name_queue== 'task_queue'):
    channel.exchange_declare(exchange='logs',
                            exchange_type='fanout')
    result = channel.queue_declare(queue='',exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs',queue=queue_name)
  channel.basic_consume(name_queue,
                    on_message_callback=callback,
                    auto_ack=False)
  print(' [*] Waiting for messages:')
  channel.start_consuming()