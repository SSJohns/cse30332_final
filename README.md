Competetive Frogger.... with turtles
=====

A game the uses the twisted and pygame libraries to connect multiple players.

##Usage
###Game Play:
	Use the w-a-s-d or the arrow keys to move your turtle. Players are divided into 2 teams, red and blue. The object of the game is to cross the street and get to the opposing teams side. As players join the game alternates which team it assigns them to play on, hopefully keeping teams as even as possible. If your turtle runs into a car, truck, or opposing player it will die. If you run into an opposing player you will also kill them. Leaving the screen will also result in your death. Three seconds after a score or death your turtle will reappear at your teams starting point. Every time you score your turtle gets faster, a death resets your turtles speed. Scores for the two teams are kept in the right hand corners.
	

###To start the game:
	Run the server.py on student02 and have any others connect as clients by running client.py on their own machine. 

##System Requirements
	Game has been tested on Linux Red hat machines, a Mac OSX 10.9 system, and an Ubuntu virtual machine. The main method of game deployment is the command line and the system needs both the pygame and twisted libraries installed.
