import rsa
import sys
import logging
import time
import stomp
import psycopg2

# COnnect to database
# Connect to queue
# Read encrypted message
# Decrypt
# Create vote item and put into database

# Database model
# Vote
#   date/time
#   email
#   name
#   postcode
#   ElectionID
#   candiateselected

#class MyListener(stomp.ConnectionListener):
class MyListener(object):
    def __init__(self,con):
        self.conn = conn
        self.count = 0
        self.start = time.time()

    def on_error(self, message):
        print('received an error "%s"' % message)

    def on_message(self, message):
        print('received a message "%s"' % message)
        sql=

pgconn = psycopg2.connect(
    host="localhost",
    database="votes",
    user="votes",
    password="votes")

hosts = [('localhost', 61613)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener(conn))
conn.connect('votes', 'votes', wait=True)
conn.subscribe('votes', 123)
print("Waiting for messages...")
while 1:
    time.sleep(10)



