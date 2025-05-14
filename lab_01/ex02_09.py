def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True 

so = int(input("Nhập một số để kiểm tra có phải là số nguyên tố không: "))
if kiem_tra_so_nguyen_to(so):
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
