from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Game(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
         blank=True, null=True )
    thumbnail = models.ImageField(blank=True)
    fun_mode = models.BooleanField(default=False)
    real_mode = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        abstract = True


class SlotGame(Game):
    jackpot = models.IntegerField()
    jackpot_currency = models.CharField(max_length=5)
    game_type = models.CharField(max_length = 20, default='Slot Game')


class LiveGame(Game):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    dealer_gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True)

    dealer_language = models.CharField(max_length=20)
    unlimited_seats = models.BooleanField(default=False)
    game_type = models.CharField(max_length = 20, default='Live Game')


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    description = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}'
