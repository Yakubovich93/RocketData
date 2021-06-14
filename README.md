docker ps -a  процессы
docker ps -a   образы

Запустить развертывание проекта: 
docker-compose up --build

Вход в контейнер:
docker exec -it <название контенера> bash