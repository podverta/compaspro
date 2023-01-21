
# Тестовое задание в Compas Pro

Проект реализован в связке Python + DRF + Postgresql + Redis

Передо мной стояли следующие задачи:

♦ Развернуть проект на DRF и создать приложение user_selection;

♦ Подключить Postgresql и Redis;

♦ Создать модель User(AbstractBaseUser), добавив поля: role_choice (Пользователь, Менеджер, CRM-администратор), Avatar (аватар пользователей);

♦ Подключить DRF API, с отображение пользователей по /api/users/{id}

♦ Используя management commands в Django создать команду create_users, которая создаст 3 типа пользователей из role_choice и стандартного avatar;







## FAQ

#### Как запустить проект?

♦  Склонируйте репозиторий: 


git clone  git@github.com:podverta/compaspro.git


♦  Запустите docker-compose: 


docker-compose up --build 


#### Посмотреть всех пользователей в api:

http://localhost:8000/ или http://localhost:8000/api/users


#### Посмотреть пользователя по id:

http://localhost:8000/api/users/{id}

#### Посмотреть ключ-значение пар Redis:

http://localhost:8000/api/redis


#### отправить команду create_users в контейнер:

 docker exec <имя_контейнера> python manage.py create_users


 #### Возможности команды create_users:

 '-u' или '--user' для создания пользователя;

 '-a' или '--admin' для создания пользоватяеля админа;

 '-m' или '--manager' для создания менеджера CRM;

 '-n' или '--name' указать имя вручную;

 '-e' или '--email' указать электронную почту вручную.

 '-p' или '--passw' указать пароль вручную.
