b=ctypes.CDLL("./add.dll")
    lib.addition.argtypes=[ctypes.c_int,ctypes.c_int]
    lib.addition.restype=ctypes.c_int
    result=lib.addition(int(num1.get()),int(num2.get()))
    result_label.config(text=f"Result = {resu