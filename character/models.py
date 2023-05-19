from django.db import models


class Character(models.Model):
    # species
    HUMAN = 'HU'
    SAIYAJIN = 'SA'
    NAMEKIANO = 'NA'
    ANDROID = 'AN'
    UNDEFINED = 'UN'
    SPECIES_CHOICES = [
        (HUMAN, 'Terrícola'),
        (SAIYAJIN, 'Saiyajin'),
        (NAMEKIANO, 'Namekiano'),
        (ANDROID, 'Android'),
        (UNDEFINED, 'Undefined')
    ]

   # gender
    FEMALE = 'FE'
    MALE = 'MA'
    GENDER_CHOICES = [
        (FEMALE, 'Mujer'),
        (MALE, 'Hombre'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='characters')
    species = models.CharField(
        max_length=2, choices=SPECIES_CHOICES, blank=False)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, blank=False)

    # planet = models.ForeignKey(
    #    Planet, on_delete=models.CASCADE, related_name='planet')

    def __str__(self):
        return self.name
