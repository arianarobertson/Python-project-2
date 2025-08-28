from django import forms    # import django forms

# specify chart type choices
CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

# define class-based Form imported from Django forms
class SalesSearchForm(forms.Form): 
    book_name = forms.CharField(max_length=120, label="Book Title")
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
