# import zmq

# context = zmq.Context()

# #
# #  create REQ socket to talk to server
# print("Connecting to server…")
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555") # connect to server

#  #Do 5 requests, waiting each time for a response
# for request in range(5):
#    print(f"Waiting for messages...")
#    socket.send(b"This is a message from CS361")

#     # Get the reply.
#    message = socket.recv()
#    print(f"Received message: {message}")

# import zmq
# context = zmq.Context()

# # create a REQ socket
# socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:5555")

# # send message to the server
# message = "This is a message from CS361"
# print(f"Sending message: {message}")
# socket.send(message.encode('utf-8'))

# # receive the response from the server
# response = socket.recv()
# print(f"Recived response: {response.decode('utf-8')}")

import zmq

context = zmq.Context()

# create a REQ socket 
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # connect to the receiver 

message = "This is a message from CS361"
print(f"Sending message: {message}")

# send the message to the receiver
socket.send(message.encode('utf-8'))  # Encode the string to bytes before sending

# wait for the response from the receiver
response = socket.recv()
print(f"Received response: {response.decode('utf-8')}")