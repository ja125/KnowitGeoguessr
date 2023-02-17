import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

# Prompt user to select an image
file_path = filedialog.askopenfilename(title="Select Image")

# Prompt user to input x and y coordinates
x_coord = input("Enter x coordinate: ")
y_coord = input("Enter y coordinate: ")

    # Write coordinates to a text file with the same name as the image
temp = file_path.split("/")

with open("coordinates" + ".txt", "a") as f:
    f.write(str(temp[-1])+"\t")
    f.write(str(x_coord) + "\t")
    f.write(str(y_coord) + "\n")
    f.close()
                
                