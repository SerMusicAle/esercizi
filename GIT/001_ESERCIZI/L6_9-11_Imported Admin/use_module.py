from admin import Admin

admin = Admin("Alice", "Oleandri")

admin.privileges.privileges = ["può aggiungere post", "può eliminare post", "può bannare utente"]

admin.show_privileges()