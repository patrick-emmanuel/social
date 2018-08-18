from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .helpers import recreate_image
from .models import ProfileImage
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'date_of_birth',)


class ProfileImageSerializer(serializers.ModelSerializer):

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = ProfileImage
        fields = ('image',)

    def create(self, validated_data):
        image_file = validated_data.pop('image')
        profile = validated_data.pop('profile')
        if profile is None:
            profile = Profile.objects.create(user=self.context['request'].user)
            profile_image = ProfileImage.objects.create(profile=profile, image=image_file)
        else:
            profile_image_set = ProfileImage.objects.filter(profile=profile)
            if profile_image_set:
                profile_image = recreate_image(profile_image_set[0].image, image_file)
            else:
                profile_image = ProfileImage.objects.create(profile=profile, image=image_file)
        return profile_image

    def update(self, instance, validated_data):
        pass
