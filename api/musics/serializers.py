from django.utils.timezone import now
from rest_framework import serializers
from musics.models import Music


class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')

    def get_days_since_created(self, obj):
        return (now() - obj.created).days
