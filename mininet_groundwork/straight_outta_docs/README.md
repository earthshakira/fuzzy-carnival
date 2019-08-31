### Important Terminologies for Mininet

``````Topo``````: the base class for Mininet topologies

```build()```: The method to override in your topology class. Constructor parameters (n) will be passed through to it automatically by Topo.__init__().

```addSwitch()```: adds a switch to a topology and returns the switch name

```addHost()```: adds a host to a topology and returns the host name

```addLink()```: adds a bidirectional link to a topology (and returns a link key, but this is not important). Links in Mininet are bidirectional unless noted otherwise.

```Mininet```: main class to create and manage a network

```start()```: starts your network

```pingAll()```: tests connectivity by trying to have all nodes ping each other

```stop()```: stops your network

```net.hosts```: all the hosts in a network

```dumpNodeConnections()```: dumps connections to/from a set of nodes.

```setLogLevel( 'info' | 'debug' | 'output' )```: set Mininet's default output level; 'info' is recommended as it provides useful information.

### Shared Filesystem

	h = Host( 'h1', privateDirs=[ '/some/directory' ] )

### Host Configuration Methods

Mininet hosts provide a number of convenience methods for network configuration:

    IP(): Return IP address of a host or specific interface.
    MAC(): Return MAC address of a host or specific interface.
    setARP(): Add a static ARP entry to a host's ARP cache.
    setIP(): Set the IP address for a host or specific interface.
    setMAC(): Set the MAC address for a host or specific interface

### Measuring Performance

These are recommended, though you’re free to use any tool you’re familiar with.

    Bandwidth (bwm-ng, ethstats)
    Latency (use ping)
    Queues (use tc included in monitor.py)
    TCP CWND statistics (tcp_probe, maybe we should add it to monitor.py)
    CPU usage (global: top, or per-container cpuacct)
