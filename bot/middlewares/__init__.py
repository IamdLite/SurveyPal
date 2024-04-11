def setup_middleware(dp):
    from .i18n import i18n
    
    
    dp.middleware.setup(i18n)