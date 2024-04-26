import os

API_ID = API_ID = 25586552

API_HASH = os.environ.get("API_HASH", "f265cba9d76dc6ad70914accbe758f47")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6987282896:AAHSaByMaus0CVFw9OkglpK96H6fKPgk_Ws")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1368753935))

LOG = -1002113866398

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6050277919 5890592765").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


