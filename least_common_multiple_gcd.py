from math import gcd
#math modülünden gcd içeri aktarılıyor.
def least_common_multiple(num1, num2):
    return num1 * num2 / gcd(num1,num2) #gcd iki sayının ebobunu veriyor.
# iki sayının ebobu ile ekokunun çarpımı, iki sayının çarpımına eşittir formülüne göre sonuç alınıyor.
num1, num2 = map(int, input("Enter two numbers: (numbers must be separated by space):").split())
print(least_common_multiple(num1, num2))