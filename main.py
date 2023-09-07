
# Renaming bulk Files

import os

def main():
    i = 1
    path = 'C:\\Users\\Lucas\\Documents\\Projects-Python\\bulk_file_rename\\rename\\'
    for filename in os.listdir(path):
        my_dest = 'Test' + str(i) + '.png'
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i +=  1

if __name__ == '__main__':
    main()