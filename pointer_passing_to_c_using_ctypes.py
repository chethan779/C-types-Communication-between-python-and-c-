import ctypes as ct

lib=ct.CDLL("./pointer_passing.dll")
lib.double_int.argtypes=[ct.POINTER(ct.c_int)]
lib.double_int.restype=None

Intptr=ct.POINTER(ct.c_int)
x=ct.c_int(7)
lib.double_int(ct.byref(x))
print(x.value)


arr=(ct.c_int * 10)(7,4,1,9,2,3,8,5,6,0)
lib.linear_sort.argtypes=[Intptr,ct.c_int]
lib.linear_sort.restype=None


lib.linear_sort(arr,10)

for value in range(10):
    print(arr[value])



rows= int(input("Enter number of rows: "))
cols=int(input("Enter number of column: "))
ArrayType = ct.c_int * (rows * cols)

a = ArrayType()
b = ArrayType()
c = ArrayType()

print("Enter Matrix A:")
for i in range(rows):
    for j in range(cols):
        a[i * cols + j] = int(input(f"A[{i}][{j}]: "))

print("Enter Matrix B:")
for i in range(rows):
    for j in range(cols):
        b[i * cols + j] = int(input(f"B[{i}][{j}]: "))

lib.add_matrix.argtypes = [
    ct.c_int,
    ct.c_int,
    ct.POINTER(ct.c_int),
    ct.POINTER(ct.c_int),
    ct.POINTER(ct.c_int)
]

lib.add_matrix.restype = None

lib.add_matrix(rows, cols, a, b, c)

print("Result:")

for i in range(rows):
    for j in range(cols):
        print(c[i * cols + j], end=" ")
    print()

# c_arr=(ct.c_int * len(c))(*c)
# print(list(c_arr))  --> [2,2,2,2] for identity matrix addition