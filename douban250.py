import urllib.request
from pyquery import PyQuery as pq
import os

def HttpGet(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html=pq(response.read().decode("utf-8"))
    return html




finfo=open("豆瓣电影TOP250.txt","w",encoding='utf-8')


cc=0
for psize in range(0,10):
     purl="https://movie.douban.com/top250?start="+str(psize*25)+"&filter="
     phtml=PyHelper.HttpGet(purl)
     mlist=phtml(".info")
     for mitem in mlist.items():
         cc+=1
         mname = str(cc)+".  《" + mitem.find(".hd").find("a").find("span").eq(0).text()+"》"
         mstar=mitem.find(".rating_num").text()
         daoyan=mitem.find(".bd").find("p").eq(0).html().split("<br/>")[0].strip().lstrip().rstrip(',')
         mtype =mitem.find(".bd").find("p").eq(0).html().split("<br/>")[1].strip().lstrip().rstrip(',')
         mtext = mitem.find(".bd").find(".inq").text()
         finfo.write("\n\n") 
         finfo.write("  -------------------------------------------\n")
         finfo.write("\n")
         finfo.write("    "+mname+"  ")
         finfo.write("  "+mstar+"分"+ "\n")
         finfo.write("\n")
         finfo.write("    "+daoyan+ "\n")
         finfo.write("    "+mtype+ "\n")
         finfo.write("    "+mtext+ "\n")
         print("正在抓取第"+str(cc)+"条  :  "+mname)

print("全部抓取完成")
finfo.close()