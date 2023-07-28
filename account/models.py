from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, phone_number, name, tc,password=None, **extra_fields):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not phone_number:
          raise ValueError('User must have a phone number')

      user = self.model(
          phone_number=phone_number,
          email=self.normalize_email(email),
          name=name,
          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  
def create_superuser(self, email,phone_number, name, tc, password=None, **extra_fields):
      """
      Creates and saves a superuser with the given email,phone_number, name, tc and password.
      """
      user = self.create_user(
          email,
          phone_number=phone_number,
          password=password,
          name=name,
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  phone_number = models.CharField(max_length=15, unique=True)
  name = models.CharField(max_length=200)
  tc = models.BooleanField()
  photo = models.ImageField(upload_to='photos/', blank=True, null=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'phone_number'
  REQUIRED_FIELDS = ['email','name','tc']

#   def user(self):
#       return f"{self.name}"

  def __str__(self):
      return self.phone_number

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin




