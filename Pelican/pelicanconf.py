#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Sameer Sahasrabuddhe'
SITENAME = 'The Inward Spiral'
SITESUBTITLE = 'Hitchhiker in the Noosphere'
THEME = '/home/sameerds/programs/src/pelican-themes/foundation-default-colours'

PLUGIN_PATHS = ['/home/sameerds/programs/src/pelican-plugins']
PLUGINS = ['tag_cloud']

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
          ('LinkedIn', 'https://linkedin.com/in/sameerds'),
          ('GitHub Personal', 'https://github.com/sameerds'),
          ('GitHub Work', 'https://github.com/ssahasra'),
         )

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
