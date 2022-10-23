from django.shortcuts import render

# Create your views here.
def main(request):
    if request.method == 'POST':
        return
    return render(request, 'calculator/index.html')