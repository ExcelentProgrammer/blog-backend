from django.db import models

from django.core import serializers
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


class Skills(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ko'nikmalar"
        verbose_name_plural = "Ko'nikmalar"

    def to_json(self):
        skills_data = Skill.objects.filter(skill=self)
        return {
            "name": self.name,
            "skills": skills_data.values("name", "icon")
        }

    def __str__(self):
        return str(self.name)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.TextField(null=True, blank=True)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill"

    def __str__(self):
        return str(self.name)


class Messages(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    class Meta:
            verbose_name = "Xabarlar"
            verbose_name_plural = "Xabarlar"

    def to_json(self):
        return {self.key: self.value}

    def __str__(self):
        return str(self.key)


class Experience(models.Model):
    image = models.ImageField(upload_to="experience/")
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tajriba"
        verbose_name_plural = "Tajriba"

    def __str__(self) -> str:
        return str(self.title)


class Education(models.Model):
    image = models.ImageField(upload_to="education/")
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Talim"
        verbose_name_plural = "Talim"

    def __str__(self) -> str:
        return str(self.title)


class Projects(models.Model):
    image = models.ImageField(upload_to="projects/")
    title = models.CharField(max_length=255)
    desc = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, null=True, blank=True)
    demo = models.URLField(null=True, blank=True)
    code = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Loyihalar"
        verbose_name_plural = "Loyihalar"

    def to_json(self):
        return {
            "image": "{}{}".format(settings.DOMAIN, self.image.url),
            "title": self.title,
            "desc": self.desc,
            "created_at": self.created_at,
            "skills": self.skills.values("name"),
            "demo": self.demo,
            "code": self.code,
        }
