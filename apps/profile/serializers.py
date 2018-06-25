from rest_framework import serializers

from apps.profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'date_of_birth',)

