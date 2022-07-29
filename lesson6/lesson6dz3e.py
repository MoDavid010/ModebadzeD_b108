import os


def current_dir(path):
    for _ in os.listdir(path):
        print(_)


path = os.getcwd()

current_dir(path)
