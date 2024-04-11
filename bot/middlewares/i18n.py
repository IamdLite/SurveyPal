"""
    The i18n middleware is used to set the language of the user.
"""

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.types import Message

from data.config import I18N_DOMAIN, LOCALES_DIR

class ACLMiddleWare(I18nMiddleware):
    async def get_user_locale(self, action: str, args: list[Message, dict[str]]):
        *_, data = args
        user = data['user']
        
        return user.language
    
    def set_user_locale(self, locale: str):
        self.ctx_locale.set(locale)

    
    async def trigger(self, action, args):
        if 'update' not in action and 'error' not in action and action.startswith('process'):
            locale = await self.get_user_locale(self, action, args)
            self.set_user_locale(locale)
            return True
    
i18n = ACLMiddleWare(I18N_DOMAIN, LOCALES_DIR)