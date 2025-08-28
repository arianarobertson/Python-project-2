from books.models import Book   # import the Book model
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# define a function to convert book_id → book name
def get_bookname_from_id(val):
    bookname = Book.objects.get(id=val)
    return bookname

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6,3))

    if chart_type == '#1':  # Bar chart
        plt.bar(data['date'], data['quantity'])
        plt.xlabel("Date")
        plt.ylabel("Quantity Sold")

    elif chart_type == '#2':  # Pie chart
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels, autopct='%1.1f%%')

    elif chart_type == '#3':  # Line chart
        plt.plot(data['date'], data['price'], marker='o')
        plt.xlabel("Date")
        plt.ylabel("Price")

    else:
        print("Unknown chart type")

    plt.tight_layout()
    chart = get_graph()
    return chart
