import re as _____________________
import ctypes as ______________________
O_O='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
def ___(o_o):
    o__o=0x7fffffff
    return(o_o+(o__o+1))%(2*(o__o+1))-o__o-1 if not -o__o-1<=o_o<=o__o else o_o
def ____(o_o,o__o):
    if o_o<0:o_o=______________________.c_uint32(o_o).value
    if o__o<0:return-___(o_o<<abs(o__o))
    return ___(o_o>>o__o)
def ____________(o_o, *o__o):return chr(o_o%0x10000)+''.join([chr(o___o%0x10000) for o___o in o__o])
def _____(o_o):
    o__o=f'{O_O}+/';o___o=o____o=0;o_____o=len(o_o);x_x=o_____o%3;o_____o=o_____o-x_x;x__x=___(int(o_____o/3)<<2)
    if x_x>0:x__x+=4
    x___x=['']*x__x
    while o___o<o_____o:
        e_e=___(ord(o_o[o___o])<<0x10);o___o+=1;e__e=___(ord(o_o[o___o])<<8);o___o+=1;e___e=ord(o_o[o___o]);o___o+=1;e____e=e_e|e__e|e___e;x___x[o____o]=o__o[e____e>>0x12]+o__o[e____e>>0xc&0x3f]+o__o[e____e>>6&0x3f]+o__o[e____e&0x3f];o____o+=1
    if x_x==1:
        e____e=ord(o_o[o___o]);o___o+=1;x___x[o____o]=o__o[e____e>>2]+o__o[___((e____e&0x03)<<4)]+'==';o____o += 1
    elif x_x==2:
        e_e=___(ord(o_o[o___o])<<8);o___o+=1;e__e=ord(o_o[o___o]);o___o+=1;e____e=e_e|e__e;x___x[o____o]=o__o[e____e>>0xa]+o__o[e____e>>4&0x3f]+o__o[___((e____e & 0x0f)<<2)]+'='
    return''.join(x___x)
def ______(o_o):
    o__o=([-1]*0x2b);o__o.extend([0x3e,*([-1]*3),0x3f,*([_ for _ in range(0x34,0x3e)]),*([-1]*7),*([_ for _ in range(0,0x1a)]),*([-1]*6),*([_ for _ in range(0x1a,0x34)]),*([-1]*5)]);o___o=len(o_o)
    if o___o%4!=0:return''
    if _____________________.findall(rf'[^{O_O}\+\/\=]', o_o):return''
    if o_o[-2]=='=':o____o=1
    elif o_o[-1]=='=':o____o=2
    else:o____o=0
    x_x=o___o
    if o____o>0:x_x-=4
    x_x=(x_x>>2)*3+o____o;x__x=['']*x_x;x___x=x____x=0
    while x___x<o___o:
        e_e=o__o[ord(o_o[x___x])];x___x+=1
        if e_e==-1:break
        e__e=o__o[ord(o_o[x___x])];x___x+=1
        if e__e==-1:break
        x__x[x____x]=____________(___(e_e<<2)|((e__e&0x30)>>4));x____x += 1;e___e=o__o[ord(o_o[x___x])];x___x+=1
        if e___e==-1:break
        x__x[x____x]=____________(___((e__e&0x0f)<<4)|((e___e&0x3c)>>2));x____x+=1;e____e=o__o[ord(o_o[x___x])];x___x+=1
        if e____e==-1:break
        x__x[x____x]=____________(___((e___e&0x03)<<6)|e____e);x____x+=1
    return''.join(x__x)
def _______(o_o,o__o):
    o___o=len(o_o);x_x=___(o___o<<2)
    if o__o:
        o____o=o_o[o___o-1];x_x-=4
        if o____o<x_x-3 or o____o>x_x:return None
        x_x = o____o
    x__x = 0
    while x__x < o___o:o_o[x__x]=____________(o_o[x__x]&0xFF,____(o_o[x__x],8)&0xFF,____(o_o[x__x],16)&0xFF,____(o_o[x__x],24)&0xFF,);x__x+=1
    x___x=''.join(o_o)
    if o__o:return x___x[0:x_x]
    return x___x
def ________(o_o,o__o,o___o,o____o,o_____o,o______o):
    return((____(o___o,5)^o__o<<2)+(____(o__o,3)^o___o<<4))^((o_o^o__o)+(o______o[o____o&3^o_____o]^o___o))
def _________(o_o):
    return ___(o_o&0xFFFFFFFF)
def __________(o_o,o__o):
    o___o=len(o_o);o____o=o___o-1;x_x=o_o[o____o];x__x=0;x___x=(int(6+0x34/o___o)|0)
    while x___x>0:
        x__x=_________(x__x+0x9E3779B9);x____x=____(x__x,2)&3;x_____x=0
        while x_____x<o____o:e_e=o_o[x_____x+1];x_x=o_o[x_____x]=_________(o_o[x_____x]+________(x__x,e_e,x_x,x_____x,x____x,o__o));x_____x+=1
        e_e=o_o[0];x_x=o_o[o____o]=_________(o_o[o____o]+________(x__x,e_e,x_x,o____o,x____x,o__o));x___x-=1
    return o_o
def ___________(o_o,o__o):
    o___o=len(o_o);o____o=o___o-1;x_x=o_o[0];x__x=int(6+0x34/o___o);x___x=_________(x__x*0x9E3779B9)
    while x___x!=0:
        x____x=____(x___x,2)&3;e_e=o____o
        while e_e>0:e__e=o_o[e_e - 1];x_x=o_o[e_e]=_________(o_o[e_e]-________(x___x,x_x,e__e,e_e,x____x,o__o));e_e-=1
        e__e=o_o[o____o];x_x=o_o[0]=_________(o_o[0]-________(x___x,x_x,e__e,0,x____x,o__o));x___x=_________(x___x-0x9E3779B9)
    return o_o
def _____________(o_o):
    if len(o_o)<4:o_o.extend([0]*(4-len(o_o)))
    return o_o
def ___________________(o_o,o__o):
    o___o=len(o_o);o____o=o___o>>2
    if o___o&3!=0:o____o+=1
    if o__o:o_____o=[0]*(o____o+1);o_____o[o____o]=o___o
    else:o_____o=[0]*o____o
    for o______o in range(o___o):o_____o[o______o>>2]=o_____o[o______o>>2]|___(ord(o_o[o______o])<<___((o______o&3)<<3))
    return o_____o
def ____________________(o_o):
    if _____________________.findall(r'^[\x00-\x7f]*$', o_o):return o_o
    o__o=[None]*len(o_o);o___o=len(o_o);o____o=o_____o=0
    while o____o<o___o:
        x_x = ord(o_o[o____o])
        if x_x<0x80:o__o[o_____o]=o_o[o____o]
        elif x_x<0x800:o__o[o_____o]=____________(0xC0|(x_x>>6),0x80|(x_x&0x3F))
        elif x_x<0xD800 or x_x>0xDFFF:o__o[o_____o]=____________(0xE0|(x_x>>12),0x80|((x_x>>6)&0x3F),0x80|(x_x&0x3F))
        else:
            if o____o+1<o___o:
                x__x=ord(o_o[o____o+1])
                if x_x<0xDC00 and 0xDC00<=x__x and x__x<=0xDFFF:x___x=(((x_x&0x03FF)<<0xa)|(x__x&0x03FF))+0x010000;o__o[o_____o]=____________(0xF0|((x___x>>18)&0x3F),0x80|((x___x>>12)&0x3F),0x80|((x___x>>6)&0x3F),0x80|(x___x&0x3F));o____o+=1
        o____o+=1;o_____o+=1
    return''.join(o__o)
def __________________(o_o,o__o):
    o___o=[0]*o__o;o____o=o_____o=0;x_x=len(o_o)
    while o____o<o__o and o_____o<x_x:
        x__x=ord(o_o[o_____o]);o_____o+=1;x___x=x__x>>4
        if x___x in(0,1,2,3,4,5,6,7):o___o[o____o]=x__x
        elif x___x in(12,13):
            if o_____o<x_x:o___o[o____o]=___((x__x&0x1F)<<6)|(ord(o_o[o_____o])&0x3F);o_____o+=1
            else:Exception('Unfinished UTF-8 octet sequence')
        elif x___x in[14]:
            if o_____o+1<x_x:
                e_e=___((ord(o_o[o_____o])&0x3F)<<6);o_____o+=1;e__e=ord(o_o[o_____o])&0x3F;o_____o+=1;o___o[o____o]=___((x__x&0x0F)<<12)|e_e|e__e
            else:Exception('Unfinished UTF-8 octet sequence')
        elif x___x in[15]:
            if o_____o+2<x_x:
                e_e=___((ord(o_o[o_____o])&0x3F)<<12);o_____o+=1;e__e=___((ord(o_o[o_____o])&0x3F)<<6);o_____o+=1;e___e=(ord(o_o[o_____o])&0x3F);o_____o+=1;e____e=(___((x__x&0x07)<<18)|e_e|e__e|e___e)-0x10000
                if 0<=e____e and e____e<=0xFFFFF:o___o[o____o]=(((e____e>>10)&0x03FF)|0xD800);o____o+=1;o___o[o____o]=(e____e&0x03FF)|0xDC00
                else:Exception('Character outside valid Unicode')
            else:Exception('Unfinished UTF-8 octet sequence')
        else:Exception('Bad UTF-8 encoding')
        o____o+=1
    if o____o<o__o:o___o=o___o[:o____o]
    return ____________(*o___o)
def _________________(o_o, o__o):
    o___o=[];o____o=[0]*0x8000;o_____o=o______o=0;x_x=len(o_o)
    while o_____o<o__o and o______o<x_x:
        x__x=ord(o_o[o______o]);o______o+=1;x___x=x__x>>4
        if x___x in[0,1,2,3,4,5,6,7]:
            o____o[o_____o] = x__x
        elif x___x in[0xc, 0xd]:
            if o______o < x_x:o____o[o_____o]=___((x__x&0x1F)<<6)|(ord(o_o[o______o])&0x3F);o______o+=1
            else:Exception('Unfinished UTF-8 octet sequence')
        elif x___x in[0xe]:
            if o______o+1<x_x:
                e_e=___((ord(o_o[o______o])&0x3F)<<6);o______o+=1;e__e=ord(o_o[o______o])&0x3F;o______o+=1;o____o[o_____o]=___((x__x&0x0F)<<12)|e_e|e__e
            else:Exception('Unfinished UTF-8 octet sequence')
        elif x___x in[0xf]:
            if o______o+2<x_x:
                e_e=___((ord(o_o[o______o])&0x3F)<<0xc);o______o+=1;e__e=___((ord(o_o[o______o])&0x3F)<<6);o______o+=1;e___e=ord(o_o[o______o])&0x3F;o______o+=1;e____e=(___((x__x&0x07)<<0x12)|e_e|e__e|e___e)-0x10000
                if 0 <= e____e and e____e <= 0xFFFFF:
                    o____o[o_____o]=(((e____e>>100)&0x03FF)|0xD800);o_____o+=1;o____o[o_____o]=((e____e&0x03FF)|0xDC00)
                else:Exception('Character outside valid Unicode')
            else:Exception('Unfinished UTF-8 octet sequence')
        else:Exception('Bad UTF-8 encoding')
        if o_____o>=0x7FFE:
            x____x=o_____o+1
            if len(o____o)>x____x:o____o=o____o[:x____x]
            else:o____o.extend([0]*(x____x-len(o____o)))
            o____o.append(____________(*o____o));o__o-=x____x;o_____o=-1
        o_____o+=1
    if o_____o>0:o____o=o____o[:o_____o];o___o.append(____________(*o____o))
    return''.join(o___o)
def ________________(o_o, o__o=None):
    if not o__o or o__o<0:o__o=len(o_o)
    if o__o==0:return ''
    if _____________________.findall(r'^[\x00-\x7f]*$',o_o) or not _____________________.findall(r'^[\x00-\xff]*$',o_o):return o_o if o__o==len(o_o) else o_o[0:o__o]
    return __________________(o_o,o__o) if o__o<0x7FFF else _________________(o_o,o__o)
def ______________(o_o,o__o):
    if not o_o or len(o_o)==0:return o_o
    o_o=____________________(o_o);o__o=____________________(o__o);return _______(__________(___________________(o_o,True),_____________(___________________(o__o,False))),False)
def _______________(o_o, o__o):
    if not o_o or len(o_o)==0:return o_o
    o__o=____________________(o__o);return ________________(_______(___________(___________________(o_o,False),_____________(___________________(o__o,False))),True))
def _(o_o,o__o):return o_o if not o_o or len(o_o)==0 else _______________(______(o_o),o__o)#decode
def __(o_o,o__o):return _____(______________(o_o,o__o))#encode
