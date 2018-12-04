
import pika
import sys

url = 'amqp://debzppsy:Kg2KfgbHxvTEztQxWkelEx5sH8jnIMDW@toad.rmq.cloudamqp.com/debzppsy'
connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()

#emit a log with a routing key "Server1.error" type:

# python emit_log_topic.py "Server1.error" "An error message from server1"