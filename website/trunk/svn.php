<?php
/*
(C) Nigel Jones, Brian Pankey and contributors to The IRC Bot Project, All Rights Reserved, 2004


$Id$


The main developers are:
	Nigel Jones <nigelj@users.berlios.de>
	Brian Pankey <pankey@users.berlios.de>

Contributors names can be found in "CREDITS"



Project Page is at:
https://developer.berlios.de/projects/ircbp/



This is currently held under the terms of the General Public License Version 2 which can be found at:
http://www.gnu.org/licenses/gpl.txt
GPL Document can also be found in the same directory as this file as "LICENSE"
*/
include("includes/header.php");
?>
<div id="content"> 
  <div id="breadCrumb"> 
    <a href="http://ircbp.berlios.de">IRCbp</a> / SVN Information</div> 
  <h2 id="pageName">Welcome to IRCbp SVN Information</h2> 
  <div class="feature"> 
    <img src="ircbp-mockup.gif" alt=""> 
    <h3>Introduction</h3> 
    <p> 
    	The developers of IRCbp use SVN for the IRC Bot Project needs.  If you wish to download the latest source (that is yet to be released) please read on.
	</p><p>
  </div> 
  <div class="story"> 
    <h3>First Time Access</h3> 
    <p>
    	If you are accessing our SVN Repository for the first time you must have the Subversion client software installed on your computer.  Debian users can download and install the needed software by performing: "apt-get install subversion".  Other users will need to download the source and compile it or you other precompiled builds from http://subversion.tigris.org
	
	After downloading and building/installing the client software you need to make sure you have a reasonably new version of Python (we recommend 2.3.x) from http://www.python.org
	
	Software can then be downloaded by performing the following command:  
		"svn checkout svn://svn.berlios.de/svnroot/repos/ircbp/framework/trunk"
  </div>
  <div class="story"> 
    <h3>Continued Updating</h3> 
    <p>
    	Downloaded source should be updated often (thats if you want to) by issuing the following command:
		"svn update" or "svn up"
    </p>
  </div>
</div> 
<!--end content --> 
<?php
include("includes/footer.php");
?>