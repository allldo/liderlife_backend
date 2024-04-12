from django.db.models import Q
from django.http import Http404

import smtplib

from django.core import mail

from django.conf import settings
from django.template.loader import render_to_string
from django.template import Context
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.exceptions import MultipleObjectsReturned
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone

from rest_framework import status

from .models import *
from .service import PaginationProduct
from .serializers import *

import uuid

from django.http import JsonResponse


class GetTextMain(APIView):
    def get(self, request, format=None):
        lead = TextMain.objects.all()
        serializer = TextMainSerializer(lead, many=True)
        return Response(serializer.data)


class TeamView(APIView):
    def get(self, request, format=None):
        lead = Team.objects.all()
        serializer = TeamSerializer(lead, many=True)
        return Response(serializer.data)


class GetMainSoloSlider(APIView):
    def get(self, request, format=None):
        lead = MainSoloSlider.objects.all()
        serializer = MainSoloSliderSerializer(lead, many=True)
        return Response(serializer.data)


class GetMainGalery(APIView):
    def get(self, request, format=None):
        lead = MainGalery.objects.all()
        serializer = MainGalerySerializer(lead, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = UserProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FullTeamInfo(APIView):
    def get(self, request, format=None):
        lead = CategoryTeam.objects.all()
        serializer = CategoryTeamSerializer(lead, many=True)
        return Response(serializer.data)


class ProgrammsFullInfo(APIView):
    def get(self, request, format=None):
        lead = Programms.objects.filter(draft=False).order_by("-date_added")
        serializer = ProgrammsSerializer(lead, many=True)
        return Response(serializer.data)


class ProgrammsSmallInfo(APIView):
    def get(self, request, format=None):
        lead = Programms.objects.filter(draft=False)
        serializer = ProgrammsSmallInfoSerializer(lead, many=True)
        return Response(serializer.data)


class ProgrammsFormInfo(APIView):
    def get(self, request, format=None):
        lead = Programms.objects.filter(draft=False)
        serializer = ProgrammsFormInfoSerializer(lead, many=True)
        return Response(serializer.data)


class GetSmenaInfo(APIView):
    def get(self, request, pk, format=None):
        smena = Smena.objects.filter(programm_id=pk)
        serializer = SmenaSerializer(smena, many=True)
        return Response(serializer.data)


class PostReserve(APIView):
    def post(self, request, format=None):
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTemplateObject(APIView):
    def get_object(self, pk):
        try:
            return Template.objects.get(programm=pk)
        except Template.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = TemplateSerializer(item)
        return Response(serializer.data)


class GetSlugProgramm(APIView):
    def get_object(self, slug):
        try:
            return Programms.objects.get(slug=slug)
        except Programms.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        programm = self.get_object(slug)
        serializer = ProgrammsSerializer(programm)
        return Response(serializer.data)


class GetProgramm(APIView):
    def get_object(self, pk):
        try:
            return Programms.objects.get(id=pk)
        except Programms.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        programm = self.get_object(pk)
        serializer = ProgrammsSerializer(programm)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def send_email_new_reserve(request):
    fio = request.data.get("fio", "")
    email = request.data.get("email", "")
    data_uchast = request.data.get("data_uchast", "")
    data_parent = request.data.get("data_parent", "")
    primechanie = request.data.get("primechanie", "")
    phone = request.data.get("phone", "")
    dop_phone = request.data.get("dop_phone", "")
    info_title = request.data.get("info_title", "")
    programm_info = request.data.get("programm_info", "")
    data_smeni = request.data.get("data_smeni", "")

    # HOST = "smtp.gmail.com"
    # PORT = 587

    # FROM_EMAIL = "info@liderlife.ru"
    # TO_EMAIL = "info@liderlife.ru"
    # PASSWORD = "cnlsurrdfxdpinyq"

    # smtp = smtplib.SMTP(HOST, PORT)

    # status_code, response = smtp.ehlo()
    # print(f"[*] Echoing the server: {status_code} {response}")

    # status_code, response = smtp.starttls()
    # print(f"[*] Starting TLS connection: {status_code} {response}")

    # status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    # print(f"[*] Logging in: {status_code} {response}")

    subject, from_email, to = (
        "Новое бронирование",
        "camp@liderlife.ru",
        "camp@liderlife.ru",
    )
    # subject, from_email, to = 'Новое бронирование', 'jakupovdmit@yandex.ru', 'info@liderlife.ru'
    # connection = mail.get_connection()
    # connection.open()

    text_content = render_to_string(
        "email.txt",
        {
            "fio": fio,
            "email": email,
            "data_uchast": data_uchast,
            "data_parent": data_parent,
            "primechanie": primechanie,
            "phone": phone,
            "dop_phone": dop_phone,
            "info_title": info_title,
            "programm_info": programm_info,
            "data_smeni": data_smeni,
        },
    )
    html_content = render_to_string(
        "email.html",
        {
            "fio": fio,
            "email": email,
            "data_uchast": data_uchast,
            "data_parent": data_parent,
            "primechanie": primechanie,
            "phone": phone,
            "dop_phone": dop_phone,
            "info_title": info_title,
            "programm_info": programm_info,
            "data_smeni": data_smeni,
        },
    )

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return Response({"Message": "Сообщение отправлено успешно"})


@api_view(["GET", "POST"])
def send_email_new_reserve_client(request):
    fio = request.data.get("fio", "")
    email = request.data.get("email", "")
    data_uchast = request.data.get("data_uchast", "")
    data_parent = request.data.get("data_parent", "")
    phone = request.data.get("phone", "")
    dop_phone = request.data.get("dop_phone", "")
    programm_info = request.data.get("programm_info", "")
    data_smeni = request.data.get("data_smeni", "")

    subject, from_email, to = (
        "Предварительное бронирование",
        "camp@liderlife.ru",
        f"{email}",
    )
    # subject, from_email, to = 'Предварительное бронирование', 'jakupovdmit@yandex.ru', f'{email}'

    text_content = render_to_string(
        "email_reserve.txt",
        {
            "fio": fio,
            "email": email,
            "data_uchast": data_uchast,
            "data_parent": data_parent,
            "phone": phone,
            "dop_phone": dop_phone,
            "programm_info": programm_info,
            "data_smeni": data_smeni,
        },
    )
    html_content = render_to_string(
        "email_reserve.html",
        {
            "fio": fio,
            "email": email,
            "data_uchast": data_uchast,
            "data_parent": data_parent,
            "phone": phone,
            "dop_phone": dop_phone,
            "programm_info": programm_info,
            "data_smeni": data_smeni,
        },
    )

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return Response({"Message": "Сообщение отправлено успешно"})


@api_view(["GET", "POST"])
def send_email_callback_client(request):
    name = request.data.get("name", "")
    phone = request.data.get("phone", "")

    # subject, from_email, to = (
    #     "Предварительное бронирование",
    #     "camp@liderlife.ru",
    #     "camp@liderlife.ru",
    # )

    # TODO: Replace by actual email
    subject, from_email, to = (
        "Предварительное бронирование",
        "redzumi@yandex.ru",
        "redzumi@yandex.ru",
    )

    text_content = render_to_string(
        "callback.txt",
        {"name": name, "phone": phone},
    )
    
    print(text_content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.send()
    return Response({"Message": "Сообщение отправлено успешно"})


# class MyProfile(APIView):
#     def get_object(self, pk):
#         try:
#             return UserProfile.objects.get(id=pk)
#         except UserProfile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         myaccount = self.get_object(pk)
#         serializer = UserProfileSerializer(myaccount)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         myaccount = self.get_object(pk)
#         serializer = UserProfileSerializer(myaccount, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
