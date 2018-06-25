from rest_framework import serializers

from apps.address.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('street', 'lga', 'state')
