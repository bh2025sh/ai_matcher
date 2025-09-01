from django.db import models
from django.conf import settings

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField(help_text="Comma-separated skills")
    min_experience = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=120, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)

    def skill_set(self):
        return {s.strip().lower() for s in self.required_skills.split(",") if s.strip()}

    def __str__(self):
        return self.title
