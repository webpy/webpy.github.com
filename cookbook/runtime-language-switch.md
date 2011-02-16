---
layout: default
title: Run-time language switch
---

# Run-time language switch

## Problem:
How to implement run-time language switch?

## Solution:

 * You must read [i18n support in template file](i18n_support_in_template_file) first, and then try below code.

File: code.py

    import os
    import sys
    import gettext
    import web
    
    # File location directory.
    rootdir = os.path.abspath(os.path.dirname(__file__))
    
    # i18n directory.
    localedir = rootdir + '/i18n'
    
    # Object used to store all translations.
    allTranslations = web.storage()
    
    def get_translations(lang='en_US'):
        # Init translation.
        if allTranslations.has_key(lang):
            translation = allTranslations[lang]
        elif lang is None:
            translation = gettext.NullTranslations()
        else:
            try:
                translation = gettext.translation(
                        'messages',
                        localedir,
                        languages=[lang],
                        )
            except IOError:
                translation = gettext.NullTranslations()
        return translation
    
    def load_translations(lang):
        """Return the translations for the locale."""
        lang = str(lang)
        translation  = allTranslations.get(lang)
        if translation is None:
            translation = get_translations(lang)
            allTranslations[lang] = translation
    
            # Delete unused translations.
            for lk in allTranslations.keys():
                if lk != lang:
                    del allTranslations[lk]
        return translation
    
    def custom_gettext(string):
        """Translate a given string to the language of the application."""
        translation = load_translations(session.get('lang'))
        if translation is None:
            return unicode(string)
        return translation.ugettext(string)
    
    urls = (
    '/', 'index'
    )
    
    render = web.template.render('templates/',
            globals={
                '_': custom_gettext,
                }
            )
    
    app = web.application(urls, globals())
    
    # Init session.
    session = web.session.Session(app,
            web.session.DiskStore('sessions'),
            initializer={
                'lang': 'en_US',
                }
            )
    
    class index:
        def GET(self):
            i = web.input()
            lang = i.get('lang', 'en_US')

            # Debug.
            print >> sys.stderr, 'Language:', lang

            session['lang'] = lang
            return render.index()
    
    if __name__ == "__main__": app.run()


Template file: templates/index.html.

    $_('Hello')

Don't forget to generate necessary po & mo files which used for translations. Reference: [i18n support in template file](/i18n_support_in_template_file)

Now run code.py in terminal:

    $ python code.py
    http://0.0.0.0:8080/

Now visit below addresses with your favourite web browser, check whether language changed:

    http://your_server:8080/
    http://your_server:8080/?lang=en_US
    http://your_server:8080/?lang=zh_CN

You should:

 * Make sure language code (en_US, zh_CN, etc) will be dynamic changed.
 * Make sure custom_gettext() calling  is as cheap as possible.

Reference:

 * Here is [another solution](http://groups.google.com/group/webpy/browse_thread/thread/a215837aa30e8f80 ) which use app.app_processor().