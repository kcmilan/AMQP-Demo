#!/usr/bin/env python
import pika

url = 'amqp://debzppsy:Kg2KfgbHxvTEztQxWkelEx5sH8jnIMDW@toad.rmq.cloudamqp.com/debzppsy'
connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()