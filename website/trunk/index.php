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
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<!-- DW6 -->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>The IRC Bot Project</title>
<link rel="stylesheet" href="ircbp.css" type="text/css">
</head>
<!-- The structure of this file is exactly the same as 2col_rightNav.html;
     the only difference between the two is the stylesheet they use -->
<body> 
<div id="masthead"> 
  <h1 id="siteName">IRCbp - The IRC Bot Project </h1> 
  <!--<div id="globalNav"> 
    <a href="#">global link</a> | <a href="#">global link</a> | <a href="#">global
    link</a> | <a href="#">global link</a> | <a href="#">global link</a> | <a href="#">global
    link</a> | <a href="#">global link</a> 
  </div>--> 
</div> 
<!-- end masthead --> 
<div id="content"> 
  <div id="breadCrumb"> 
    <a href="http://ircbp.berlios.de">Home</a> / </div> 
  <h2 id="pageName">Welcome to IRCbp's Homepage </h2> 
  <div class="feature"> 
    <img src="ircbp-mockup.gif" alt=""> 
    <h3>Introduction</h3> 
    <p> 
    IRCbp is a free, open source, Python based IRC Bot.  It consists of a single script (in the future, two files may be used; one for config options, one for the actual bot) which does all of the work.  This Project was created for the sole purpose of aiding in us, the developers, learning the python scripting language. 
	</p><p>
	Stay tuned for more info on a release date of the bot. =)
    </p> 
  </div> 
<!--  <div class="story"> 
    <h3>another title</h3> 
    <p> 
    more text here
    </p> 
  </div>--> 
</div> 
<!--end content --> 
<div id="navBar"> 
  <div id="search">  </div> 
  <div id="sectionLinks"> 
    <ul> 
      <li><a href="http://ircbp.berlios.de/index2.php">Home Page </a></li> 
      <li><a href="http://developer.berlios.de/projects/ircbp/">Project Page </a></li>
	  <li><a href="http://berlios.de">BerliOS Website</a></li> 
      <li><a href="http://www.irchelp.org">IRChelp.org</a></li> 
      <li><a href="http://www.python.org">Python.org</a></li>  
    </ul> 
  </div> 
  <div class="relatedLinks"> 
    <?php
    //  BerliOS Stats
    include("/home/users/nigelj/ircbp/projhtml.cache");
    ?>
  </div> 
  <div class="relatedLinks"></div> 
  <div id="advert">
  <a href="http://developer.berlios.de" title="BerliOS Developer">
  <img src="http://developer.berlios.de/bslogo.php?group_id=2320" width="124px" height="32px" border="0" alt="BerliOS Developer Logo">
  </a>
  <br>
  <!--end navbar --> 
</div> 
</div> 
<div id="siteInfo"> 
  <!--<img src="" width="44" height="22">--> <a href="http://developer.berlios.de/project/memberlist.php?group_id=2320">About Us</a> | <a href="#">Site
  Map</a> | <a href="#">Privacy Policy</a> | <a href="#">Contact Us</a> | &copy;2004
  Don't-Have-A-Company-Name-Yet, Inc.
</div> 
<br> 
</body>
</html>
