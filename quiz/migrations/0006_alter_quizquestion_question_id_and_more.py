# Generated by Django 5.1.4 on 2024-12-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_quizquestion_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='question_id',
            field=models.TextField(),
        ),
        migrations.AddConstraint(
            model_name='quizquestion',
            constraint=models.UniqueConstraint(fields=('question_id',), name='unique_question_id', opclasses=['varchar(255)']),
        ),
    ]
