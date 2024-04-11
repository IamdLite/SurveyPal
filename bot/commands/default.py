from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from loader import _, bot, i18n

def get_default_commands():
    commands = [
        BotCommand(command="/start", description=_("Start the bot")),
        BotCommand(command="/help", description=_("Get help")),
        BotCommand(command="/view", description=_("Settings")),
        BotCommand(command="/surveys", description=_("Show ongoing surveys")),
        BotCommand(command="/create", description=_("Change language")),
        BotCommand(command="/lang", description=_("Change language")),
        BotCommand(command="/feedback", description=_("Cancel the current operation")),
    ]
    
    return commands

async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())

    for lang in i18n.available_locales:
        await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeChat(), language_code=lang)
    
async def set_user_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(get_default_commands(commands_lang), scope=BotCommandScopeChat(user_id))