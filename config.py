import os

API_ID = API_ID = 29540156

API_HASH = os.environ.get("API_HASH", "775d47859519f34f01549344a392280b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6713545950:AAG5Y-f4UDaVXeLnB1b1PV_NRW_OwaIk6m4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5684410709))

LOG = -1002100914747

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5684410709").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


