import logging
import ptvsd
ptvsd.enable_attach(address =('0.0.0.0',5678))
ptvsd.wait_for_attach()

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/errbot/data'
BOT_EXTRA_PLUGIN_DIR = r'/errbot/plugins'

BOT_LOG_FILE = r'/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@xiaolong', )  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!

BOT_IDENTITY = {
  'token': 'xoxb-480833052976-492872057856-PzFP4VYTN6JIJDOFH1EqTu2D'
}