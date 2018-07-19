import chardet

def getFileEncoding( filename ):
    print("getFileEncoding START")
    rawdata = open(filename , 'rb').read()
    result = chardet.detect(rawdata)
    print(result)
    print("getFileEncoding FIN")
    return result['encoding']