# Lee Haynes
# Phone: + 44 (0) 785 374 0636
# Email: LeeHaynes2019@yandex.com
# Website: http: // www.devcoder.me.uk/
# Instagram: junior_web_developer_2020
# Devcoder Youtube: https: // www.youtube.com/channel/UCXqnASrfdoRlyt82YR7n7pQ?view_as
# Lee Haynes Youtube: https: // www.youtube.com/channel/UCjqLeiVDygmpCHXyeDzH04g

import socket

host = "localhost"
port = 8080

# IPV 4 = AF_INET and TCP Connection = SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The connection "MUST" be in a tuple, "OR" an error will be thrown
s.connect((host, port))

# creating a variable to receive the message
# 1024 is the byte size of the file, the maximum file size
message = s.recv(1024)

# setting ap a loop to stay cennocted whilst message is being erceived
while message:

    # whsilt the message is being received, decode it "AND" store it in the varailble message
    print("Message:", message.decode())
    message = s.recv(1024)
s.close()
