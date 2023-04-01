from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/czQH55rn8y2Jk4is5")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/hvRp5UsR8j3z2wcB9")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Riyaddsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RiyaddSupport")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5519651365").split()))


FAILED = "https://images.app.goo.gl/czQH55rn8y2Jk4is5"
