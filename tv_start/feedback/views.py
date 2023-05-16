from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from .utils import send_feedback_email

class FeedbackView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # send_feedback_email(serializer.data)
            return redirect(request.META['HTTP_REFERER']) # Отправляем пользователя обратно на предыдущую страницу
        else:
            return Response(serializer.errors, status=400)