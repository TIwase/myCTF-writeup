#### 作成日: 2021/07/10

# [Misc] git-leak - 58 points

## Description:
後輩が誤って機密情報をコミットしてしまったらしいです。ひとまずコミットを上書きして消したからこれで大丈夫ですよね？  
[git-leak.zip](git-leak.zip) df0dc798437439dac5195f2b56adb35ce0d93b61
## Hints:
None.

## Solution:
$ git reflog を実行すると、masterブランチにコミットした```めもを追加```がrebaseされていることが分かる。  
なので、```git checkout```コマンドでrebase前のコミット番号を選択すると、削除されていたフラグが復元されている。  
