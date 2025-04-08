from django.db import models

class Problem(models.Model):
    problem_uva_id = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    acceptance = models.DecimalField(max_digits=4, decimal_places=2)
    difficulty = models.CharField(max_length=50)
    solved = models.PositiveIntegerField()
    url = models.URLField()