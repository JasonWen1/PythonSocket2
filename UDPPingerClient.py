#UDPPingerClient.py
# Import necessary libraries
import time
from socket import *

# server address and port
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout to 1 second
clientSocket.settimeout(1)

# Initialize list to store RTTs
rtts = []

# Total number of pings
total_pings = 10
# Counter for lost packets
lost_packets = 0


# Send 10 pings to the server
for sequence_number in range(1, total_pings + 1):
    #create ping message with sequence number and current time
    message = f'Ping {sequence_number} {time.time()}'
    print(f"Sending message: {message}")
    try:
        #send ping message to server
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        #record the send time
        send_time = time.time()

        #attempt to receive message from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        #record the receive time
        receive_time = time.time()

        #calculate the round trip time
        rtt = receive_time - send_time
        rtts.append(rtt)
        print(f"Received reply from server: {modifiedMessage.decode()}")
        print(f"Round Trip Time (RTT): {rtt} seconds")
    except timeout:
        # Print message if request times out
        print("Request timed out")
        lost_packets += 1


# Calculate and print statistics
if rtts:
    min_rtt = min(rtts)
    max_rtt = max(rtts)
    avg_rtt = sum(rtts) / len(rtts)
    print(f"Min RTT: {min_rtt} seconds")
    print(f"Max RTT: {max_rtt} seconds")
    print(f"Average RTT: {avg_rtt} seconds")
else:
    print("No RTT available. All packets might be lost.")

# Calculate packet loss rate
packet_loss_rate = (lost_packets / total_pings) * 100
print(f"Packet loss rate: {packet_loss_rate}%")

# Close the client socket
clientSocket.close()



