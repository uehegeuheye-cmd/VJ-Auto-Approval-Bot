# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "36154467"))
    API_HASH = getenv("API_HASH", "20830bf1774be22f6e71062add7048f0")
    BOT_TOKEN = getenv("BOT_TOKEN", "7053950485:AAFl5dQ4Itnv3OGxll2ZzVrxm6hCJjTKkDI")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "8470897487").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://uehegeuheye:<pO3wD0nJFU5nDY4O>@cluster0.jv4ebii.mongodb.net/?appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
