from django.db import models
from django.contrib.auth.models import User


class TopicModel(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='topic_images/', blank=True, null=True)

    class Meta:
        verbose_name = "Topic"

    def __str__(self):
        return self.name

class QuestionModel(models.Model):
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE, related_name="question")
    name = models.CharField(max_length=150)
    answer = models.TextField()

    class Meta:
        verbose_name = "Question"

    def __str__(self):
        return self.name

class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name="choice")
    name = models.CharField(max_length=150)
    is_true = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Choice"
    
    def __str__(self):
        return self.name


class UserAnwserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="anwser")
    choice = models.ForeignKey(ChoiceModel, on_delete=models.CASCADE, related_name="choice_anwser")

    class Meta:
        verbose_name = "User anwser"
    
    def __str__(self):
        return self.user.username