##9.2 Exercise: Catching several errors at once
filename = input('Give the file name: ')

try:
    myfile = open(filename, 'r')
    filehandle = myfile.read()
    intfile = float(filehandle)
    result = 1000 / intfile 
    print('The result was', result)
    myfile.close()


except IOError:
    print('There seems to be no file with that name.')
except ValueError:
    print('The file contents were unsuitable.')
except Exception:
    print('There was a problem with the program.')

        