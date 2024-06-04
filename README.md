Для запуска необходимо иметь предустановленный docker. Далее при вызове 'up.sh' запуститься билд и поднятие контейнера. Для остановки сервиса вызовите 'down.sh'. 
При развёртывании контейнера создаётся база данных postgresSQL и заполняется начальными данными. Так же запускается сервис к которому можно обращаться по localhost:5000
Сервис позволяет обращаться к картотеке состоящей из каталогов с возможной вложенностью и документов внутри каталогов. Например, существует катало 'movie_reviews' с вложенным в него каталогом '80s', где в свою очередь лежит документ 'Blade_Runner'
Примеры запросов:
GET запросы
По запросу curl -X GET localhost:5000/ выдаётся список всех каталогов и внутренних вложенностей с документами
Для получения информации на счёт какого то конкретного документа необходимо прописать путь до каталога в котором находится документ и имя документа в формате 'document=name'. Пример curl -X GET localhost:5000/games_soundtracks/Forza_horizon/document=The_Black_Keys_Lonely_Boy
Для получения информации про конкретный каталог необходимо прописать путь до этого каталога curl -X GET localhost:5000/games_soundtracks/Forza_horizon
POST запросы
Для отправки пост запросов необходима авторизация. Username:admin, password:admin.
Для добавления документа в базу данных существует запрос curl -u admin:admin -X POST localhost:5000 -d [document,movie_reviews,second_document,txt,12345,123] (с авторизацией). Где первый аргумент является флагом обозначающим, что добавляется документ. Второй аргумент это путь к каталогу в который необходимо добавить документ. Третий - имя. Четвёртый - формат файла. Пятый-размер файла. Шестой - Хэш сумма файла
Для добавления нового каталога в базу curl -u admin:admin -X POST localhost:5000 -d [katalog,movie_reviews/80s,year_85]




