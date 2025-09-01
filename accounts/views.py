from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import CandidateProfile
from .serializers import RegisterSerializer, CandidateProfileSerializer
from .permissions import IsCandidateUserRole

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CandidateProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsCandidateUserRole]

    def get_object(self):
        return CandidateProfile.objects.get(user=self.request.user)

