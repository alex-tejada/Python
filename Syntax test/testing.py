import sys
import csv


def stringFunctions():
    print('\n' * 100)

    cadena = " Hola , jose "
    print(cadena.find("l"))
    print(cadena)
    cadenaReplace = cadena.replace("Hola","#$%%^")
    print((cadenaReplace))

    cadenaStrip = cadena.rstrip()
    print(cadenaStrip)

    cadenaStrip = cadena.lstrip()
    print(cadenaStrip)

    upperCase = cadena.upper()
    print(upperCase)

    split = cadena.split(",")
    print(split)

def orderingMethods():
    list = [0,0,2,12,45,6]
    print(sorted(list, reverse=True))

    orderedList = sorted(list)
    print(orderedList)

    list = ["xc1","fm5","fwf"]
    orderedList = sorted(list)
    print(orderedList)

def conjunctionMethods():
    conjunction = set('7042')
    conjunction2 = {'5','0','4','3'}

    print(conjunction)
    print(conjunction2)

    print(conjunction | conjunction2)
    print(conjunction & conjunction2)

    print(conjunction.intersection(conjunction2))
    print(conjunction.union(conjunction2))
    print(conjunction.difference(conjunction2))

def csvWriteMethods():

    doc = open("file.csv", "w")

    doc_csv_w = csv.writer(doc)
    list = [["jose",99836],["juan", 99836, 'fjw'],["david",92394,"3242","32"]]
    #doc_csv_w.writerow(list)
    #doc_csv_w.writerows(list)

    for item in list:
        doc_csv_w.writerow(item)

    doc.close()

def csvReadMethods():
    doc = open("file.csv","r")
    doc_csv_r = csv.reader(doc)

    for item in doc_csv_r:
        print(item)

    doc.close()