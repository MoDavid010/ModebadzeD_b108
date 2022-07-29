import os

directories = [('dir_' + str(i + 1)) for i in range(9)]


def delete_dir(dir_path):
        dir_path = os.path.join(os.getcwd(), dir_path)
        try:
            0
            os.rmdir(dir_path)
        except:
            print(dir_path + ' - такой директории нет')


for i in directories:
    delete_dir(i)