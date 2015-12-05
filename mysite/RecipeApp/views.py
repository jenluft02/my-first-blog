from django.shortcuts import render

def post_list(request):
    return render(request, 'RecipeApp/post_list.html', {})
