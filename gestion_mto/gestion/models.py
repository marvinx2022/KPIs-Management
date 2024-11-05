import re
from django.db import models
from django.forms import ValidationError


def week_test(week):
        result = re.match(r'(\d{2})/(\d{4})', week)
        if result == None: 
            raise ValidationError("Ingresa el nombre de semana en formato correcto, ejemplo ===>  << 39/2009 >> ")

    
PARADA__STATUS_CHOICES = [
    ("PL", "En planificación"),
    ("PR", "Programada"),
    ("GC", "Gestión de compras"),
    ("EJ", "En ejecución"),
    ("FN", "Finalizada"),
]

class Parada(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sch_s_date = models.DateField()
    sch_f_date = models.DateField()
    status = models.CharField(max_length=50, choices=PARADA__STATUS_CHOICES)
    
    
    def __str__(self):
        
        return(f"{self.name} -- Fecha estimada: {self.sch_s_date}")

class Week(models.Model): 
    
    name =  models.CharField(max_length=7, validators=[week_test])
    s_date = models.DateField()
    f_date = models.DateField()
    ot_prev = models.IntegerField()
    ot_corr = models.IntegerField()
    ot_prev_exe = models.IntegerField()
    ot_corr_exe = models.IntegerField()
    
    def __str__(self):
        
        return(f"Semana {self.name} --- del {self.s_date} al {self.f_date}")
    
    class Meta:
        verbose_name = "Semana"
        verbose_name_plural = "Semanas"

    