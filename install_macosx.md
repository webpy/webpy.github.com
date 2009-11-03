---
layout: default
title: install macos x
---

# install macos x

Install Webpy 0.1 via darwinports.  

Adapted from [macdevlog](http://macdevlog.com/webpy01-install.html)

0. Install [macports](http://macports.org/downloads/DarwinPorts-1.3.1-10.4.dmg).

1. update macports.
    
        sudo port selfupdate

2. Get python.  
    
        sudo port install python24

3. Install postgreSQL

        sudo port install postgresql81

4. Get web.py
    
        curl -O "http://webpy.org/web.py"
5. Install Cheetah 

        curl -O "http://jaist.dl.sourceforge.net/sourceforge/cheetahtemplate/Cheetah-1.0.tar.gz"        gunzip Cheetah-1.0.tar.gz
        tar -xvf Cheetah-1.0.tar
        rm Cheetah-1.0.tar
        cd Cheetah-1.0
        sudo python ./setup.py install
        cd ..
        sudo rm -Rf Cheetah-1.0

6. Install pyscopg

    The version in darwinports is the older 1.x code branch.  Since we've installed Postgres in to a non-standard location, we have to nugde the setup.cfg file just a little bit.

        curl -O "http://initd.org/pub/software/psycopg/psycopg2-latest.tar.gz"        tar -xzvf psycopg2-latest.tar.gz
        rm psycopg2-latest.tar.gz
        cd psycopg2-2.0.4
        echo library_dirs=/opt/local/lib/postgresql81 >> setup.cfg
        echo include_dirs=/opt/local/include/postgresql81 >> setup.cfg
        sudo python setup.py install
        cd ..
        sudo rm -Rf psycopg2-2.0.4
    
8. Download [pgadmin](http://www.pgadmin.org/download/macosx.php) (optional)

9. Setup postgresql

    To create a postgre user and group, we are going to use netinfo.  According to reports, Mas OS X 10.5 Leopard will be stripped of netinfo.  These commands are likely to be Tiger only.
    
    First, find an unused userID and groupID.  typically anything in the 200s or 300s will be unused on most Mac OS X non-server systems.  Let's assumes uid 206 and gid 207
    If you need to check which uid and gid are in use, the following netinfo commands can be used:
    
        nireport / /users name uid
        nireport / /groups name gid
    
    Make the users and groups:
    
        sudo niutil -create / /groups/postgres
        sudo niutil -createprop / /groups/postgres gid 207
        sudo niutil -create / /users/postgres
        sudo niutil -createprop / /users/postgres uid 206
        sudo niutil -createprop / /users/postgres gid 207
        sudo niutil -destroyprop / /users/postgres passwd changeme
    
    Now, we need a data store.  We can use the Users/Shared directory for this.
    
        mkdir /Users/Shared/PostgreSQL
        sudo mkdir /Users/Shared/PostgreSQL/data
        sudo chown postgres /Users/Shared/PostgreSQL/data
        sudo chgrp postgres /Users/Shared/PostgreSQL/data
        sudo -u postgres /opt/local/lib/postgresql81/bin/initdb -D /Users/Shared/PostgreSQL/data
    
    The initdb comnmand will take a moment, but output the status and notify you of success at the end.
        
10. Starting and stopping postgreSQL
    
    The -b will launch the process in the backgroud.
    
        sudo -b -u postgres /opt/local/lib/postgresql81/bin/postmaster -D /Users/Shared/PostgreSQL/data >/Users/Shared/PostgreSQL/logfile 2>&1
    
    This is how you stop a postgres process.
    
        sudo -u postgres /opt/local/lib/postgresql81/bin/pg_ctl -D /Users/Shared/PostgreSQL/data stop

11. Preparing PostgreSQL

    Create a user and a test db.  Our user is called webpy and the name of the database is webpydb.  
    
        sudo -u postgres /opt/local/lib/postgresql81/bin/createuser --no-superuser --createdb --no-createrole webpy
        sudo -u postgres /opt/local/lib/postgresql81/bin/createdb  --username=webpy webpydb
        sudo -u postgres /opt/local/lib/postgresql81/bin/createlang  plpgsql webpydb
        sudo -u postgres /opt/local/lib/postgresql81/bin/psql -c "create group webpydb"        sudo -u postgres /opt/local/lib/postgresql81/bin/psql -c "alter group webpydb add user webpy"        
    
    If these commands are successful, you should see 'CREATE ROLE', 'CREATE DATABASE', 'CREATE LANGUAGE', 'CREATE ROLE', and 'ALTER ROLE' printed out for the respective commands.  
        
12. Hardening PostgreSQL

    During most of these steps, we shell into root.  Be careful or your could break something.

        cd /Users/Shared/PostgreSQL/
        sudo sh
        cd data

    Backup the pg_hba.conf file and then remove the 1 line that starts with local and the 2 lines that start with host.  These default values are way to insecure.
    
        mv pg_hba.conf pg_hba.conf.bak
        sed -e '/^local/ d' -e '/^host / d' pg_hba.conf.bak > pg_hba.conf
    
    Make the conf file secure.  These are based off of the [Apple recommended settings](http://developer.apple.com/internet/opensource/postgres.html).  Feel free to customize if you know what you are doing.
    
        echo 'local   all         all                               md5' >> pg_hba.conf
        echo 'host    all         postgres    127.0.0.1/32          md5' >> pg_hba.conf
        echo 'host    samegroup   all         127.0.0.1/32          md5' >> pg_hba.conf
        echo 'host    all         postgres    ::1/128               md5' >> pg_hba.conf
        echo 'host    samegroup   all         ::1/128               md5' >> pg_hba.conf
        chown postgres pg_hba.conf
        exit
    
    Done with root.  All that remains is to assign passwords to the username.  Have you have ever had that dream where you go to school or work but have forgotten your pants?.  Skipping this step is kind of like that part of the dream where the cute girl is laughing and pointing at your open port.  Make sure the command outputs 'ALTER ROLE' to verify success.

        sudo -u postgres /opt/local/lib/postgresql81/bin/psql -c "alter user postgres with password 'changeme1'"        sudo -u postgres /opt/local/lib/postgresql81/bin/psql -c "alter user webpy with password 'changeme2'"            
    Time to reload and restart pgSQL

        sudo -u postgres /opt/local/lib/postgresql81/bin/pg_ctl -D /Users/Shared/PostgreSQL/data reload

---
            
You can follow the [webpy tutorial](http://webpy.org/tutorial) as long as you make the following change:    
    
    web.db_parameters = dict(dbn='postgres', user='webpy', pw='changeme2', db='webpydb')

Also, you can use the following command to send database SELECT and INSERT querys:

    /opt/local/lib/postgresql81/bin/psql webpy webpy SOME_QUERY

These folowing  two items are for production deployment.  You won't not need them if you are just taking a quick look at web.py.  If you do want to play with around with a simple server setup, the following commands will get you started.

    sudo port install lighttpd
    curl -O http://www.saddi.com/software/flup/dist/flup-r2028.tar.gz
        
    
References:

* [PostgreSQL 8.1.4 Documentation](http://www.postgresql.org/docs/8.1/interactive/)
* [PostgreSQL on Mac OS X](http://developer.apple.com/internet/opensource/postgres.html)
* [PostgreSQL for Mac OS X](http://www.macdevcenter.com/pub/a/mac/2002/06/07/postgresql.html?page=1)



[macports]: http://macports.org/