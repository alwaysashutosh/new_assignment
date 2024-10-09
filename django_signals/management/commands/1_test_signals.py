from django.core.management.base import BaseCommand
from django_signals.models import MyModel
import time

class Command(BaseCommand):
    help = 'Demonstration of  synchronous signal execution'

    def handle(self, *args, **options):
        start_time = time.time()
        
        print("Creating first object")
        obj1 = MyModel.objects.create(name="Object 1")
        print("First object created")
        
        print("Creating second object")
        obj2 = MyModel.objects.create(name="Object 2")
        print("Second object created")
        
        end_time = time.time()
        print(f"total execution time: {end_time - start_time} seconds")