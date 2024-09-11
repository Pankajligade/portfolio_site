from django.core.management.base import BaseCommand
from faker import Faker
from maintain.models import LoanRecord
import random

class Command(BaseCommand):
    help = 'Populate the database with dummy loan records'

    def handle(self, *args, **kwargs):
        fake = Faker()
        loan_types = ['Personal', 'Home', 'Auto', 'Education']
        
        for _ in range(1000):
            LoanRecord.objects.create(
                account_no=fake.unique.ssn(),
                customer_id=fake.unique.uuid4(),
                loan_amount=round(random.uniform(1000, 50000), 2),
                loan_date=fake.date_this_decade(),
                interest=round(random.uniform(1, 10), 2),
                loan_type=random.choice(loan_types),
                loan_score=random.randint(300, 850)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data.'))
