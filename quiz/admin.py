from django.contrib import admin
from quiz.models import TopicModel, QuestionModel, ChoiceModel, UserAnwserModel

admin.site.register(TopicModel)
admin.site.register(QuestionModel)
admin.site.register(ChoiceModel)
admin.site.register(UserAnwserModel)