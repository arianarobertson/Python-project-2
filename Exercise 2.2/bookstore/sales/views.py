from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm
from .models import Sale
import pandas as pd
from .utils import get_bookname_from_id, get_chart
from .utils import get_chart

# Create your views here.

def home(request):
    return render(request, 'sales/home.html')

@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)

    # Initialize variables
    sales_qs = None
    sales_df = None
    chart = None

    if request.method == 'POST':
        book_title = request.POST.get('book_name')
        chart_type = request.POST.get('chart_type')

        # Filter by book title
        sales_qs = Sale.objects.filter(book__name=book_title)

        if sales_qs.exists():
            # Convert queryset to DataFrame
            sales_df = pd.DataFrame(sales_qs.values())

            # Replace book_id with book name for readability
            sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)

            # ✅ Use "date" (your field) instead of "date_created"
            chart = get_chart(chart_type, sales_df, labels=sales_df['date'].values)

    context = {
        'form': form,
        'sales_qs': sales_qs,
        'sales_df': sales_df,
        'chart': chart,
    }
    return render(request, 'sales/records.html', context)