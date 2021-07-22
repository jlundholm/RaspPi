#Fletcher Wadsworth
#Tello drone keyboard control with sockets, template

#Import necessary libraries
import socket
import threading
import time

#Define send function for sending messages to Tello
def send(message):
    #Try sending message, otherwise print exception
    try:
        sock.sendto(message.encode(), tello_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

#Define receive function for receiving messages from Tello
def receive():
    #continuously monitor for incoming messages
    while True:
        #Try receiving message, otherwise print exception
        try:
            response, ip_address = sock.recvfrom(128)
            print("Received message: " + response.decode(encoding='utf-8'))
        except Exception as e:
            sock.close()
            print("Error receiving: " + str(e))
            break
        
#Create tuples for local and tello IP addresses and ports
tello_address = ('192.168.10.1', 8889)
local_address = ('', 9000)
#Create and bind local UDP socket for communication with tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Insert line to bind socket to local address


#Create and begin thread for listening for incoming Tello messages.
#Thread runs in background and continuously listens for datagrams
recvThread = threading.Thread(target=receive)
recvThread.daemon=True
#Insert line to start receiving thread



if __name__ == '__main__':
    #Insert line which prints user instruction to shell
    
    while True:
        #try to send inputs, except for Ctl-C keyboard interrupt
        try:
            #Insert line to obtain message from user input at the shell
            
            
            if 'quit' in message:
                #Insert line to print message indicating program exit
                
                #Insert line to instruct Tello to land
                
                #Insert line to close socket 
                
                #Break from while loop
                break
            #Insert line to send the command from the user
            
            
        except KeyboardInterrupt as e:
            print("Keyboard interrupt! Exiting program!")
            sock.close()
            break
