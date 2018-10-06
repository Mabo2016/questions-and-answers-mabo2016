from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from questions.models import Answer

class AnswerComment(models.Model):
    """A short reply to an answer"""

    description = models.CharField(
        max_length = 500,
        null=True,
        blank=True,
        help_text="Describe your opinion in 2-3 sentences or less",
    )

    date_time_posted = models.DateField(auto_now = True)

    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        null=True,
        help_text="The answer being replied to",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        """Identifies the object"""
        return f"Comment {self.id} by {author.username} to answer {answer.id} of question '{answer.question.title}'"

    def get_absolute_url(self):
        """Returns url to detail page of the question"""
        return reverse("question_detail", args = [str(self.answer.question.id)])
