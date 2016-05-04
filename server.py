#Shaquille Johnson
#Nathan Kowaleski
#Programming Paradigms Spring 2016 Final

#9063: port for ssh for localhost
#should be run on student02

#::::::::::Running Commands::::::::::
#python2.6 home.py&
#(somewhere else) python2.6 work.py
#ssh localhost -p 9033
#::::::::::::::::::::::::::::::::::::

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.defer import DeferredQueue
from sys import stdout
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.protocol import ClientFactory
from twisted.web.http_headers import Headers

#command connection
class Command(LineReceiver):
	def __init__(self, factory, currPos):
		self.factory = factory
		#self.user = None
		self.id = currPos
	def connectionMade(self):
		print 'ConnctionMadeTo %s, client %d' % (str(self.transport.getPeer()), self.id)
		for client in self.factory.clients:
			client.gs.newEnemy(self.id)
		self.factory.clients.append(self)

	def dataReceived(self,data):
		position = data
		position['id'] = self.id
		for client in factory.clients:
			client.transport.write(position + "\r\n")
	def connectionLost(self,reason):
		print "connection lost to,", str(self.transport.getPeer())
		self.factory.clients.remove(self)
	#def sendLine(self,data):
	#	self.transport.write(data)
class CommandFactory(Factory):
	def __init__(self):
		self.clients = []
	def buildProtocol(self,addr):
		return Command(self, len(self.clients))

#Beginning connect to computers
def main():
	f = CommandFactory()
	reactor.listenTCP(9063,f)
	reactor.run()

if __name__ == '__main__':
	main()
