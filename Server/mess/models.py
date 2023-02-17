from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User



DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)

TIME=(
    ('0','Morning'),
    ('1','AfterNoon'),
    ('2','Night'),
)

Rate=(
    (1,'1 star'),
    (2,'2 star'),
    (3,'3 star'),
    (4,'4 star'),
    (5,'5 star'),
)




#model representing student 
class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    rollNo=models.CharField(max_length=10,null=True,blank=True)
    #field when true user has admin accesses
    isAdmin=models.BooleanField(default=False)
    #field for checking if he/she is a subscriber
    isGoldMember=models.BooleanField(default=True)
    def __str__(self):
        rs=self.FirstName+'-'+self.LastName
        return rs
    

#model representing meals in mess
# class Food(models.Model):
#     Food=models.CharField(max_length=50,null=True,blank=True)
#     def __str__(self):
#         return self.Food

#model representing mess menu unique for particular day and particular time slot
class Menu(models.Model):
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time=models.CharField(max_length=1,choices=TIME)
    meal=models.TextField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    #here UniqueConstraint are true means for particular day and time there can be a one menu
    UniqueConstraint(fields=['days','time'],name='timeSlot')
    def __str__(self):
        rs=self.day+'-'+self.time
        return rs


#model representing details of user how has taken 45/90 tokens 
class GoldToken(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    TokenCount=models.IntegerField()
    #Expiry will be generally 30 days from the day of buying tokens
    TokenExpiry=models.DateField()
    #minimum fee needed for user to continue his gold token 
    # passRenewalFee=models.IntegerField(null=True,blank=True)


#model for Student who want to just buy token for a particular day or so
class SilverToken(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #day and time representing the timeslot they will be eating
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time=models.CharField(max_length=1,choices=TIME)
    expiryDate=models.DateField(null=True,blank=True)


#models representing the Feedback 
class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    #date for testinomial its an auto field will be added by there own
    date=models.DateField(auto_now_add=True)
    # this is an testinomial provided by the user for food
    message=models.CharField(max_length=256)
    # rating will be used to rate the food
    rating=models.CharField(max_length=1, choices=Rate)


# models representing pull out from a particular meal of a user
class NotEatingToday(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # day time combine will present a particular meal
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    time=models.CharField(max_length=1,choices=TIME)
    # field representing is that user pulling out from that dish every week 
    isRecurring=models.BooleanField(default=False)



