from django.apps import AppConfig
import threading

class IotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iot'
    def ready(self):
        # Import mqtt_subscriber_cloud only when the app is ready
        from . import mqtt_subscriber_cloud

        # Start the MQTT subscriber in a background thread
        mqtt_thread = threading.Thread(target=mqtt_subscriber_cloud.start_mqtt_client)
        mqtt_thread.daemon = True  # Ensures the thread will exit when the main program exits
        mqtt_thread.start()
