from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request,"html1.html",)

def bye(request):
    return render(request,"html2.html",)