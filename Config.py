oximport os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "27983733"))
    API_HASH = os.environ.get("API_HASH", "56ca4efd9003ada32e79409505a34ec1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7298110350:AAFkTsX0wTbNEx8VLf70X-jN7fltq5h_rho")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI0Bu68456EREmx6PjbFEjeho5mT3SaeRxrh-Eyqd_8PCR8PFLyjQ2isNNrc-Lt563NVexQdh_ho6ltY1VYgNCBemY-FySTuXASuLYQ30nXjHGQOVO0QtFDR2K9BZxfWM08XB3Q-escf11Z_nRF67ApdagD2Ndeu8nq3SE1HkCZJ6k8gfv7N9wce7WwZhyA2gueiUofy7r9KM25-nZjPvOv4Gglc2LFg9k2SMfmuwvSiqSzBYL8EhpGRi1bq3GzqVhL_W40KVFvFx5BP3-xgTP63pyphYHr-tk_U4SaKC_t5db7n6Bdh7uQOiJiRsQ35imSL-VhC4AKXfaAmj_JXjpXep4o=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "marvinnn143_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
