import requests, json, pprint


token = 'bac0931a61f0f8c1823b5b644811ca205a79b549'
auth = {'Authorization': 'token '+str(token)}
url = 'https://api.github.com/search/repositories?q=django&sort=stars'

file = open('Output02.txt', 'w')
file.write('liberay\t\t\t fequency\n')

request = requests.get(url,headers=auth)
data = json.loads(request.content)

if request.ok:
	data1 = data['items'][:20]
	url2 = 'https://api.github.com/search/code?q=filename:requirements.txt+repo:'
	url3 = 'https://api.github.com/search/code?q=filename:requirements-dev.txt+repo:'
	dictionary = {}
	for i in range(len(data1)):
		request1 = requests.get(url2+data1[i]['full_name'],headers=auth)
		data2 = json.loads(request1.content)
		if 'total_count' not in data2.keys():
			continue
		if data2['total_count'] == 0:
			request2 = requests.get(url3+data1[i]['full_name'],headers=auth)
			data2 = json.loads(request1.content)
			if 'total_count' not in data2.keys() or data2['total_count'] == 0:
				continue
		for j in range(len(data2['items'])):
			dat = data2['items'][j]
			# print(dat['url'])
			print('something is running')
			print('.....wait')
			file1 = requests.get(dat['url'],headers=auth)
			filedata = json.loads(file1.content)
			if 'download_url' not in filedata.keys():
				continue
			res = requests.get(filedata['download_url'])
			res = res.content
			res = res.split('\n')
			for k in res:
				if k in dictionary.keys():
					dictionary[k]+=1
				else:
					dictionary[k]=1
	l = sorted(dictionary.items(), key=lambda x: x[1])
	l.pop()
	for i in range(len(l)):
		file.write(str(l[i])+'\n')