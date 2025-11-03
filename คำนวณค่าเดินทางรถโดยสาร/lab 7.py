print ("="*30)
dis_travel = int(input("ระยะทางที่เดินทาง:"))
if dis_travel < 100:
    fare = 2.50
    print("กิโลเมตรละ 2.50 บาท")
elif dis_travel >= 100 and dis_travel <= 200:
    fare = 4.00
    print("กิโลเมตรละ 4.00 บาท")
elif dis_travel >= 201 and dis_travel <= 400:
    fare = 5.50
    print("กิโลเมตรละ 5.50 บาท")
else:
    print("กิโลเมตรละ 6.00 บาท")
travel_car = int(input("ระบุรถในการเดินทาง:")
if travel_car == 1
    fee = 100
    print("ค่าธรรมเนียมการเดินทาง 100 บาท")
elif travel_car == 2
    fee = 50
    print("ค่าธรรมเนียมการเดินทาง 50 บาท")
net = dis_travel*fare+fee
tax = net*7/100
total = net+tax
print ("-"*30)
print ("ระยะทางที่เดินทาง =",dis_travel,"กิโลเมตร")
print ("กิโลเมตรละ =",fare,"บาท")
print ("เดินทางด้วยรถ =",travel_car)
print ("ค่าธรรมเนียมเดินทาง =",fee,"บาท")
print ("ราคาสุทธิ =",net,"บาท")
print ("ภาษี 7% =",tax,"บาท")
print ("ราคารวม =",total,"บาท")
print ("="*30)

    
