#### 作成日: 2021/01/09

# [Crypto] The Numbers - 50 points

## Description:
The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

## Hints:
The flag is in the format PICOCTF{}

## Solution:
URL先のpngファイルを開くと、flagの文字列が数字で表示されている。
数字[1-26]をアルファベット[A-Z]に置換してflagを取得。

# [Crypto] caesar - 100 points

## Description:
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext).

## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solution:
URL先のテキストファイル```ciphertext```を開く

	$ file ciphertext
	ciphertext: ASCII text, with no line terminators
	$
	$ cat ciphertext
	picoCTF{dspttjohuifsvcjdpoabrkttds}

シーザー暗号は各文字に対して数文字シフトするものなので、プログラムを作成してflagを調べてみる。
ここでは、asciiコードを用いて全文字数シフトさせた結果を出力させる。

[CaesarCipher.py](solver/CaesarCipher.py)


下記コマンドでpython実行

	$ python3 CaesarCipher.py dspttjohuifsvcjdpoabrkttds  
	GAP = 0 :  
	dspttjohuifsvcjdpoabrkttds  
	GAP = 1 :  
	crossingtherubiconzaqjsscr  
	GAP = 2 :  
	bqnrrhmfsgdqtahbnmyzpirrbq  
	GAP = 3 :  
	apmqqglerfcpszgamlxyohqqap  
	GAP = 4 :  
	zolppfkdqeboryfzlkwxngppzo  
	GAP = 5 :  
	ynkooejcpdanqxeykjvwmfooyn  
	GAP = 6 :  
	xmjnndiboczmpwdxjiuvlennxm  
	GAP = 7 :  
	wlimmchanbylovcwihtukdmmwl  
	GAP = 8 :  
	vkhllbgzmaxknubvhgstjcllvk  
	GAP = 9 :  
	ujgkkafylzwjmtaugfrsibkkuj  
	GAP = 10 :  
	tifjjzexkyvilsztfeqrhajjti  
	GAP = 11 :  
	sheiiydwjxuhkrysedpqgziish  
	GAP = 12 :  
	rgdhhxcviwtgjqxrdcopfyhhrg  
	GAP = 13 :  
	qfcggwbuhvsfipwqcbnoexggqf  
	GAP = 14 :  
	pebffvatgurehovpbamndwffpe  
	GAP = 15 :  
	odaeeuzsftqdgnuoazlmcveeod  
	GAP = 16 :  
	nczddtyrespcfmtnzyklbuddnc  
	GAP = 17 :  
	mbyccsxqdrobelsmyxjkatccmb  
	GAP = 18 :  
	laxbbrwpcqnadkrlxwijzsbbla  
	GAP = 19 :  
	kzwaaqvobpmzcjqkwvhiyraakz  
	GAP = 20 :  
	jyvzzpunaolybipjvughxqzzjy  
	GAP = 21 :  
	ixuyyotmznkxahoiutfgwpyyix  
	GAP = 22 :  
	hwtxxnslymjwzgnhtsefvoxxhw  
	GAP = 23 :  
	gvswwmrkxlivyfmgsrdeunwwgv  
	GAP = 24 :  
	furvvlqjwkhuxelfrqcdtmvvfu  

実行結果より、GAP:1の出力がflag
