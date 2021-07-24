# Importa librerías
from django.db import models
import re
from django.db.models.base import Model

# Validations
#=================== UserManager=====================
# Valida caracteres y/o formato para ingreso de correo
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Invalid first name. First Name must be at least 3 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Invalid last name. Last Name must be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        users_with_email = User.objects.filter(email = postData['email'])

        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        if len(postData['password']) < 3:
            errors['password'] = "Password must be at least 3 characters."
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        
        return errors

#=============== AppointmentManager =================
class GroupManager(models.Model):
    def appointment_validator(self, postData):
        errors = {}
        if len(postData['org_name']) < 3:
            errors['task'] = "Organization Name must be at least 3 characters."
        if len(postData['description']) < 3:
            errors['description'] = "Description must be at least 3 characters."

# Models Creation
#=================== Usuarios ==========================
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

#=================== Grupos ==========================
class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250) 
    user_create = models.ForeignKey(User, related_name='users_create', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GroupManager()
#=================== Miembros ==========================
class Member(models.Model):
    users = models.IntegerField()
    group = models.ForeignKey(Group, related_name='group', on_delete=models.CASCADE)



