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

# Introduce Arrays for Users/Channels and Prefixes

privledged = []
channels = []
prefixes = []

# Add functions for Users/Channels and Prefixes
def addmask(HOSTMASK):
    privledged.append(HOSTMASK)

def addchan(CHANNEL):
    channels.append(CHANNEL)

def addprefix(PREFIX):
    prefixes.append(PREFIX)

#CONFIG IS HERE
    
addmask('*!*@*')
  
# Channels that the bot will join by default
 
addchan('#IRCBP')

# Bot Nickname and Realname (Must not be null) for the IRC Bot to use
    
NICKNAME = 'IRCBP'
REALNAME = 'The Internet Chat Relay Bot Project'
    
# Add your bots nickserv password here, if none leave blank!

NSPASSWORD = ''

# Server Connection Details
# In future this should be in a seperate file!
    
# IRC Server DNS Name OR IP
SERVER = 'irc.freenode.net'
    
# Port IRC Server Listerns on
PORT = 6667

# Password for logining into the server (normally blank unless you have a special I:line)
SVRPASSWORD = ''

# 1 if using a IRCd that you are connecting to is DancerIRCd (Freenode for example)
# 0 if not
DANCERMODE = 1
