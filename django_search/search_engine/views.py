from django.shortcuts import render
import names

from .models import contentModel

def index(request):
    dbcontent = contentModel.objects.all()
    if not dbcontent:
        for _ in range(50):
            name = names.get_full_name()
            contentModel_obj = contentModel(content=name)
            contentModel_obj.save()
    return render(request, 'search.html')

def search_results(request):
    query = request.POST['query']
    results = contentModel.objects.all()
    if query:
        results = contentModel.objects.filter(content__icontains=query)

    return render(request, 'results.html',{'results':results})