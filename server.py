#Shaquille Johnson Paradigms 2016

#9033: port for ssh for localhost
#9062: client connection
#9063: data connection

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

#data connection, make the transfer of things complete
class GetJSON(LineReceiver):
	def __init__(self):
		#self.d = DeferredQueue()
		#self.buffer = None
		#self.client = None
		pass
	def connectionMade(self):
		print 'connetion made to ', str(self.transport.getPeer())
		#factory = protocol.ClientFactory()
		#factory.protocol = ClientProtocol
		#factory.server = self
		reactor.connectTCP("student03.cse.nd.edu",22,ssh)
		
	def dataReceived(self, data):
		print "Received ", data
		#if self.client:
		#	print data
		#	self.d.put(data)
		#	self.d.get().addCallback(self.clientWrite)
		#else:
		#	self.buffer = data
		#	self.d.get().addCallback(self.clientWrite)
		ssh.getProt().clientWrite(data)
	def connectionLost(self, reason):
		print "connection lost to", str(self.transport.getPeer()), "because", reason
		#reactor.stop()
	def clientWrite(self,data):
		self.transport.write(data)

#ssh connection details
class SSH(LineReceiver):
	def connectionMade(self):
		pass

	def dataReceived(self,data):
		date.getProt().clientWrite(data)
	
	def connectionLost(self, reason):
		print "connection lost to", str(self.transport.getPeer()), "because", reason
	
	def clientWrite(self,data):
		self.transport.write(data)

class SSHFactory(ClientFactory):
	def __init__(self):
		self.protocol = SSH()
	
	def buildProtocol(self,addr):
		return self.protocol

	def getProt(self):
		return self.protocol

class DataFactory(ClientFactory):
	#protocol = GetJSON()
	def __init__(self):
		self.p = GetJSON()
	def buildProtocol(self,addr):
		return self.p
	def getProt(self):
		return self.p

#command connection
class Command(Protocol):
	def __init__(self):
		self.count = 0
	def connectionMade(self):
		print "in business"
	def dataReceived(self,data):
		#once established and sent connect to next one
		#print "Command: ", data
		if data == 'data\r\n' and self.count == 0:
			reactor.connectTCP('student01.cse.nd.edu',9063,date)
			self.count = 1 
class CommandFactory(ClientFactory):
	#protocol = Command()
	
	def buildProtocol(self,addr):
		return Command()

#Beginning connect to computers
def main():
	f = CommandFactory()
	reactor.connectTCP('student01.cse.nd.edu',9062,f)
	reactor.run()


ssh = SSHFactory()
date = DataFactory()

if __name__ == '__main__':
	main()
