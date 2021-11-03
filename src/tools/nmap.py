import socket, sys, time, subprocess

__version__ = "1.0"

ports = {
		20:	"/tcp",
		21:	"/tcp",
		22:	"/tcp",
		23:	"/tcp",
		25:	"/tcp",
		50:	"/",
		51:	"/",
		53:	"/tcp",
		67:	"/upd",
		68:	"/upd",
		69:	"/upd",
		80:	"/tcp",
		110: "/tcp",
		119: "/tcp",
		123: "/upd",
		135: "/tcp",
		139: "/tcp",
		143: "/tcp",
		161: "/tcp",
		162: "/tcp",
		389: "/tcp",
		443: "/tcp",
		989: "/tcp",
		990: "/tcp",
		3389: "/tcp"
}

ports_service = {
		20:	"ftp",
		21:	"ftp",
		22:	"ssh",
		23:	"telnet",
		25:	"smtp",
		50:	"ipsec",
		51:	"ipsec",
		53:	"dns",
		67:	"dhcp",
		68:	"dhcp",
		69:	"tftp",
		80:	"http",
		110: "pop3",
		119: "nntp",
		123: "ntp",
		135: "netbios",
		139: "netbios",
		143: "imap4",
		161: "snmp",
		162: "snmp",
		389: "ldap",
		443: "https",
		989: "ftp",
		990: "ftp",
		3389: "rdp"
}

def get_ping(host):
	p = subprocess.Popen(["ping", "-n", "1", host], stdout=subprocess.PIPE)
	out, err = p.communicate()
	out = out.decode()
	split_out = out.split(" ")
	ping = split_out[-1].strip().replace("ms", "")
	return int(ping)/1000

def nmap(host):
	w_ports = []
	hosts_up = []
	ip_a = []
	socket.setdefaulttimeout(0.01)

	print(f"Starting Nmap {__version__}")
	try:
		host_ip = socket.gethostbyname(host)
		status = "up"
		hosts_up.append(host)
		ip_a.append(host_ip)
		print(f"Nmap scan report for {host} ({host_ip})")
		latency = get_ping(host)
		print(f"Host is {status} ({latency}s latency).")
		
	except socket.error:
		host_ip = None
		status = "down"
		print(f"Failed to resolve '{host}'.")

	start = time.time()
	if not host_ip == None:
		for port in ports:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(0.2)
				s.connect((host, port))
				w_ports.append(port)
				s.close()
			except:
				pass

		if len(w_ports) > 0:
			not_shown_p = len(ports) - len(w_ports)
			print(f"Not shown: {not_shown_p} closed port")
			print("PORT       STATE SERVICE")
			for p in w_ports:
				print(f"{p}{ports.get(p)}{' '*(len('PORT       ') - len(str(p) + ports.get(p)))}{'open' if p in w_ports else 'close'}{' '*(len('STATE ') - len(str('open' if p in w_ports else 'close')))}{ports_service.get(p)}")
			print()
		else:
			pass
	else:
		pass

	end = time.time()

	print(f"Nmap done: {len(ip_a)} IP addresses ({len(hosts_up)} host up) scanned in {round((end - start), 2)} seconds")