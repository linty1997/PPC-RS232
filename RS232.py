import serial
import re
import binascii
import numpy as np
import time

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM5'
pattern = re.compile('.{2}')

ser.open()

print("""
    娃娃機韌體測試
""")
print(hex(0x02^0x01^0xaa))
#機台查詢測試
print("機台參數查詢測試")
print("\n傳送 : BB 73 01 05 00 00 00 00 00 00 00 00 00 00 00 AE - 參數回報 1投/1局?元")
ser.write(b"\xbb\x73\x01\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xae")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))

print("傳送 : BB 73 01 01 00 00 00 00 00 00 00 00 00 15 00 BF - 狀態查詢")
ser.write(b"\xbb\x73\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x15\x00\xbf")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
print("傳送 : BB 73 02 01 00 00 00 00 00 00 00 00 00 00 00 a9 - 遠端帳目 (5,6)(7,8)(9,10)(11,12)")
ser.write(b"\xbb\x73\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (悠遊卡支付次數)(悠遊卡贈局次數)(投幣次數)(禮品出獎數)")
print("傳送 : BB 73 02 02 00 00 00 00 00 00 00 00 00 18 00 B2 - 投幣帳目 (5,6)(7,8)(9,10)(11,12)")
ser.write(b"\xbb\x73\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\xb2")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (中獎率銀行)(總遊戲次數)(次數)(禮品出獎數)")
input("\n確認無誤後按下任意鍵繼續")

print("\n娃娃機台設定查詢")
print("\n傳送 : BB 73 03 01 00 00 00 00 00 00 00 00 00 01 00 A9 - 基本設定A (5)(6,7)(8,9)(10)(11)(12)")
ser.write(b"\xbb\x73\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (遊戲時間)(禮品售價)(目前累加金額)(累加保留時間)(音樂時間)(空中取物)")
print("傳送 : BB 73 03 01 01 00 00 00 00 00 00 00 00 02 00 AB - 基本設定B (5)(6)(7,8)(9)(10)(11)")
ser.write(b"\xbb\x73\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xab")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (下爪延遲)(上停延遲)(下爪&夾亂數)(下爪長度時間)(上停上拉時間)(上拉延遲)")
print("傳送 : BB 73 03 01 02 00 00 00 00 00 00 00 00 03 00 A9 - 基本設定C (5)(6)(7)")
ser.write(b"\xbb\x73\x03\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (促銷功能開關)(促銷幾局開始)(促銷強爪次數)")

print("\n傳送 : BB 73 03 01 03 00 00 00 00 00 00 00 00 04 00 AF - 爪力電壓 (5)(6)(7)(8)(9)")
ser.write(b"\xbb\x73\x03\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\xaf")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (強電壓)(中電壓)(弱電壓)(中壓頂點距離)(保夾強電壓)")
print("傳送 : BB 73 03 01 04 00 00 00 00 00 00 00 00 05 00 A9 - 馬達速度 (5)(6)(7)(8)(9)(10)(11)")
ser.write(b"\xbb\x73\x03\x01\x04\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (往前速度)(往後速度)(往左速度)(往右速度)(往下速度)(往上速度)(轉速)")

#螢幕顯示測試
print("\n螢幕顯示測試 - 更新中")
print("\n傳送 : BB 73 05 01 04 00 00 00 00 00 00 00 11 22 00 99")
ser.write(b"\xbb\x73\x05\x01\x04\x00\x00\x00\x00\x00\x00\x00\x11\x22\x00\x99")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 網路異常")
print("\n傳送 : BB 73 05 01 03 00 00 00 00 00 00 00 00 00 00 ad")
ser.write(b"\xbb\x73\x05\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xad")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 支付故障 77")
print("\n傳送 : BB 73 05 01 02 4D 00 00 00 00 00 00 00 00 00 ad")
ser.write(b"\xbb\x73\x05\x01\x02\x4d\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 服務中")
print("\n傳送 : BB 73 05 01 01 00 00 00 00 00 00 00 11 22 00 9C")
ser.write(b"\xbb\x73\x05\x01\x01\x00\x00\x00\x00\x00\x00\x00\x11\x22\x00\x9c")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 再刷X局送Y局")
print("\n傳送 : BB 73 05 03 01 01 02 03 00 00 00 00 00 00 00 AD - (7)(8)")
ser.write(b"\xbb\x73\x05\x03\x01\x01\x02\x03\x00\x00\x00\x00\x00\x00\x00\xad")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 再刷(7)局送(8)局")
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 再玩X局送Y局")
print("\n傳送 : BB 73 05 03 01 02 03 05 00 00 00 00 00 00 00 A9 - (7)(8)")
ser.write(b"\xbb\x73\x05\x03\x01\x02\x03\x05\x00\x00\x00\x00\x00\x00\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 再玩(7)局送(8)局")
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 免費遊戲第X局")
print("\n傳送 : BB 73 05 03 01 03 04 00 00 00 00 00 00 00 00 AA - (7)")
ser.write(b"\xbb\x73\x05\x03\x01\x03\x04\x00\x00\x00\x00\x00\x00\x00\x00\xaa")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 免費遊戲第(7)局")
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 剩X局刷卡享Y元")
print("\n傳送 : BB 73 05 03 01 04 02 09 00 00 00 00 00 00 00 A2 - (7)(8)")
ser.write(b"\xbb\x73\x05\x03\x01\x04\x02\x09\x00\x00\x00\x00\x00\x00\x00\xa2")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 剩(7)局刷卡享(8)元")
input("\n確認無誤後按下任意鍵繼續")

print("\n螢幕顯示測試 - 關閉優惠訊息")
print("\n傳送 : BB 73 05 03 00 04 02 09 00 00 00 00 00 00 00 A3 - (5)")
ser.write(b"\xbb\x73\x05\x03\x00\x04\x02\x09\x00\x00\x00\x00\x00\x00\x00\xa3")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - (5)為0即關閉")
input("\n確認無誤後按下任意鍵繼續")

#功能測試
print("\n功能測試 - 關閉刷卡功能")
print("\n傳送 : 46 4C 49 04 00 00 00 00 00 00 00 00 00 00 00 E7")
ser.write(b"\x46\x4c\x49\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe7")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
input("\n按下黃鈕 確認無法刷卡後按下任意鍵繼續")

print("\n功能測試測試 - 開啟刷卡功能")
print("\n傳送 : 46 4C 49 03 00 00 00 00 00 00 00 00 00 00 00 E0")
ser.write(b"\x46\x4c\x49\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
print("\n按下黃鈕 如正常 將進入倒數測試\n")

while True:

    data = ser.read(16).hex()

    if "2d8a810300000a01" in data :
        print("接收 : " + ' '.join(pattern.findall(data.upper())) + " - 按下黃鈕")

    if "2d8a810101040000" in data :
        print("接收 : " + ' '.join(pattern.findall(data.upper())) + " - 等待刷卡")
        print("\n傳送 : BB 73 01 31 0A 00 00 00 00 00 00 00 00 00 00 90 - 開始倒數 10")
        ser.write(b"\xbb\x73\x01\x31\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90")
        print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
        time.sleep(1)

        for counter in range(9,0, -1) :

            command = b"\xbb\x73\x01\x31\x09\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90"
            check = int(hex(0x01^0x31^0x0+counter^0xaa), 16)
            command = command[:4] + bytes([counter]) +command[5:]
            command = command[:15] + bytes([int(check)]) +command[16:]
            print(f"傳送 : BB 73 01 31 0{counter} 00 00 00 00 00 00 00 00 00 00 90 - 開始倒數 {counter}")
            ser.write(command)
            print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))
            time.sleep(1)

        print("\n傳送 : BB 73 01 31 FF 00 00 00 00 00 00 00 00 84 00 E1 - 刷卡失敗/超時")
        ser.write(b"\xbb\x73\x01\x31\xff\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xe1")
        print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))

        break

#遊戲啟動測試
print("\n進入遊戲遊玩測試 將啟動遊戲,請將局數遊玩完畢")
print("\n傳送 : BB 73 01 02 01 01 00 00 00 00 00 00 00 07 00 AE - 啟動遊戲")
ser.write(b"\xbb\x73\x01\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x07\x00\xae")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))

print("\n接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 遊戲開始-尚未動搖桿")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 遊戲開始-動搖桿")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 按取物鈕")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 收爪")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 回洞口中")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 遊戲結束")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())) + " - 回到待機狀態")

#遠端帳目清除
print("\n遠端帳目清除測試")
print("\n傳送 : BB 73 02 01 00 01 00 01 00 01 00 01 00 00 00 A9")
ser.write(b"\xbb\x73\x02\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\xa9")
print("接收 : " + ' '.join(pattern.findall(ser.read(16).hex().upper())))


ser.close()

print("\n - 結束 -")