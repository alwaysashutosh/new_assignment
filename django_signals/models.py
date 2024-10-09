from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def slow_function(sender, instance, created, **kwargs):
    print(f"Signal receiver started for {instance.name}")
    time.sleep(5)  # Simulate a time-consuming operation
    print(f"Signal receiver finished for {instance.name}")


class ThreadTrackingModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=ThreadTrackingModel)
def signal_handler(sender, instance, created, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name}")
    time.sleep(2)  # Simulate some work
    print(f"Signal handler for {instance.name} completed")


class SignalBehave(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=SignalBehave)
def signal_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal handler for {instance.name} completed")
    else:
        print(f"Signal handler for {instance.name} updated")

class RelatedModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

@receiver(post_save, sender=SignalBehave)
def related_model_handler(sender, instance, created, **kwargs):
    RelatedModel.objects.create(name=f"Related to {instance.name}")




    
                