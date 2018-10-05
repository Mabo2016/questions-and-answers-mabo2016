from django.shortcuts import render

def show_index(request):
    """View function for home page of site."""
    return render(request, "index.html")
