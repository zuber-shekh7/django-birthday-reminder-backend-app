from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password2': {'write_only': True}
        }

    def save(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        user = User.objects.create(
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
