import argparse
import pika
import os
import config, simple_queue_publish as publish, simple_queue_read as read

parser = argparse.ArgumentParser()
parser.add_argument('-read','-r', action='store_true')
parser.add_argument('-message', '-m', type=str)
parser.add_argument('-concurrency', action='store_true')

args = parser.parse_args()

if args.read == False:
    if args.message:
        print('Sender mode')
        print('Connexion and send in progress...')
        publish.simple_queue_publish(args.message, concurrency = args.concurrency)
    else:
        print('Aucun message passé en paramètre. Action annulée.')
else:
    print('Reader mode')
    print('Connexion in progress...')
    read.simple_queue_read(concurrency = args.concurrency)