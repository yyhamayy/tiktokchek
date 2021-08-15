# Decompiled By YY HAMA YY
import requests,random
import bs4,threading,time
n = '\033[1;32m'
o  = '\033[1;31m'
jmatin = '\033[1;33m'
_matin  = '\033[1;31m'
BGreen='\033[1;32m'
matin__ = '\033[1;36m'
BRed ='\033[1;31m'
t='\033[1;36m'
p='\033[1;31m'
E=(t+'='*60)
print(f"""{jmatin}{E}
{matin__}
		                        
 __  ____  __     __ _____   __  ______     __  ____  __
 \ \/ /\ \/ /    / // / _ | /  |/  / _ |    \ \/ /\ \/ /
  \  /  \  /    / _  / __ |/ /|_/ / __ |     \  /  \  / 
  /_/   /_/    /_//_/_/ |_/_/  /_/_/ |_|     /_/   /_/  
                                                        
		                  
  	  	{o}~{t} Coded By YY HAMA YY {o}~
{E}""")

tuks1 = 'poiuytrewqasdfghjklmnbvcxz12'
hcx = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) InspectBrowser',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-us'
}
tok = input(jmatin+'['+_matin+'+'+jmatin+']'+matin__+' TOKEN BOT! -> ;'+BGreen)
id = input(jmatin+'['+_matin+'+'+jmatin+']'+matin__+' ID TELEGRAM ! -> ;'+BGreen)
print(E)
Number =0
while True:
	Number +=1
	user = str("".join(random.choice(tuks1)for i in range(4)))
	r = requests.get(f'http://tiktok.com/@{user}',headers=hcx).text
	
	try:
		html = bs4.BeautifulSoup(r,'html.parser')
		ruks = html.findAll("div",{"class":"jsx-2735606716 main user-page"})[0]
		#print(matin)
		
		kk =ruks.findAll("h2",{"class":"jsx-720436192 user-profile-nickname"})[0]
		
		#print(o+usertiktok.txt)
		print(jmatin+'['+BRed+f'{Number}'+jmatin+'] NYA'+BRed+f'-[{usertiktok.txt}]')		
	except:
		
		print(jmatin+'['+BGreen+f'{Number}'+jmatin+'] HAYA'+BGreen+f' [@{user}]')
		tt=time.asctime()	
		req = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=⌯  NEW USER ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{user}\n⌯ {tt} \n. — — — — —  — — — — —\n• Tele : @iiyiyiyi . @iiyiyiyi .')          	
		
