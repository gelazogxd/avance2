from django.contrib.auth.models import User
from django.db import models

# Create your models here.

    ### GRANT GOALS ####
# Base de datos

STATE_CHOICES = (
        ('Done', 'DN'),
        ('Doing', 'DG'),
        ('Not Stared', 'NS'),
)

class GrantGoal(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)

            gg_tittle = models.CharField(max_length=128, default="Generic Grant Goal Tittle")
            # Charfield es el varchar del mysql
            description= models.CharField(max_length=256, default="Generic Grant Goal Description")

            timestamp = models.DateField(auto_now_add=True)
            days_duration = models.IntegerField(default=7)
            final_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
            # Este campo va a ser calculado, y dice que no tome del servideo la fecha de actualizacion. y que puede estar en blanco y vacio
            status = models.BooleanField(default=True)
            state = models.CharField(max_length=16, choices=STATE_CHOICES)
            # El choices, nos permite elejir de una lista de elemneto un elemento para el campo   
            sprint = models.IntegerField(default=1) #Avances a mostrar en el objetivo
            slug = models.SlugField(max_length=16) #Campo extra, el cual puede dar la respuesta con menor cantidad de caracteres
            

            def __str__(self):
                    return self.gg_tittle
            # Regresa el titulo



    #  #### GOALS ####
    # ### SUBGOALS ####
    # ### ISSUES ####


