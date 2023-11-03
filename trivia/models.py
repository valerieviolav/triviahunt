from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    def __str__(self):
        return self.question_text
    def found_by_user(self, user):
        try:
            interaction = UserQuestionInteraction.objects.get(user=user, question=self)
            return interaction.viewed
        except UserQuestionInteraction.DoesNotExist:
            return False

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text
    
class UserQuestionInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} viewed {self.question}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)