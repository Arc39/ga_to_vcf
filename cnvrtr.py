import json
import argparse
import os

"""This functions accesses the individual variant files by storing the path"""
def readVarFiles():
    varData = []
    path = "/Users/mathuser2/Documents/work/vcf_to_ga/output/variantSet/variants/"
    for file in os.listdir(path):
        if file.endswith(".txt"):
            varData.append(path+file)

if __name__ == '__main__':
    #sets command line input file 
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input file")
    #need to add path argument here
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


    for item in loadItems:
        items.append(item)
    """GA4GH object does not contain VCF version so just assigning 4.1 for now"""
    print "##fileformat=VCFv4.1"
    print "##name={name}".format(name=name)
    readVarFiles()

    """Separating the items in metadata"""
    for x,y in enumerate(metadata):
        print "##INFO=<ID={id}".format(id=y['id']),"Number={number}".format(number=y['number']),"Type={type}".format(type=y['type']),"Description={description}".format(description=y['description']),"Info={info}".format(info=y['info']),"value={value}".format(value=y['value']),"key={key}>".format(key=y['key'])
  