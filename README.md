# CloudPhoto

Консольное приложение для работы с облачным хранилищем:
  * Загрузка локальных директорий в хранилище
  * Скачивание директорий из хранилища
  * Просмотр списка альбомов, расположенных в хранилище
  * Просмотр файлов, расположенных в заданных альбомов

## Установка

1. Скачиваем репозиторий
```console
$ git clone https://github.com/EminAliev/cloudphoto.git
```
2. Устанавливаем библиотеку
```console
$ python setup.py develop
```

## Основные команды

1. `cloudphoto upload -p path_name -a album_name` - загрузка из локальной папки в облачное хранилище
2. `cloudphoto download -p path_name -a album_name` - загрузка из облачного хранилища в локальную папку
3. `cloudphoto list` - список всех альбомов в облачном хранилище
4. `cloudphoto list -a album_name` - список всех фотографий в заданном альбоме
