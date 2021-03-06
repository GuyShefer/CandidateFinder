# Generated by Django 3.2.6 on 2021-08-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PYTHON', 'Python'), ('NODEJS', 'NodeJS'), ('REACT', 'React'), ('ANGULAR', 'Angular'), ('CSS', 'Css'), ('HTML', 'Html'), ('MYSQL', 'Mysql'), ('POSTGRESQL', 'Postgressql'), ('MONGODB', 'Mongodb')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BACKEND_DEVELOPER', 'Backend Developer'), ('FRONTEND_DEVELOPER', 'Frontend Developer'), ('FULLSTACK_DEVELOPER', 'Fullstack Developer'), ('DATABASE_MASTER', 'DB Master ')], max_length=200)),
                ('skills', models.ManyToManyField(to='matcher.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(choices=[('BACKEND_DEVELOPER', 'Backend Developer'), ('FRONTEND_DEVELOPER', 'Frontend Developer'), ('FULLSTACK_DEVELOPER', 'Fullstack Developer'), ('DATABASE_MASTER', 'DB Master ')], max_length=200)),
                ('skills', models.ManyToManyField(to='matcher.Skill')),
            ],
        ),
    ]
