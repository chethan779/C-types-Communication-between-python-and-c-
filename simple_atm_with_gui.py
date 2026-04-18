import tkinter as tk
import ctypes
global lib
global deposit_amt
root=tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("800x900")

tk.Label(root,text="Enter ur inital balance here:").pack()
initial_bal=tk.Entry(root)
initial_bal.pack()
    
def open_deposit_window():
    deposit_win=tk.Toplevel(root)
    deposit_win.title("Deposit section")
    deposit_win.geometry("800x900")
    def deposit():
        lib=ctypes.CDLL("./atm.dll")
        lib.deposit.argtypes=[ctypes.c_float,ctypes.c_float]
        lib.deposit.restype=ctypes.c_float
        result=lib.deposit(float(initial_bal.get()),float(deposit_amt.get()))
        final_amt.config(text=f"Final Balance = {result}")
    deposit_amt=tk.Entry(deposit_win)
    deposit_amt.pack()
    final_amt=tk.Label(deposit_win,text="FINAL BALANCE")
    final_amt.pack()
    deposit_final_button=tk.Button(deposit_win,text="Deposit",command=deposit)
    deposit_final_button.pack()


deposit_buton=tk.Button(root,text="Deposit",command=open_deposit_window)
deposit_buton.pack()

root.mainloop()