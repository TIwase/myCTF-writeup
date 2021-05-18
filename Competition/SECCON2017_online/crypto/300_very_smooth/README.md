#### 作成日: 2021/05/11

# [Crypto] very smooth - 300 points

## Description:

Very smooth  
Decrypt index.html from PCAP.  
Please, submit the flag in the format: "SECCON{" + Answer + "}"  
\* Answer is written in index.html  
[very_smooth_36c055008b945516b9c17e2ecce1c582c184b57c2945bbffba20372a8f9a3449.zip](https://github.com/SECCON/SECCON2017_online_CTF/blob/master/crypto/300_very_smooth/files/very_smooth_36c055008b945516b9c17e2ecce1c582c184b57c2945bbffba20372a8f9a3449.zip)

## Hints:
(No Hint)

## Solution:

wiresharkでパケットファイル開くと、通信内容はTLS通信で保護されているため、index.htmlの中身を見ることができない。  
下記画像の30行目「Server Hello, Certificate, Server Hello Done」にて、サーバ認証にRSA(sha256WithRSAEncryption)が使用されている。  
また、60行目「Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message」の通信内容の暗号化にも同じRSA(RSA Encrypted PreMaster Secret)が使用されていることから、通信内容の暗号化に使用する共通鍵とサーバ認証で使用する秘密鍵が同じであると仮定する。

![s.pcap_30.png](image/s.pcap_30.png)  

![s.pcap_60.png](image/s.pcap_60.png)  

よって、通信内容の復号化をするために下記手順を試みる。  
1. サーバ証明書に付属される公開鍵(n,e)を抽出する
2. nを素因数分解し、p, qを得ることで秘密鍵を生成する
3. 生成した秘密鍵を用いて通信内容を復号化する


### 手順1
wiresharkで開いた```s.pcap```の30行目「Server Hello, Certificate, Server Hello Done」にある、  
[Transport Layer Security] > [TLSv1 Record Layer: Handshake Protocol: Certificate] > [Handshake Protocol: Certificate] > [Certificates] > [Certificates: 3082...]で右クリックし、[Export Packet Bytes]を選択したら、```<任意のファイル名>.der```で保存する。(※本説明ではserver.derとして保存する)  
次に、保存した証明書がテキスト表示できることを下記コマンドで確認する。  
```
$ openssl x509 -inform der -in server.der -text

Certificate:
     Data:
         Version: 1 (0x0)
         Serial Number:
             a1:8b:63:0c:7b:30:99:df
         Signature Algorithm: sha256WithRSAEncryption
         Issuer: C = JP, ST = Kawasaki, O = SRL
         Validity
             Not Before: Oct  8 02:47:17 2017 GMT
             Not After : Oct  8 02:47:17 2018 GMT
         Subject: C = JP, ST = Kawasaki, O = SRL
         Subject Public Key Info:
             Public Key Algorithm: rsaEncryption
                 RSA Public-Key: (1024 bit)
                 Modulus:
                     00:d5:46:aa:82:5c:f6:1d:e9:77:65:f4:64:fb:fe:
                     48:89:ad:8b:f2:f2:5a:21:75:d0:2c:8b:6f:2a:c0:
                     c5:c2:7b:67:03:5a:ec:19:2b:37:41:dd:1f:4d:12:
                     75:31:b0:7a:b0:12:eb:86:24:1c:09:c0:81:49:9e:
                     69:ef:5a:ea:c7:8d:c6:23:0d:47:5d:a7:ee:17:f0:
                     2f:63:b6:f0:9a:2d:38:1d:f9:b6:92:8e:8d:9e:07:
                     47:fe:ba:24:8b:ff:df:f8:9c:df:af:47:71:65:89:
                     19:b6:98:1c:9e:14:28:e9:a5:34:25:ca:2a:31:0a:
                     a6:d7:60:83:31:18:ee:0d:71
                 Exponent: 65537 (0x10001)
     Signature Algorithm: sha256WithRSAEncryption
          78:92:11:fb:6c:e1:7a:f7:2a:33:b8:8b:08:a7:f7:5b:de:cf:
          62:0b:a0:ed:be:d0:69:88:38:93:94:9d:05:41:73:bd:7e:b3:
          32:ec:8e:10:bc:3a:62:b0:56:c7:c1:3f:60:66:a7:be:b9:46:
          f7:46:22:6a:f3:5a:25:d5:66:94:57:0e:fc:b5:16:33:05:1c:
          6f:f5:85:74:57:a4:a0:c6:ce:4f:fd:64:53:94:a9:83:b8:96:
          bf:5b:a7:ee:8b:1e:48:a7:d2:43:06:0e:4f:5a:86:62:69:05:
          e2:c0:bd:4e:89:c9:af:04:4a:77:a2:34:86:6a:b8:d2:3b:32:
          b7:39
 -----BEGIN CERTIFICATE-----
 MIIB0zCCATwCCQChi2MMezCZ3zANBgkqhkiG9w0BAQsFADAuMQswCQYDVQQGEwJK
 UDERMA8GA1UECAwIS2F3YXNha2kxDDAKBgNVBAoMA1NSTDAeFw0xNzEwMDgwMjQ3
 MTdaFw0xODEwMDgwMjQ3MTdaMC4xCzAJBgNVBAYTAkpQMREwDwYDVQQIDAhLYXdh
 c2FraTEMMAoGA1UECgwDU1JMMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDV
 RqqCXPYd6Xdl9GT7/kiJrYvy8lohddAsi28qwMXCe2cDWuwZKzdB3R9NEnUxsHqw
 EuuGJBwJwIFJnmnvWurHjcYjDUddp+4X8C9jtvCaLTgd+baSjo2eB0f+uiSL/9/4
 nN+vR3FliRm2mByeFCjppTQlyioxCqbXYIMxGO4NcQIDAQABMA0GCSqGSIb3DQEB
 CwUAA4GBAHiSEfts4Xr3KjO4iwin91vez2ILoO2+0GmIOJOUnQVBc71+szLsjhC8
 OmKwVsfBP2Bmp765RvdGImrzWiXVZpRXDvy1FjMFHG/1hXRXpKDGzk/9ZFOUqYO4
 lr9bp+6LHkin0kMGDk9ahmJpBeLAvU6Jya8ESneiNIZquNI7Mrc5
 -----END CERTIFICATE-----
```

公開鍵nのみ抽出するため、下記コマンドを実行する。
```
$ openssl x509 -in server.der -inform der -modulus -noout > modulus
$ cat modulus
Modulus=D546AA825CF61DE97765F464FBFE4889AD8BF2F25A2175D02C8B6F2AC0C5C27B67035AEC192B3741DD1F4D127531B07AB012EB86241C09C081499E69EF5AEAC78DC6230D475DA7EE17F02F63B6F09A2D381DF9B6928E8D9E0747FEBA248BFFDFF89CDFAF4771658919B6981C9E1428E9A53425CA2A310AA6D760833118EE0D71
```

### 手順2
Pollardのp-1法でnをp,qに素因数分解できるかどうか、下記プログラム[(p-1.py)](solver/p-1.py)を実行する。

``` python p-1.py
# -*- coding: utf-8 -*-
import os
from math import gcd

cwd = os.getcwd()
modulus = open(cwd + '/modulus','r').read().rsplit('Modulus=')[1]

n = int(modulus, 16)
seed = 2  # seedは通常2か3, うまく分解できなかったときに動かす
B = 100000 # B-smoothと仮定する 通常100000まで

a = seed
G = 1
cnt = 0
M = 1
while(G<=1): 
    M = M + 1
    # print("M: ", M)
    if M >= B:
        break
    if M % B == 0:
        print("M=" + str(M))
    # print("a = a ^ M mod n = ", a, "^", M, " mod ", n)
    a = pow(a, M, n)
    # print("= ", a)
    G = gcd(a-1, n)
    # print("G = gcd( a-1, n ) = ", "gcd(" , a-1, ", ", n, ") = ", G)
if G > 1 and G < n:
    print("factor is " + str(G) + ", M = " + str(M))
else:
    print("try new seed")

print("p: " + str(G))
print("q: " + str(n//G))
```

実行結果

```
$ python3 p-1.py
factor is 11807485231629132025602991324007150366908229752508016230400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001, M = 400
p: 11807485231629132025602991324007150366908229752508016230400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
q: 12684117323636134264468162714319298445454220244413621344524758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897
```

以上より、nは素数p,qに素因数分解することが可能である。  
上記のプログラム[(p-1.py)](solver/p-1.py)に対し、秘密鍵を生成するコードを付け加えた下記[(solve.py)](solver/solve.py)を実行する。  
※pythonライブラリのpycryptodomeを使用しています。インストールは```$ pip install pycryptodome```を実行  

```python 
# -*- coding: utf-8 -*-
import os
from math import gcd
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

cwd = os.getcwd()
modulus = open(cwd + '/modulus','r').read().rsplit('Modulus=')[1]

n = int(modulus, 16)
e = 65537

########## p-1法 ##########
seed = 2  # seedは通常2か3, うまく分解できなかったときに動かす
B = 100000 # B-smoothと仮定する 通常100000まで

a = seed
G = 1
cnt = 0
M = 1
while(G<=1): 
    M = M + 1
    # print("M: ", M)
    if M >= B:
        break
    if M % B == 0:
        print("M=" + str(M))
    # print("a = a ^ M mod n = ", a, "^", M, " mod ", n)
    a = pow(a, M, n)
    # print("= ", a)
    G = gcd(a-1, n)
    # print("G = gcd( a-1, n ) = ", "gcd(" , a-1, ", ", n, ") = ", G)
if G > 1 and G < n:
    # print("factor is " + str(G) + ", M = " + str(M))
else:
    print("try new seed")

# print("p: " + str(G))
# print("q: " + str(n//G))

########## 秘密鍵生成 ##########
p = G
q = n//G
d = inverse(e, (p-1)*(q-1))
key = RSA.construct(map(int, (n, e, d)))
open("prikey", "bw").write(key.exportKey())
```
実行結果

```
$ python solve.py
$ ls -l
drwxrwxrwx 1 root root  4096 May 11 15:51 ./
drwxrwxrwx 1 root root  4096 May 11 17:41 ../
-rwxrwxrwx 1 root root   471 Apr 28 19:06 server.der*
-rwxrwxrwx 1 root root   265 May  2 16:37 modulus*
-rwxrwxrwx 1 root root   729 May 11 15:51 p-1.py*
-rwxrwxrwx 1 root root   886 May 10 00:05 prikey*
-rwxrwxrwx 1 root root  1190 May 10 00:17 solve.py

$ cat prikey
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDVRqqCXPYd6Xdl9GT7/kiJrYvy8lohddAsi28qwMXCe2cDWuwZ
KzdB3R9NEnUxsHqwEuuGJBwJwIFJnmnvWurHjcYjDUddp+4X8C9jtvCaLTgd+baS
jo2eB0f+uiSL/9/4nN+vR3FliRm2mByeFCjppTQlyioxCqbXYIMxGO4NcQIDAQAB
AoGAPQ26uBD2n79636Pj2MOFbmxQ+N5p8NQyIN5Vl46RzkfXSH2Zwua9LcyoLj8P
b4cOyCLSa5cgs6X5HOMNfmivdqUALjAm67P5h8aSDlpViYVRR4drg+LcWgfYZyVj
pjGFX2d3ebo7rpC//wAA//8AAP//AAD//wAA//8AAP//AAECQQDhcckcnndfBoAt
g8vyFkOhN7V2pYLh/uW74VZrpcUyQAcX36ohIiKcRAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAABAkEA8i6si1r5GmXwNUQbk9ciJpsbgHkyvMdO/ahcHSuPNbeefWo4E/b3
GxW2mByeFCjppTQlyioxCqbXYIMxGO4NcQJBAIMVQBSN52avRvQv//OhEm25EKAO
GI4DQdz+Zttspb5UEEvHVwqw6GLn/wAA//8AAP//AAD//wAA//8AAP//AAECQQCL
pbo8yQJm5Gz0agd04lKA7GOZW0mUbWDxB0nGUD3N/clYDA22BWxLo+OcJrRIb6b6
ae14e4e32qjKsBt5gpshAkBes+o6cqWQ+cjzIajq0+Buo0xj58wJk6HlmhlfXHqX
iraaWHqSC6BFRNaEnOokajrgRxHAliX1/ONrPe+djahQ
-----END RSA PRIVATE KEY-----
```
秘密鍵```prikey```が生成されていることを確認。

### 手順3
wiresharkを起動し、[Edit] > [Preferences] > [Protocols] > [TLS] > [RSA keys list]を選択し、先ほど生成した秘密鍵```prikey```を入力する。  
暗号化されていた通信内容が復号化され、HTTP通信内容が見えるようになる。
下記画像のindex.htmlの中身と、問題文に記述されている```Please, submit the flag in the format: "SECCON{" + Answer + "}"```より、  
FLAGは```SECCON{One of these primes is very smooth.}```
  
![(s.pcap_decrypted.png)](image/s.pcap_decrypted.png)