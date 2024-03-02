## Explanation

### Header Files:

The code includes necessary header files for socket programming (sys/socket.h, netinet/in.h, arpa/inet.h) and other standard input/output operations (stdio.h, stdlib.h, strings.h).

### Main Function:

The main function is the entry point of the program.

### Command Line Arguments:

It checks if the correct number of command-line arguments (server IP and port number) is provided. If not, it displays an error message and exits.

### Socket Creation:

It creates a TCP socket using the socket function. If the creation fails, it prints an error message and exits.

### Socket Addressing:

The server's IP address and port number are set in the saddress structure.

### Connection to Server:

It connects to the server using the connect function. If the connection fails, it prints an error message and exits.

### Receiving Initial Message:

It receives an initial message from the server and prints it.

### Communication Loop:

It enters a loop where the client can input messages, send them to the server, and receive and print responses from the server.
