# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pika 
f = open("P:\\Git_algo\key.txt", "r")
connec_string =f.read()
f.close()

connection = pika.BlockingConnection(pika.URLParameters(connec_string))
channel=connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! ça marche ou pas ?')
print("[x] Sent 'Hello World'")
connection.close()
