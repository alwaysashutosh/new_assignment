from django.core.management.base import BaseCommand
from django_signals.models import ThreadTrackingModel
import threading

class Command(BaseCommand):
    help = 'Demonstrates that Django signals run in the same thread as the caller'

    def handle(self, *args, **options):
        def create_object(name):
            current_thread = threading.current_thread()
            print(f"Creating object in thread: {current_thread.name}")
            obj = ThreadTrackingModel.objects.create(name=name)
            print(f"Object {name} created")

        
        create_object("MainThreadObject")

       
        thread = threading.Thread(target=create_object, args=("ThreadObject",))
        thread.start()
        thread.join()