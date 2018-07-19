def bihurtzen( filename , newFilename , encoding_from , encoding_to = 'UTF-8' ):
    print("bihurtzen START")
    print(filename)
    with open(filename , 'r' , encoding = encoding_from) as fr:
        with open(newFilename , 'w' , encoding = encoding_to) as fw:
            for line in fr:
                linea = line[:-1] + '\r\n'
                print (linea)

                fw.write(linea.decode(encoding_from).encode(encoding_to))

        print("bihurtzen END")