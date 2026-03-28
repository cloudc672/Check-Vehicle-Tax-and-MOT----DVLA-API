import customtkinter as ctk
import validator as v
from datetime import datetime

#helper function
def get_date_color(date_string):
    try:
        expiry = datetime.strptime(date_string, "%Y-%m-%d")
        if expiry < datetime.now():
            return "red"
        else:
            return "green"
    except:
        return "white" 

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

root = ctk.CTk()

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))

font_size_error = max(20, int(height * 0.02))
font_size_large = max(42, int(height * 0.03))
font_size_medium = max(36, int(height * 0.02))
font_size_small = max(22, int(height * 0.02))
padding_large = max(1, int(height * 0.03))
padding_medium = max(2, int(height * 0.02))
padding_small = max(3, int(height * 0.02))

frame = ctk.CTkFrame(master=root)
frame.pack_propagate(True)
frame.place(relx=0.5, rely=0.5, anchor='center')

error_label = ctk.CTkLabel(master=frame, text="", font=("Roboto", font_size_error), text_color="red")
error_label.pack(pady=(padding_medium, 0))

label = ctk.CTkLabel(master=frame, text="Enter your Registration", font=("Roboto", font_size_large))
label.pack(pady=padding_medium, padx=padding_medium, anchor="center")

entry1 = ctk.CTkEntry(master=frame, justify=ctk.CENTER, font=("Arial", font_size_medium), width=550)
entry1.pack(pady=(padding_medium, 0), padx=padding_medium, anchor="center")

results_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
results_frame.pack(pady=padding_small)
results_frame.pack_propagate(True)

success_label_tax = ctk.CTkLabel(master=frame, text="", font=("Roboto", font_size_small))
success_label_mot = ctk.CTkLabel(master=frame, text="", font=("Roboto", font_size_small))

button_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
button_frame.pack(pady=55)

button = ctk.CTkButton(master=button_frame, text="Retrieve", command=lambda: onNext(), width=200, height=50, font=("Roboto", font_size_small))
button.pack(side="right", padx=20)


def onNext():
    for widget in results_frame.winfo_children():
        widget.destroy()

    error_label.configure(text="")
    success_label_tax.pack_forget()
    success_label_mot.pack_forget()

    registration = entry1.get().strip().upper()
    if not registration:
        error_label.configure(text="Please enter a registration number.")
        return

    taxStatus, taxDueDate, motStatus, motExpiryDate= v.checkMotTax(registration)
    if taxStatus and motStatus:

        mot_frame = ctk.CTkFrame(results_frame)
        mot_frame.pack(pady=padding_small)

        success_label_mot_title = ctk.CTkLabel(mot_frame,text="MOT Status: ",font=("Roboto", font_size_small))
        success_label_mot_title.pack(side="left")

        mot_status_color = "green" if motStatus.lower() == "valid" else "red"

        success_label_mot_status = ctk.CTkLabel(mot_frame,text=motStatus,text_color=mot_status_color,font=("Roboto", font_size_small))
        success_label_mot_status.pack(side="left", padx=(0, 5))

        success_label_mot_text = ctk.CTkLabel(mot_frame,text="valid until ",font=("Roboto", font_size_small))
        success_label_mot_text.pack(side="left")

        mot_color = get_date_color(motExpiryDate)

        success_label_mot_date = ctk.CTkLabel(mot_frame,text=motExpiryDate,text_color=mot_color,font=("Roboto", font_size_small))
        success_label_mot_date.pack(side="left")

        tax_frame = ctk.CTkFrame(results_frame)
        tax_frame.pack(pady=padding_small)
        success_label_tax_title = ctk.CTkLabel(tax_frame,text="Tax Status: ",font=("Roboto", font_size_small))
        success_label_tax_title.pack(side="left")

        tax_status_color = "green" if taxStatus.lower() == "taxed" else "red"

        success_label_tax_status = ctk.CTkLabel(tax_frame,text=taxStatus,text_color=tax_status_color, font=("Roboto", font_size_small))
        success_label_tax_status.pack(side="left", padx=(0, 5))

        success_label_tax_text = ctk.CTkLabel( tax_frame,text="valid until ", font=("Roboto", font_size_small))
        success_label_tax_text.pack(side="left")

        tax_color = get_date_color(taxDueDate)

        success_label_tax_date = ctk.CTkLabel(tax_frame,text=taxDueDate,text_color=tax_color,font=("Roboto", font_size_small))
        success_label_tax_date.pack(side="left")
        
    else:
        error_label.configure(text="Oops, seems like we have no data on this vehicle.")

root.mainloop()
