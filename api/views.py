from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Skills, Messages, Projects, Education, Experience
from api.serializers import EducationSerializer, ExperienceSerializer
from .serializers import ContactSerializer
from config.settings import bot,env


class SkillsAPI(APIView):

    def get(self, request):
        response = []
        skills = Skills.objects.all()

        for skill in skills:
            response.append(skill.to_json())

        return Response(response)


class MessagesAPI(APIView):

    def get(self, request):
        response = {}
        messages = Messages.objects.all()

        for m in messages:
            response[m.key] = m.value

        return Response(response)


class ProjectsAPI(APIView):
    def get(self, request):
        response = []

        projects = Projects.objects.all()

        for project in projects:
            response.append(project.to_json())

        return Response(response)


class EducationAPI(ListAPIView):
    model = Education
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceAPI(ListAPIView):
    model = Experience
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ContactAPI(APIView):

    serializer_class = ContactSerializer

    def post(self,request):
        
        ser = ContactSerializer(data=request.data)

        if not ser.is_valid():
            return Response({"error":ser.errors,"message":"form.not.valid","success":False})
        data = ser.data

        message = '''🤓 Yangi Xabar\n🙎‍♂️ Ism: {name}\n📬 Email: {email}\n🖌 Subject: {subject}\n✍️ Xabar: {message}'''.format(name=data.get("name"),email=data.get("email"),subject=data.get("subject"),message=data.get("message"))

        bot.send_message(chat_id=env.int("ADMIN_ID"),text=message)
        

        return Response({"response":"ok","success":True})