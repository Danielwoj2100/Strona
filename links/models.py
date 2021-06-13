from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Kurs(models.Model):
    nazwa = models.CharField(max_length=256)
    kategoria = models.ForeignKey('Kategoria', models.DO_NOTHING, db_column='nazwa_kategorii',default=None)

    class Meta:
        managed = True
        db_table = 'kursy'
        verbose_name_plural = "kursy"
    def __str__(self):
        return str(self.nazwa)

class Kategoria(models.Model):
    nazwa_kategorii = models.CharField(max_length=256)


    class Meta:
        db_table = 'kategorie'
        verbose_name_plural = "kategorie"
    def __str__(self):
        return str(self.nazwa_kategorii)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uczelnia = models.TextField(max_length=50, blank=True)
    wydzial = models.CharField(max_length=30, blank=True)
    kierunek = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = True
        verbose_name_plural = "profile"
    def __str__(self):
        return str(self.user.username)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Film(models.Model):
    hiperlacze = models.CharField(max_length=256)
    tytul = models.CharField(max_length=256)
    opis = models.CharField(max_length=256, default=None, null=True )
    kurs = models.ForeignKey('Kurs', models.DO_NOTHING, db_column='nazwa',default=None)

    

    class Meta:
        managed = True
        verbose_name_plural = "filmy"
        db_table = 'filmy'
    
    def __str__(self):
        return str(self.tytul) 