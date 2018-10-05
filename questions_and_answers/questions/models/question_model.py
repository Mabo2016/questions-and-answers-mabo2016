from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Question(models.Model):
    """A question asked by registered users on a certain topic"""

    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="This will be displayed when browsing the list of questions"
    )

    date_time_posted = models.DateField(auto_now = True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        help_text="Explain the question in detail"
    )

    up_votes_count = models.IntegerField(
        default=0,
    )

    down_votes_count = models.IntegerField(
        default=0,
    )

    def __str__(self):
        """Identifies the object"""
        return f"{self.title}"

    def get_absolute_url(self):
        """Returns url to detail page of the question"""
        return reverse("question_detail", args = [str(self.id)])
