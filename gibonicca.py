# i = 1

# while i <= 10:

#     print(i)

#     i = i + 1

from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

ent_no = Entry(root)

label_series = Label(root, text="Fibonacci Series: ")
label2 = Label(root, text="Fibonacci Sum: ")

def fibonacci():
    num = int(ent_no.get())

    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        label2["text"] = "Fibonacci Sum: " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum

ent_no.pack()

btn = Button(root, text="Show Fibonacci Series", command = fibonacci)

btn.pack()
label_series.pack()
label2.pack()

root.mainloop()