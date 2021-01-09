#### 2021/01/09 作成

# picoCTF 2020 Mini-Competition writeup

## [Web] Web Gauntlet - 200 points

### Description:
Can you beat the filters? Login as admin  
http://jupiter.challenges.picoctf.org:19593/  
http://jupiter.challenges.picoctf.org:19593/filter.php  

### Hints:
- You are not allowed to login with valid credentials.  
- Write down the injections you use in case you lose your progress.  
- For some filters it may be hard to see the characters, always (always) look at the raw hex in the response.  
- sqlite  
- If your cookie keeps getting reset, try using a private browser window  

### Solution:
#### Round 1/5
![sample Image](images/round1.png)
filter.phpに```Round1: or```と記載されており、ORが使えない。  
シングルクォートとハイフンを使用してログインをする。