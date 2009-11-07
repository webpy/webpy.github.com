---
layout: default
title: Installazione
---

# Installazione

Prima di installare web.py dobbiamo scaricare i sorgenti:
    
    http://webpy.org/static/web.py-0.33.tar.gz

estraiamolo e copiamo la cartella "_web_" in una directory dove risiede la nostra applicazione.
Se invece vogliamo rendere web.py accessibile a tutte le applicazioni, dobbiamo installarlo in modo che sia reperibile nella cartella dei moduli di python.
Facciamo questo danto il seguente comando:
    
    python setup.py install

Nota: su alcuni sistemi unix-like bisogna, prima di dare il precedente comando, acquisire i privilegi di root (amministratore di sistema), o usare il comando sudo, come segue:

    sudo python setup.py install

guarda il [setup raccomandato](/recommended_setup) -in inglese-.

Un'altra opzione è quella di usare[Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall). Una volta che [Easy Install](http://peak.telecommunity.com/DevCenter/EasyInstall) è stato settato correttamente, usare il seguente comando per installare automaticamente web.py:


    easy_install web.py

## Sviluppo

Web.py è fornito con un webserver integrato. Impara a creare una applicazione con web.py seguento il [tutorial](http://webpy.org/tutorial2) -inglese-.  Una volta che avrai scritto la tua applicazione, supponendo che il file si chiami "code.py", avvialo con il seguente comando:

     python code.py

Apri il tuo browser e vai alla pagina [http://localhost:8080/](http://localhost:8080/) per vedere la tua applicazione funzionante! Se non vuoi usare la porta 8080, ma invece un'altra, fai seguire al precedente comando il numero della porta voluta: `python code.py 1234`.

##  Produzione

Il webserver fornito con web.py è utile in fase di sviluppo, ma per siti popolari che richiedono maggiori prestazioni avrai bisogno di qualcosa di più serio e performante. Web.py implementa [WSGI](http://www.python.org/dev/peps/pep-0333/) e viene eseguito su qualunque webserver che supporti questo standard. WSGI è una API standard di comunicazione tra il webserver e l'applicazione, analogamente alla Interfaccia Servlet di Java. Per eseguire web.py con CGI, FastCGI o SCGI avrai bisogno di installare anche [flup](http://trac.saddi.com/flup) ([download here](http://www.saddi.com/software/flup/dist/)), che fornisce una interfaccia WSGI per queste API.

Per tutte le varianti CGI (CGI, FastCGI, SCGI), aggiungi all'inizio del sorgente della tua applicazione (nell'esempio precedente "code.py"):

    #!/usr/bin/env python

ed esegui `chmod +x code.py` per renderlo eseguibile.

### LightTPD

#### ... con FastCGI

FastCGI con lighttpd è la soluzione raccomandata di usare web.py in fase di produzione. [reddit.com][3] gestisce milioni di richieste con questa configurazione!

   [3]: http://reddit.com/

La tua configurazione per LightTPD può essere simile a questa:
    
     server.modules = ("mod_fastcgi", "mod_rewrite")
     server.document-root = "/path/to/root/"     
     fastcgi.server = ( "/code.py" =>     
     (( "socket" => "/tmp/fastcgi.socket",
        "bin-path" => "/path/to/root/code.py",
        "max-procs" => 1
     ))
     )
    
     url.rewrite-once = (
       "^/favicon.ico$" => "/static/favicon.ico",
       "^/static/(.*)$" => "/static/$1",
       "^/(.*)$" => "/code.py/$1"
     )
    

Con alcune versioni di LightTPD, è importante assicurarsi che la proprietà "check-local" di fastcgi.server sia settata a "false". Specialmente se il tuo programma (code.py) si trova fuori dalla document root del webserver.

Se ricevi qualche errore circa l'impossibilità di importare flut, installalo inserendo "easy_install flup" nell terminale (necessiti di installare easy_install, prima).

Dalla revisione 145 (della versione 0.31), è necessario settare una variabile d'ambiente nella configurazione fastcgi se la tua applicazione fà uso di redirect (redirezioni).
Se il tuo codice re-indirizza a http://dominio.com/ e nella tua barra degli indirizzi vedi http://dominio.com/code.py/ (supponendo che code.py sia la tua applicazione) avrai bisogno di settare la variabile d'ambiente.
Questo comporta una variazione della tua configurazione del webserver ala voce fastcgi.server, qualcosa come:
     
    fastcgi.server = ( "/code.py" =>
    ((
       "socket" => "/tmp/fastcgi.socket",
       "bin-path" => "/path/to/root/code.py",
       "max-procs" => 1,
       "bin-environment" => (
         "REAL_SCRIPT_NAME" => ""
       ),
       "check-local" => "disable"
    ))
    )
    
### Apache

#### .. con CGI

Aggiungi le seguenti righe al tuo file `httpd.conf` o `apache2.conf`.

    Alias /foo/static/ /path/to/static
    ScriptAlias /foo/ /path/to/code.py


#### .. con CGI usando il file .htaccess

CGI è facile da configurare, ma non è adeguato per i siti che richiedono elevate prestazioni.
Per usare web.py con CGI aggiungi le seguenti righe al tuo `.htaccess`:

    Options +ExecCGI
    AddHandler cgi-script .py

e scrivi nella barrra degli indirizzi del tuo browser `http://example.com/code.py/`. Non dimenticare lo slash (barra) finale, altrimenti vedrai visualizzato un messaggio `not found` (non trovato) (poichè la lista delle url che hai definito non combacia con niente). Per rendere funzionante l'applicazione senza il bisogno di inserire nell'indirizzo `code.py` devi aver abilitato il modulo mod_rewrite e aggiungere nella configurazione le appropriate regole.

Nota: Il modo in cui `web.py` è implementato non lavora con il modulo `cgitb` poichè cattura lo `stdout`.
    
    import cgitb; cgitb.enable()
    import sys
    
    # ... import web etc qui...
    
    def cgidebugerror():
        """                                                                         
        """        _wrappedstdout = sys.stdout
    
        sys.stdout = web._oldstdout
        cgitb.handler()
    
        sys.stdout = _wrappedstdout
    
    web.internalerror = cgidebugerror

#### .. con FastCGI

FastCGI è facile da configurare e agisce come mod_python.
Aggiungi quanto segue al tuo `.htaccess`:
    
    <Files code.py>      SetHandler fastcgi-script
    </Files>

Sfortunatamente, diversamente da lighttpd, Apache non accenna al fatto che vuole che il codice della tua applicazione agisca come un server FastCGI quindi a web.py devi dirlo esplicitamente. Puoi farlo aggiungendo al tuo `code.py` prima della riga in cui scrivi `if __name__ == "__main__":`
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    
e indirizza il tuo browser a `http://example.com/code.py/`. Non dimenticare lo slash (barra) finale, altrimenti vedrai visualizzato un messaggio `not found` (non trovato) (poichè la lista delle url che hai definito non combacia con niente). Per rendere funzionante l'applicazione senza il bisogno di inserire nell'indirizzo `code.py` devi aver abilitato il modulo mod_rewrite e aggiungere nella configurazione le appropriate regole.

[Walter ha altri consigli](http://lemurware.blogspot.com/2006/05/webpy-apache-configuration-and-you.html)[e](http://www.dofollownet.com/).

#### .. con SCGI
https://www.mems-exchange.org/software/scgi/
scarica i sorgenti di `mod_scgi` da qui: http://www.mems-exchange.org/software/files/mod_scgi/
Per gli utenti apache su Windows: 
edita il tuo httpd.conf come segue:

    LoadModule scgi_module Modules/mod_scgi.so
    SCGIMount / 127.0.0.1:8080

riavvia il webserver apache e poi avvia la tua applicazione code.py con il seguente comando:

    python code.py 127.0.0.1:8080 scgi

e apri il tuo browser, visita 127.0.0.1
E' tutto a posto! 

#### .. con mod_python

mod_python funziona come FastCGI, ma non è semplice da configurare.

Per python2.5 segui questi comandi:

    cd /usr/lib/python2.5/wsgiref
    # o in windows: cd /python2.5/lib/wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # o richiedi il file dal tuo browser

Per python < 2.5 (precedente a 2.5) fai questo:

    cd /usr/lib/python2.4/site-packages
    # o in windows: cd /python2.4/lib/site-packages
    svn co svn://svn.eby-sarna.com/svnroot/wsgiref/wsgiref
    cd wsgiref
    wget -O modpython_gateway.py http://projects.amor.org/misc/browser/modpython_gateway.py?format=raw
    # o richiedi il file dal tuo browser 


Rinomina il tuo `code.py` a qualcosa come `codep.py` e aggiungi:
    
    main = web.wsgifunc(web.webpyfunc(urls, globals()))

Nel tuo `.htaccess`, aggiungi:
    
    
    AddHandler python-program .py
    PythonHandler wsgiref.modpython_gateway::handler
    PythonOption wsgi.application codep::main
    

Probabilmente tu vorrai aggiungere una `RewriteRule` che punta `/` a `/codep.py/`

Sii sicuro di visitare `/codep.py/` con lo slash `/` extra alla fine. Altrimenti vedrai un messaggio di errore come `A server error occurred. Please contact the administrator.`

#### .. con mod_wsgi

mod\_wsgi è un nuovo modulo Apache che [tipicamente supera le peformance di mod_python](http://code.google.com/p/modwsgi/wiki/PerformanceEstimates)per hostare applicazioni WSGI, ed è veramente semplice da settare.

Alla fine del tuo `code.py`, aggiungi:

    application = web.wsgifunc(web.webpyfunc(urls, globals()))

mod\_wsgi offre [molti modi](http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives) per esporre una applicazione WSGI nella gerarchia delle url di apache, ma una semplice via può essere quella di aggiungere le seguenti righe al tuo file .htaccess:

    <Files code.py>
        SetHandler wsgi-script
        Options ExecCGI FollowSymLinks
    </Files>

Se ottieni un errore di tipo "ImportError: No module named web" nel tuo error.log di apache, potrai provare a settare il percorso assoluto in code.py prima di importare web (moduli web.py):

    import sys, os
    abspath = os.path.dirname(__file__)
    sys.path.append(abspath)
    os.chdir(abspath)
    import web

Inoltre, potresti voler leggere la sezione "Application Working Directory" da [Common problems with WSGI application](http://code.google.com/p/modwsgi/wiki/ApplicationIssues)[s] (http://www.destination-casino.com/modules/news/article.php?storyid=13) -in inglese-.

Dovrebbe essere poi accessibile a `http://example.com/code.py/` come al solito.

#### Regole di mod_rewrite per Apache

Se vuoi rendere accessibile la tua applicazione web.py all'indirizzo 'http://example.com' anzichè 'http://example.com/code.py/' aggiungi le seguenti regole al file `.htaccess`:

    <IfModule mod_rewrite.c>      
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_URI} !^/icons
      RewriteCond %{REQUEST_URI} !^/favicon.ico$
      RewriteCond %{REQUEST_URI} !^(/.*)+code.py/
      RewriteRule ^(.*)$ code.py/$1 [PT]
    </IfModule>

Se il file `code.py` è nella sottodirectory `myapp/`, modifica la RewriteBase  rendendola similie a `RewriteBase /myapp/`. Se hai file statici come i file CSS ed immagini da rendere disponibili, duplica la regola per ogni percorso tu voglia rendere disponibile. Per maggiori informazioni circa l'utilizzo delle rewrite rule di apache fai riferimento alle pagini ufficiali del modulo mod_rewrite presente sul sito ufficiale del progetto apache.