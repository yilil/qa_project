from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)