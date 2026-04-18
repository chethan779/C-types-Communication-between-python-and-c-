import tkinter as tk
import ctypes

root=tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

num1=tk.Entry(root)
num1.pack()

num2=tk.Entry(root)
num2.pack()

result_label = tk.Label(root, text="Result")
result_label.pack()

def add():
    lib=ctypes.CDLL("./add.dll")
    lib.addition.argtypes=[ctypes.c_int,ctypes.c_int]
    lib.addition.restype=ctypes.c_int
    result=lib.addition(int(num1.get()),int(num2.get()))
    result_label.config(text=f"Result = {result}")


add_button=tk.Button(root,text="Add",command=add)
add_button.pack()

root.mainloop()