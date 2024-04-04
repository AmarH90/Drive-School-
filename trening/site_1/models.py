
from random import choices
from django.db import models
from django.utils import timezone



# Create your models here.

class Registar1(models.Model):
    GENDER_CHOICES = [
        ('O', 'Other'),
        ('M', 'Male'),
        ('F', 'Female'),
       
    ]
    class_CHOICES = [
        ("A", "A  Motorcycles"),
        ("B", "B  Car 3.500 kg "),
        ("C", "C  Small truck 7.500 kg"),
    ]
    Pay_Choices = [
        ("all", "Pay all"),
        ("24", "24"),
        ("12","12"),
        ("6", "6"),
        ("3", "3"),
        
    ]
    id_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    b_year = models.CharField(max_length=20)
    card_id = models.CharField(max_length=50)
    passp = models.ImageField(upload_to="img-library", blank=True ,null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,  default='0000000')
    class_user = models.CharField(max_length=1, choices=class_CHOICES, default='0000000' )
    pay = models.CharField(max_length=3, choices=Pay_Choices, default='0000000' )
    create_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return  self.first_name
        #return f"{self.id_number } | { self.first_name }| { self.last_name } | { self.create_date}"
        #return "{}:{}..".format(self.id, self.paragraph[:10])
         
    
    
    #id = models.ForeignKey(on_delete=models.CASCADE, primary_key=True,)
 
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Report_1(models.Model):
    values_choices =  [
        ("1","1"),
        ("2","2"),
        ("3", "3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
    ] 
    teacher = models.CharField(max_length=80)
    student_name = models.CharField(max_length=80)
    year_of_report = models.CharField(max_length=12)
    city_driving = models.CharField(max_length=3, choices=values_choices, default='0000000')
    suburbs_driving = models.CharField(max_length=3 ,choices=values_choices, default='0000000')
    vehicle_parking = models.CharField(max_length=3 ,choices=values_choices, default='0000000')
    driving_behavior = models.CharField(max_length=3 ,choices=values_choices, default='0000000')
    comment = models.CharField(max_length=500)
     
     
     
    #def total_score(self):
    #    # Convert char values to integers and sum them
    #    total = int(self.city_driving) + int(self.suburbs_driving) + int(self.vehicle_parking) + int(self.driving_behavior)
    #    return total   




#kid = "10-18"
#   teen = "18-25"
#   older = "25-40"
#   master = "40-60"
#   legend = "60-90"
#   years_choices = (
#       (kid, "10-18"),
#       (teen, "18-25"),
#       (older, "25-40"),
#       (master, "40-60"),
#       (legend, "60-90"),
#   )
#   years_of_user = models.CharField(max_length=5, choices=years_choices)
    




