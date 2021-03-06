#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'chef'
SITENAME = 'try out'
SITEURL = 'https://github.com/jgruber99/mywebsite.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/pelican-svbhack"
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#PLUGIN_PATH = './pelican-plugins'
#PLUGINS = ['ipynb.markup']

# Jupyter
#MARKUP = ('md', 'ipynb')
#IPYNB_USE_META_SUMMARY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
