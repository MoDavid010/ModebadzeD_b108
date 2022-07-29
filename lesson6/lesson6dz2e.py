import os


directories = [('dir_' + str(i + 1)) for i in range(9)]


def create_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')


for i in directories:
    create_dir(i)



