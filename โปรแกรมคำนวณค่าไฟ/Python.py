print("="*30)
mn_this = int(input("เลขมิเตอร์เดือนปัจจุบัน:"))
mn_before = int(input("เลขมิเตอร์เดือนก่อนหน้า:"))
num_unit = mn_this - mn_before
if num_unit < 80:
    dis_unit = 4.50
elif num_unit >= 80 and num_unit <= 500:
    dis_unit = 6.50
elif num_unit >= 501 and num_unit <= 1000:
    dis_unit = 8.00
else:
    dis_unit = 10.00
print("-"*30)
FT = num_unit * 3.61
re_mn = 150
dis_total = num_unit * dis_unit + FT + re_mn
tax = dis_total*7/100
total = dis_total + tax
print ("เลขมิเตอร์ปัจจุบัน =",mn_this)
print ("เลขมิเตอร์เดือนก่อนหน้า =",mn_before)
print ("จำนวนหน่วยที่ใช้ =",num_unit,"หน่วย")
print ("ราคาหน่วยละ =",dis_unit,"บาท")
print ("ค่า FT =",FT,"บาท")
print ("ค่าบำรุงมิเตอร์ =",re_mn,"บาท")
print ("ค่าไฟฟ้า =",dis_total,"บาท")
print ("ค่าภาษี =",tax,"บาท")
print ("ค่าไฟฟ้าเดือนนี้ =",total,"บาท")
print("="*30)




