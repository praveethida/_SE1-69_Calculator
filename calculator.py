def add (x,y):
    """ฟังก์ชันสำหรับการบวกเลข"""
    return x + y

def subtract (x,y):
    """ฟังก์ชันสำหรับการลบเลข"""
    return x - y

def multiply (x,y):
    """ฟังก์ชันสำหรับการคูณเลข"""
    return x * y

def divide (x,y):
    """ฟังก์ชันสำหรับการหารเลข"""
    return x / y

# ----- Main Function -----#
print('Simple Calculator by Praveethida')
num1 = float(input('กรุณากรอกตเลขตัวที่ 1 ที่นี่ : '))
num2 = float(input('กรุณากรอกตเลขตัวที่ 2 ที่นี่ : '))

print("-"*25)
print("Addition (+):", add(num1, num2))