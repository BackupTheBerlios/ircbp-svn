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

# Don't edit the following "import" line!

import MySQLdb



class mysqlconfig:
    # EDIT THE FOLLOWING LINE TO THE NAME OF YOUR SQL HOST
    SQLHOST = 'localhost'
    # EDIT THE FOLLOWING LINE TO THE NAME OF YOUR SQL USER
    SQLUSER = 'IRCBP'
    # EDIT THE FOLLOWING LINE TO THE PASSWORD OF YOUR SQL USER
    SQLPASS = ''
    # EDIT THE FOLLOWING LINE TO THE PORT USED BY YOUR SQL SERVER
    SQLPORT = 3306

    
# DO NOT EDIT ANYTHING MORE 

# SQL Connection

sqlconfig = mysqlconfig()

# Connecting...

db=MySQLdb.connect(host=sqlconfig.SQLHOST, user=sqlconfig.SQLUSER, passwd=sqlconfig.SQLPASS, db='IRCBP', port=sqlconfig.SQLPORT)

# Main configuration!

db.query("""SELECT * from config LIMIT 0 , 1""")
if db.errno() != 0:
    print "MySQL has produced an error! Which is as follows:"
    print db.errno() + " " + db.error()
    print "Location of error:  Configuration Query"

configprops=db.use_result().fetch_row()

# Channels we join!

db.query("""SELECT * from channels""")
if db.errno() != 0:
    print "MySQL has produced an error! Which is as follows:"
    print db.errno() + " " + db.error()
    print "Location of error:  Channels Query"
    
prechannels=db.store_result()
channels=[c[0] for c in prechannels.fetch_row(prechannels.num_rows())]

# Now from privledged users!

db.query("""SELECT * from users""")
if db.errno() != 0:
    print "MySQL has produced an error! Which is as follows:"
    print db.errno() + " " + db.error()
    print "Location of error:  Users Query"
    
preprivs=db.store_result()
privledged=[c[0] for c in preprivs.fetch_row(prechannels.num_rows())]


# Bot Nickname and Realname (Must not be null) for the IRC Bot to use
    
NICKNAME = configprops[0][0]
REALNAME = configprops[0][1]
    
# Add your bots nickserv password here, if none leave blank!

NSPASSWORD = configprops[0][2]

# Server Connection Details
# In future this should be in a seperate file!
    
# IRC Server DNS Name OR IP
SERVER = configprops[0][3]
    
# Port IRC Server Listerns on
PORT = int(configprops[0][4])

# Password for logining into the server (normally blank unless you have a special I:line)
SVRPASSWORD = configprops[0][5]

# 1 if using a IRCd that you are connecting to is DancerIRCd (Freenode for example)
# 0 if not
DANCERMODE = int(configprops[0][6])


