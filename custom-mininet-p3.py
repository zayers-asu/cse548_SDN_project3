#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import os

def customNet():
    
    # Setup miniNet, enable auto Mac IDs
    net = Mininet(autoSetMacs=True);

    # Add OVS switch, OVSSwitch is same as --switch=ovsk
    s1 = net.addSwitch('s1',switch=OVSSwitch)
    
    # Add 1 remote controllers on ports 6655
    c1 = net.addController('c1',controller=RemoteController,port=6655)
    
    # Add hosts with custom IP addresses
    h1 = net.addHost('h1', ip='192.168.2.10')
    h2 = net.addHost('h2', ip='192.168.2.20')
    h3 = net.addHost('h3', ip='192.168.2.30')
    h4 = net.addHost('h4', ip='192.168.2.40')
    
    # Add Links between hosts and swtich
    net.addLink(h1,s1)
    net.addLink(h2,s1)
    net.addLink(h3,s1)
    net.addLink(h4,s1)
    

    print("before start")
    net.start()
    print("after start")
    CLI(net)
    print("after net")
    net.stop()
    print("after stop")

if __name__ == '__main__':
    setLogLevel('info')
    customNet()
