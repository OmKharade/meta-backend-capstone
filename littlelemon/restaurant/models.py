from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.IntegerField()

    # add the following method in Menu class
    def __str__(self):
        return f"{self.title} : {str(self.price)}"