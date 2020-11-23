from rest_framework import serializers

from .models import Main, Jobs


class MainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Main
        fields = ('__all__',)


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('__all__',)

