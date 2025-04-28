def addfile(msg):
    file = open('./file/output.txt','a')
    file.write(msg)
    print('file append sucess !!')

u_input = input('write text for add in file : ')
try :
    addfile(u_input)
except :
    print('file not found')