#Fletcher Wadsworth, June 2021
#ESP4T basic Tello flight with sockets, template

#Import socket library to communicate with Tello via UDP
import socket
#Import threading library to run separate 'receive' thread
import threading
#Import time module for delays
import time

#Function to send instruction to Tello and delay
def send(message,delay):
    #Try to send message, otherwise print exception
    try:
        #Insert line to send encoded message to Tello address
        
        #Insert line to print the sent message
        
    except Exception as e:
        print("Error sending: " + str(e))
        
    #Insert line to create delay for time (in seconds) passed to function by user
    
    
#Function for receiving message from Tello
def receive():
    #Continuously loop and listen for incoming messages
    while True:
        #Try to receive message, otherwise print exception
        try:
            response, ip_address = sock.recvfrom(128)
            print("Received message: " + response.decode(encoding='utf-8'))
        except Exception as e:
            print("Error receiving: " + str(e))
            break
    
#Define the network socket and create a thread for receiving UDP messages    
#IP and port of Tello (values set by the manufacturer)
tello_address = ('192.168.10.1', 8889)
#IP and port of local machine
local_address = ('', 9000)
#Create socket object for UDP connection between local machine and Tello
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Insert line to bind socket to local address and port


#Create and start a listening thread that runs in the background
#Thread uses 'receive()' function and continuously monitors for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
#Insert line to start listening thread


if __name__ == '__main__':
    """Main function. See provided documentation on Tello command
       syntax. Specify adqeuate delays to ensure commands are fully
       before another is sent."""
    #Insert line to set Tello to command mode
    
    #Insert line to check battery level
    
    #Insert line to command Tello to take off (>= 5 second delay)
    
    #Insert lines to create custom mission. 



    #Insert line to land the tello
    
    #Print message signaling end of mission
    print("Mission completed successfully")
    #Close socket before script is terminated
    sock.close()