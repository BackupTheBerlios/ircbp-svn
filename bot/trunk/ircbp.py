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

#################################################################################
# CODE STARTS HERE								#
# It is strongly recommended that you do not touch anything below this point!	#
#################################################################################

import fnmatch
import socket
import string
import sys
import time
import ircbpconfig
import ircbpcommon
    
ircbpcommon.sockcreate()

buffer = ''
while (1):
    buffer += ircbpcommon.IRC.recv(1024)

    while '\n' in buffer:
        msg, buffer = buffer.split('\n', 1)

        print msg
        msg = msg.split()
        if msg[0] == "PING": #check if server have sent ping command
            ircbpcommon.irccommand("PONG %s" % msg[1]) #answer with pong as per RFC 1459
        if msg[1] == 'PRIVMSG' and msg[2] == ircbpconfig.NICKNAME:
            print "We got a PM!!!"
            nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
            print "Sent by " + nick_name
            message = ' '.join(msg[3:])
            print "The message was: " + message
        #if msg[1] == 'PRIVMSG' and ircbpcommon.ischanmember(msg[2]):
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
                    if ircbpcommon.privcheck(HOSTMASK, "U"):
                        print "We need to say something :P"
                        message = ' '.join(msg[4:])
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :" + message)
                    else:
                        # They don't have privledges!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")

                # Topic Command

                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!topic'):
                    if ircbpcommon.privcheck(HOSTMASK, "O"):
                        if len(msg) > 4:
                            print "Changing Topic"
                            message = ' '.join(msg[4:])
                            print "The new topic will be: " + message
                            ircbpcommon.irccommand("TOPIC " + CHANNEL + " :" + message)
                        else:
                            print "This is work in process"
                    else:
                        # They don't have privledges!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
    
                # Kick Command
    
                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!kick'):
                    if ircbpcommon.privcheck(HOSTMASK, "O"):
                        print "Someone's being bad, I need to kick!"
                        #if msg[4] != '':
                        if len(msg) > 4:
                            if ircbpcommon.ischanmember(string.upper(msg[4])):
                                ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :Oh someones being bad! LETS KICK!")
                                if len(msg) > 5:
                                    #if msg[5] != '':
                                    if len(msg) > 6:
                                        message = ' '.join(msg[6:])
                                        ircbpcommon.irccommand("KICK " + msg[4] + " " + msg[5] + " :" + message)
                                    else:
                                        ircbpcommon.irccommand("KICK " + msg[4] + " " + msg[5] + " :You've being a BAD boy!")
    
                                    ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :" + nick_name + ", your dirty work is done!")
                                else:
                                    ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :SYNTAX IS: !kick \x02<#channel> <nick>\x02 [Optional Message]")
                            else:
                                ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :" + nick_name + ", I'm not in that channel!")
                        else:
                            ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :SYNTAX IS: !kick \x02<#channel> <nick>\x02 [Optional Message]")
                    else:
                        # They don't have privledges!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
    
                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!list'):
                    x = 0
                    print "Starting the loop"
                    while (len(ircbpconfig.channels)-1 >= x):
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :I am in: " + ircbpconfig.channels[x][0])
                        x = x+1
    
                # Join Command

                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!join'):
                    print "Joining a channel!"
                    # Need to make sure that nick_name has in our privledged array
                    if ircbpcommon.privcheck(HOSTMASK, "A"):
                        # He/She is, making sure that they provided a channel - We will need a string check on this too.
                        if len(msg) > 4:
                            # Something has being provided, need to make sure it is a channel for now by only checking if it has # at the start
                            if msg[4][0] == "#" and not ircbpcommon.ischanmember(msg[4]):
                                # All ok, adding the channel to the array, JOIN sent normally because we have gone past the time of dojoin
                                ircbpcommon.addchan(msg[4])
                                ircbpcommon.irccommand("JOIN " + msg[4])
                            else:
                                # Not a channel, return error
                                ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :" + msg[4] + " is not a channel or I am already on it.")
                        else:
                            # Nothing provided, syntax error!
                            ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :Syntax error, correct syntax is: !join \x02<channel>\x02")
                    else:
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
    
	        # Cycle Command
    
	        if string.upper(string.lstrip(msg[3], ':')) == string.upper('!cycle'):
                    if ircbpcommon.privcheck(HOSTMASK, "A"):
                        print "Cycling!"
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :Okie Doke!")
                        ircbpcommon.irccommand("PART " + CHANNEL)
                        ircbpcommon.irccommand("JOIN " + CHANNEL)
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :Did you miss me?")
                    else:
                        # Oh dear they cycle our bot!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
    
                # Part Command
    
                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!part'):
                    if ircbpcommon.privcheck(HOSTMASK, "A"):
                        if len(msg) > 4:
                            if msg[4][0] == "#" and ircbpcommon.ischanmember(msg[4]):
                                print "Parting!"
                                ircbpcommon.irccommand("PRIVMSG " + msg[4] + " :buh-bye now! =)")
                                ircbpcommon.irccommand("PART " + msg[4] + " :Part from %s" % nick_name)
                                ircbpcommon.remchan(msg[4])
                            else:
                                ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :" + msg[4] + " is not a channel or I am not in it.")
                        else:
                            ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :buh-bye now! =)")
                            ircbpcommon.irccommand("PART " + CHANNEL + " :Part from %s" % nick_name)
                            ircbpcommon.remchan(CHANNEL)
                    else:
                        # Oh dear they tried to part our bot!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
    
                # Quit Command
    
                if string.upper(string.lstrip(msg[3], ':')) == string.upper('!quit'):
                    if ircbpcommon.privcheck(HOSTMASK, "A"):
                        print "It's a quit"
                        ircbpcommon.irccommand("QUIT :Quit from " + nick_name)
                        print "Sent quit message, exiting"
                        sys.exit()
                    else:
                        # Oh dear they quit our bot!
                        ircbpcommon.irccommand("PRIVMSG " + CHANNEL + " :No privledges for this command!")
            else:
                # Somethings wrong with the server but yeah, we can save running some code
                print "This is work in process"
        if msg[1] == 'KICK':
            ircbpcommon.irccommand("JOIN " + msg[2])
        if msg[1] == 'JOIN':
            # Doing this for HOSTMASK auth method which is now in use
            HOSTMASK = string.lstrip(msg[0], ':')
            # Some functions still need nick_name so lets keep it!
            nick_name = string.lstrip(msg[0][:string.find(msg[0],"!")], ':')
            
            if ircbpcommon.privcheck(HOSTMASK, "O"):
                ircbpcommon.irccommand("MODE " + string.lstrip(msg[2], ':') + " +o " + nick_name)
            else:
                ircbpcommon.irccommand("PRIVMSG " + nick_name + " :Welcome to " + string.lstrip(msg[2], ':') + " please enjoy your stay!")
        #Wait until end of MOTD to do nickserv stuff and joins.
        if msg[1] == '376':
            ircbpcommon.sendnickserv()
            ircbpcommon.dojoins()
        if msg[1] == '433':
            ircbpconfig.NICKNAME = msg[3] + "_"
            ircbpcommon.irccommand("NICK :" + ircbpconfig.NICKNAME)
        #Join Blocking Modes
        if msg[1] == '467' or msg[1] == '471' or msg[1] == '473' or msg[1] == '474' or msg[1] == '475':
            #We can't join channels that are invite only
            print "The channel the bot just tried to join is invite only..."
            print "Removing from list"
            ircbpcommon.remchan(msg[3])
            if len(ircbpconfig.CHANNELS) == 0:
                print "There has being an error join the IRC Channels that you have provided,  and we cannot proceed."
                print "For your convinence the bot has being cleanly shutdown"
                ircbpcommon.irccommand("QUIT :Bot Error")
                sys.exit()
        if ircbpconfig.DANCERMODE:
            if msg[1] == '379':
                print "We are being forwarded"
                ircbpcommon.remchan(msg[3])
                ircbpconfig.addchan(msg[4])
            #join blocking modes
            if msg[1] == '437' or msg[1] == '480' or msg[1] == '515':
                #We can't join channels that are invite only
                print "The channel the bot just tried to join is invite only..."
                print "Removing from list"
                ircbpcommon.remchan(msg[3])
                if len(ircbpconfig.CHANNELS) == 0:
                    print "There has being an error join the IRC Channels that you have provided,  and we cannot proceed."
                    print "For your convinence the bot has being cleanly shutdown"
                    ircbpcommon.irccommand("QUIT :Bot Error")
                    sys.exit()
