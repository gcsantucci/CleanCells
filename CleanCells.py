import sys
import os

def call_exit():
    print('\nExiting...\n')
    sys.exit(0)

def usage():
    print('\nUsage:')
    print('python CleanCells.py [full or relative path of input file]')
    call_exit()

def ninputs(n):
    if n != 2:
        usage()

def check_file(infile):
    print('')
    if not os.path.isfile(infile):
        print('File {0} does not exist.'.format(infile))
        call_exit()
    else:
        print('Removing jupyther cells from file:\n {0}\n'.format(infile))

def get_temp(infile):
    path = infile.strip().split('/')
    temp = 'temp.py'
    temp = os.path.join('/'.join(path[:-1]), temp)
    return temp

def clean_cells(infile):
    check_file(infile)
    tempf = get_temp(infile)
    temp = []
    with open(infile, 'r') as inf:
        for line in inf:
            temp.append(line)
            if line.startswith('# In['):
                temp = temp[:-3]
    with open(tempf, 'w') as outf:
        for line in temp:
            outf.write(line)
    rename(infile, tempf)

def rename(infile, temp):
    os.remove(infile)
    os.rename(temp, infile)

def main():
    ninputs(len(sys.argv))
    infile = sys.argv[1]
    clean_cells(infile)
    print('Done!')

if __name__ == "__main__":
    main()
