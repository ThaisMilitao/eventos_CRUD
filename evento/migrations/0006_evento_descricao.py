# Generated by Django 4.2.1 on 2023-06-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0005_alter_evento_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='descricao',
            field=models.TextField(null=True, verbose_name='descricao'),
        ),
    ]
