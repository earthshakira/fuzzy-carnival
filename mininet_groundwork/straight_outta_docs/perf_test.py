#!/usr/bin/python
"""
In addition to basic behavioral networking, Mininet provides performance limiting
and isolation features, through the CPULimitedHost and TCLink classes.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo( Topo ):
    """Single switch connected to n hosts."""
    def build( self, n=2 ):
	switch = self.addSwitch( 's1' )
	for h in range(n):
	    # Each host gets 50%/n of system CPU
	    host = self.addHost( 'h%s' % (h + 1),
		                 cpu=.5/n )
	    # 10 Mbps, 5ms delay, 2% loss, 1000 packet queue

	    self.addLink( host, switch, bw=10, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True )

""" 
~~A Better Way to write in code~~

linkopts = dict(bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
    # (or you can use brace syntax: linkopts = {'bw':10, 'delay':'5ms', ... } )
self.addLink(node1, node2, **linkopts)

"""

def perfTest():
    """Create network and run simple performance test"""
    topo = SingleSwitchTopo( n=4 )
    net = Mininet( topo=topo,
	           host=CPULimitedHost, link=TCLink )
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get( 'h1', 'h4' )
    net.iperf( (h1, h4) )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    perfTest()