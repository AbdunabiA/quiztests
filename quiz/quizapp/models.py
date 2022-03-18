from django.db import models

class Quiz(models.Model):
    nom = models.CharField(max_length=30)
    batafsil = models.CharField(max_length=150)
    savol_soni = models.PositiveSmallIntegerField()
    davomiyligi = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nom
class Savol(models.Model):
    matn = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.matn
class Javob(models.Model):
    matn = models.CharField(max_length=200)
    togri = models.BooleanField(default=False)
    savol = models.ForeignKey(Savol, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.matn