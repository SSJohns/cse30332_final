#Nathan Kowaleski
#Daily 18
#twisted 3
#d18-A.py
#client
#4/22/16

from twisted.internet.protocol import ClientFactory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

SERVER_HOST = 'student02.cse.nd.edu'
SERVER_PORT = 40069

#overwrite functions from Protocol class
#defines what this connection does when certain events happen
class ClientConnection(Protocol):
	def __init__(self):#on creation pass
		pass

	def connectionMade(self):#when connection is made send data
		print 'new connection made to', SERVER_HOST, 'port', SERVER_PORT 
		self.transport.write("GET /movies/32 HTTP/1.0\r\n\r\n")

	def dataReceived(self, data):#when data is recieved print it 
		print 'recieved data:\n', data
		self.transport.loseConnection()

	def connectionLost(self, reason):#when connection is lost stop reactor
		print 'lost connection to', SERVER_HOST, 'port', SERVER_PORT
		reactor.stop()
	

#class that creates instances of ClientConnection Class
class ClientConnFactory(ClientFactory):
	def __init__(self):
		self.clientconnection = ClientConnection()

	def buildProtocol(self, addr):
		return self.clientconnection


if __name__ == '__main__':
	reactor.connectTCP(SERVER_HOST, SERVER_PORT, ClientConnFactory())
	reactor.run()


