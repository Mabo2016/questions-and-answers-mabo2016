from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from questions.models import Question

class Answer(models.Model):
    """An answer to a certain question"""

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Describe the answer in detail"
    )

    date_time_posted = models.DateField(auto_now = True)

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    up_votes_count = models.IntegerField(
        default=0,
    )

    down_votes_count = models.IntegerField(
        default=0,
    )

    def __str__(self):
        """Identifies the object"""
        return f"Answer {self.id} to {self.question.title}"

    def get_absolute_url(self):
        """Returns url to detail page of the answer"""
        return reverse("answer_detail", args = [str(self.id)])
