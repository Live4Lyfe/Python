from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("This is how we do it: Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")                # It worked!!

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to display blog {number}')

def destroy(request,number):
    return redirect("/")                # It worked!!

# Create your views here.
def one_method(request):                # no values passed via URL
    return HttpResponse("Holy Momma")

def another_method(request, my_val):	# my_val would be a number from the URL
    return HttpResponse(my_val)         # given the example above, my_val would be 23
    
def yet_another(request, name):         # name would be a string from the URL
    return HttpResponse(name)           # given the example above, name would be 'pooh'
    
def one_more(request, id, color):       # id would be a number, and color a string from the URL
    return HttpResponse(id,color)       # given the example above, id would be 17 and color would be 'brown'


# TEMPLATES    
def templates(request):                 # This works as Well :)
    context = {
	"name": "Noelle",
	"favorite_color": "turquoise",
	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

