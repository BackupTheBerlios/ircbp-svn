#########################################################################################################
# (C) Nigel Jones, Brian Pankey and contributors to The IRC Bot Project, All Rights Reserved, 2004	#
# Some Portions are copyright to Gian Mario Tagliaretti, portions of his code will be replaced shortly	#
#########################################################################################################

# $Id$ #

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

import socket, string, sys, time, fnmatch

# Introduce Privledged User System

privledged = []

def addmask(HOSTMASK):
    privledged.append(HOSTMASK)

# Introduce Channel System

channels = []

def addchan(CHANNEL):
    channels.append(CHANNEL)

prefixes = []

def addprefix(PREFIX):
    prefixes.append(PREFIX)

# Introduce Users allowed to control "powerful" features
# Features include !quit, !topic, !kick, !cycle

# Usage:
# addmask('nick!ident@host')
addmask('*!*@nigel.user')
addmask('*!*@ghettobp19.user')

# Add Channels

addchan('#IRCBP')

# Add Prefixes

addprefix('!')
addprefix('IBP.')

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
#def ircjoin(channel):
#    irccommand("JOIN %s" % channel)

def dojoins():
    print "dojoins called"
    x = 0
    print "Starting the loop"
    while (len(channels)-1 >= x):
	print "The loop is going to join the channel in channels[" + str(x) + "] which is " + channels[x]
	irccommand("JOIN " + channels[x])
	x = x+1
    print "dojoins Complete!"


#send login data (customizable)
def irclogin(nickname, username='pbot', password = SVRPASSWORD, realname='Nigels PBot', hostname='Nigel', servername='Freenode'):
    #We need to see if we need to send a password, so here we go
    if password != "":
	#Pass Required so lets send it!
	irccommand("PASS " + password)

    #IRC "USER" RFC says: "USER Username Hostname Servername :Realname"
    irccommand("USER %s %s %s %s" % (username, hostname, servername, realname))
    irccommand("NICK " + nickname)


# This function will check if a user is in the privledged[x] array

def privcheck(USERHOSTTBC):
    print "User PrivCheck Called"
    x = 0
    print "starting the loop"
    while (len(privledged)-1 >= x):
	print "The data we got is: " + USERHOSTTBC
	print "The loop is checking privledged[" + str(x) + "] which is " + privledged[x]
	if fnmatch.fnmatch(USERHOSTTBC,privledged[x]):
	#if fnmatch.fnmatch('Nigel!~nigel@nigel.user','*!*@nigel.user'):
	    print "OMG MATCH!"
	    return 1
	else:
	    x = x+1
	    print "NOT A MATCH!"
    return 0
    print "No Matches"

# This function will check if the channel is one the bot has joined

def ischanmember(CHKCHANNEL):
    print "ischanmember Called"
    x = 0
    print "Starting the loop"
    while (len(channels)-1 >= x):
	print "The loop is checking if we are in channels[" + str(x) + "] which is " + channels[x]
	if string.upper(channels[x]) == string.upper(CHKCHANNEL):
	    print "We are in it!"
	    return 1
	else:
	    #Keep going!
	    x = x+1
	    print "No match yet"
    return 0
    print "No matches"

def isusingprefix(INDATA,COMMAND):
    print "Checking if command has a set prefix in it"
    x = 0
    print "Starting the loop"
    while (len(prefixes)-1 >= x):
	print "The loop is checking if the prefix in " + INDATA + " is using the prefix in prefixes[" + str(x) + "] which is " + prefixes[x]
	if string.upper(prefixes[x] + COMMAND) == string.upper(INDATA):
	    print "We are in it!"
	    return 1
	else:
	    #Keep going!
	    x = x+1
	    print "No match yet"
    return 0
    print "No matches"

srvconnect()
irclogin(NICKNAME)
#ircjoin(CHANNEL)
dojoins()

while (1):
    buffer = IRC.recv(1024)

    msg = string.split(buffer)
    print buffer,

    if msg[0] == "PING": #check if server have sent ping command
	irccommand("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg[1] == 'PRIVMSG' and msg[2] == NICKNAME:
	print "We got a PM!!!"
	nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
	print "Sent by " + nick_name
	message = ' '.join(msg[3:])
	print "The message was: " + message
    #if msg[1] == 'PRIVMSG' and ischanmember(msg[2]):
    if msg[1] == 'PRIVMSG' and msg[2][0] == "#":
	# Doing this for HOSTMASK auth method which is now in use
	HOSTMASK = string.lstrip(msg[0], ':')
	# Some functions still need nick_name so lets keep it!
	nick_name = string.lstrip(msg[0][:string.find(msg[0],"!")], ':')
	CHANNEL = msg[2]
	if len(msg) > 3:
	    print "We have a channel message! - W00T!!!"

	    # Say Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!say'):
	    #if isusingprefix(string.lstrip(msg[3], ':'), 'say'):
		print "We need to say something :P"
		message = ' '.join(msg[4:])
		irccommand("PRIVMSG " + CHANNEL + " :" + message)

	    # Topic Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!topic'):
		if privcheck(HOSTMASK):
		    if len(msg) > 4:
			print "Changing Topic"
			message = ' '.join(msg[4:])
			print "The new topic will be: " + message
			irccommand("TOPIC " + CHANNEL + " :" + message)
		    else:
			print "This is work in process"
		else:
		    # They don't have privledges!
		    irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")

	    # Kick Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!kick'):
	    # msg[4] = channel
	    # msg[5] = nickname
	    # msg[6->] = reason
		if privcheck(HOSTMASK) == 1:
		    print "Someone's being bad, I need to kick!"
		    #if msg[4] != '':
		    if len(msg) > 4:
			if ischanmember(string.upper(msg[4])):
			    irccommand("PRIVMSG " + CHANNEL + " :Oh someones being bad! LETS KICK!")
			    if len(msg) > 5:
				#if msg[5] != '':
				if len(msg) > 6:
				    message = ' '.join(msg[6:])
				    irccommand("KICK " + msg[4] + " " + msg[5] + " :" + message)
				else:
				    irccommand("KICK " + msg[4] + " " + msg[5] + " :You've being a BAD boy!")

			        irccommand("PRIVMSG " + CHANNEL + " :" + nick_name + ", your dirty work is done!")
			    else:
			        irccommand("PRIVMSG " + CHANNEL + " :SYNTAX IS: !kick \x02<nick>\x02 [Optional Message]")
			else:
			    irccommand("PRIVMSG " + CHANNEL + " :" + nick_name + ", I'm not in that channel!")
		    else:
			irccommand("PRIVMSG " + CHANNEL + " :SYNTAX IS: !kick \x02<nick>\x02 [Optional Message]")
		else:
		    # They don't have privledges!
		    irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")

	    # Join Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!join'):
		print "Joining a channel!"
		# Need to make sure that nick_name has in our privledged array
		if privcheck(HOSTMASK):
		    # He/She is, making sure that they provided a channel - We will need a string check on this too.
		    if len(msg) > 4:
			# Something has being provided, need to make sure it is a channel for now by only checking if it has # at the start
			if msg[4][0] == "#":
			    # All ok, adding the channel to the array, JOIN sent normally because we have gone past the time of dojoin
			    addchan(msg[4])
			    irccommand("JOIN " + msg[4])
			else:
			    # Not a channel, return error
			    irccommand("PRIVMSG " + CHANNEL + " :" + msg[4] + " is not a channel")
		    else:
			# Nothing provided, syntax error!
			irccommand("PRIVMSG " + CHANNEL + " :Syntax error, correct syntax is: !join \x02<channel>\x02")
		else:
		    irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")

	    # Cycle Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!cycle'):
		if privcheck(HOSTMASK):
		    print "Cycling!"
		    irccommand("PRIVMSG " + CHANNEL + " :Okie Doke!")
		    irccommand("PART " + CHANNEL)
		    irccommand("JOIN " + CHANNEL)
		    irccommand("PRIVMSG " + CHANNEL + " :Did you miss me?")
		else:
		    # Oh dear they cycle our bot!
		    irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")

	    # Quit Command

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!quit'):
		if privcheck(HOSTMASK):
		    print "It's a quit"
		    irccommand("QUIT :Quit from " + nick_name)
		    print "Sent quit message, exiting"
		    sys.exit()
		else:
		    # Oh dear they quit our bot!
		    irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
	else:
	    # Somethings wrong with the server but yeah, we can save running some code
	    print "This is work in process"
    if msg[1] == 'KICK':
    	print "Oh yay it worked!"
	#More to come here
