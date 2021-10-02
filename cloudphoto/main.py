import os
import boto3


class S3Service:
    def __init__(self):
        self.session = boto3.session.Session()
        self.s3_client = self.session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net'
        )
        self.bucket_name = 'cloudphoto-itis'

    def upload_files(self, folder, album):
        """
        Загрузка фотографий в облачное хранилище
        :param folder: локальная папка
        :param album: название альбома
        :return:
        """
        if os.path.exists(folder):
            if os.path.isdir(folder):
                for filename in os.listdir(folder):
                    try:
                        print('Загрузка в S3 ' + self.bucket_name + ' файла ' + filename )
                        self.s3_client.put_object(Bucket=self.bucket_name, Key=album + '/' + filename, Body=filename)
                    except Exception as error:
                        print('Ошибка загрузки ' + folder + str(error))
            else:
                print('Указанный путь не является каталогом')
        else:
            print('Такого пути не существует')

    def download_files(self, local_dir, album):
        """
        Загрузка файлов из S3 в локальную папку
        :param album: название альбома
        :param local_dir: локальная папка
        :return:
        """
        if os.path.exists(local_dir):
            if os.path.isdir(local_dir):
                try:
                    for obj in self.s3_client.list_objects(Bucket=self.bucket_name, Prefix=album)['Contents']:
                        print('Загрузка в папку' + local_dir + ' ' + obj['Key'].split('/'[1]))
                        self.s3_client.download_file(Bucket=self.bucket_name, Key=obj['Key'],
                                                     Filename=os.path.join(local_dir, obj['Key'].split('/')[1]))
                except Exception:
                    print('Такого альбома не существует')
            else:
                print('Указанный путь не является каталогом')
        else:
            print('Такого пути не существует')

    def list_albums(self):
        """
        Список альбомов
        :return: список с названием альбомов
        """
        albums = []
        for albums_list in self.s3_client.list_objects_v2(Bucket=self.bucket_name, Delimiter='/')['CommonPrefixes']:
            albums.append(albums_list['Prefix'])
        print(*albums)

    def list_photos_album(self, album):
        """
        Список фотографии в определенном альбоме
        :param album: название альбома
        :return: список с названиями фотографий
        """
        photos = []
        try:
            for photo in self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=album)['Contents']:
                photos.append(photo['Key'].split('/')[1])
        except Exception:
            print('Такого альбома не существует')
        print(*photos)
