from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'message', 'phone', 'email')
    # phone = serializers.RegexField(
    #     regex=r'^\+?\d{1,3}\)?\d{6,14}$',
    #     error_messages={
    #         'invalid': 'Некорректный номер телефона'
    #     }
    # )
    # def validate_phone(self, phone):
    #     """
    #     Проверяет, что номер телефона начинается с '+' и состоит только из цифр
    #     """
    #     if not phone.startswith('+'):
    #         phone = '+' + phone
    #     if not phone[1:].isdigit():
    #         raise serializers.ValidationError('Некорректный номер телефона')
    #     return