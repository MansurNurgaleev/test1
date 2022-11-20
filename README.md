# Запуск приложения

Приложение доступно по ссылке http://23.23.200.182:8000/item/1

Так же можно изменять данные через админ панель http://23.23.200.182:8000/admin/
- Username: admin
- Password: 12345

Для запуска приложения выполните следующие действия:
- Установите Docker
- Выполните клонирование репозитория командой git clone https://github.com/MansurNurgaleev/test1.git
- Заполните файл .env
- Перейдите в папку где расположен файл docker-compose.yml
- Выполните команду docker-compose up --build

Прложение будет доступно по ссылке http://localhost:8000/admin/

Сначала необходимо заполнить таблицу Item через админ панель

Товары будут доступны по ссылке http://localhost:8000/item/1
