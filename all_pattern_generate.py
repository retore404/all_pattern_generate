######################################################################
## スクリプト名：all_pattern_generate.py
## スクリプト内容：コマンドライン引数で渡した文字列に含まれる文字から
## 　　　　　　　　任意の長さnの文字列を生成するときの全パターンをcsvに出力する．
## 引数：並び替え対象文字列，出力文字列の長さ, csv出力先ディレクトリパス
## 戻り値：なし（csvを出力）
######################################################################

######################################################################
## インポート定義
import sys
import math
import itertools
import csv

######################################################################
## スクリプト本体

# 精査
## 引数を受け取り，引数の数が3でないとき異常とみなし実行を終了する
args = sys.argv
if len(args) != 4: # 0番目の引数はパスなので
    print('引数は2つ指定してください．')
    print('引数1：並び替え対象文字列')
    print('引数2：出力する文字列の長さ')
    print('引数3：結果出力ディレクトリパス')
    sys.exit(1)
input_strings = args[1]
target_length = args[2]
directory_path = args[3]

## 対象文字列の長さが2以上ないとき，異常とみなして終了する
if(len(input_strings)) < 2:
    print('並び替え対象文字列は2文字以上必要です．指定された並び替え対象文字列：'+ input_strings)
    sys.exit(1)

## 出力文字列長をintに変換できないとき，異常とみなして終了する
try:
    target_length = int(target_length)
except:
    print('出力する文字列の長さは数字を指定してください．　指定された文字列長：' + target_length)
    sys.exit(1)

# 入力された対象文字列を分解してlistに格納する．
input_strings_list = [s for s in input_strings]
input_strings_list

# 対象文字列から長さtarget_lengthの重複あり順列を導出
result = list(itertools.product(input_strings_list, repeat=target_length))

# 導出された順列をを，タプル内要素を結合してstringify
result = [''.join(t) for t in result]

# csv書き出し用にリストを整形
words = [[w] for w in result]
print(words) 

# csv書き出し
file_path = directory_path + "pattern_" + str(target_length) + "_letters.csv"
with open(file_path, "w") as f:
    writer = csv.writer(f, lineterminator="\n")
    for word in words:
        writer.writerow(word)






