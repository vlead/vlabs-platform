import json
import os


def safe_make_folder(i):

	'''makes folder if not present'''
	try:
		os.mkdir(i)
        except:
		pass
def experiments(data_dict):
	'''returns experiments'''
	try:
	   	exps = data_dict.get('experiments')
	except:
		   pass
	return exps
def createFiles(exps, srcPath):
	'''creates folders for exp and files inside them'''
	n = len(exps)
	for i in range(0,n):
		expName = exps[i].get('name')
		tmpPath = srcPath + '/' + expName
		safe_make_folder(tmpPath)
		subsec = exps[i].get('subsections')
		m = len(subsec)
		for j in range(0,m):
			fileName = subsec[j].get('name')
			filePath = tmpPath + '/' + fileName + '.org'
			open(filePath, 'a').close()
if __name__ == '__main__':
	with open('/home/akshay1123/Desktop/VLABS/lab-specifications/IIIT-Hyderabad/natural-language-processing-lab.labspec.json') as data_file:
		data = json.load(data_file)
	exps = experiments(data)
	createFiles(exps, '/home/akshay1123/Desktop/CreatedByCode')

