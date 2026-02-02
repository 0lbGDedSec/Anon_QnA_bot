Anononymous Q&A bot
~~~~~~~~~~~~~~~~~~~~~~~~~
This is customizable telegram bot to get/send/answer anonymous messages. I'll mark some parts of the code, that you can customize.

Introduction and examples
~~~~~~~~~~~~~~~~~~~~~~~~~
This bot uses Python, asynchronous interface for the Telegram Bot API. It's compatible with Python versions 3.10+.

You can use this bot to send messages, send videos, send voice messages and video messages.

To use bot you must have 

* Python 3.10 or newer

* `python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Concurrency>`_ 

* Git

Installing
~~~~~~~~~~

Python
------
Windows
=======
For the first time - you have to install Python.

Link for the official website: `click here. <https://www.python.org/downloads/>`_

MacOS
=====
We have two methods: 

#. **Official Installer**

    1.1. **Download**: Go to `click here <https://python.org/downloads/macos/>`_ and click the download button for the latest macOS installer.

    1.2. **Run Installer**: Open the downloaded ``.pkg`` file and follow the on-screen steps, clicking "Continue", agreeing to the license, and entering your password when prompted.
    
    1.3. **Verify**: Open the Terminal (Applications > Utilities > Terminal) and type command below to see the installed version. 
    
    .. code:: shell
    
         $ python3 --version

#. **Homebrew**

    2.1. **Install Homebrew**: Open Terminal and run the installation command from brew.sh
    
    .. code:: shell
    
        $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    
    2.2. **Install Python**: After Homebrew is installed, type command below in the Terminal.
    
    .. code:: shell
    
        $ brew install python
    
    2.3. **Verify**: Check the installation via command below in the Terminal.
    
    .. code:: shell
    
        $  python3 --version

Git
---
Windows
=======
You can install Git on the official website.

Link for the official website: `click here. <https://git-scm.com/install/windows>`_

MacOS
=====


ㅤPython-telegram-bot
-------------------

To install or upgrade ``python-telegram-bot`` write

.. code:: shell

    $ pip install python-telegram-bot --upgrade

Or you can use second method

.. code:: shell

    $ git clone https://github.com/python-telegram-bot/python-telegram-bot
    $ cd python-telegram-bot
    $ pip install build
    $ python -m build

You can also use your favored package manager (such as ``uv``, ``hatch``, ``poetry``, etc.) instead of ``pip``.

Anonymous QnA Bot
-----------------
To install starter for telegram bot - write this in console.
                                               
.. code:: shell

    $ git clone https://github.com/0lbGDedSec/Anon_QnA_bot/
