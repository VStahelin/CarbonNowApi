from rest_framework import serializers

from imager.models import Snippets


class SnippetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippets
        fields = '__all__'