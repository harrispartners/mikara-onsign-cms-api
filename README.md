Python implementation to connect the OnSign CMS API.

Tags
----

Harris Partners, Python, OnSign CMS API

Development
===========

Configure a **Python v3.6.0 virtual environment** and activate.

From console go the directory root in the repo and use next commands:

+ ``virtualenv --no-site-packages env --always-copy``
+ ``source env/bin/activate``

Install dependencies:

+ ``pip install -r requirements.txt``

Only for development you should disable OAUTHLIB_INSECURE_TRANSPORT, you must not do this on production servers.

+ ``export OAUTHLIB_INSECURE_TRANSPORT=1``


Examples
=============

First you need to copy the settings.py.dist to settings.py and configure the correct values.

+ ``cp settings.py.dist settings.py``

Then run some example just like this:

+ ``python examples/misc.py``
