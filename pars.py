import re 
import os

print(' < -o- > hallo mate, lets start!')

word_dir = 'text'
res_dir = 'result'

def formatme(nfile):
	path = os.path.join(word_dir, nfile)
	print (" < -o- > File: " + path)
	file = open(path,"r")
	fulltext = ''
	result = ''

	for line in file:
		fulltext += line

	# sents = re.split(r' *[\.*\?*!*]\s', fulltext)
	for sent in re.split(r' *[\n{2}\.\?!;][\.\?!]*', fulltext):
		print(' <- + ->')
		print(sent)
		tmp = ''
		for pice in re.split('\n', sent):
			if pice == r'\n+' or pice == '':
				continue
			tmp += pice
		print(' < : > ' + tmp)
		if len(tmp) > 3: 
			result += tmp.strip() + '\n' 
		else:
			continue
	# for i in range(0, len(sent)):
	# 	print(' <:>')
		# print(pice[i])
		

	# for line in file:
	# 	tmp = line.split('\n')
	# 	print(' <:>')
	# 	print(line)
	# 	# tmp = line
	# 	for text in tmp:
	# 		if text == '':
	# 			continue
	# 		if text == '\n':
	# 			continue

	# 		# pice = re.split(r' *[\.\?!][\'"\)\]]*\s', text)
	# 		pice = re.split(r' *[\.\?!...]', text)

	# 		tmp = ''
	# 		tmp2 =''
	# 		# for text in split:
	# 		for i in range(0, len(pice)):
	# 			text = pice[i]
	# 			print(' <+>')
	# 			print(text)
	# 			if text == '':
	# 				continue
	# 			if text == '\n':
	# 				continue
	# 			word = text.split(' ')[-1]pice = re.split(r' *[\.\?!][\'"\)\]]*\s', text)
	# 			first = pice[0]

	# 			if len(tmp) > 0:
	# 				text = tmp + text
	# 				tmp = ''
				
	# 			result += text + "\n"
	file.close();
	file = open(os.path.join(res_dir, nfile), 'w+')
	file.write(result)
	file.close();

class MySentences(object):
	def __init__(self, dirname):
		self.dirname = dirname

	def format(self):
		for fname in os.listdir(self.dirname):
			formatme(fname)

sentences = MySentences( word_dir )
sentences.format();

print(' < -o- > The work is done!')
