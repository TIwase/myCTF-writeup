#### 作成日: 2021/01/31

# [Forensics] WhitePages - 250 points

## Description:
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

## Hints:
(None)

## Solution:

リンク先のテキストファイルwhitepages.txtを開くと、半角スペースと全角スペースが混在している。  
これらを0と1に置き換えてbinary -> ascii 変換を行うとflagが表示される。  

![whitepages.png](image/whitepages.png)