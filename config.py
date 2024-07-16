# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21857983"))
API_HASH = getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
BOT_TOKEN = getenv("BOT_TOKEN", "7289060685:AAEfteCWvdrQoNZ2JPstVPnBv9Rql_iaLBA")
OWNER_ID = int(getenv("OWNER_ID", "833465134"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://yogesh:vFojzRVGQQKWNmoj@master.2cdyk37.mongodb.net/?retryWrites=true&w=majority&appName=MASTER")
LOG_GROUP = int(getenv("LOG_GROUP", "4258671109"))
FORCESUB = getenv("FORCESUB", "2221310765")
