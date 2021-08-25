from urllib import request
from urllib.error import URLError

try:
    file = request.urlopen('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data'
                       '/sdg_08_10.tsv.gz&unzip=true')
except URLError:
    print("La URL no existe!")
else:
    text = file.read().decode("utf-8").split("\n")  # el .decode("utf-8") convierte el objeto file en un str
                                                # lo que me permite utilizar luego el split()
    # Lo siguientes codigos son equivalentes############################################################################
    '''
    text = [i.split("\t") for i in text]
    text = [list(map(str.strip, i)) for i in text]  # Eliminar espacios en blanco
    '''

    a = 0
    for i in text:
        i = i.split("\t")  # Armo una lista, a partir de las tabulaciones
        text[a] = list(map(str.strip, i))    # strip: borro los espacios en blanco
                                             # map: aplico a cada elemento de la lista
                                             # list: convierte el obj map en formato lista
        a += 1

    ####################################################################################################################
    ano = "2001"  # Esto se puede pedir al usuario
    pais = "AT"  # Esto se puede pedir al usuario
    posicion_x = 0
    posicion_y = 0

    if ano in text[0]:
        posicion_x = text[0].index(ano)

    for i in text:
        i = i[0].split(",")
        if pais in i:
            print(text[posicion_y][posicion_x])
        posicion_y += 1

