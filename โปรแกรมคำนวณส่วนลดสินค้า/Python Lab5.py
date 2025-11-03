print("="*30)
number = int(input("จำนวนสินค้า:"))
product = 1000
total = number*product
if total < 3000:
    per = 10
    print("ลด 10%")
elif total >= 3000 and total <= 8000:
    per = 20
    print("ลด 20%")
elif total >= 8001 and total<=15000:
    per = 30
    print("ลด 30%")
else:
    per = 40
    print("ลด 40%")
print("-"*30)
dis = total*per/100
net = total-dis
print("จำนวนสินค้า =",number)
print("ราคาสินค้า =",product)
print("ราคารวม =",total)
print("ส่วนลด =",dis)
print("ราคาสุทธิ =",net)
print("="*30)
