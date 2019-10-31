from django.shortcuts import render

# Create your views here.
#def index(request):
#    return render(request,'basic_app/index.html')

# This example is for template filter
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'basic_app/index.html',context_dict)

# for other page
def other(request):
    return render(request, 'basic_app/other.html')

#for relative uRL page
def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')