import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometer")
window.config(pady=30)


#Calculation
def miles_to_km_conversion():
    amount = int(input.get())
    kilometer = amount * 1.609344
    label3.config(text=f"{kilometer}")



#Entry

input = tkinter.Entry(width=10)
# input.place(x=150, y=-20)
input.grid(column=1, row=0)

#Label1
label1 = tkinter.Label(text="Miles", font=("Poppins", 20))
label1.grid(column =2, row =0)


#label2
label2 = tkinter.Label(text="is equal to", font=("Poppins", 20))
label2.grid(column =0, row =1)


#label3
label3 = tkinter.Label(text= 0, font=("Poppins", 20))
label3.grid(column =1, row =1)

#label4
label4 = tkinter.Label(text= "Km", font=("Poppins", 20))
label4.grid(column =2, row =1)


#button

button = tkinter.Button(text="Calculate" ,command= miles_to_km_conversion)
button.grid(column =1,row = 2)
window.mainloop()
