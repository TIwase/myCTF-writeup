#### 作成日: 2021/04/04

# [Crypto] Play Nice - 110 points

## Description:
Not all ancient ciphers were so bad... The flag is not in standard format. ```nc mercury.picoctf.net 40742``` [playfair.py](file/playfair.py)
## Hints:
None.

## Solution:

netcatコマンドでこのサーバに接続すると、以下の出力が返ってくる。  

	$ nc mercury.picoctf.net 40742
	Here is the alphabet: irlgektq8ayfp5zu037nov1m9xbc64shwjd2
	Here is the encrypted message: h5a1sqeusdi38obzy0j5h3ift7s2r2
	What is the plaintext message?

alphabetとencrypted messageが与えられ、plaintext messageが求められる。

本問題はplayfair暗号を模した作りになっており、平文(plaintext message)に対して暗号鍵(alphabet)をかけて、暗号文(encrypted message)が作成される。  
なので、暗号化手順と真逆の処理をして復号を試みる。(playfair暗号の暗号化手順について、詳しくは[wiki](https://en.wikipedia.org/wiki/Playfair_cipher)を参照)  

まずは、暗号文(encrypted message)を2文字ずつ区切っていく。  
```h5-a1-sq-eu-sd-i3-8o-bz-y0-j5-h3-if-t7-s2-r2```  

次に下表の暗号鍵(alphabet)より、```h5```は同じ列に存在しているため、復号すると一つ上の文字```xq```、```a1```は行列の交点となる```yv```へ復号される。  
※2文字が同じ行に存在している時、一つ左の文字へずらして復号される。
(表の一番左の文字が対象だった場合、同じ行の一番右文字が復号先となる)

|   |I  |II |III|IV |V  |VI |
|-- |-- |-- |-- |-- |-- |-- |
|I  | i | r | l | g | e | k |
|II | t | q | 8 | a | y | y |
|III| p | 5 | z | u | 0 | 3 |
|IV | 7 | n | o | v | 1 | m |
|V  | 9 | x | b | c | 6 | 4 |
|VI | s | h | w | j | d | 2 |

この手順を繰り返して復号した平文を、上記のサーバ接続時にて```What is the plaintext message?```で入力するとFLAGが表示される。

