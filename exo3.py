import tkinter as tk

def inscription():
    pseudo = pseudo_entry.get()
    mot_de_passe = mot_de_passe_entry.get()
    email = email_entry.get()

    print("Félicitations ! Votre inscription est terminée.")
    print("Pseudo:", pseudo)
    print("Mot de passe:", mot_de_passe)
    print("Email:", email)

fenetre = tk.Tk()
fenetre.title("Inscription")

pseudo_label = tk.Label(fenetre, text="Pseudo:")
pseudo_label.pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:")
mot_de_passe_label.pack()
mot_de_passe_entry = tk.Entry(fenetre, show="*")
mot_de_passe_entry.pack()

email_label = tk.Label(fenetre, text="Email:")
email_label.pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()

inscription_button = tk.Button(fenetre, text="Inscription", command=inscription)
inscription_button.pack()

fenetre.geometry("800x500")

fenetre.mainloop()