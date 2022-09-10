"""
By: Sílvio Silva
   07/09/2022
"""

import os
import platform
import shutil
from os import listdir
from os.path import isfile, join
from colorama import Fore

DRYRUN = False


try:
    extensions = {
        'Images': [
            '.png',
            '.jpeg',
            '.jpg',
            '.gif',
            '.ai',
            '.bmp',
            '.ico',
            '.ps',
            '.psd',
            '.svg',
            '.tif'
        ],

        'Sounds': [
            '.wav',
            '.mp3',
            '.m4a',
            '.mid',
            '.midi',
            '.ogg',
            '.wma',
            '.wpl',
            '.cda'
        ],

        'Videos': [
            '.mp4',
            '.mkv',
            '.avi',
            '.webm',
            '.3g2',
            '.3gp',
            '.flv',
            '.h264',
            '.m4v',
            '.mov',
            '.mpg',
            '.mpeg',
            '.wmv'
        ],
        'Documents': [
            '.pdf',
            '.docx',
            '.doc',
            '.pptx',
            '.pptm',
            '.ppt',
            '.txt',
            '.torrent',
            '.deb',
            '.ods',
            '.xls',
            '.xlsm',
            '.xlsx',
            '.rtf',
            '.wpd'
        ],
        'Android': [
            '.apk',
            '.xapk'
        ],
        'Compressed': [
            '.zip',
            '.rar',
            '.tar.xz',
            '.xz',
            '.7z',
            '.gz',
            '.arj',
            '.pkg',
            '.tar.gz',
            '.z',
            '.tar'
        ],
        'Executables': [
            '.exe',
            '.bat',
            '.bin',
            '.cgi',
            '.pl',
            '.jar',
            '.msi',
            '.wsf'
        ],
        'Midia': [
            '.bin',
            '.dmg',
            '.iso',
            '.cso',
            '.toast',
            '.vcd'
        ],
        'Data': [
            '.csv',
            '.dat',
            '.db',
            '.dbf',
            '.log',
            '.mdb',
            '.sav',
            '.sql',
            '.xml'
        ],
        'Fonts': [
            '.fnt',
            '.fon',
            '.otf',
            '.ttf'
        ],
        'Programming': [
            '.htm',
            '.html',
            '.php',
            '.css',
            '.js',
            '.jsp',
            '.rss',
            '.xhtml',
            '.c',
            '.cs',
            '.h',
            'java',
            '.sh',
            '.swift',
            '.vb',
            '.json'
        ],
        'System': [
            '.bak',
            '.cfg',
            '.dll',
            '.ini',
            '.lnk',
            '.sys',
            '.tmp'
        ]
    }

    def clear_screen():
        """
        Função para limpar a tela após a inicialização
        """

        if "windows" in platform.system().lower():
            command = 'cls'
        else:
            command = 'clear'

        os.system(command)

    clear_screen()

    def get_extension(path: list):
        """
        Função para pegar as extensões dos arquivos
        """
        split_name = os.path.splitext(path)
        return split_name

    def create_dir(directory: list, location: str):
        """
        Função para criar os diretórios onde serão organizados os arquivos
        """
        try:
            os.chdir(location)
            if os.path.isdir(directory):
                pass
            else:
                if DRYRUN:
                    print(f'Creating directory {directory}')
                else:
                    os.mkdir(directory)
        except Exception:
            pass

    def _move(arg1, arg2):
        if DRYRUN:
            print(f"DRYRUN: {arg1} -> {arg2}")
        else:
            return shutil.move(arg1, arg2)

    def order(directory: str):
        tdd = 0
        keys = list(extensions.items())
        if os.path.isdir(directory):
            onlyfiles = [f for f in listdir(directory)
                         if isfile(join(directory, f))]
            for arquivo in onlyfiles:
                for count in range(len(extensions)):
                    create_dir(keys[count][0], directory)
                    extension = "".join(get_extension(arquivo)[1]).lower()
                    if extension in keys[count][1]:
                        all = "".join(get_extension(arquivo))
                        if os.path.isfile(f"{keys[count][0]}"):
                            pass
                        else:
                            if shutil.move(f"{all}", f"{keys[count][0]}"):
                                tdd = tdd + 1
            if tdd > 0:
                print(f"{Fore.GREEN}Organization made with success[!]")
            if tdd == 0:
                print(f"{Fore.YELLOW}This dir is already organizaded[!]")
        else:
            print(f'{Fore.RED} The Directory {directory} '
                  f'Does not exist. Try Again [!]')
except Exception as e:
    print(f"{Fore.RED}Aconteceu um erro não esperado: {e.__class__.__name__}."
          f" Tente Novamente [!]")
