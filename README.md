# xxtea
xxtea纯Python实现

> 参考:https://github.com/xxtea/xxtea-js  
> 虽然上面链接里面有python版本,但是通过调用C实现的  
> 照抄js版本改成python代码实现  

# 使用方法
```Python
from xxtea import encryptToBase64, decryptFromBase64

enString = 'Hello World!!!'
Key = 'password'
a = encryptToBase64(enString, Key)
print(a)  # OI1WQdt0sA2ZtgDPe6qMV1F+YYI=
b = decryptFromBase64(a, Key)
print(b)  # Hello World!!!
print(enString == b)  # True
```
