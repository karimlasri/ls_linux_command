import argparse
import os
import re
import stat
import datetime


def parseArguments():
    # Creating parser
    parser = argparse.ArgumentParser()
    # Adding needed arguments to parser
    parser.add_argument('-l', help='lastModification', action='store_true')
    parser.add_argument('path', type = str, nargs = '+')
    # Parsing arguments
    arguments = parser.parse_args()
    return arguments


def listFiles(path, l_flag):
    output_s = ''
    # The path given as an argument is either a directory...
    if os.path.isdir(path):
        try:
            for file in os.listdir(path):
                # Checking flag -l
                if l_flag:
                    # Getting file mode
                    stats = os.stat(path + '/' + file)
                    mode = stats.st_mode
                    file_mode = stat.filemode(mode)
                    # Getting last access date and time
                    last_access_datetime = datetime.datetime.fromtimestamp(stats.st_mtime)
                    last_access_date = last_access_datetime.date()
                    last_access_time = '{}:{}'.format(last_access_datetime.hour, last_access_datetime.minute)
                    output_s += '{} {} {} {}'.format(file_mode, last_access_date, last_access_time, file) + '\n'
                else:
                    output_s += file + '\n'
        except FileNotFoundError:
            output_s = 'The specified folder can not be found.'
    # ...or it looks like one but can't be found...
    elif path[-1] in ['/', '\\']:
        output_s = 'The specified folder can not be found.'
    # ...or it is the path of a directory followed by a prefix
    else:
        path_split = re.split(r'/|\\', path)
        if len(path_split) > 1:
            dir_path = '/'.join(path_split[:-1])
        else:
            dir_path = '.'
        prefix = path_split[-1]
        if os.path.isdir(dir_path):
            try:
                counter = 0
                for file in os.listdir(dir_path):
                    if file[:len(prefix)] == prefix:
                        counter += 1  # Counting files that begin with prefix in the folder
                        if l_flag:
                            # Getting file mode
                            stats = os.stat(dir_path + '/' + file)
                            mode = stats.st_mode
                            file_mode = stat.filemode(mode)
                            # Getting last access date as YYYY-MM-DD and time as HH:mm
                            last_access_datetime = datetime.datetime.fromtimestamp(stats.st_mtime)
                            last_access_date = last_access_datetime.date()
                            last_access_time = '{}:{}'.format(last_access_datetime.hour,
                                                              last_access_datetime.minute)
                            # Adding resulting string to output
                            output_s += '{} {} {} {}'.format(file_mode, last_access_date, last_access_time, file) + '\n'
                        else:
                            output_s += file + '\n'
                if counter == 0:
                    output_s = 'None of the file names in the folder contain \'{}\' as a prefix.'.format(prefix)
            except FileNotFoundError:
                output_s = 'The specified folder can not be found.'
    return output_s


if __name__ == '__main__':
    args = parseArguments()
    path = ' '.join(args.path) # Permet de gérer les chemins contenant des espaces
    l_flag = args.l
    output_s = listFiles(path, l_flag)
    print(output_s)