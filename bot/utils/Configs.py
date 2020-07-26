"""This module contains configuration objects."""


class Messages(object):
    """This object represents a Message."""

    START_TEXT = """
    This is a sample Bot.
    This Bot will send news for you.
    """

    HELP_TEXT = """
    This is a sample Bot.
    This Bot will send news for you.
    You can un-register or re-register by using /switchreg command.
    """

    SWITCH_REGISTRATION_TEXT = """
    Your registration switched successfully
    """
    # Add your custom messages here.


class DB(object):
    """This object represents DB configurations"""

    # Change Information or add other information.
    NAME = 'nmk1000'
    HOST = 'nmknmknmk.mysql.pythonanywhere-services.com'
    PORT = 3306
    USER = 'nmknmknmk'
    PASSWORD = 'nmk1000'

    # The table which the clients data will be stored.
    CLIENTS_TABLE = 'clients'


class RSS(object):
    """This object represents RSS configurations"""

    # The RSS address
    ADDRESS = 'http://www.theguardian.com/world/rss'


class Server(object):
    """This object represents Server configurations"""

    # The server address
    SERVER_ADDRESS = 'https://bot.server.com'

    # The web-hook address
    WEB_HOOK_ADDRESS = '/web_hook'

    # Your Bot secret token.
    TELEGRAM_TOKEN = '1296488130:AAFWbVyse8ls5xNLhzrnKCkL8kFXekN-mkc'


class CRON(object):
    """This object represents CRON configurations"""

    # Intervals to check feed, in Seconds
    CHECK_INTERVALS = 60
