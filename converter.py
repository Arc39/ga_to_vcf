class converter(AbstractConverter):

	def writeHeader(self):
		variantSet = self._container
        print("##fileformat=VCFv4.1")
        print("##datasetid={datasetid}".format(datasetid=variantSet.dataset_id))
        print("##variantSetId={id}".format(id=variantSet.id))

        for metadata in variantSet.metadata:
            print("##INFO=<ID={key}".format(key=metadata.key),"Number={number}".format(number=metadata.number),"Type={type}".format(type=metadata.type),"Description={description}".format(description=metadata.description),"Info={info}".format(info=metadata.info),"value={value}".format(value=metadata.value))
        print("#CHROM POS ID REF ALT QUAL FILTER INFO")

	
	def writeVariants(self):
		varIter = self._objectIterator

		for variant in varIter:
			print variant

	def writeVCF(self):
		self.writeHeader(opfile)
		self.writeVariants(opfile)