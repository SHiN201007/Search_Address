import csv

bangoList = []
addressList = []
flag = False

#MARK:----------------------------------------------------------------------------
# 1 検索
def search():
    print("郵便番号一覧\n")
    for i in addressDict:
        print(i)
    bango = input("\n郵便番号を入力してください＞")
    value = addressDict[bango]
    print(value)

#MARK:----------------------------------------------------------------------------
# 2 追加, 更新
def add():
    bangoKey = input("追加, 更新する郵便番号を入力してください＞")
    addressValue = input("追加, 更新する住所を入力してください＞")
    addressDict[bangoKey] = addressValue
    print(addressDict)

#MARK:----------------------------------------------------------------------------
# 3 削除
def remove():
    bangoKey = input("削除する郵便番号を入力してください＞")
    remove = addressDict.pop(bangoKey)
    print(addressDict)
#MARK:----------------------------------------------------------------------------
# 3 終了
def end():
    exit()


with open('bango.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        bangoRow = ''.join(row)
        bangoList.append(bangoRow)

with open('ken.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        addressRow = ''.join(row)
        addressList.append(addressRow)
addressDict = dict(zip(bangoList,addressList))

while flag == False:
    # コマンド
    code = input("search / add / remove / end＞")
    if code == "search":
        search()
    elif code == "add":
        add()
    elif code == "remove":
        remove()
    elif code == "end":
        end()
    else:
        print("error\nコードが違います。")