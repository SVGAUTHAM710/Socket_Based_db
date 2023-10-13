# Socket-Based MySQL Database Operations

This repository contains a client-server system for performing basic MySQL database operations (create table, insert data, display data) using sockets in Python.

## Prerequisites

Make sure you have Python installed on your system and a MySQL server running locally or at the specified host.

## How to Run

1. Clone the repository.
2. Navigate to the project directory in your terminal or command prompt.

### Server Side

1. Modify the server code (`server.py`) with your MySQL database credentials (host, user, password, database_name).
2. Run the server code:

    ```sh
    python server.py
    ```

### Client Side

1. Run the client code (`client.py`):

    ```sh
    python client.py
    ```

## Usage

The client-side script provides a simple user interface for creating tables, inserting data, displaying data, and quitting the program. The server-side script handles the incoming requests and performs the corresponding database operations.

## Files

- **client.py**: Client-side script for interacting with the server.
- **server.py**: Server-side script for handling client requests and database operations.

## Database Operations

- **Create Table**: Creates a table in the specified database.
- **Insert Data**: Inserts a new record into the specified table.
- **Display Data**: Retrieves and displays all records from the specified table.

## Author

S.V.GAUTHAM

Contact: gauthamsv924@gmail.com

