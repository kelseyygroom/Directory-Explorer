from pathlib import Path
import os 
import shutil
import datetime
import time


def flatten(lst):
    '''
    Given a multidimensional list of unknown depth, this function recursively
    flattens it into a single-dimensional list and returns that list.
    '''
    
    if type(lst) == list: 
        if len(lst) == 0: # base case to prevent infinite recursion
            return []
        first = lst[0]
        remaining = lst[1:]
        All = flatten(first) + flatten(remaining) # recursion
        return All
    else:
        return [lst]


def print_files(lst):
    '''
    Given a single-dimensional list of paths, prints each path on a new line.
    Returns nothing.
    '''

    # streamlining the file printing process w/ a function
    for file in lst: 
        print(file)


def D(directory):
    '''
    Given a directory with no subdirectories, prints each file and
    returns all files as a list.
    '''
    # list and sort every file in a directory
    dir_lst = os.listdir(directory) 
    dir_lst.sort()

    files = []

    for file in dir_lst:
        p = os.path.join(directory, file)
        files.append(p)
        print(p)

    return files


def R(directory):
    '''
    Given a directory, compiles all files in the directory and any subdirectories
    into a multidimensional list. Calls flatten() to flatten into a single list
    and returns that list. 
    '''

    
    dir_lst = os.listdir(directory)
    files = []
    sub_dir = []
    for element in dir_lst:
        p = os.path.join(directory, element) # create full path from filename
        if os.path.isfile(p):
            files.append(p)
        if os.path.isdir(p): # if path is directory: recurse until all files
            sub = R(p)
            sub_dir.append(sub)

    files.sort()

    # append the files from the subdirectories to main files list
    if len(sub_dir) > 0:
        for each in sub_dir:
            files.append(each)
    
    # returns the flattened mutli-dimensional list
    return flatten(files)


def N(files_lst, name):
    '''
    Given a list of files and a desired name, filters through the list to only include
    "interesting" files which match the desired name. Returns the list of interesting
    files.
    '''

    interesting = []

    for file in files_lst:
        base_name = os.path.basename(file) # gets just the filename to compare
        if base_name == name:
            interesting.append(file)

    return interesting
            

def E(lst, ext):
    '''
    Given a list of paths and a desired extension, this function appends all files
    with the desired extension to a list, then returns that list.
    '''

    interesting = []

    # ensures the ext inputs are in the format .ext and converts them if not
    if ext[0] != '.':
        ext = '.' + ext

    for file in lst:
        root_ext = os.path.splitext(file) # separates filename into list of root and extension
        if root_ext[1] == '':
            if root_ext[0] == ext:
                interesting.append(file)
        else:
            if root_ext[1] == ext:
                interesting.append(file)

    return interesting
        

def T(lst, phrase):
    '''
    Given a list of paths and a desired phrase, this function filters through
    readable files for files that contain the desired phrase. Returns a list
    of files with the desired phrase.
    '''

    interesting = []
    
    for file in lst:
        f = open(file)
        try:
            contents = f.read() # tries reading file to verify if it's a text file
        except:
            pass # no action needs to be taken in the case of failure
        else:
            if phrase in contents:
                interesting.append(file)
        finally:
            f.close # always close files!

    return interesting  
        

def less_than(lst, size):
    '''
    Given a list of paths and a threshold byte size, paths that meet do not exceed
    the threshold size are appended to a list. Returns a list of interesting files.
    '''

    interesting = []
    for file in lst:
        file_stats = os.stat(file) # returns the stats of the files
        file_size = file_stats.st_size # finds the file size from stats
        if file_size < int(size):
            interesting.append(file)

    return interesting


def greater_than(lst, size):
    '''
    Given a list of paths and a threshold byte size, paths that meet the threshold
    size are appended to a list. Returns a list of interesting files.
    '''

    interesting = []
    for file in lst:
        file_stats = os.stat(file) # returns the stats of the files
        file_size = file_stats.st_size # finds the file size from stats
        if file_size > int(size):
            interesting.append(file)

    return interesting

def F(lst):
    '''
    Given a list of interesting files, determines which are text files and, if
    applicable, prints the first line of text. Returns nothing.
    '''

    for file in lst:
        f = open(file)
        try:
            contents = f.readlines() # try reading to determine if a text file
        except:
            print('NOT TEXT')
        else:
            first_line = contents[0].rstrip() # strip end of line in case of \n
            print(first_line)
        finally:
            f.close


def D2(lst):
    '''
    Given a list of interesting files, make a copy of each file in the same
    directory with '.dup' added. Returns nothing.
    '''

    for file in lst:
        original = file
        duplicate = file + '.dup'
        shutil.copyfile(original, duplicate) # copies file with given conditions

def T2(lst):
    '''
    Given a list of files, "touch" each file; changes the last modified time to
    curent date/time. Returns nothing.
    '''

    for file in lst:

        original_atime = os.stat(file).st_atime # gets access time 
        current_datetime = datetime.datetime.now().timestamp() # gets current date/time in seconds
        
        mod = (original_atime, current_datetime) # creates mod time from current date/time and atime, which doesn't change
        os.utime(file, mod) # changes mtime of the file


if __name__ == '__main__':

    invalid = True # initialize value for while loops (for readability)


    # taking first iteration of input
    
    while invalid: # taking input until recieving valid first input
        first_input = input()
        valid_inputs1 = ['D', 'R']
        
        first_split = first_input.split(' ', 1)
        if len(first_split) != 2:
            print('ERROR')
            continue
        if len(first_split) == 2:
            if first_split[1].isspace():
                print('ERROR')
                continue
            elif first_split[1] == '':
                print('ERROR')
                continue
        
        char1 = first_split[0]
        directory1 = Path(first_split[1])
        
        if char1 not in valid_inputs1:
            print('ERROR')
            continue
        elif not(os.path.isdir(directory1)):
            print('ERROR')
            continue
        else:
            break

    # taking action based on first character entered

    if char1 == 'D':
        list1 = D(directory1)

    if char1 == 'R':
        list1 = R(directory1)
        print_files(list1)


    #taking second iteration of input

    while invalid: # taking input until it recieves valid second input
        second_input = input()
        valid_inputs2 = ['A', 'N', 'E', 'T', '<', '>']

        second_split = second_input.split(' ', 1)
        char2 = second_split[0]

        if len(second_split) > 1:
            filter2 = second_split[1] # assigns the filtering criteria to filter2
            if (char2 != 'A' and char2 != 'N') and filter2.isspace():
                print('ERROR')
                continue
            if char2 != 'A' and filter2 == '':
                print('ERROR')
                continue
    
        if char2 != 'A' and len(second_split) != 2:
            print('ERROR')
            continue
    
        if char2 not in valid_inputs2:
            print('ERROR')
            continue
        elif char2 == '<' or char2 == '>':
            try:
                num = int(filter2)
                if num < 0:
                    print('ERROR')
                    continue
            except:
                print('ERROR')
                continue
            else:
                break
        else:
            break

    # taking action based on char2 entered

    if char2 == 'A': # assigns list1 to list2, since all files are considered interesting
        list2 = list1
        if len(list2) != 0:
            print_files(list2)
        else:
            quit()

    if char2 == 'N': 
        list2 = N(list1, filter2) # list2 is now only files that fit name entered
        if len(list2) != 0:
            print_files(list2)
        else:
            quit()

    if char2 == 'E':
        list2 = E(list1, filter2) # list2 includes files with given extension
        if len(list2) != 0:
            print_files(list2)
        else:
            quit()
        
    if char2 == 'T':
        list2 = T(list1, filter2) # list2 includes files with given text
        if len(list2) != 0:
            print_files(list2)
        else:
            quit()

    if char2 == '<':
        list2 = less_than(list1, filter2) # list2 includes files less than threshold of bytes
        if len(list2) != 0:
            print_files(list2)
        else:
            quit()

    if char2 == '>':
        list2 = greater_than(list1, filter2) # list2 includes files greater than threshold num
        if len(list2) != 0: 
            print_files(list2)
        else:
            quit()


    # taking third iteration of input

    while invalid:
        last_input = input()
        valid_inputs3 = ['F', 'D', 'T']
        
        char3 = last_input[0]

        if last_input not in valid_inputs3:
            print('ERROR')
            continue
        else:
            break


    if char3 == 'F':
        F(list2)

    if char3 == 'D':
        D2(list2)

    if char3 == 'T':
        T2(list2)
