from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username=None, email=None, phone=None, password=None, **extra_fields):
        if username:
            if not email and not phone:
                raise ValueError('The given email/phone must be set')
            email = self.normalize_email(email)
            user = self.model(username=username, phone=phone, email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(username=username, password=password, **extra_fields)
