from rest_framework import serializers

from .models import Main, Jobs, Skils, Languages, Educations


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class SkilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skils
        fields = '__all__'


class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    jobs = JobsSerializer(many=True, read_only=True)
    languages = LanguagesSerializer(many=True, read_only=True)
    skils = SkilsSerializer(many=True, read_only=True)
    educations = EducationsSerializer(many=True, read_only=True)

    class Meta:
        model = Main
        fields = '__all__'

