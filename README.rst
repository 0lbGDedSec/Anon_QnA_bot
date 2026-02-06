About bot
~~~~~~~~~~~~~~~~~~~~~~~~~
This is customizable telegram bot to get/send/reply anonymous messages. I'll mark some parts of the code, that you can customize. You can talk to someone and reply to messages, and no one will know who are you. In repository you can find two versions. First is full anonymous, but you cannot reply to messages, second gives you possibility to reply messages, ban users and unban users, but you will see other users IDs.

Introduction and examples
~~~~~~~~~~~~~~~~~~~~~~~~~
This bot uses Python, asynchronous interface for the Telegram Bot API. It's compatible with Python versions 3.10+.

You can use this bot to send messages, send videos, send voice messages and video messages.

To use bot you must have 

* Python 3.10 or newer

* `python-telegram-bot <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Concurrency>`_ 

* Git

Examples
--------

Text message:

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/example_1.jpg

Photo:

.. image:: https://github.com/0lbGDedSec/Pictures/blob/main/screenshots/example_2.jpg

Video:

.. image:: https://github.com/0lbGDedSec/Pictures/blob/main/screenshots/example_5.jpg

Voice message:

.. image:: https://github.com/0lbGDedSec/Pictures/blob/main/screenshots/example_3.jpg

Video message:

.. image:: https://github.com/0lbGDedSec/Pictures/blob/main/screenshots/example_4.jpg

Using 
-----

To start bot, use ``/start``. After this you can send messages or check commands by ``/help`` (commands from ``/help`` available only in replies version).


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

To install or upgrade ``python-telegram-bot`` write command below in Terminal.

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
To install starter for telegram bot - write command below in Terminal.
                                               
.. code:: shell

    $ git clone https://github.com/0lbGDedSec/Anon_QnA_bot
    $ cd Anon_QnA_bot

Configuring the code and launching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bot API Key
-----------

To get Bot API Key - follow pictures and steps below.

1. You have to find bot with username "@BotFather" and open its app.

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/bot_api_1.png

2. Than you have to click on "Create a New Bot" button.

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/bot_api_2.png

3. The next step is to enter the information for your bot and click the "Create Bot" button.

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/bot_api_3.png

4. The final step is to simply click on the "Copy" button and write it down in the BOT_TOKEN code section.

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/bot_api_4.png

User ID
-------

To find your own telegram ID - follow again next steps and pictures.

1. You have to dind bot with username "@raw_info_bot".

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/user_id_1.png

2. For now - you have to write ``/start`` to this bot and get your info.

.. image:: https://raw.githubusercontent.com/0lbGDedSec/Pictures/refs/heads/main/screenshots/user_id_2.png

Editing code
------------

After that, you need to open ``Anon_QnA_bot.py`` or ``Anon_QnA_bot(replies).py`` with any text editors and put some information in the commented lines of code.

If you have done this, you can launch your own bot.

Launching
---------

To start full anonymous version without replies - write command below in Terminal or just open file with python.

.. code:: shell

    $ python Anon_QnA_bot.py

Or start this version with replies and only user IDs.

.. code:: shell

    $ python Anon_QnA_bot(replies).py

Troubleshooting and updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If anyone have any problems with bot(s). You can write in our Telegram chat, and we will help you.

Link to chat: `Click here <https://t.me/+eN9xmS0hBJQ4ZGVi>`_

 

If you have any ideas or questions, write them in `Issues <https://github.com/0lbGDedSec/Anon_QnA_bot/issues>`_.


