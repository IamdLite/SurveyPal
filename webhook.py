import logging

from aiogram import Dispatcher
from aiogram.utils.executor import start_webhook

from bot.commands import set_default_commands
from loader import dp, bot, config
from utils.misc.logging import logger

logging.basicConfig(level=logging.INFO)

WEBHOOK_HOST = config.WebhookConfig.host
WEBHOOK_PATH = config.WebhookConfig.path
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = config.WebhookConfig.port

async def on_startup(dp: Dispatcher):
    logger.logger.info('Bot startup')
    logger.logger.info(f'{WEBHOOK_HOST, WEBHOOK_PATH, WEBHOOK_URL}')
    
    await bot.set_webhook(WEBHOOK_URL)
    
    for admin_id in config.bot.admins:
            await bot.send_message(admin_id, 'Bot started successfully')

## To-DO Fix this isssue    
    await set_default_commands()

async def on_shutdown(dp: Dispatcher):
    logger.logger.info('Bot shutdown down..')
    
    await bot.delete_webhook()
    
    await dp.storage.close()
    await dp.storage.wait_closed()
    
    logger.logger.warning('Bye!')

if __name__ == '__main__':
    from bot.middlewares import setup_middleware
    from bot import filters, handlers
    
    setup_middleware(dp)
    
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=int(WEBAPP_PORT),
    )