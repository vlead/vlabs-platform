from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join, splitext
import sys, json, re

def editName(name):
	name = name.lower()
	newName = re.sub(r'[^a-zA-Z0-9\s+-]', '', name)
	newName = newName.strip()
	finalName = re.sub('\s+', '-', newName)
	return finalName

def addHooks(files, expPath, labName, expName):
	for f in files:
		fileName, ext = splitext(f)
		if ext == '.html':
			ptree = BeautifulSoup(open(join(expPath, f)))
			headList = ptree.find_all(re.compile("^h[0-9]$"))
			for h in headList:
				h['id'] = labName + '-' + expName + '-' + fileName
				print h['id']
			pList = ptree.find_all('p')
			for p in pList:
				p['id'] = labName + '-' + expName + '-' + fileName +'-content'	
			new_html_content = ptree.prettify()
			k = open('/home/akshay1123/Desktop/VLABS/newhtml.html', 'w')
			k.write(new_html_content)
			k.close()
if __name__ == '__main__':
	try:
		dirPath = sys.argv[1]
		jsonPath = sys.argv[2]
	except Exception as error:
		print('Error: '+str(error))
	with open(jsonPath) as data_file:
		data = json.load(data_file)
	exps = data.get('experiments')
	labName = data.get('course').get('display_name')
	labName = editName(labName)
	for i in exps:
		expName = i.get('name')
		expName = editName(expName)
		expPath = join(dirPath, expName)
		expName = editName(expName)
		onlyfiles = [f for f in listdir(expPath) if isfile(join(expPath, f))]
		addHooks(onlyfiles, expPath, labName, expName)
		
	
