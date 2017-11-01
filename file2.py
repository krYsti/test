def kraje():
    cfile = open('countries.py','r')
    tabela = cfile.read()
    for i in tabela:
        print (i)

kraje()