from django import forms
from todoApp.models import Todo
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title','description','due_date','status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.RadioSelect(),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']  # Use 'cleaned_data' instead of 'cleaned_date'
        if due_date < timezone.now().date():
            raise forms.ValidationError(_("Due date cannot be in the past."))
        return due_date

    
class TodoSearchForm(forms.Form):
   search_query = forms.CharField(max_length=100, required=False, label='Search') 