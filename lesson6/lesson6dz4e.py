import shutil
import sys


def copy_file(current_file, backup_file):
    shutil.copy(current_file, backup_file)


current_file = sys.argv[0]
backup_file = current_file + '.backup'
copy_file(current_file, backup_file)
