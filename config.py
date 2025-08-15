# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22118129"))
API_HASH = getenv("API_HASH", "43c66e3314921552d9330a4b05b18800")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "5203820046"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://maijaathu:cd1vpNwiCZQT3LvS@cluster0.4taoyli.mongodb.net/")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002843745742"))
FORCESUB = getenv("FORCESUB", "-1002888079062")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested

