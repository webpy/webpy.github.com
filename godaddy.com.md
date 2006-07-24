---
layout: default
title: godaddy.com
---

# godaddy.com

I signed up for the Deluxe Linux account. I don't know anything about the Windows account. Presumably, the virtual and dedicated Linux accounts are also possible.

Godaddy has support for Python and MySQL (albeit an older version).

1) Extract flup and copy the "flup" folder to a folder called "flup" in your root directory.<br/>2) Extact Cheetah and copy the contents of "src" to a folder called "Cheetah" in your root directory.<br/>3) The version of MySQL is 4.0.*, so the "todo" table in the tutorial will need to be massaged (coming soon).<br/>It looks like this:
<p>CREATE TABLE `todo` (<br/>  `id` bigint(20) unsigned NOT NULL auto_increment primary key,<br/>  `title` text,<br/>  `created` timestamp(14) NOT NULL,<br/>  `done` tinyint(1) default '0',<br/>  PRIMARY KEY  (`id`),<br/>  UNIQUE KEY `id` (`id`)<br/>)<br/></p>(Setting DEFAULT CURRENT_TIMESTAMP didn't seem to work for me, athough I'm new to MySQL, and impatient.)
4) Log into your Account Manager to get the exact address for the MySQL database. It will be something like mysql##.secureserver.com. The exact value of ## will differ. I had to implicitly specify the host database address in the connection parameters (host=mysql##.secureserver.com); the local socket didn't work.<br/>
Don't forget to chmod +x your Python scripts.  

Otherwise, things are working fine for me, so far.  

Getting Cheetah to work the way I wish it would is another matter...

