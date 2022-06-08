list1 = []
input_to_list1 = input("Nhap cac so nguyen: ")

while input_to_list1 != "end":
    list1.append(int(input_to_list1))
    input_to_list1 = input("Nhap cac so nguyen: ")

list1.sort()
print("So lon nhat trong danh sach la: ", list1[-1])
print("So lon thu hai trong danh sach la: ", list1[-2])