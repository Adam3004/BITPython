import os
import shutil

# Dict shouldnt be created earlier, enter path to folnder which u want to sort, and the rest will do itslef

# Enter patch of dict which u want to sort
files = os.listdir('./')


def creator(dictName: str):
    # Enter path to dict in which u want to have sorted files
    os.mkdir(f'./{dictName}')


def directory_creation():
    creator('images')
    creator('films')
    creator('documents')
    creator('music')
    creator('other')


def checker(fileName: str):
    images_extensions = ['png', 'jpg', 'psd', 'tiff', 'gif', 'jpeg', 'jps', 'bmp', 'xcf', 'xpm']
    films_extensions = ['mp4', 'avi', 'gp', 'asf', 'dv', 'dvd', 'flv', 'm2ts', 'mkv', 'mov', 'mpg', 'ogg', 'smv',
                        'svcd', 'ts', 'wmv', 'vcd']
    documents_extensions = ['doc', 'docx', 'odt', 'pdf', 'txt', ' docm', 'dot', 'dotx', 'ott', 'ods', 'csv']
    music_extensions = ['mp3', 'xwm', 'wav', 'wma', 'aac', 'flac', 'm4a', 'ape', 'mpl']

    *_, file_extension = fileName.strip('\n').split('.')
    file_extension = file_extension.lower()
    if file_extension in images_extensions:
        transporter(fileName, 'images')
    elif file_extension in films_extensions:
        transporter(fileName, 'films')
    elif file_extension in documents_extensions:
        transporter(fileName, 'documents')
    elif file_extension in music_extensions:
        transporter(fileName, 'music')


def transporter(fileName: str, directory: str):
    source = f'./{fileName}'
    destination = f'./{directory}'
    shutil.move(source, destination)


if __name__ == '__main__':
    directory_creation()
    for file in files:
        checker(file)
