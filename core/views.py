from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .serializers import ProjectSerializer
from .models import Project


class ProjectView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ContactView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get("username", None)
        subject = request.data.get("subject", None)
        message = request.data.get("message", None)
        email = request.data.get("email", None)

        if (
            name is not None
            and subject is not None
            and message is not None
            and email is not None
        ):
            try:
                email_from = settings.EMAIL_HOST_USER
                subject = email + "-" + subject
                body = name + "-" + message
                send_mail(
                    subject,
                    body,
                    email_from,
                    ["sadekirfan3@gmail.com"],
                    fail_silently=False,
                )

                return Response(
                    {"message: Your message has sent"},
                    status=status.HTTP_200_OK,
                )
            except BadHeaderError:
                return Response({"message": "Invalid header found."})
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
