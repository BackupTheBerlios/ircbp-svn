#!/usr/bin/python

#########################################################################################################
# (C) 2004 Nigel Jones, Brian Pankey and contributors to The IRC Bot Project, All Rights Reserved.	#
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

# Edit ircbpconfig.py for configuration

# Imports for sockets etc

import socket, string, sys, time, fnmatch, ircbpconfig
    
#################################################################################
# CODE STARTS HERE								#
# It is strongly recommended that you do not touch anything below this point!	#
#################################################################################

# This basic socket will provide 1 connection to an IRC Server, in future we can most likely man it into an array
# of sockets
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def srvconnect():
    IRC.connect((ircbpconfig.SERVER, ircbpconfig.PORT))

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
    while (len(ircbpconfig.channels)-1 >= x):
        print "The loop is going to join the channel in ircbpconfig.channels[" + str(x) + "] which is " + ircbpconfig.channels[x]
        irccommand("JOIN " + ircbpconfig.channels[x])
        x = x+1
    print "dojoins Complete!"


def sendnickserv():
    if ircbpconfig.NSPASSWORD != "": 
        irccommand("PRIVMSG NICKSERV :IDENTIFY " + ircbpconfig.NSPASSWORD)
        time.sleep(10)

#send login data (customizable)
def irclogin():
    #We need to see if we need to send a password, so here we go
    if ircbpconfig.SVRPASSWORD != "":
        #Pass Required so lets send it!
        irccommand("PASS " + ircbpconfig.SVRPASSWORD)

    #IRC "USER" RFC says: "USER Username Hostname Servername :Realname"
    irccommand("USER %s %s %s :%s" % (ircbpconfig.NICKNAME, ircbpconfig.NICKNAME, ircbpconfig.SERVER, ircbpconfig.REALNAME))
    irccommand("NICK " + ircbpconfig.NICKNAME)


# This function will check if a user is in the privledged[x] array

def privcheck(USERHOSTTBC):
    print "User PrivCheck Called"
    x = 0
    print "starting the loop"
    while (len(ircbpconfig.privledged)-1 >= x):
        print "The data we got is: " + USERHOSTTBC
        print "The loop is checking ircbpconfig.privledged[" + str(x) + "] which is " + ircbpconfig.privledged[x]
        if fnmatch.fnmatch(USERHOSTTBC,ircbpconfig.privledged[x]):
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
    while (len(ircbpconfig.channels)-1 >= x):
        print "The loop is checking if we are in ircbpconfig.channels[" + str(x) + "] which is " + ircbpconfig.channels[x]
        if string.upper(ircbpconfig.channels[x]) == string.upper(CHKCHANNEL):
            print "We are in it!"
            return 1
        else:
            #Keep going!
            x = x+1
            print "No match yet"
    return 0
    print "No matches"
    
def remchan(CHANNEL):
    print "remchan Called"
    x = 0
    print "Starting the loop"
    while (len(ircbpconfig.channels)-1 >= x):
        print "The loop is checking if the channel is a match @ ircbpconfig.channels[" + str(x) + "] which is " + ircbpconfig.channels[x]
        if string.upper(ircbpconfig.channels[x]) == string.upper(CHANNEL):
            print "We are in it!"
            del ircbpconfig.channels[x]
            return 1
        else:
            #Keep going!
            x = x+1
            print "No match yet"
    return 0
    print "No matches"

#def isusingprefix(INDATA,COMMAND):
#    print "Checking if command has a set prefix in it"
#    x = 0
#    print "Starting the loop"
#    while (len(prefixes)-1 >= x):
#        print "The loop is checking if the prefix in " + INDATA + " is using the prefix in prefixes[" + str(x) + "] which is " + prefixes[x]
#        if string.upper(prefixes[x] + COMMAND) == string.upper(INDATA):
#            print "We are in it!"
#            return 1
#        else:
#            #Keep going!
#            x = x+1
#            print "No match yet"
#    return 0
#    print "No matches"

srvconnect()
irclogin()
sendnickserv()
dojoins()

while (1):
    buffer = IRC.recv(1024)

    msg = string.split(buffer)
    print buffer,

    if msg[0] == "PING": #check if server have sent ping command
        irccommand("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg[1] == 'PRIVMSG' and msg[2] == ircbpconfig.NICKNAME:
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

	    if string.upper(string.lstrip(msg[3], ':')) == string.upper('!list'):
                    x = 0
                    print "Starting the loop"
                    while (len(ircbpconfig.channels)-1 >= x):
                        irccommand("PRIVMSG " + CHANNEL + " :I am in: " + ircbpconfig.channels[x])
                        x = x+1
    
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
                            ircbpconfig.addchan(msg[4])
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

            # Part Command

            if string.upper(string.lstrip(msg[3], ':')) == string.upper('!part'):
                if privcheck(HOSTMASK):
                    if len(msg) > 4:
                        if msg[4][0] == "#":
                            print "Parting!"
                            irccommand("PRIVMSG " + msg[4] + " :buh-bye now! =)")
                            irccommand("PART " + msg[4] + " :Part from %s" % nick_name)
                            remchan(msg[4])
                        else:
                            irccommand("PRIVMSG " + CHANNEL + " :" + msg[4] + " is not a channel")
                    else:
                        irccommand("PRIVMSG " + CHANNEL + " :buh-bye now! =)")
                        irccommand("PART " + CHANNEL + " :Part from %s" % nick_name)
                        remchan(CHANNEL)
                else:
                    # Oh dear they tried to part our bot!
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
        irccommand("JOIN " + msg[2])
    #Join Blocking Modes
    if msg[1] == '467' or msg[1] == '471' or msg[1] == '473' or msg[1] == '474' or msg[1] == '475':
        #We can't join channels that are invite only
        print "The channel the bot just tried to join is invite only..."
        print "Removing from list"
        remchan(msg[3])
        if len(ircbpconfig.CHANNELS) == 0:
            print "There has being an error join the IRC Channels that you have provided,  and we cannot proceed."
            print "For your convinence the bot has being cleanly shutdown"
            irccommand("QUIT :Bot Error")
            sys.exit()
    if ircbpconfig.DANCERMODE:
        if msg[1] == '379':
            print "We are being forwarded"
            remchan(msg[3])
            ircbpconfig.addchan(msg[4])
        #join blocking modes
        if msg[1] == '437' or msg[1] == '480' or msg[1] == '515':
            #We can't join channels that are invite only
            print "The channel the bot just tried to join is invite only..."
            print "Removing from list"
            remchan(msg[3])
            if len(ircbpconfig.CHANNELS) == 0:
                print "There has being an error join the IRC Channels that you have provided,  and we cannot proceed."
                print "For your convinence the bot has being cleanly shutdown"
                irccommand("QUIT :Bot Error")
                sys.exit()
