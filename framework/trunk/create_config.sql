-- 
-- Table structure for table `config`
-- 

DROP TABLE IF EXISTS `config`;
CREATE TABLE IF NOT EXISTS `config` (
  `NICKNAME` tinytext NOT NULL,
  `REALNAME` mediumtext NOT NULL,
  `NSPASSWORD` tinytext NOT NULL,
  `SERVER` text NOT NULL,
  `PORT` smallint(5) unsigned NOT NULL default '6667',
  `SVRPASSWORD` text NOT NULL,
  `DANCERMODE` char(1) binary NOT NULL default '1'
) TYPE=MyISAM;

-- 
-- Dumping data for table `config`
-- 

INSERT INTO `config` VALUES ('IRCBP', 'The Internet Relay Chat Bot Project', '', 'irc.freenode.net', 6667, '', 0x31);
