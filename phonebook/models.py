from django.db import models

class Personality(models.Model):
    happiness = models.IntegerField(default=5)
    introvert = models.BooleanField(default=False)
    mbti = models.CharField(max_length=20, default="")

    def __repr__(self):
        return f"Personality: {self.happiness} {self.mbti}"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    character = models.OneToOneField(Personality, on_delete=models.CASCADE, null=True)

    def __repr__(self):
        return f"Person: {self.first_name} {self.last_name}"


class Car(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="mycars",
    )

    def __repr__(self):
        return f"Car: {self.make} {self.model}"