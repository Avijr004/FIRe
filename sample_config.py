import os


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 21568806))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "83c41043d5ada58ad3dc95652afa70d5")
    eviral_STRING = os.environ.get("eviral_STRING", "1BVtsOKoBu4E9-6FZqRCVAZwRFTBMcV6NxbzyJ31WzTjH1ZCk4EQkcTnqOQM6hQ0L9kutohIhfr8k0FKg32gAhmEl9z8ouNrQNH5koUY_RhAhxgAYvPJF7HUIg-fePYTh__wP957t7sO-vnRWaQkHy85PK2_oTsrd0F1JtvGhPVbmgoyGvLVRdraQ8nRSrEC6iKkDaBFCJ6jKgbQR5t3YwmfCbpUfo1BRYaOwmlE8wyFTnZ5cnU47GAZBTiXN1HHzkBA7UVokEULFjqxZQQIMr1qT-spBQb7y6r9IJGWWfWwZL8PZ6w5YrlYRQTInkm_zTPvYKpDTnnVeK5UKIb1yUx-DFEHYO7U=")
    DB_URI = os.environ.get("DATABASE_URL", "postgres://tthweluc:8GjAmGVf0CKBrPNQ0U-8vfIg9kedaTHT@silly.db.elephantsql.com/tthweluc")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "655594746").split())
    WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "lochakpochak").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6049338121").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6811455634:AAH_TMHXyS_ZGFUCmeKcAYBVW-s9IiXXMDU")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Sk_kai_bot")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", "-1001808960170")
    if PRIVATE_GROUP_ID != :
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )


class Development(Var):
    LOGGER = True
