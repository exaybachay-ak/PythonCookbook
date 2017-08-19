#basic sniffing
p = sniff(iface='eth1', timeout=10, count=5)

#sniffing with a filter
p = sniff(filter="tcp and (port 25 or port 110)")

#full packet cap mode
def packet_callback(packet):
    print packet.show()

sniff(filter='icmp', iface='eth1', prn=packet_callback, count=1)

#capture packets out to a pcap file
p = sniff(filter='icmp', iface='eth1', timeout=10, count=5,  prn = lambda x:x.summary())
wrpcap('packets.pcap', p)

#

