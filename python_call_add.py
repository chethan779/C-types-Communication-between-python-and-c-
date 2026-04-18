import ctypes

lib=ctypes.CDLL("./add.dll")
lib.addition.argtypes=[ctypes.c_int,ctypes.c_int]
lib.addition.restype=ctypes.c_int

result=lib.addition(19090,45678)
print(result)