km = float(input("Nhập số km: "))
tongtien = 0
if km <= 0:
    tongtien = 0
elif km <= 1:
    tongtien = 15000
elif km <= 20:
    tongtien = 15000 + 12000 * (km - 1)
else:
    tongtien = 15000 + 12000 * 19 + 10000 * (km - 20)
print(f"Tổng tiền phải trả: {tongtien:,.0f} VND")
