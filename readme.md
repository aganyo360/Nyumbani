# TCP Server in C

## Header Files:

```c
#include <sys/socket.h>
#include <strings.h>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
```

These are the necessary header files for socket programming in C. They include definitions and functions related to sockets, strings, system types, input/output, and network-related structures.

### Main Function

    int main(int argc, char *argv[]) {

The main function takes command-line arguments: argc (argument count) and argv (argument vector)

### Command-line Argument Check:

<code>
    if(argc != 2){ <br>
    perror("check command-line arguments\n");<br>
    exit(1);<br>
}<br>
</code>

<p> Checks if the program is run with the correct number of command-line arguments. It expects one argument, the port number.
ignore this statement: also this part
</p>

## Socket Creation:

<code>
sockfd = socket(AF_INET, SOCK_STREAM, 0);
if(sockfd < 0){<br>
    perror("Tcp socket creation failure\n");<br>
    exit(1);<br>
}

</code>

<br>
Creates a TCP socket. If unsuccessful, an error message is printed, and the program exits.

## Socket Naming (Binding)

<code>portno = atoi(argv[1]);<br>
saddress.sin_family = AF_INET;<br>
saddress.sin_addr.s_addr = INADDR_ANY;<br>
saddress.sin_port = htons(portno);<br>

bnd = bind(sockfd, (struct sockaddr \*) &saddress, sizeof(saddress));<br>
if(bnd < 0){<br>
perror("created TCP socket binding failure\n");<br>
exit(1);<br>
}
</code>
<br>
Sets up the server address structure and binds the socket to the specified port. If the binding fails, an error message is printed, and the program exits.

#Listening for Clients:
<code>
listen(sockfd, 5);<br>
</code>
<br>
Listens for incoming client connections with a queue size of 5

## Accepting a Client Connection:

<code>
newsock = accept(sockfd, (struct sockaddr *) &caddress, &clientlen);
if(newsock < 0){<br>
    perror("accept failure\n");<br>
    exit(1);<br>
}
</code>
<br>
Accepts an incoming connection and creates a new socket (newsock) for communication with the connected client. If the acceptance fails, an error message is printed, and the program exits.

## Sending a Message to the Client:

<code>
send(newsock, "Just connected continue communicating", 50, 0);<br>

</code>
<br>

Sends a welcome message to the connected client.

## Communicating with the Client:

<code>
for(;;) {<br>
    bzero(buffer, sizeof(buffer));<br>
    recv(newsock, buffer, sizeof(buffer), 0);<br>
    printf("%s\n", buffer);<br>
    send(newsock, "The server has received your input\n", 50, 0);<br>
}

</code>
<br>
Enters an infinite loop to continuously receive messages from the client, print them, and send an acknowledgment back to the client.

Note: The bzero function is used to set the buffer to zero, and perror is used to print error messages associated with the last system call that set errno.
