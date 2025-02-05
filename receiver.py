# import zmq

# context = zmq.Context()

# # create REQ socket to talk to server
# print("Connecting to server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555") # connect to server

# # Do 5 requests, waiting each time for a response
# for request in range(5):
#    print(f"Waiting for messages...")
#    socket.send(b"This is a message from CS361")

#     # Get the reply.
#    message = socket.recv()
#    print(f"Received message: {message.decode('utf-8')}")

import zmq

# Create a context for ZeroMQ
context = zmq.Context()

# Create a REP socket (Reply type)
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")  # Bind to port 5555

print("Waiting for message...")

while True:
    # Wait for a message from the sender
    message = socket.recv()
    print(f"Received message: {message.decode('utf-8')}")