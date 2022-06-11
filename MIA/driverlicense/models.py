from django.db import models
from django.core.validators import  MinLengthValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date


class Cars(models.Model):
    # ნომერი ფერი გამოშვების წელი მარკა მოდელი სურათი (სასურველია)

    def check_num(value):  # checking car number if it is a correct 
        if value[:2].isdigit()==True or value[2:5].isdigit() == False or value[5:7].isdigit() == True:
            raise ValidationError('ERROR: requred style is : NN000NN')  

    number = models.CharField(max_length=7, unique=True, validators=[MinLengthValidator(7, message='Car Numer must contain 7 symbol : NN000NN'), check_num], null=True)
    color = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True,  help_text=('Publish date'), validators=[MaxValueValidator(limit_value=date.today)]) 
    marck = models.CharField(null=True,  max_length=25)
    model = models.CharField(null=True, max_length=30)
    image = models.ImageField(blank=True, upload_to = "")

    #its good for vizualition 
    def __str__(self):
        return self.number


class Person(models.Model):
    #პირადი ნომერი, სახელი,გვარი, მამის სახელი, დაბადების თარიღი

    def only_int(value):  # checkin employeer's personal number 
        if value.isdigit()==False:
            raise ValidationError('ERROR: ID contains characters, it only contains integers:')  

    selfid = models.CharField(null=True, unique=True, max_length=11, validators=[MinLengthValidator(11, message='Card ID Length has to be contain 11 integer : ***********'), only_int],)
    lastname = models.CharField(max_length=150, null=True)
    name = models.CharField(max_length=60, null=True)
    father = models.CharField(help_text=("Father's name"), max_length=150, null=True)
    birth = models.DateField(null=True, help_text=('Enter the date of birth'))
    car = models.ManyToManyField(Cars, blank=True,  help_text=('Choose if employeer has a car or cars') )

    def __str__(self):
        return self.name + '  ' + self.lastname
    

    @property
    def check_car(self):
        cars= []
        for car in self.car.all():            
            cars.append(car)
        return cars 

# class CarDriver(models.Model):


#     person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
#     enrol_date = models.DateTimeField(auto_now_add=True, null=True)
#     car = models.ManyToManyField(Cars)
    

#     def __str__(self):
#         return f'{self.person.name}  {self.person.lastname}  :  {self.car}'