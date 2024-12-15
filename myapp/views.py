from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer

def welcome_view(request):
    return render(request, 'welcome.html')

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer