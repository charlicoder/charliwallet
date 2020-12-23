from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, default='inactive')
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey('poll.Choice', on_delete=models.CASCADE)
    note = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text
