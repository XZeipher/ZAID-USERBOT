import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID","7902063694"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "7081283522:AAElDVzZhtj9JfSuIUpEyKEvxfSF10cYLtc")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCMBx8AIGtYMQ1HjWf_DaFGoLEIB6w28bLuTz_535mhzVp8rYlPPiJevA2Xs_SaSfc_FtwBv13fhqJNIx62ACnrEBFaHdcJAgwsS1axRbOrd8JXQfaZexqkXsC5pz01bf5AOyxTNMiXUjuwTfFGJsY_yHI5b7hgblp4rMdUNUWn95B_pFeNWXffA5mJT_XCU4-gln4vNQMxUuGmJFXBFuRZRWOaNsUqLuyKzZoZdkuHVi1I45l8sHtTxUFu4GgClW2ixPiGJBEouWGJbNCLqzNk1t41HfBsGrOjRgwH8QHXBS8USw0wsLMLrRlnVW6jF0fryHtDQDRV497-vgrqo5Hmb9Nl0AAAAAHW_-xOAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
