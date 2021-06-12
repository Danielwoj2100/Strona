from django.db import models

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