CREATE TABLE `config` (
  `NICKNAME` tinytext NOT NULL,
  `REALNAME` mediumtext NOT NULL,
  `SERVER` text NOT NULL,
  `PORT` smallint(5) unsigned NOT NULL default '6667',
  `SVRPASSWORD` text NOT NULL,
  `DANCERMODE` char(1) binary NOT NULL default '1'
) TYPE=MyISAM