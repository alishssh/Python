from django.shortcuts import render
from django.http import JsonResponse
from .models import Author
from django.http import HttpResponse

def home(request):
        return HttpResponse("Welcome to the Homepage!")

def author_list(request):
    authors = Author.objects.all().values()
    return JsonResponse(list(authors), safe=False)

def author_detail(request, id):
    try:
        author = Author.objects.get(id=id)
        return JsonResponse({'id': author.id, 'name': author.name, 'email': author.email})
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author not found'}, status=404)

    

