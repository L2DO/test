import socket 

def main():
    udp_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_sock.bind(("",8899))
    recv_data = udp_sock.recvfrom(1024)
    udp_sock.sendto(recv_data,("",7788))


def print():
    print("new line")


if __name__ == "__main__":
    main()
