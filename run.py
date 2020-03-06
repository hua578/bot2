import os,sys,time,platform,json,codecs

def CleanMSG():
    if 'Windows' in platform.platform():
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def loadFile():
    if 'Windows' in platform.platform():
        path = '\\'
    else:
        path = '/'
    return str(path)
print("本程式為群組防翻機器2.0\n感謝您的使用^^\n")
while 1:
    way = str(input('[※]請選擇欲執行之系統 :\n 1.執行無限連機(請記得先存入您的帳號token)\n 2.管理您的機器帳號\n您的選擇為 :'))
    if way == '1':
        CleanMSG()
        tkn = json.load(codecs.open("bot"+loadFile()+"tokens.json","r","utf-8"))
        try:
            num = int(input('請輸入您欲登入的機器數(至少大於2)\n登入隻數 :'))
            if num > 2:
                tkn['botnum'] = num
                json.dump(tkn, codecs.open("bot"+loadFile()+'tokens.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
                break
            else:
                print('機器數請至少大於2')
        except:
            pass
    elif way == '2':
        CleanMSG()
        os.system('cd bot&&python st.py')
        CleanMSG()
    else:
        sys.exit()
CleanMSG()
os.system('cd bot&&python kicker.py')
