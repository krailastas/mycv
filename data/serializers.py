from rest_framework import serializers

from .models import Main, Jobs, Skils


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class SkilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skils
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    jobs = JobsSerializer(many=True, read_only=True)
    languages = LanguagesSerializer(many=True, read_only=True)
    skils = SkilsSerializer(many=True, read_only=True)

    class Meta:
        model = Main
        fields = '__all__'

