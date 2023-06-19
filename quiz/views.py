from django.shortcuts import render, redirect
from quiz.models import TopicModel, QuestionModel, ChoiceModel, UserAnwserModel
from django.http import Http404

def index(request):
    topics = TopicModel.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'index.html', context)

def quiz_questions(request, id, number):
    topic = TopicModel.objects.get(id = id)
    questions = QuestionModel.objects.filter(topic = topic)
    #questions = topic.question.all()
    context = {
        'question': questions[number]
    }
    if request.method == "POST":
        choice_id = request.POST["choice"]
        choice = ChoiceModel.objects.get(id = choice_id)
        user_anwser = UserAnwserModel.objects.create(
            choice = choice,
            user = request.user
        )
        if number < len(questions) - 1:
            return redirect('questions', id = topic.id, number = number + 1)
        else:
            return redirect('results', topic_id = topic.id)
    return render(request, 'questions.html', context)

def results(request, topic_id):
    topic = TopicModel.objects.get(id = topic_id)
    results = UserAnwserModel.objects.filter(
        user = request.user,
        choice__question__topic = topic 
    )
    true_anwsers = results.filter(choice__is_true = True)
    context = {
        'topic': topic,
        'results': results,
        'true_anwsers': true_anwsers
    }
    return render(request, 'results.html', context)