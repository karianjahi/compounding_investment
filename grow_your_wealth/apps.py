from django.apps import AppConfig


class GrowYourWealthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grow_your_wealth'
    def ready(self):
        import grow_your_wealth.signals  # 👈 this ensures signals are registered
