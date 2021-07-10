from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
