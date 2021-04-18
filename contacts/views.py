from typing import re

from django.shortcuts import render
from rest_framework.response import Response
from .models import Contact
from rest_framework.decorators import api_view
from .serializers import ContactSerializers


# Create your views here.

@api_view(['GET'])
def list_contact(request):
    contact = Contact.objects.all()
    serializer = ContactSerializers(contact, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_contact(request):
    serializer = ContactSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
