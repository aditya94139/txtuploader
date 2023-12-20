import os

API_ID = API_ID = "18618422"

API_HASH = os.environ.get("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22ab")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6737838348:AAF6nFskxaPdtWD9OVIhnFNZ2BGPoADShaU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6050277919))

LOG = -1002113866398

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6050277919").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


