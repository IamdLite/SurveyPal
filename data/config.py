import os

from dotenv import load_dotenv

from dataclasses import dataclass
from pathlib import Path

DIR = Path(__file__).resolve().parent
I18N_DOMAIN = 'bot'
LOCALES_DIR = f'{DIR}/locales'
ADMINS = [int(_) for _ in os.getenv('ADMINS', default='').split()]
RATE_LIMIT = os.getenv('RATE_LIMIT')


@dataclass
class WebhookConfig:
    host: str
    port: int
    path: str

@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str
    
@dataclass
class BotConfig:
    token: str
    admins: tuple[int]
    # password: str
    # username: str
    # database: str

@dataclass
class Config:
    token: str
    admins: tuple[int]
    use_redis: bool 
    redis_password: str = None
    
@dataclass
class Config:
    bot: BotConfig
    # database: DatabaseConfig
    WebhookConfig: WebhookConfig

def load_config():
    load_dotenv()
    
    return Config(
        bot=BotConfig(
        token=os.getenv('BOT_TOKEN'),
        admins=os.getenv('ADMINS', default='').split()
        # password = os.getenv('BOT_PASSWORD'),
        # database=os.getenv('BOT_DATABASE'),
        ),
        
    #     database = DatabaseConfig(
    #         host=os.getenv('DB_HOST'),
    #         port=int(os.getenv('DB_PORT')),
    #         user=os.getenv('DB_USER'),
    #         password=os.getenv('DB_PASSWORD'),
    #         database=os.getenv('DB_NAME')    
    # ),
        WebhookConfig = WebhookConfig(
            host=os.getenv('WEBHOOK_HOST'),
            port= os.getenv('WEBHOOK_PORT'),
            path=os.getenv('WEBHOOK_PATH')
        )
    )
# config = load_config().bot