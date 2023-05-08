from django.db import models


class Character(models.Model):
    # species
    HUMAN = 'HU'
    SAIYAJIN = 'SA'
    NAMEKIANO = 'NA'
    SPECIES_CHOICES = [
        (HUMAN, 'Humano'),
        (SAIYAJIN, 'Saiyajin'),
        (NAMEKIANO, 'Namekiano'),
    ]


   # gender
    FEMALE = 'FE'
    MALE = 'MA'
    GENDER_CHOICES = [
        (FEMALE, 'Woman'),
        (MALE, 'Man'),
    ]



    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='characters')
    species = models.CharField(max_length=2, choices=SPECIES_CHOICES, blank=False)
    gender =  models.CharField(max_length=2, choices=GENDER_CHOICES, blank=False)


    #planet = models.ForeignKey(
    #    Planet, on_delete=models.CASCADE, related_name='planet')

    def __str__(self):
        return self.name
