from rest_framework import serializers

from imager.models import Snippets


class SnippetsSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Snippets
        fields = '__all__'