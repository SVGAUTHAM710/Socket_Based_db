import socket
import mysql.connector

# connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ur_pass',
    database='database_name'
)
cursor = db.cursor()

# create socket
s = socket.socket()
host = 'localhost' # IP address of server
port = 12345 # choose a port number

# bind socket to host and port
s.bind((host, port))

# listen for incoming connections
s.listen(1)
print('Server listening on port', port)

while True:
    # accept incoming connection
    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        # receive data from client
        data = conn.recv(1024).decode()
        if not data:
            break
            
        # execute appropriate function based on client request
        tokens = data.split()
        if tokens[0] == 'create':
            table_name = tokens[1]
            cursor.execute(f'CREATE TABLE {table_name} (name VARCHAR(255), age INT, Id INT)')
            conn.send(f'Table \'{table_name}\' created successfully'.encode())
        elif tokens[0] == 'insert':
            table_name = tokens[1]
            name = tokens[2]
            age = tokens[3]
            Id= tokens[4]
            cursor.execute(f'INSERT INTO {table_name} (name, age, Id) VALUES (%s, %s, %s)', (name, age, Id))
            db.commit()
            conn.send('Data inserted successfully'.encode())
        elif tokens[0] == 'display':
            table_name = tokens[1]
            cursor.execute(f'SELECT * FROM {table_name}')
            rows = cursor.fetchall()
            for row in rows:
                conn.send(f'{row[0]}, {row[1]}, {row[2]}\n'.encode())
            
        elif tokens[0] == 'quit':
            break

    conn.close()
    print('Connection closed')
