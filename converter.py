class converter(AbstractConverter):

	def writeHeader(self,opFile):
		variantSet = self._container
		opFile.write("##fileformat=VCFv4.1")
		opFile.write("##datasetid={datasetid}".format(datasetid=variantSet.datasetId))
        opFile.write("##variantSetId={id}".format(id=variantSet.id))

        for metadata in variantSet.metadata:
        	opFile.write("##INFO=<ID={id}".format(id=metadata.id),"Number={number}".format(number=metadata.number),"Type={type}".format(type=metadata.type),"Description={description}".format(description=metadata.description),"Info={info}".format(info=metadata.info),"value={value}".format(value=metadata.value),"key={key}>".format(key=metadata.key))
		opFile.write("#CHROM POS ID REF ALT QUAL FILTER INFO")

	
	def writeVariants(self,opFile):
		varIter = self._objectIterator

		for variant in varIter:
			opfile.write(variant)

	def writeVCF(self):
		opFile = open('self._outputFile', 'w')
		self.writeHeader(opfile)
		self.writeVariants(opfile)
		opfile.close()