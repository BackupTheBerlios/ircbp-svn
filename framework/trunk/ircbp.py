#########################################################################################################
# (C) Nigel Jones, Brian Pankey and contributors to The IRC Bot Project, All Rights Reserved, 2004	#
# Some Portions are copyright to Gian Mario Tagliaretti, portions of his code will be replaced shortly	#
#########################################################################################################

#################################################
# The main developers are:			#
#	Nigel Jones <nigelj@users.berlios.de>	#
#	Brian Pankey <pankey@users.berlios.de>	#
#						#
# Contributors names can be found in "CREDITS"	#
#						#
# Project Page is at:				#
# https://developer.berlios.de/projects/ircbp/	#
#################################################

#########################################################################################################
# This is currently held under the terms of the General Public License Version 2 which can be found at:	#
# http://www.gnu.org/licenses/gpl.txt									#
# GPL Document can also be found in the same directory as this file as "LICENSE"			#
#########################################################################################################

# Imports for sockets etc

import socket, string, sys, time


# Connection Details
# In future this should be in a seperate file!

# IRC Server DNS Name OR IP
SERVER = 'irc.freenode.net'

# Port IRC Server Listerns on
PORT = 6667

# Password for logining into the server (normally blank unless you have a special I:line)
SVRPASSWORD = ''

# Nickname for the IRC Bot to use
NICKNAME = 'IRCBP'

# Channel for the IRC Bot to join on connect (only channel at this moment that it will listen to
# Will be made into an array soon
CHANNEL = '#IRCBP'


### CODE STARTS HERE ###


# This basic socket will provide 1 connection to an IRC Server, in future we can most likely man it into an array
# of sockets
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def srvconnect():
    IRC.connect((SERVER, PORT))

#simple function to send data through the socket
def irccommand(command):
    IRC.send(command + '\n')

#join the channel
def ircjoin(channel):
    irccommand("JOIN %s" % channel)

#send login data (customizable)
def irclogin(nickname, username='pbot', password = SVRPASSWORD, realname='Nigels PBot', hostname='Nigel', servername='Freenode'):
    #We need to see if we need to send a password, so here we go
    if password != "":
	#Pass Required so lets send it!
	irccommand("PASS " + password)

    #IRC "USER" RFC says: "USER Username Hostname Servername :Realname"
    irccommand("USER %s %s %s %s" % (username, hostname, servername, realname))
    irccommand("NICK " + nickname)

srvconnect()
irclogin(NICKNAME)
ircjoin(CHANNEL)

while (1):
    buffer = IRC.recv(1024)

    msg = string.split(buffer)
    print buffer

    if msg[0] == "PING": #check if server have sent ping command
	irccommand("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg[1] == 'PRIVMSG' and msg[2] == NICKNAME:
	print "We got a PM!!!"
	nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
	print "Sent by " + nick_name
	message = ' '.join(msg[3:])
	print "The message was: " + message
    if msg[1] == 'PRIVMSG' and msg[2] == CHANNEL:
	print "We have a channel message! - W00T!!!"
	nick_name = string.lstrip(msg[0][:string.find(msg[0],"!")], ':')
	if string.lstrip(msg[3], ':') == '!say':
	    print "We need to say something :P"
	    message = ' '.join(msg[4:])
	    irccommand("PRIVMSG " + CHANNEL + " :" + message)
	if string.lstrip(msg[3], ':') == '!topic':
	    print "Changing Topic"
	    message = ' '.join(msg[4:])
	    print "The new topic will be: " + message
	    irccommand("TOPIC " + CHANNEL + " :" + message)
	if string.lstrip(msg[3], ':') == '!kick':
	    print "Someone's being bad, I need to kick!"
	    #if msg[4] != '':
	    if len(msg) > 4:
		irccommand("PRIVMSG " + CHANNEL + " :Oh someones being bad! LETS KICK!")

		#if msg[5] != '':
		if len(msg) > 5:
		    message = ' '.join(msg[5:])
		    irccommand("KICK " + CHANNEL + " " + msg[4] + " :" + message)
		else:
		    irccommand("KICK " + CHANNEL + " " + msg[4] + " :You've being a BAD boy!")

		irccommand("PRIVMSG " + CHANNEL + " :" + nick_name + ", your dirty work is done!")
	    else:
		irccommand("PRIVMSG " + CHANNEL + " :SYNTAX IS: !kick <nick> [Optional Message]")
	if string.lstrip(msg[3], ':') == '!cycle':
	    print "Cycling!"
	    irccommand("PRIVMSG " + CHANNEL + " :Okie Doke!")
	    irccommand("PART " + CHANNEL)
	    irccommand("JOIN " + CHANNEL)
	    irccommand("PRIVMSG " + CHANNEL + " :Did you miss me?")
	    if string.lstrip(msg[3], ':') == '!quit':
	    print "It's a quit"
	    irccommand("QUIT :Quit from " + nick_name)
	    print "Sent quit message, exiting"
	    sys.exit()
    if msg[2] == 'KICK':
    	print "Oh yay it worked!"
	#More to come here
