from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app123.models import Employee
from app123.models import Stuff
from app123.models import Aboutstuff
from .forms import LoginForm
from .forms import AddProjectForm 
from .forms import AddReviewForm 
from .forms import AddCommentForm 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Stuff
from .serializers import StuffSerializer


def index(request):
	return HttpResponse("This employee thing seems to be working....")

def form(request):
	return render(request, 'app123/form.html')
	
def detail(request,emp_id):
    return render(request, 'app123/detail.html')	
	# return HttpResponse("You have requested employee number %s." % emp_id)
	
	

def dood(request):
    pmod=Stuff.objects.all()
    mr=settings.MEDIA_ROOT
    #mu=settings.MEDIA_URL
    if request.method == 'POST':
        addprojectform = AddProjectForm(request.POST,request.FILES)
        # print addprojectform
        if addprojectform.is_valid():
		   
            newproject = addprojectform.save(commit=False)
            # print newproject
            #print request.FILES
            newproject.photo = request.FILES['photo']
            newproject.save()
            # print newproject.photo
    else:
        addprojectform = AddProjectForm()
    #newProposalNum = projectProposal.objects.filter(solved=False).count()
    return render(request, 'app123/dood.html', {'pmod': pmod,'mr':mr,'addprojectform':addprojectform})	
	
# trying to implement generic form....
	

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'app123/login.html', {'form': form})

def all(request):
    return render(request, 'app123/all.html')
	
def indoors(request):
    return render(request, 'app123/indoors.html')

def outdoors(request):
    return render(request, 'app123/outdoors.html')	
	
	
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)	


def Stuff_list(request):
    """
    List all code Stuffs, or create a new Stuff.
    """
    if request.method == 'GET':
        Stuffs = Stuff.objects.all()
        serializer = StuffSerializer(Stuffs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StuffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)		
		

def Stuff_detail(request, pk):
    """
    Retrieve, update or delete a code Stuff.
    """
    try:
        Stuff = Stuff.objects.get(pk=pk)
    except Stuff.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StuffSerializer(Stuff)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StuffSerializer(Stuff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Stuff.delete()
        return HttpResponse(status=204)	
	
def eventdetails(request):
    aboutobj = Aboutstuff.objects.all()
    mr="dummy"
    return render(request, 'app123/eventdetails.html',{'aboutobj': aboutobj,'mr':mr})	


	
	
	
def addcomment(request):
    #pmod=Stuff.objects.all()
    mr=settings.MEDIA_ROOT
    #mu=settings.MEDIA_URL
    if request.method == 'POST':
        addreviewform = AddReviewForm(request.POST,request.FILES)
        # print addreviewform
        if addreviewform.is_valid():
		   
            newreview = addreviewform.save(commit=False)
            # print newproject
            #print request.FILES
            newreview.photo = request.FILES['photo']
            newreview.save()
            # print newreview.photo
    else:
        addreviewform = AddReviewForm()
    #newProposalNum = projectProposal.objects.filter(solved=False).count()
    return render(request, 'app123/dood.html', {'mr':mr,'addreviewform':addreviewform})		