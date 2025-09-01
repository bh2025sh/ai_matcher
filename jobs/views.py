from rest_framework import viewsets, permissions, decorators, response, status
from accounts.permissions import IsAdminUserRole
from accounts.models import CandidateProfile
from .models import Job
from .serializers import JobSerializer
from matching.services import rank_candidates_for_job

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by("-created_at")
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy", "recommendations", "list", "retrieve"]:
            return [permissions.IsAuthenticated(), IsAdminUserRole()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @decorators.action(detail=True, methods=["get"], url_path="recommendations")
    def recommendations(self, request, pk=None):
        job = self.get_object()
        top = int(request.query_params.get("top", 5))
        candidates = CandidateProfile.objects.select_related("user").all()
        ranked = rank_candidates_for_job(job, candidates, top=top)
        return response.Response(ranked, status=status.HTTP_200_OK)
