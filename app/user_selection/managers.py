from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True
# создание пользователя с полями
    def _create_user(self, email, password, username, avatar, **extra_fields):

        if not email:
            raise ValueError('Внимание. Почта является обязательным полем.')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            avatar=avatar,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
# создание пользователя с настраиваемыми полями

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)