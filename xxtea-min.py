from re import findall as a2;import ctypes as a1;A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';B=True;C=False;D='Unfinished UTF-8 octet sequence';E='Character outside valid Unicode';F='Bad UTF-8 encoding';G=-1;H=63;I=128;J=65536;K=12;c0=len;c1=range;c2=Exception;c3=ord
def a0(i,j=0x7fffffff):return(i+(j+1))%(2*(j+1))-j-1 if not-j-1<=i<=j else i
def b0(i,j):
 if i<0:i=a1.c_uint32(i).value
 if j<0:return-a0(i<<abs(j))
 return a0(i>>j)
b2=lambda i,*j:chr(i%J)+''.join([chr(k%J) for k in j])
def b9(i):
 j=f'{A}+/';k=l=0;m=c0(i);s=m%3;m=m-s;t=a0(int(m/3)<<2)
 if s>0:t+=4
 u=['']*t
 while k<m:o=a0(c3(i[k])<<16);k+=1;p=a0(c3(i[k])<<8);k+=1;q=c3(i[k]);k+=1;r=o|p|q;u[l]=j[r>>18]+j[r>>K&H]+j[r>>6&H]+j[r&H];l+=1
 if s==1:r=c3(i[k]);k+=1;u[l]=j[r>>2]+j[a0((r&3)<<4)]+'==';l+=1
 elif s==2:o=a0(c3(i[k])<<8);k+=1;p=c3(i[k]);k+=1;r=o|p;u[l]=j[r>>10]+j[r>>4&H]+j[a0((r&15)<<2)]+'='
 return''.join(u)
def b8(i):
 j=([G]*43);j.extend([62,*([G]*3),H,*([_ for _ in c1(52,62)]),*([G]*7),*([_ for _ in c1(0,26)]),*([G]*6),*([_ for _ in c1(26,52)]),*([G]*5)]);k=c0(i)
 if k%4!=0:return''
 if a2(rf'[^{A}\+\/\=]',i):return''
 if i[-2]=='=':l=1
 elif i[G]=='=':l=2
 else:l=0
 s=k
 if l>0:s-=4
 s=(s>>2)*3+l;t=['']*s;u=v=0
 while u<k:
  o=j[c3(i[u])];u+=1
  if o==G:break
  p=j[c3(i[u])];u+=1
  if p==G:break
  t[v]=b2(a0(o<<2)|((p&48)>>4));v += 1;q=j[c3(i[u])];u+=1
  if q==G:break
  t[v]=b2(a0((p&15)<<4)|((q&60)>>2));v+=1;r=j[c3(i[u])];u+=1
  if r==G:break
  t[v]=b2(a0((q&3)<<6)|r);v+=1
 return''.join(t)
def b7(i,j,t=0):
 k=c0(i);s=a0(k<<2)
 if j:
  l=i[k-1];s-=4
  if l<s-3 or l>s:return None
  s=l
 while t<k:i[t]=b2(i[t]&255,b0(i[t],8)&255,b0(i[t],16)&255,b0(i[t],24)&255,);t+=1
 u=''.join(i)
 return u[0:s] if j else u
b6=lambda i,j,k,l,m,n:((b0(k,5)^j<<2)+(b0(j,3)^k<<4))^((i^j)+(n[l&3^m]^k))
b5=lambda i:a0(i&0xFFFFFFFF)
def b4(i,j):
 k=c0(i);l=k-1;s=i[l];t=0;u=(int(6+52/k)|0)
 while u>0:
  t=b5(t+0x9E3779B9);v=b0(t,2)&3;w=0
  while w<l:o=i[w+1];s=i[w]=b5(i[w]+b6(t,o,s,w,v,j));w+=1
  o=i[0];s=i[l]=b5(i[l]+b6(t,o,s,l,v,j));u-=1
 return i
def b3(i,j):
 k=c0(i);l=k-1;s=i[0];t=int(6+52/k);u=b5(t*0x9E3779B9)
 while u!=0:
  v=b0(u,2)&3;o=l
  while o>0:p=i[o - 1];s=i[o]=b5(i[o]-b6(u,s,p,o,v,j));o-=1
  p=i[l];s=i[0]=b5(i[0]-b6(u,s,p,0,v,j));u=b5(u-0x9E3779B9)
 return i
def b1(i):i.extend([0]*(4-c0(i)));return i
def a4(i,j):
 k=c0(i);l=k>>2
 if k&3!=0:l+=1
 if j:m=[0]*(l+1);m[l]=k
 else:m=[0]*l
 for n in c1(k):m[n>>2]=m[n>>2]|a0(c3(i[n])<<a0((n&3)<<3))
 return m
def a3(i):
 if a2(r'^[\x00-\x7f]*$',i):return i
 j=[None]*c0(i);k=c0(i);l=m=0
 while l<k:
  s = c3(i[l])
  if s<I:j[m]=i[l]
  elif s<2048:j[m]=b2(192|(s>>6),I|(s&H))
  elif s<0xD800 or s>0xDFFF:j[m]=b2(224|(s>>K),I|((s>>6)&H),I|(s&H))
  else:
    if l+1<k:
     t=c3(i[l+1])
     if s<0xDC00 and 0xDC00<=t and t<=0xDFFF:u=(((s&0x03FF)<<10)|(t&0x03FF))+J;j[m]=b2(240|((u>>18)&H),I|((u>>K)&H),I|((u>>6)&H),I|(u&H));l+=1
  l+=1;m+=1
 return''.join(j)
def a5(i,j):
 k,s=[0]*j,c0(i);l=m=0
 while l<j and m<s:
  t=c3(i[m]);m+=1;u=t>>4
  if u in(0,1,2,3,4,5,6,7):k[l]=t
  elif u in(K,13):
   if m<s:k[l]=a0((t&31)<<6)|(c3(i[m])&H);m+=1
   else:c1(D)
  elif u in[14]:
   if m+1<s:o=a0((c3(i[m])&H)<<6);m+=1;p=c3(i[m])&H;m+=1;k[l]=a0((t&15)<<K)|o|p
   else:c1(D)
  elif u in[15]:
   if m+2<s:
    o=a0((c3(i[m])&H)<<K);m+=1;p=a0((c3(i[m])&H)<<6);m+=1;q=(c3(i[m])&H);m+=1;r=(a0((t&7)<<18)|o|p|q)-J
    if 0<=r and r<=0xFFFFF:k[l]=(((r>>10)&0x03FF)|0xD800);l+=1;k[l]=(r&0x03FF)|0xDC00
    else:c1(E)
   else:c1(D)
  else:c1(F)
  l+=1
 if l<j:k=k[:l]
 return b2(*k)
def a6(i, j):
 k,l,s=[],[0]*0x8000,c0(i);m=n=0
 while m<j and n<s:
  t=c3(i[n]);n+=1;u=t>>4
  if u in[0,1,2,3,4,5,6,7]:
   l[m] = t
  elif u in[K,13]:
   if n < s:l[m]=a0((t&31)<<6)|(c3(i[n])&H);n+=1
   else:c2(D)
  elif u in[14]:
   if n+1<s:o=a0((c3(i[n])&H)<<6);n+=1;p=c3(i[n])&H;n+=1;l[m]=a0((t&15)<<K)|o|p
   else:c2(D)
  elif u in[15]:
   if n+2<s:
    o=a0((c3(i[n])&H)<<K);n+=1;p=a0((c3(i[n])&H)<<6);n+=1;q=c3(i[n])&H;n+=1;r=(a0((t&7)<<18)|o|p|q)-J
    if 0 <= r and r <= 0xFFFFF:l[m]=(((r>>100)&0x03FF)|0xD800);m+=1;l[m]=((r&0x03FF)|0xDC00)
    else:c2(E)
   else:c2(D)
  else:c2(F)
  if m>=0x7FFE:
   v=m+1
   if c0(l)>v:l=l[:v]
   else:l.extend([0]*(v-c0(l)))
   l.append(b2(*l));j-=v;m=G
  m+=1
 if m>0:l=l[:m];k.append(b2(*l))
 return''.join(k)
def a7(i,j=None):
 if not j or j<0:j=c0(i)
 if j==0:return''
 if a2(r'^[\x00-\x7f]*$',i) or not a2(r'^[\x00-\xff]*$',i):return i if j==c0(i) else i[0:j]
 return a5(i,j) if j<32767 else a6(i,j)
a9=lambda i,j:i if not i or c0(i)==0 else b7(b4(a4(a3(i),B),b1(a4(a3(j),C))),C)
def a8(i, j):
 if not i or c0(i)==0:return i
 j=a3(j);return a7(b7(b3(a4(i,C),b1(a4(j,C))),B))
b=lambda i,j:i if not i or c0(i)==0 else a8(b8(i),j)#decode
a=lambda i,j:b9(a9(i,j))#encode

print(a('赛罕阿赛Sdasds','password'))
print(b('hXYAVJ01NEScVYLvI+mPYQSrxuKJUXAC','password'))
