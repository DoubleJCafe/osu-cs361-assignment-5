import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to CS361 server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


print(f"Sending message 'A message from CS361'…")
socket.send(b"A message from CS361")

#  Get the reply.
message = socket.recv()
print(f"Received reply [ {message} ]")