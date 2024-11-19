from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


class aboutView(viewsets.ModelViewSet):
    queryset = about.objects.all()
    serializer_class = aboutSerializer
    parser_classes = (MultiPartParser, FormParser)


class projectHomeView(viewsets.ModelViewSet):
    queryset = projectHome.objects.all()
    serializer_class = projecctHomeSerializer
    parser_classes = (MultiPartParser, FormParser)


class projectView(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer
    parser_classes = (MultiPartParser, FormParser)


class cvView(viewsets.ModelViewSet):
    queryset = cv.objects.all()
    serializer_class = cvSerializer
    parser_classes = (MultiPartParser, FormParser)


@api_view(["POST"])
def contact_view(request):
    serializer = contactSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        name = validated_data.get("name")
        phoneNumber = validated_data.get("phoneNumber")
        email = validated_data.get("email")
        message = validated_data.get("message")

        contact.objects.create(
            name=name, phoneNumber=phoneNumber, email=email, message=message
        )
        return Response({"message": "Form data received and saved"})
    else:
        return Response(serializer.errors, status=400)
