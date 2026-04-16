
n = int(input("Nhập số nguyên dương n: "))
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print(f"Tổng các số lẻ từ 1 đến {n} là: {sum_odd}")
print(f"Tổng các số chẵn từ 1 đến {n} là: {sum_even}")
