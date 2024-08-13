import socket as sk

s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
ip_address = "127.0.0.1"
port_no = 2525
address = (ip_address,port_no)

s.bind(address)

while True:
    Data = s.recvfrom(100)
    message = Data[0]
    ip_address = Data[1][0]
    print(ip_address," >>>>>>> ", message)




#     import socket as sk

# s=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
# ip_address = "127.0.0.1"
# port_no = 2525
# address = (ip_address,port_no)

# s.bind(address)

# while True:
#     message =s.recvfrom(100)
#     print(message)
