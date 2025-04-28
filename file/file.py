try :
    data = open('./file/sample.txt',"r")
    filedata = data.read()
    print(filedata)
except:
    print('file is does not exits ')