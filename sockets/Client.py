import socket  # Import socket module

s = socket.socket()  # Create a socket object
  # Get local machine name
port = 6969  # Reserve a port for your service.

s.connect(('192.168.56.1', port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
