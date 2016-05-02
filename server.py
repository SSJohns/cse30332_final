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
	def __init__(self):
		self.userName = ''
	def connectionMade(self):
		print 'ConnctionMadeTo', str(self.transport.getPeer())
		factory.clients.append(self)
		self.sendLine("User name: ")
	def lineReceived(self,data):
		self.userName = data
	def connectionLost(self,reason):
		print "connection lost to,", str(self.transport.getPeer())
		factory.clients.remove(self)
	def sendLine(self,data):
		self.transport.write(data)
class CommandFactory(ServerFactory):
	def buildProtocol(self,addr):
		return Command()

#Beginning connect to computers
def main():
	factory.clients = []
	f = CommandFactory()
	reactor.listenTCP(9063,f)
	reactor.run()

if __name__ == '__main__':
	main()
