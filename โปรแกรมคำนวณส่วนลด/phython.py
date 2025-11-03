print("="*30)
print ("Tvเครื่องละ 5000 บาท") 
num_tv = int(input("จำนวนTvที่ต้องการซื้อ:"))
dis_tv = num_tv*5000
print("-"*30)
print("โทรศัพท์เครื่องละ 8000 บาท")
num_phone = int(input("จำนวนโทรศัพท์ที่ต้องการซื้อ:"))
dis_phone = num_phone*8000
print("-"*30)
print("โต๊ะตัวละ 4000 บาท")
num_table = int(input("จำนวนโต๊ะที่ต้องการซื้อ:"))
dis_table = num_table*4000
print("-"*30)
dis_total = dis_tv + dis_phone + dis_table
if dis_total>10000:
    per = 50
else:
    per = 0
dis = dis_total*50/100
net = dis_total-dis
print("Tv =",num_tv,"เครื่อง")
print("ราคารวมของTv =",dis_tv,"บาท")
print("โทรศัพท์ =",num_phone,"เครื่อง")
print("ราคารวมของโทรศัพท์ =",dis_phone,"บาท")
print("โต๊ะ =",num_table,"ตัว")
print("ราคารวมของโต๊ะ =",dis_table,"บาท")
print("ราคารวม =",dis_total,"บาท")
print("ส่วนลด50% =",dis,"บาท")
print("ราคาสุทธิ =",net,"บาท")
print("="*30)

