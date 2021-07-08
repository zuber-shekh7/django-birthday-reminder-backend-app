from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError('Please enter valid email')

        if not password:
            raise ValueError('Please enter valid password')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(('Email'), unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)

    objects = UserManager()

    def has_module_perms(self, obj):
        return True

    def has_perm(self, obj):
        return True
