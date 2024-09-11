from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from two_factor.views import OTPRequiredMixin
from django.views.generic import TemplateView

import csv
import io
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import Record

class SecuredSectionView(OTPRequiredMixin, TemplateView):
    template_name = 'maintain/secured_section.html'

@login_required
def power_bi_dashboard(request):
    return render(request, 'maintain/power_bi_dashboard.html')

@login_required
def ml_prediction(request):
    return render(request, 'maintain/ml_prediction.html')

@login_required
def crud_operations(request):
    return render(request, 'maintain/crud_operations.html')

@login_required
def report_page(request):
    return render(request, 'maintain/report_page.html')


from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_onboarding(request):
    # Logic for admin onboarding can go here, or you can just render a template
    return render(request, 'maintain/admin_onboarding.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Record
from .forms import RecordForm
from django.utils import timezone

def crud_operations(request, sr_no=None):
    if sr_no:
        record = get_object_or_404(Record, sr_no=sr_no)
        form = RecordForm(instance=record)
    else:
        record = None
        form = RecordForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            form = RecordForm(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.insert_date = timezone.now()
                record.save()
                messages.success(request, 'Record created successfully.')
                return redirect('crud_operations')
        elif action == 'update' and record:
            form = RecordForm(request.POST, instance=record)
            if form.is_valid():
                record.date_modified = timezone.now()
                form.save()
                messages.success(request, 'Record updated successfully.')
                return redirect('crud_operations')
        elif action == 'delete' and record:
            record.delete()
            messages.success(request, 'Record deleted successfully.')
            return redirect('crud_operations')

    records = Record.objects.all().order_by('-insert_date')
    return render(request, 'maintain/crud_operations.html', {'form': form, 'records': records})

def delete_record(request, sr_no):
    record = get_object_or_404(Record, sr_no=sr_no)
    if request.method == 'POST':
        record.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('crud_operations')
    return render(request, 'maintain/delete_confirmation.html', {'record': record})


import csv
import io
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import Record

def download_csv(request):
    records = Record.objects.all().values()
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
    
    response = HttpResponse(buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'
    return response


import io
import pandas as pd
from django.http import HttpResponse
from .models import Record
from datetime import datetime


def download_excel(request):
    # Fetch records from the database
    records = Record.objects.all().values()
    
    # Convert records to a list of dictionaries with timezone-naive datetimes
    data = []
    for record in records:
        record_data = {}
        for key, value in record.items():
            if isinstance(value, (pd.Timestamp, datetime)) and value.tzinfo is not None:
                record_data[key] = value.replace(tzinfo=None)  # Convert to naive
            else:
                record_data[key] = value
        data.append(record_data)
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Write DataFrame to an in-memory Excel file
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Records')
    
    # Prepare the response
    response = HttpResponse(buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="records.xlsx"'
    return response


import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import LoanRecord
from django.db.models import Q

def report_page(request):
    # Start with an empty Q object (which is always True) and build it based on filters.
    filter_criteria = Q()

    # Handle filters - using Q to allow for "OR" conditions.
    if 'date' in request.GET and request.GET['date']:
        filter_criteria |= Q(loan_date=request.GET['date'])
    if 'customer_id' in request.GET and request.GET['customer_id']:
        filter_criteria |= Q(customer_id=request.GET['customer_id'])
    if 'account_no' in request.GET and request.GET['account_no']:
        filter_criteria |= Q(account_no=request.GET['account_no'])

    # Query the database with the filters applied
    records = LoanRecord.objects.filter(filter_criteria).order_by('-loan_date')[:5]  # Display only the first 5 records

    # If the export option is selected, download CSV
    if request.GET.get('export') == 'csv':
        return export_csv(records)

    return render(request, 'maintain/report_page.html', {'records': records})

def export_csv(records):
    df = pd.DataFrame(list(records.values()))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="loan_records.csv"'

    df.to_csv(path_or_buf=response, index=False)
    return response

