---
layout: default
title: Installazione
---

# Installazione

[Work in Progress - Da completare]

Prima di installare web.py dobbiamo scaricare i sorgenti:
    
    http://webpy.org/static/web.py-0.31.tar.gz

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

Dalla revisione 145, è necessario settare una variabile d'ambiente nella configurazione fastcgi se la tua applicazione fà uso di redirect (redirezioni).
Se il tuo codice re-indirizza a http://dominio.com/ e nella tua barra degli indirizzi vedi http://dominio.com/code.py/ (supponendo che code.py sia la tua applicazione) avrai bisogno di settare la vatiabile d'ambiente.
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
    
[da continuare...]