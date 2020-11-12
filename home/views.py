from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse





from django.shortcuts import render,redirect

from home.models import Contactus

from .forms import ContactusForm

from django.views.decorators.http import require_POST





from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from home.serializers import ContactsSerializer
from rest_framework.decorators import api_view





from django.contrib import messages
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request, 'home/index.html')



def list_page(request):
    contacts = Contactus.objects.order_by('id')
    form = ContactusForm()
    context = {'contacts':contacts,'form': form}
    return render(request, 'home/list_page.html',context)






def detail(request):
    contactus_items = Contactus.objects.order_by('id')
    form = ContactusForm()
    context = {'contactus_items' : contactus_items, 'form' : form}
    return render(request,'home/detail.html', context)




@require_POST
@csrf_exempt
def add(request):
    form = ContactusForm(request.POST)

    if form.is_valid():
        new_contactus = Contactus(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], description=request.POST['description'],)
        new_contactus.save()

        messages.success(request, 'Details added successfully')
    
    return redirect('detail')





@api_view(['GET','POST'])
def contacts_list(request):
    if(request.method=='GET'):
        contacts=Contactus.objects.all()
        name=request.GET.get('name',None)
        if name is not None:
            contacts=Contactus.filter(name__icontains=name)
        contacts_serializer=ContactsSerializer(contacts,many=True)
        return JsonResponse(contacts_serializer.data,safe=False)
    elif(request.method=='POST'):
        contacts_data=JSONParser().parse(request)
        contacts_serializer=ContactsSerializer(data=contacts_data)
        if contacts_serializer.is_valid():
            contacts_serializer.save()
            return JsonResponse(contacts_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(contacts_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def contacts_detail(request,pk):
    try:
        contacts=Contactus.objects.get(pk=pk)
    except Contactus.DoesNotExist:
        return JsonResponse({'message':'The contact does not exist '},status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        contacts_serializer=ContactsSerializer(contacts)
        return JsonResponse(contacts_serializer.data)
    elif(request.method=='POST'):
        contacts_data=JSONParser().parse(request)
        contacts_serializer=ContactsSerializer(contacts,data=contacts_data)
        if(contacts_serializer.is_valid()):
            contacts_serializer.save()
            return JsonResponse(contacts_serializer.data)
        return JsonResponse(contacts_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        contacts.delete()
        return JsonResponse({'message':'contact was deleted successfully! '},status=status.HTTP_204_NO_CONTENT)
