from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models import Skills, Skill, Messages, Experience, Projects,Education


class SkillsView(ModelAdmin):
    list_display = ['name']


class SkillView(ModelAdmin):
    list_display = ['name']


class MessagesView(ModelAdmin):
    list_display = ['key', "value"]


class ProjectsView(ModelAdmin):
    list_display = ['title', "created_at", "demo", "code"]


admin.site.register(Skills, SkillsView)
admin.site.register(Skill, SkillView)
admin.site.register(Messages, MessagesView)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Projects, ProjectsView)
