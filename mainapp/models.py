from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=255)
    izmerenie  = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    img = models.ImageField(upload_to='location_rick_morty', blank=True, null=True)

    def __str__(self):
        return self.title


class Character(models.Model):
    male = 'ml'
    female = 'fl'
    genderless = 'gl'
    choices_gender = [
        ('al', 'alive'),
        ('dd', 'dead'),
        ('un', 'unknown'),
    ]
    choices_live = [
        ('ml', 'male'),
        ('fm', 'female'),
        ('gl', 'genderless'),
        ('un', 'unknown')
    ]
    img = models.ImageField(upload_to='Characters_rick_morty', blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=choices_gender)
    desc = models.TextField(max_length=255)
    race = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices= choices_live)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    birth_loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location_birth')

    def __str__(self):
        return self.name


class Episode(models.Model):
    title = models.CharField(max_length=255)
    numb_episode = models.IntegerField()
    desc = models.TextField(max_length=255)
    characters = models.ManyToManyField(Character, blank=True, null=True)
    img = models.ImageField(upload_to='episode_rick_morty', blank=True, null=True)

