# import socket as sk

# s = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

# target_ip = "127.0.0.1"
# port_no = 2525
# target_address = (target_ip, port_no)

# quiet = True
# while True:
#     message = input("Enter a message:")
#     message_encrypt = message.encode('ascii')
#     user_input = input("Dont want to send ")
#     if user_input == "Y" or user_input == "y":
#         quiet = False
#     else: 
#         s.sendto(message_encrypt, target_address)

        





import socket as sk

s = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)

target_ip = "127.0.0.1"
port_no = 2525


target_address = (target_ip, port_no)

quiet = True
while True:
    message = input("Enter a message:")
    message_encrypt = message.encode('ascii')
    s.sendto(message_encrypt, target_address)

    user_input = input("message should not be sent")

    if user_input == "Y" or user_input == "y":
       break





