# Generated by Django 2.2 on 2019-04-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('Pop', 'Pop'), ('Reggae', 'Reggae'), ('Country', 'Country'), ('Jazz', 'Jazz'), ('Hip Hop', 'Hip Hop'), ('Rock', 'Rock'), ('R&B and Souls', 'R&B and Souls'), ('Dangdut', 'Dangdut')], default='Pop', max_length=25)),
                ('singer', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
