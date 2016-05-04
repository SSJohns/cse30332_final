#Nathan Kowaleski
#Shaquille Johnson
#Programming Paradigms Spring 2016
#Final project
#client.py
#5/4

import json

from gamestate import *
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import stdio
from twisted.internet.protocol import Protocol
from twisted.internet import reactor, stdio

SERVER_HOST = 'student02.cse.nd.edu'
SERVER_PORT = 9063

#overwrite functions from Protocol class
#defines what this connection does when certain events happen
class ClientConnection(LineReceiver):
	def __init__(self, factory):#on creation pass
		self.gs = factory.gs

	def connectionMade(self):#when connection is made send data
		print 'new connection made to', SERVER_HOST, 'port', SERVER_PORT
		self.gs.main(self)

	def lineReceived(self, data):#when data is recieved print it
		print json.loads(data)

	def connectionLost(self, reason):#when connection is lost stop reactor
		print 'lost connection to', SERVER_HOST, 'port', SERVER_PORT
		#reactor.stop()
	def write(self,data):
		self.transport.getHandle().sendall(data)

#class that creates instances of ClientConnection Class
class ClientConnFactory(ClientFactory):
	def __init__(self):
		self.gs = GameSpace()
		#self.clientconnection = ClientConnection()

	def buildProtocol(self, addr):
		return ClientConnection(self)


if __name__ == '__main__':
	reactor.connectTCP(SERVER_HOST, SERVER_PORT, ClientConnFactory())
	reactor.run()
