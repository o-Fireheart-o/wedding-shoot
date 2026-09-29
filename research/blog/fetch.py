import re, json, urllib.request, concurrent.futures as cf, html
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36"}
urls=[l.strip() for l in open('cand.txt') if l.strip()]
def get(u):
    b,n=u.rsplit('/',2)[-2:]
    try:
        r=urllib.request.urlopen(urllib.request.Request(f"https://blog.naver.com/PostView.naver?blogId={b}&logNo={n}",headers=UA),timeout=20).read().decode('utf-8','ignore')
    except Exception as e: return dict(url=u,err=str(e))
    t=re.search(r'<meta property="og:title" content="([^"]*)"',r); t=html.unescape(t.group(1)) if t else ''
    d=re.search(r'se_publishDate[^>]*>([^<]+)<',r) or re.search(r'"publishDate"\s*:\s*"([^"]+)"',r)
    body=re.sub(r'<[^>]+>',' ',r[r.find('se-main-container'):]) if 'se-main-container' in r else ''
    imgs=[]
    for m in re.finditer(r'data-lazy-src="(https://postfiles\.pstatic\.net/[^"]+)"',r):
        s=html.unescape(m.group(1)).split('?')[0]
        if s not in imgs: imgs.append(s)
    txt=re.sub(r'\s+',' ',html.unescape(body))
    return dict(url=u,title=t,date=d.group(1).strip() if d else '',bong=('봉스튜디오' in txt or '봉 스튜디오' in txt or '봉스' in t or '봉스튜디오' in t),
      hanam=bool(re.search(r'하남|미사',txt)),imgs=imgs,n=len(imgs),text=txt[:6000])
with cf.ThreadPoolExecutor(12) as ex: res=list(ex.map(get,urls))
json.dump(res,open('posts.json','w',encoding='utf-8'),ensure_ascii=False)
ok=[r for r in res if r.get('bong') and r.get('hanam') and r.get('n',0)>0 and ('봉' in r.get('title',''))]
print(len(res),'ok',len(ok),'err',sum('err' in r for r in res))
for r in ok: print(r['n'],r['date'][:12],r['url'],r['title'][:60])
