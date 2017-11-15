import requests, json

token = 'bac0931a61f0f8c1823b5b644811ca205a79b549'	
auth = {'Authorization': 'token '+str(token)}
url = 'https://api.github.com/search/repositories?q=django&sort=stars'

file = open('firstOutpur.txt', 'w')
file.write('Name \t Repo\n')

request = requests.get(url,headers=auth)
data = json.loads(request.content)

if request.ok:
	data1 = data['items'][:20]
	# d= sorted(d, key=lambda x:(x['score']))
	# print(len(d))
	# i =20;
	for i in range(0,20):
		file.write(data1[i]['name']+'\t'+data1[i]['full_name']+'\n')
