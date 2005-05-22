<?php
/*
(C) Nigel Jones, Brian Pankey and contributors to The IRC Bot Project, All Rights Reserved, 2004

$Id: svn.php 75 2005-05-21 20:30:57Z nigelj $

*/

$title = "Development Information";

/*

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
    <a href="http://ircbp.berlios.de">IRCbp</a> / Development Information</div> 
  <h2 id="pageName">Welcome to IRCbp Development Information</h2> 
  <div class="feature"> 
    <img src="ircbp-mockup.gif" alt=""> 
    <h3>Introduction</h3> 
    <p> 
    	IRCbp now provides development information for all of our current/upcoming/old releases.  You may select the release that you wish to have information for on the left.
	</p>
  </div>
  <?php
  	if ($HTTP_GET_VARS['v'] == '0.1.0')
	{
	    include("devinfo/0-1-0.php");
	}
	elseif ($HTTP_GET_VARS['v'] == '0.1.1')
	{
	    include("devinfo/0-1-1.php");
	}
	elseif ($HTTP_GET_VARS['v'] == ('0.2.0' || 'zilda'))
	{
	    include("devinfo/0-2-0.php");
	}
	else
	{
	    include("devinfo/0-2-0.php");
	}
    ?>
</div>
<?
include("includes/footer.php");
?>
