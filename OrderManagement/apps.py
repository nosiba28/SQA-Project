from django.apps import AppConfig

# Configuration class for the OrderManagement app
class OrdermanagementConfig(AppConfig):
    # Define the default auto-generated primary key field for models
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define the name of the app
    name = 'OrderManagement'
