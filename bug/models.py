from django.db import models

# Create your models here.


class Bug(models.Model):

    BUG_TYPE = (
        ('error', 'error'),
        ('new features', 'new features'),
        ('new deployment', 'new deployment')
    )
    BUG_STATUS = (
        ('Done', 'Done'),
        ('TO do', 'TO do'),
        ('In progress', 'In progress'),
        ('Almost Done', 'Almost Done')
    )
    bug_description = models.TextField()
    bug_type = models.CharField(max_length=50, choices=BUG_TYPE)
    bug_report_date = models.DateField(blank=True, null=True)
    bug_status = models.CharField(max_length=50, choices=BUG_STATUS)

    def __str__(self):
        return self.bug_description

