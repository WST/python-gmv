
# (C) 2014 Ilya Averkov (WST)
# http://ilya.averkov.net

from struct import unpack

class Movie:
	def __init__(self, filename):
		with open(filename, 'rb') as f:
			header = f.read(64)
			if not header.startswith('Gens Movie TEST'):
				raise Exception("The file is not a valid Gens movie file")

			self.header = unpack('15scib2bb40s', header)

	def rerecords(self):
		return self.header[2]

	def comment(self):
		return self.header[7].replace('\x00', '')
