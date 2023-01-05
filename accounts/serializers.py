from datetime import datetime

from rest_framework import serializers
from datetime import date

from .models import Author


def is_after_today(value):
    if value > date.today():
        raise serializers.ValidationError('Не верно указана дата')


class AuthorSerializer(serializers.ModelSerializer):
    register_date = serializers.DateField(
        validators=[is_after_today, ]
    )

    class Meta:
        model = Author
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Author.objects.all(),
                fields=['name', 'phone_number'],
                message= 'ФИО не уникально'
            )
        ]

    def validate_name(self, value):
        if ' ' not in value:
            raise serializers.ValidationError("Введите ФИО полностью")
        return value

    def validate_phone(self, value):
        if "0" not in value[:1]:
            raise serializers.ValidationError("Начинай с 0")
        return value

    def validate(self, data):
        if data['register_date'].year - data['birth_date'].year < 18:
            raise serializers.ValidationError('Вам должно быть 18')
