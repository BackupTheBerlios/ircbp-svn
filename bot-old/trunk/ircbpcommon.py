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

import socket
import string
import sys
import time
import fnmatch
import ircbpconfig

# This basic socket will provide 1 connection to an IRC Server, in future we can most likely make it into an array
# of sockets
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def sockcreate():
    #open a connection with the server
    IRC.connect((ircbpconfig.SERVER, ircbpconfig.PORT))
    
    #We need to see if we need to send a password, so here we go
    if ircbpconfig.SVRPASSWORD != "":
        #Pass Required so lets send it!
        irccommand("PASS " + ircbpconfig.SVRPASSWORD)

    #IRC "USER" RFC says: "USER Username Hostname Servername :Realname"
    irccommand("USER %s %s %s :%s" % (ircbpconfig.NICKNAME, ircbpconfig.NICKNAME, ircbpconfig.SERVER, ircbpconfig.REALNAME))
    irccommand("NICK " + ircbpconfig.NICKNAME)
    

#simple function to send data through the socket
def irccommand(command):
    IRC.send(command + '\n')

def dojoins():
    print "dojoins called"
    x = 0
    print "Starting the loop"
    while (len(ircbpconfig.channels)-1 >= x):
        print "The loop is going to join the channel in ircbpconfig.channels[" + str(x) + "][0] which is " + ircbpconfig.channels[x][0]
        irccommand("JOIN " + ircbpconfig.channels[x][0])
        x = x+1
    print "dojoins Complete!"


def sendnickserv():
    if ircbpconfig.NSPASSWORD != "": 
        irccommand("PRIVMSG NICKSERV :IDENTIFY " + ircbpconfig.NSPASSWORD)
        time.sleep(10)

def addchan(CHANNEL):
    ircbpconfig.channels.append([CHANNEL])
        
# This function will check if a user is in the privledged[x] array

def privcheck(USERHOSTTBC, LEVEL):
    print "User PrivCheck Called"
    x = 0
    print "starting the loop"
    while (len(ircbpconfig.privledged)-1 >= x):
        print "The data we got is: " + USERHOSTTBC
        print "The loop is checking ircbpconfig.privledged[" + str(x) + "][0] which is " + ircbpconfig.privledged[x][0]
        if fnmatch.fnmatch(USERHOSTTBC,ircbpconfig.privledged[x][0]):
            print "We have a match on the host, now to check access"
            print ircbpconfig.privledged[x][1]
            if LEVEL == "A" and ircbpconfig.privledged[x][1] == "A":
                    return 1
            elif LEVEL == "O" and ircbpconfig.privledged[x][1] in "AO":
                    return 1
            elif LEVEL == "U" and ircbpconfig.privledged[x][1] in "AOU":
                    return 1
            else:
                return 0
                print "Auth Level does not match"
        else:
            x = x+1
            print "NOT A MATCH!"
            continue
    return 0
    print "No Matches"

# This function will check if the channel is one the bot has joined

def ischanmember(CHKCHANNEL):
    print "ischanmember Called"
    x = 0
    print "Starting the loop"
    while (len(ircbpconfig.channels)-1 >= x):
        print "The loop is checking if we are in ircbpconfig.channels[" + str(x) + "][0] which is " + ircbpconfig.channels[x][0]
        if string.upper(ircbpconfig.channels[x][0]) == string.upper(CHKCHANNEL):
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
        print "The loop is checking if the channel is a match @ ircbpconfig.channels[" + str(x) + "][0] which is " + ircbpconfig.channels[x][0]
        if string.upper(ircbpconfig.channels[x][0]) == string.upper(CHANNEL):
            print "We are in it!"
            del ircbpconfig.channels[x]
            return 1
        else:
            #Keep going!
            x = x+1
            print "No match yet"
    return 0
    print "No matches"
