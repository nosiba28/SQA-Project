from django.apps import AppConfig

# Define AppConfig for the OrderManagement app
class OrdermanagementConfig(AppConfig):
    # Define the default auto field for model creation
    default_auto_field = "django.db.models.BigAutoField"
    
    # Define the name of the app
    name = "OrderManagement"
