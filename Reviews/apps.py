from django.apps import AppConfig

class ReviewsConfig(AppConfig):
    """
    Configuration class for the Reviews app.

    Attributes:
        default_auto_field (str): The default primary key field type for models in the app.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Reviews'
