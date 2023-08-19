from rest_framework import serializers

from api.models import Skills, Education, Experience


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name"]
        model = Skills


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Education


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Experience


class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()
