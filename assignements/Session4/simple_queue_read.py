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
  print(" [x] Received " + str(body))
  ch.basic_ack(delivery_tag = method.delivery_tag)


def simple_queue_read(channel, connection):
  '''
        read all messages
        Parameters:
            channel, connection
        Returns:
            void
        Raises:
            no raise
  '''
  channel.basic_consume('hello',
                    on_message_callback=callback,
                    auto_ack=False)
  print(' [*] Waiting for messages:')
  channel.start_consuming()