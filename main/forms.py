from django import forms
from .models import JobApplication
from django import forms
from .models import DemoRequest

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'full_name',
            'email',
            'mobile',
            'education',
            'year_passed_out',
            'resume',
            'cover_letter'
        ]

class DemoRequestForm(forms.ModelForm):
    class Meta:
        model = DemoRequest
        fields = [
            "organization_name",
            "email",
            "mobile",
            "category",
            "custom_requirement",
        ]

        widgets = {
            "organization_name": forms.TextInput(attrs={"class": "form-control","placeholder": "Organization Name"}),

            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "Email Address"}),

            "mobile": forms.TextInput(attrs={"class": "form-control","placeholder": "Mobile Number"}),

            "category": forms.Select(attrs={"class": "form-select" }),

            "custom_requirement": forms.Textarea(attrs={"class": "form-control","rows": 4,"placeholder": "Please specify your requirement" }),
        }