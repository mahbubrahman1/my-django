# Generated by Django 4.0.4 on 2022-06-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating_star', models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excellent')])),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.actor')),
            ],
        ),
    ]
