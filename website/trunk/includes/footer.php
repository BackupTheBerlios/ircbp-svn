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
<div id="navBar"> 
  <div id="search">  </div> 
  <div id="sectionLinks"> 
    <ul> 
      <li><a href="index.php">Home Page </a></li> 
      <li><a href="devinfo.php">Development Information</a></li>
      <li><a href="svn.php">SVN Information </a></li>
      <li><a href="http://developer.berlios.de/projects/ircbp/">Project Page </a></li>
<!--      <li><a href="http://berlios.de">BerliOS Website</a></li> 
      <li><a href="http://www.irchelp.org">IRChelp.org</a></li> 
      <li><a href="http://www.python.org">Python.org</a></li>  -->
    </ul> 
  </div> 
  <div class="relatedLinks"> 
    <?php
    //  BerliOS Stats
    $filename = "/home/users/nigelj/ircbp/projhtml.cache";
    include($filename);
    // From php.net
    if (file_exists($filename)) {
        echo "Stats Updated: " . date ("F d Y H:i:s.", filemtime($filename));
    }
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
  <!--<img src="" width="44" height="22">--> <a href="#">About Us</a> | <a href="#">Site
  Map</a> | <a href="#">Privacy Policy</a> | <a href="http://developer.berlios.de/project/memberlist.php?group_id=2320">Contact Us</a> | &copy;2004
  The IRC Bot Project (Brian Pankey & Nigel Jones).  All Rights Reserved<br>
  Page Last Updated: <?php echo $version; ?>
  
  <p>
     <a href="http://jigsaw.w3.org/css-validator/check/referer">
       <img style="border:0;width:88px;height:31px" src="images/vcss.png" alt="Valid CSS!">
     </a>
  </p>
</div> 
<br> 
</body>
</html>
