==============
SCOAP3 overlay
==============

This is an source code overlay for Invenio v.2.0. It installs on top of
Invenio digital library platform source code as `explained here <http://invenio.readthedocs.org/en/latest/getting-started/overlay.html>`_.


------------
Installation
------------

To install the overlay, simply clone this repository and run:

.. code-block:: bash

    (scoap3)$ cdvirtualenv src/scoap3-next
    (scoap3)$ pip install -r requirements.txt --exists-action i

The parameter `exists-action` ignores any existing installations (for example, Invenio).

Next step is to install assets (js, css etc.):

.. code-block:: bash

    (scoap3)$ inveniomanage bower -i bower-base.json > bower.json
    Generates or update bower.json for you.
    (scoap3)$ cat .bowerrc
    {
        "directory": "scoap3/base/static/vendors"
    }
    (scoap3)$ bower install
    (scoap3)$ ls scoap3/base/static/vendors
    bootstrap
    ckeditor
    hogan
    jquery
    jquery-tokeninput
    jquery-ui
    plupload
    ...

Now you can follow the standard invenio installation and development procedures, such as running `inveniomanage collect`.

---------------------
Demosite installation
---------------------

Populate demo records and enable demo-site:

.. code-block:: bash

    (scoap3)$ cdvirtualenv src/scoap3-next
    (scoap3)$ inveniomanage demosite populate -p scoap3.base -f scoap3/testsuite/data/demo-records.xml

Start the server:

.. code-block:: bash

    (scoap3)$ inveniomanage runserver

Now you should have a running SCOAP3 demo site running at `http://localhost:4000 <http://localhost:4000>`_!

--------------------------
SCOAP3 workflow and tools
--------------------------

SCOAP3 uses `Grunt <http://gruntjs.com/>`_ and `Bower <http://bower.io/>`_ with convenient methods for compiling code, run tasks, install libraries and more. To use them, install the required dependencies as directed and then run some Grunt commands.

Install Grunt
-------------

From the command line:

1. Install ``grunt-cli`` globally with ``npm install -g grunt-cli``.

2. Navigate to the root directory, then run ``npm install``. ``npm`` will look at package.json and automatically install the necessary local dependencies listed there.


| When completed, you'll be able to run the various Grunt commands provided from the command line.

| **Unfamiliar with npm? Don't have node installed?** That's a-okay. npm stands for `node packaged modules <https://www.npmjs.org/>`_ and is a way to manage development dependencies through node.js. `Download and install node.js <http://nodejs.org/download/>`_ before proceeding.

Available Grunt commands
------------------------

| **Development**

``grunt jshint``

| This is a task to lint JavaScript according to `JSHint <http://www.jshint.com/>`_.

``grunt jsbeautifier``

| This is a task to prettifiy JavaScript according to `JSbeautifier <https://www.npmjs.org/package/grunt-jsbeautifier/>`_.

Troubleshooting dependencies
----------------------------

Should you encounter problems with installing dependencies or running Grunt commands, uninstall all previous dependency versions (global and local). Then, rerun ``npm install``.

==============
Happy hacking!
==============
