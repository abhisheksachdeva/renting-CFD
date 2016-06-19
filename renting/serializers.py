from rest_framework import serializers
from renting.models import MyUser, Posts


class UserRegSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'address', 'city', 'state', 'country' 'first_name', 'last_name', 'contact_no',
                  'password', )

    def create(self, validated_data):
        user = MyUser(email=validated_data['email'], address=validated_data['address'], city=validated_data['city'],
                      state=validated_data['state'], country=validated_data['country'],
                      first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                      contact_no=validated_data['contact_no']
                      )
        user.set_password(validated_data['password'])
        user.save()
        return user

