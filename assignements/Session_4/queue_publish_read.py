import argparse
import amqpURL
import pika
import os

parser= argparse.ArgumentParser(description="How to")
parser.add_argument('-read', action='store_true')
flags = parser.parse_args()

#Test pour savoir le type d'exucution à effectuer
if flags.read:
    exec(open("simple_queue_read.py").read())
else:
    exec(open("simple_queue_publisher.py").read())
