from django.apps import AppConfig

class ReviewsConfig(AppConfig):
    """
    AppConfig for the Reviews app.

    This class defines configuration settings for the Reviews app, including the default auto-generated field
    and the name of the app.

    Attributes:
        default_auto_field (str): The name of the auto-generated field used for primary keys in models.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Reviews'
