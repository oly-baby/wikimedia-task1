from django import forms
from .models import Bug
from django.forms.widgets import DateInput
from django.utils import timezone


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ["bug_description", "bug_type", "bug_report_date", "bug_status"]
        widgets = {
            'report_date': forms.DateInput(attrs={'type': 'date'}),
        }

