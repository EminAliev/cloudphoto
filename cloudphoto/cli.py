import click
from cloudphoto.main import S3Service

s3 = S3Service()


@click.group()
def main():
    print("======================================================")


@main.command()
@click.option('-p', help='Путь до локальной папки')
@click.option('-a', help='Название альбома')
def upload(p, a):
    if (p is not None) & (a is not None):
        s3.upload_files(p, a.lower())
    else:
        click.echo("ERROR", color='red')
        click.echo("Введите верные значения")


@main.command()
@click.option('-p', help='Путь до локальной папки')
@click.option('-a', help='Название альбома')
def download(p, a):
    if (p is not None) & (a is not None):
        s3.download_files(p, a.lower())
    else:
        click.echo("ERROR", color='red')
        click.echo("Введите верные значения")


@main.command()
@click.option('-a', help='Название альбома')
def list(a):
    if a is not None:
        s3.list_photos_album(a.lower())
    else:
        s3.list_albums()


def start():
    main()


if __name__ == "__main__":
    start()
