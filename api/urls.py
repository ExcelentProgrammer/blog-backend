from django.urls import path

from api.views import SkillsAPI, MessagesAPI, ProjectsAPI, EducationAPI, ExperienceAPI,ContactAPI

app_name = "skills"

urlpatterns = [
    path("skills/", SkillsAPI.as_view(), name="skills"),
    path("messages/", MessagesAPI.as_view(), name="messages"),
    path("projects/", ProjectsAPI.as_view(), name="projects"),
    path("education/", EducationAPI.as_view(), name="education"),
    path("experience/", ExperienceAPI.as_view(), name="experience"),
    path("contact/", ContactAPI.as_view(), name="contact"),
]
