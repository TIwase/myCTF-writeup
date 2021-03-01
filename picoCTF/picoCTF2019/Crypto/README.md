#### �쐬��: 2021/01/09

# [Crypto] The Numbers - 50 points

## Description:
The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

## Hints:
The flag is in the format PICOCTF{}

## Solution:
URL���png�t�@�C�����J���ƁAflag�̕����񂪐����ŕ\������Ă���B
����[1-26]���A���t�@�x�b�g[A-Z]�ɒu������flag���擾�B

# [Crypto] caesar - 100 points

## Description:
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext).

## Hints:
caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

## Solution:
URL��̃e�L�X�g�t�@�C��```ciphertext```���J��

	$ file ciphertext
	ciphertext: ASCII text, with no line terminators
	$
	$ cat ciphertext
	picoCTF{dspttjohuifsvcjdpoabrkttds}

�V�[�U�[�Í��͊e�����ɑ΂��Đ������V�t�g������̂Ȃ̂ŁA�v���O�������쐬����flag�𒲂ׂĂ݂�B
�����ł́Aascii�R�[�h��p���đS�������V�t�g���������ʂ��o�͂�����B

[CaesarCipher.py](solver/CaesarCipher.py)


���L�R�}���h��python���s

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

���s���ʂ��AGAP:1�̏o�͂�flag
