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
    <a href="http://ircbp.berlios.de">IRCbp</a> / Home</div> 
  <h2 id="pageName">Welcome to IRCbp's Homepage </h2> 
  <div class="feature"> 
    <img src="ircbp-mockup.gif" alt=""> 
    <h3>Introduction</h3> 
    <p> 
    IRCbp is a free, open source, Python based IRC Bot.  It consists of a single script (in the future, two files may be used; one for config options, one for the actual bot) which does all of the work.  This Project was created for the sole purpose of aiding in us, the developers, learning the python scripting language. 
	</p><p>
  </div> 
<div class="story"> 
    <h3>Project News</h3> 
<!--    <p> 
    more text here
    </p> -->
    <?php
    	include("/home/users/nigelj/ircbp/projnews.cache");
    ?> 
  </div>
</div> 
<!--end content --> 
<?php
include("includes/footer.php");
?>