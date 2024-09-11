from django.db import models
from django.utils import timezone

class Record(models.Model):
    sr_no = models.AutoField(primary_key=True)
    insert_date = models.DateTimeField(default=timezone.now)
    record_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    address = models.TextField()
    date_modified = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.record_date}"
    
from django.db import models

class LoanRecord(models.Model):
    account_no = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_date = models.DateField()
    interest = models.DecimalField(max_digits=5, decimal_places=2)
    loan_type = models.CharField(max_length=50)
    loan_score = models.IntegerField()

    def __str__(self):
        return f"Account No: {self.account_no} - Customer ID: {self.customer_id}"

