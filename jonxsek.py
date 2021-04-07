import requests,re

url = "https://zone-xsec.com/archive/page="

for a in range(1,50):
  r = requests.get(url+str(a))
  r = r.text.replace("\n","")
  preg = re.findall(r'<tr class="texw">(.*?)<\/tr>',r)
  for oey in preg:
    pel = re.findall(r'<td>(.*?)<\/td>',oey)
    ler = re.findall(r'(.*?)\/(.*?)',pel[5])
    if ler:
      open('hasil.txt','a').write(ler[0][0]+"\n")
    else:
      open('hasil.txt','a').write(pel[5]+"\n")
print("Done in hasil.txt")
