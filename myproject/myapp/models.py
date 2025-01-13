from django.db import models
class SemesterNote(models.Model):
    REGULATION_CHOICES = [
        ('MIC18', 'MIC18'),
        ('MIC20', 'MIC20'),
        ('MIC23', 'MIC23'),
    ]

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('EEE', 'Electrical'),
        ('MECH', 'Mechanical'),
        ('CIV', 'Civil'),
        ('AID', 'Artificial Intelligence and DS'),
        ('AIM', 'Artificial Intelligence & ML'),
        ('MBA', 'MBA'),
        ('MCA', 'MCA'),
        ('MTECH', 'M.Tech'),
    ]

    SEMESTER_CHOICES = [
        ('SEM1', 'Semester 1'),
        ('SEM2', 'Semester 2'),
        ('SEM3', 'Semester 3'),
        ('SEM4', 'Semester 4'),
        ('SEM5', 'Semester 5'),
        ('SEM6', 'Semester 6'),
        ('SEM7', 'Semester 7'),
        ('SEM8', 'Semester 8'),
    ]

    regulation = models.CharField(max_length=10, choices=REGULATION_CHOICES)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    title = models.CharField(max_length=255, default="Untitled")
    pdf = models.FileField(upload_to='semester_notes/')

    def __str__(self):
        return f"{self.regulation} - {self.branch} - {self.semester}"
