#Nathan Kowaleski
#Shaquille Johnson
#Programming Paradigms
#Spring 2016
#Final Project
#5/4
#client.py

import json

from gamestate import *
from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import stdio
from twisted.internet.protocol import Protocol
from twisted.internet import reactor, stdio

SERVER_HOST = 'student02.cse.nd.edu'
SERVER_PORT = 9063

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except ValueError, e:
		return False
	return True

#overwrite functions from Protocol class
#defines what this connection does when certain events happen
class ClientConnection(LineReceiver):
	def __init__(self, factory):#on creation pass
		self.gs = factory.gs

	def connectionMade(self):#when connection is made send data
		print 'new connection made to', SERVER_HOST, 'port', SERVER_PORT
		self.gs.main(self)

	def lineReceived(self, data):#when data is recieved print it
		print data
		if is_json(data):
			data_dumps = json.loads(data)
			print data_dumps
			#self.gs.enemyUpdate(data_dumps)
		else:
			data_enemy = data.split(':')
			#self.gs.newEnemy(int(data_enemy[1]))
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
	cliFac =  ClientConnFactory()
	reactor.connectTCP(SERVER_HOST, SERVER_PORT,cliFac)
	reactor.run()
