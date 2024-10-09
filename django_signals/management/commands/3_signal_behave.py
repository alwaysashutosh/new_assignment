from django.db import models, transaction
from django.db.models.signals import post_save
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django_signals.models import SignalBehave, RelatedModel


class Command(BaseCommand):
    help = 'Demonstrates that Django signals run in the same transaction as the caller'

    def handle(self, *args, **options):
        # Scenario 1: Successful transaction
        with transaction.atomic():
            obj = SignalBehave.objects.create(name="Test1")
            print("Main transaction completed")

        # Verify both objects exist
        print(f"SignalBehave count: {SignalBehave.objects.count()}")
        print(f"RelatedModel count: {RelatedModel.objects.count()}")

        # Scenario 2: Failed transaction due to integrity error
        try:
            with transaction.atomic():
                obj = SignalBehave.objects.create(name="Test2")
                print("Object created, now raising IntegrityError")
                raise IntegrityError("Simulated integrity error")
        except IntegrityError:
            print("IntegrityError caught, transaction should be rolled back")

        
        print(f"SignalBehave count: {SignalBehave.objects.count()}")
        print(f"RelatedModel count: {RelatedModel.objects.count()}")

