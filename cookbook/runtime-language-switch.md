---
layout: default
title: Run-time language switch
---

# Run-time language switch

## Problem:
How to implement run-time language switch?

## Solution:

    import os
    import sys
    import gettext
    import web
    
    # File location directory.
    rootdir = os.path.abspath(os.path.dirname(__file__))
    
    # i18n directory.
    localedir = rootdir + '/i18n'
    
    allTranslations = web.storage()
    
    # Object used to store all translations.
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
            print >> sys.stderr, 'Language:', lang
            session['lang'] = lang
            return render.index()
    
    if __name__ == "__main__": app.run()