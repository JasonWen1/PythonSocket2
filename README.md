# PythonSocket2

Run method:
First start server using command 'python3 ./UDPPingerServer.py'
Then start client using command 'python3 ./UDPPingerServer.py'

Description:
In the UDPPingerClinet.py, it can generate the message first,
the format is 'Ping sequence_number time', sequence_number 
is the number of the ping request, from 1 to 10.
After sending requests to server, server will maybe response to 
client. There is a timeout detaction. The limit is 1second.
If the client receive the message from server in 1s, then print
the message from server and calculate rtt and print, otherwise print "Request timed out".

Optional(Bonus) part description:
In the client code, I use list 'rtts' to clollect every successful request rtt.
If the reuqest is timeout, lost_packets will increase 1.
So we can easily calculate min, max, average rtt, and packet loss rate.

Dependency
Just use socket and time, which don't need download by ourselves.

TroubleShooting
No trouble at all. LOL~~~