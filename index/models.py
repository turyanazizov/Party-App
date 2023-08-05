from django.db import models

class Ticket(models.Model):
    ticket_number=models.BigIntegerField()
    name=models.CharField(max_length=55)
    surname=models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"{self.name} {self.surname}"
    