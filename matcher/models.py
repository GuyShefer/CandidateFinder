from django.db import models

SKILL_CHOICES = [
    ('PYTHON', 'Python'),
    ('NODEJS', 'NodeJS'),
    ('REACT', 'React'),
    ('ANGULAR', 'Angular'),
    ('CSS', 'Css'),
    ('HTML', 'Html'),
    ('MYSQL', 'Mysql'),
    ('POSTGRESQL', 'Postgressql'),
    ('MONGODB', 'Mongodb'),
]

JOB_TITLE_CHOICES = [
    ('BACKEND_DEVELOPER', 'Backend Developer'),
    ('FRONTEND_DEVELOPER', 'Frontend Developer'),
    ('FULLSTACK_DEVELOPER', 'Fullstack Developer'),
    ('DATABASE_MASTER', 'DB Master '),
]

class Skill(models.Model):
    name = models.CharField(max_length=200, choices = SKILL_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, choices = JOB_TITLE_CHOICES, null=False, blank=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f'{self.name}, {self.title}'

class Job(models.Model):
    title = models.CharField(max_length=200, choices = JOB_TITLE_CHOICES, null=False, blank=False)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


