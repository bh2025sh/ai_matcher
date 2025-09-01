from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin (HR)"
        CANDIDATE = "CANDIDATE", "Candidate"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CANDIDATE)

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, blank=True)
    years_experience = models.PositiveIntegerField(default=0)
    skills = models.TextField(blank=True, help_text="Comma-separated skills")
    location = models.CharField(max_length=120, blank=True)
    education = models.CharField(max_length=120, blank=True)
    resume_url = models.URLField(blank=True)

    def skill_set(self):
        return {s.strip().lower() for s in self.skills.split(",") if s.strip()}

    def __str__(self):
        return f"{self.full_name or self.user.username}"
