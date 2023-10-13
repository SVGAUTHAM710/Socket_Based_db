import socket

# create socket
s = socket.socket()
host = 'localhost' # IP address of server
port = 12345 # choose the same port number as in the server code

# connect to server
s.connect((host, port))



while True:
    # display user interface
    print('1. Create table\n2. Insert data\n3. Display data\n4. Quit')
    choice = input('Enter choice: ')
    
    # execute appropriate function based on user choice
    if choice == '1':
        table_name = input('Enter table name: ')
        s.send(('create ' + table_name).encode())
        print(s.recv(1024).decode())
    elif choice == '2':
        table_name = input('Enter table name: ')
        name = input('Enter name: ')
        age = input('Enter age: ')
        Id = input('enter id: ')
        
        s.send(('insert ' + table_name + ' ' + name + ' ' + age + ' ' + Id).encode())
        print(s.recv(1024).decode())
    elif choice == '3':
        table_name = input('Enter table name: ')
        s.send(('display ' + table_name).encode())
        data = s.recv(1024).decode()
        while data:
            print(data)
            data = s.recv(1024).decode()
    elif choice == '4':
        s.send('quit'.encode())
        break
    else:
        print('Invalid choice')
        
s.close()
