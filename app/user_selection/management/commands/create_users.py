from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()


class Command(BaseCommand):
    help = 'Создание пользователей users, administrator, manager CRM'

    def handle(self, *args, **options):

        name = options['name']
        mail = options['email']
        passw = options['password']

        if name:
            username = name
        else:
            username = get_random_string(7)

        if mail:
            email = mail
        else:
            email = 'user@' + get_random_string(5) + '.ru'

        if passw:
            password= passw
        else:
            password='1234567890'

        if options['user']:
            User.objects.create_user(username=username,
                                     email=email,
                                     password=password,
                                     avatar='media/user.png'
                                     )

        elif options['admin']:
            User.objects.create_superuser(username=username,
                                          email=email,
                                          password=password,
                                          avatar='media/admin.png'
                                          )

        elif options['manager']:
            User.objects.create_user(username=username,
                                     email=email,
                                     password=password,
                                     avatar='media/manager.png'
                                     )

        else:
            print(
                "\nВыберите команду, которую хотите выполнить:\n\n"
                " '-u' или '--user' для создания пользователя;\n"
                " '-a' или '--admin' для создания пользоватяеля админа;\n"
                " '-m' или '--manager' для создания менеджера CRM;\n"
                " '-n' или '--name' указать имя вручную;\n"
                " '-e' или '--email' указать электронную почту вручную.\n"
                " '-p' или '--passw' указать пароль вручную.\n"
            )

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--user',
            action='store_true',
            default=False,
            help='Создание пользователя user'
        )

        parser.add_argument(
            '-a',
            '--admin',
            action='store_true',
            default=False,
            help='Создание пользователя admin'
        )

        parser.add_argument(
            '-m',
            '--manager',
            action='store_true',
            default=False,
            help='Создание пользователя manager'
        )

        parser.add_argument(
            '-n',
            '--name',
            type=str,
            help='Указать имя вручную'
        )
        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='Указать электронную почту вручную'
        )
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            help='Указать пароль'
        )
