from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from book_store.models import Publisher


def index(request):
    return render(request, "book/index.html")


def index_two(request):
    queryset = Publisher.objects.all()
    return render(request, "index.html", context={"publishers": list(queryset)})
