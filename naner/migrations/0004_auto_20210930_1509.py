# Generated by Django 3.1.3 on 2021-09-30 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('naner', '0003_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='nota',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naner.jogo'),
        ),
    ]
