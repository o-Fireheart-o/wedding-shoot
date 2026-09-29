import re, json, sys, urllib.request, html, os
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36"}
os.makedirs('seq',exist_ok=True)
def seq(u):
    b,n=u.rstrip('/').rsplit('/',2)[-2:]
    fn=f'seq/{b}_{n}.txt'
    if os.path.exists(fn): return open(fn,encoding='utf-8').read()
    r=urllib.request.urlopen(urllib.request.Request(f"https://blog.naver.com/PostView.naver?blogId={b}&logNo={n}",headers=UA),timeout=20).read().decode('utf-8','ignore')
    r=r[r.find('se-main-container'):]
    r=r[:r.find('post_footer_contents')] if 'post_footer_contents' in r else r
    out=[];k=0
    for m in re.finditer(r'data-lazy-src="(https://postfiles\.pstatic\.net/[^"]+)"|<p[^>]*class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>|class="se-caption[^"]*"[^>]*>(.*?)</div>',r,re.S):
        if m.group(1):
            k+=1; out.append(f"[IMG{k}] "+html.unescape(m.group(1)).split('?')[0])
        else:
            t=re.sub(r'<[^>]+>','',m.group(2) or m.group(3) or ''); t=re.sub(r'\s+',' ',html.unescape(t)).strip()
            if t and t!='\u200b': out.append(("(캡션) " if m.group(3) else "")+t)
    s="\n".join(out); open(fn,'w',encoding='utf-8').write(s); return s
if __name__=='__main__':
    for u in sys.argv[1:]: print('=====',u); print(seq(u))
