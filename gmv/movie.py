
# (C) 2014 Ilya Averkov (WST)
# http://ilya.averkov.net

class Movie:
	def __init__(self, filename):
		f = open(filename, 'r')
		header = f.read(63)
		if not header.startswith('Gens Movie TEST'):
			raise Exception("The file is not a valid Gens movie file")

		self.header = struct.unpack('15scib2bb40s', header)
		f.close()

	def rerecords(self):
		return self.header[2]

	def comment(self):
		return self.header[7]
