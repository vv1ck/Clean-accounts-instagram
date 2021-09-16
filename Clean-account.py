import requests , time
from json import dumps
r = requests.session()


print("""
    _     By JOKER insta @221298  _ 
   / \   ___ ___ ___  _   _ _ __ | |_ ___
  / _ \ / __/ __/ _ \| | | | '_ \| __/ __|
 / ___ \ (_| (_| (_) | |_| | | | | |_\__ \ 
/_/   \_\___\___\___/ \__,_|_| |_|\__|___/

[1] delet following | [2] delet chat
[3] delet your post | [4] delet Saved Post
""")
joker = input('Enter the number : ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
time.sleep(1)
user = input("\nEnter username : ")
pess = input("Enter password : ")
def deletSEVE():
	def poSF():
		global iid , sis
		sis = go.cookies['sessionid']
		urPF = 'https://www.instagram.com/web/save/{}/unsave/'.format(iid)
		
		hedPF = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CMsEWimjxqE/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'}
		
		jok = r.post(urPF,headers=hedPF)
		if '"status":"ok"' in jok.text:
			print('[+] The saved video has been deleted')
		else:
			print('[-] You have been banned !')
	
	def infoSEV():
		global go , iid , slp
		while True:
			sis = go.cookies['sessionid']
			ur = 'https://www.instagram.com/{}/?__a=1'.format(user)
			
			hedID = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'cache-control': 'no-cache',
			'cookie': 'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; fbm_124024574287414=base_domain=.instagram.com; ig_nrcb=1; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid='+sis,
			'pragma': 'no-cache',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'cross-site',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
			time.sleep(slp)
			id = requests.get(ur,headers=hedID)
			try:
				iid = id.json()['graphql']['user']['edge_saved_media']['edges'][0]['node']['id']
				poSF()
			except IndexError:
				print('There are no saved videos !')
				print('Follow me | insta: 221298 | tele: vv1ck')
				exit()
	infoSEV()
def chatMS():
	def aco():
		global go , foCH , foCU
		sis = go.cookies['sessionid']
		urA = 'https://i.instagram.com/api/v1/direct_v2/threads/{}/hide/'.format(foCH)
		
		hedA = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '1217981644879628',
			'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEmIg',
			'x-instagram-ajax': '753ce878cd6d'}
		
		g = r.post(urA,headers=hedA)
		
		if '"status":"ok"' in g.text:
			print(f'[+] The chat has been deleted -> {foCU}')
		
		else:
			print('[-] You have been banned ! ')
	
	def idCHT():
		global go , foCH , foCU , slp
		sis = go.cookies['sessionid']
		while True:
			urCH = 'https://i.instagram.com/api/v1/direct_v2/inbox/?persistentBadging=true&cursor='
			
			hedCH = {
				'accept': '*/*',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
				'origin': 'https://www.instagram.com',
				'referer': 'https://www.instagram.com/',
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-site',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
				'x-ig-app-id': '936619743392459',
				'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'}
			time.sleep(slp)
			j=r.get(urCH,headers=hedCH)
			
			try:
				foCH = str(j.json()['inbox']['threads'][0]['thread_id'])
				
				foCU = str(j.json()['inbox']['threads'][0]['users'][0]['username'])
				aco()
			except IndexError:
				print('\nThere are no messages to delete !')
				print('Follow me | insta: 221298 | tele: vv1ck')
				exit()
	idCHT()
def post():
	def pos():
		global iid , go , iid
		sis = go.cookies['sessionid']
		urDP = 'https://www.instagram.com/create/{}/delete/'.format(iid)
		
		hedDP = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; ds_user_id=46165248972; shbid=13126; shbts=1616804137.1316793; rur=PRN; csrftoken=mnnbqhStTDAfu10DkI2VrW5VoCg9InFk; sessionid='+sis,
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/p/CM5_0EfBliscG9z8SJBY1iasqct_jP0jEJsNCU0/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'mnnbqhStTDAfu10DkI2VrW5VoCg9InFk',
			'x-ig-app-id': '1217981644879628',
			'x-ig-www-claim': 'hmac.AR24Fkd2DvunQ5ELQD_I_6FoVMTbIdkiDD08ZF2jyPhpEvg3',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'}
		
		dl = r.post(urDP,headers=hedDP)
		if '"status":"ok"' in dl.text:
			print(f'[+] Deleted [ id post > {iid}]')
		else:
			print('[-] You have been banned !')
	def usID():
		global go , iid , slp
		while True:
			sis = go.cookies['sessionid']
			ur = 'https://www.instagram.com/{}/?__a=1'.format(user)
			
			hedID = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
			'cache-control': 'no-cache',
			'cookie': 'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; fbm_124024574287414=base_domain=.instagram.com; ig_nrcb=1; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid='+sis,
			'pragma': 'no-cache',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'cross-site',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
			time.sleep(slp)
			id = requests.get(ur,headers=hedID)
			try:
				iid = id.json()['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['id']
				pos()
			except IndexError:
				print('There are no videos to delete !')
				print('Follow me | insta: 221298 | tele: vv1ck')
				exit()
	usID()
def folloing():
	def dltFLG():
		global foID , foNM , go , iid
		cook = go.cookies['sessionid']
		url = 'https://www.instagram.com/web/friendships/{}/unfollow/'.format(foID)
		
		hedDLT = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '0',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid='+cook,
			'origin': 'https://www.instagram.com',
			'referer': f'https://www.instagram.com/{user}/following/',
			'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
			'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
			'x-instagram-ajax': '753ce878cd6d',
			'x-requested-with': 'XMLHttpRequest'}
		
		don = r.post(url,headers=hedDLT)
		
		if '"status":"ok"' in don.text:
			print(f'[+] Deleted username >> {foNM}')
		elif 'Please' in don.text:
			print('[-] Banned, try again another time !')
		else:
			print('error !')
	def userID():
		global go , foID , foNM , iid , slp
		while True:
			cook = go.cookies['sessionid']
			tok = 'd04b0a864b4b54837c0d870b0e77e076'
			
			cookies = {
			"sessionid": cook,}
			
			variables = {
				"id": iid,
				"first": 50}
			
			params = {
				"query_hash": tok,
				"variables": dumps(variables)}
			time.sleep(slp)
			ok = r.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
			try:
				foID = str(ok.json()['data']['user']['edge_follow']['edges'][0]['node']['id'])
				foNM = str(ok.json()['data']['user']['edge_follow']['edges'][0]['node']['username'])
				dltFLG()	
			except IndexError:
				print('There is no account to delete')
				print('Follow me | insta: 221298 | tele: vv1ck')
				exit()
	def usID():
		global go , iid 
		sis = go.cookies['sessionid']
		ur = 'https://www.instagram.com/{}/?__a=1'.format(user)
		
		hedID = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		'cache-control': 'no-cache',
		'cookie': 'ig_did=D5BC7E80-9785-4758-B94C-E128617D353B; mid=XsL1CAAAAAG9iRyIP2cLrfuZ7CUm; fbm_124024574287414=base_domain=.instagram.com; ig_nrcb=1; datr=9D0-YLR0rApS9iOG6npp3drV; shbid=489; shbts=1616344547.8202462; rur=ASH; csrftoken=origpnsxJ21mHIJCxkuOltceXsKKhTA2; ds_user_id=45572593982; sessionid='+sis,
		'pragma': 'no-cache',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'cross-site',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
		
		id = requests.get(ur,headers=hedID)
		iid = id.json()['graphql']['user']['id']
		userID()
	usID()
def sc():
	global headLG , go , datLG , slp
	st = go.json()['checkpoint_url']
	coke = go.cookies
	urSC= 'https://www.instagram.com' + st
	g=r.post(urSC,data=datLG,headers=headLG,cookies=coke)
	if ("phone_number") in g.text:
		print("\n 0 >> Phone \n")
	if ("email") in g.text:
		print("\n 1 >> Email \n")
	snd = input('Enter the type of send : ')
	datSC = {
		"choice": snd}
	go1 = r.post(urSC,data=datSC,headers=headLG,cookies=coke)
	if ("security_code") in go1.text:
		code = input('\n Enter the security code : ')
		datCO = {
			"security_code": code}
		go = requests.post(urSC,data=datCO,headers=headLG,cookies=coke)
		if ("ok") in go.text:
			print(f'\n\tHello {user} | Done login\n')
			if joker == '1':
				slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
				print('')
				folloing()
		elif joker == '2':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '3':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			post()
		elif joker == '4':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			deletSEVE()
		else:
			print('\n The security code is invalid !')
def ta():
	global headLG , go ,slp
	print('  \ntwo factor ')
	st = go.json()['two_factor_info']['two_factor_identifier']
	coke = go.cookies
	cod = input('\n Enter the security code : ')
	
	datTA = {
		'username': user,
		'verificationCode': cod,
		'identifier': st,
		'queryParams': '{"next":"/"}'}
	
	go = r.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=headLG,data=datTA,cookies=coke)
	
	if ("userId") in go.text:
		print(f'\n\tHello {user} | Done login\n')
		if joker == '1':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			folloing()
		elif joker == '2':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '3':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			post()
		elif joker == '4':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			deletSEVE()
	elif ("checkpoint_url")  in go.text:
		sc()
	else:
		print('\n The security code is invalid !')

def login():
	global headLG , go , datLG , slp 
	urLG = "https://www.instagram.com/accounts/login/ajax/"
	headLG = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'content-length': '272',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/accounts/login/',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
		'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		'x-instagram-ajax': '790551e77c76',
		'x-requested-with': 'XMLHttpRequest'}
	
	datLG = {
		"username": user,
		"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
		"queryParams": "{}",
		"optIntoOneTap": "false"}
	
	go = r.post(urLG,headers=headLG,data=datLG)
	
	if ("userId") in go.text:
		print(f'\n\tHello {user} | Done login\n')
		if joker == '1':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			folloing()
		elif joker == '2':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			chatMS()
		elif joker == '3':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			post()
		elif joker == '4':
			slp = int(input('[+] Enter sleep [ 3 / 7 ] : '))
			print('')
			deletSEVE()
	elif ("two_factor") in go.text:
		print('\n Binary verification \n')
		ta()
	elif ("checkpoint_url")  in go.text:
		print('\n Account Secure \n')
		sc()
	else:
		print('\nThe username or password is wrong ! \n')
login()
