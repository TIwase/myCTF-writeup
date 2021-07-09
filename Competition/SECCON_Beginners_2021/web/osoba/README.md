#### 作成日: 2021/07/10

# [Web] osoba - 51 points

## Description:
美味しいお蕎麦を食べたいですね。フラグはサーバの /flag にあります！  
https://osoba.quals.beginners.seccon.jp/  
[osoba.tar.gz](osoba.tar.gz) 566021e832a474559dfb67f5d3cd0bed14147f9b
## Hints:
None.

## Solution:
ディレクトリトラバーサルを使った問題。
圧縮ファイルのディレクトリ構造を見ると、htmlのトップページの上の階層にフラグファイルがあることが分かる。  
またページ遷移すると、?page=クエリを使っていることが分かる。  
下記にアクセスするとフラグを取得できる。  
```$ curl https://osoba.quals.beginners.seccon.jp/?page=../../flag```  
