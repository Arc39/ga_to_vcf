import json
import argparse

if __name__ == '__main__':
    #sets command line input file 
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input file")
    p = parser.parse_args()
    assert p.input

    inputFile = open(p.input)
    oFile = open('outputData.txt','w')
    items = []
    readItems = inputFile.read()
    loadItems = json.loads(readItems)

    metadata = loadItems['metadata']
    name = loadItems['name']
    refsetId = loadItems['referenceSetId']
    datasetId = loadItems['datasetId']
    _id = loadItems['id']

    d = [[]]

    for item in loadItems:
        items.append(item)

    """Separating the items in metadata"""
    for x,y in enumerate(metadata):
        print "##INFO=<ID=",y['id'],"Number=",y['number'],"Type=",y['type'],"Description=",y['description'],"Info=",y['info'],"value=", y['value'],"key=", y['key'],">"
        