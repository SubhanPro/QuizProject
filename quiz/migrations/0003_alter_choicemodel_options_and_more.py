# Generated by Django 4.1.4 on 2023-05-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0002_choicemodel_is_true"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="choicemodel", options={"verbose_name": "Choice"},
        ),
        migrations.AlterModelOptions(
            name="questionmodel", options={"verbose_name": "Question"},
        ),
        migrations.AlterModelOptions(
            name="topicmodel", options={"verbose_name": "Topic"},
        ),
        migrations.AddField(
            model_name="topicmodel",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="topic_images/"),
        ),
    ]