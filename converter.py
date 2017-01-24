class converter(AbstractConverter):

    def writeHeader(self):
        variantSet = self._container
        outputFile = self._outputFile
        outputFile.write("##fileformat=VCFv4.1")
        outputFile.write("##datasetid={datasetid}".format(datasetid=variantSet.dataset_id))
        outputFile.write("##variantSetId={id}".format(id=variantSet.id))

        for metadata in variantSet.metadata:
            outputFile.write("##INFO=<ID={key},Number={number},Type={type},Description={description},Info={info},value={value}".format(key=metadata.key,number=metadata.number,type=metadata.type,description=metadata.description,info=metadata.info,value=metadata.value))
        outputFile.write("#CHROM POS ID REF ALT QUAL FILTER INFO")

    
    def writeVariants(self):
        varIter = self._objectIterator

        for variant in varIter:
            print variant

    def writeVCF(self):
        self.writeHeader()
        self.writeVariants()