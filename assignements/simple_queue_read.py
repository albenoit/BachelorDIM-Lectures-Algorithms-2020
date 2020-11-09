# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:00:26 2020

@author: cuvellin
"""

import time

count_read = 0


#  https://stackoverflow.com/questions/57989692/how-can-i-pass-arbitrary-args-to-a-callback-function-in-rabbitmq
def callback_with_sleep(time_sleep=0):
    def callback(ch, method, properties, body):
        """
        Show each message with incremental number

        Parameters:
            ch, method, properties, body
        Return:
            void
        """
        global count_read
        count_read += 1
        print(" [" + str(count_read) + "] Received " + str(body))
        time.sleep(time_sleep)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    return callback


def read(channel, queue_name: str, time_sleep=0):
    """
    Read all new messages

    Parameters:
        channel
        queue_name
        time_sleep
    Return:
        void
    """
    if queue_name == 'task_queue':
        channel.exchange_declare(exchange='logs',
                                 exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='logs',
                           queue=queue_name)

    channel.basic_consume(queue_name,
                          callback_with_sleep(time_sleep),
                          auto_ack=False)

    print(' [*] Waiting for messages:')
    channel.start_consuming()
