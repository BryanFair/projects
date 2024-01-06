import sys
from scapy import *
from scapy.layers.inet import *
from scapy.all import sendp


MacAdd = str(sys.argv[1] + " ") #mac address of target 
#could be a better way to determine or add the space


ETHER_BROADCAST = "ff:ff:ff:ff:ff:ff " 
MultiMac = MacAdd *16
Content = ETHER_BROADCAST.replace(":", " "), MultiMac.replace("-", " ") 
Content = "".join(Content).encode('utf-8')
#creating the payload by combining MAC addess *16 and the 8 FFs and converting to bits using encoding and .join
#also replaced : and - with spaces because I think that is how bits are formatted


magicP = Ether(dst=ETHER_BROADCAST)/IP(dst='255.255.255.255')/UDP(sport=727, dport=9)/raw(Content)
#use port 727 for no reason other than to find it on wireshark

IfaceName = 'VirtualBox Host-Only Ethernet Adapter'
#selecting interface, might need to change based on situation
#can be found by typing ipconfig /all and looking at the "description" tag

magicP.show() 

sendp([magicP], iface=IfaceName )

