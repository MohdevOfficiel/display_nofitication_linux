from gi.repository import Notify
from gi.repository import Gtk

Notify.init('example')
notif = Notify.Notification.new(
    'Title', # titre
    'Longer message', # message
    'dialog-information' # icône
)

# définition de la callback exécutée lors du clic sur le bouton
def callback(notif_object, action_name, users_data):
    # on peut faire des choses ici
    notif_object.close()
    Gtk.main_quit()

# ajout de notre action sur la notification
notif.add_action(
    'our_callback', # identifiant
    'Callback and quit', # texte du bouton
    callback, # function callback de notre bouton
    None, # user_datas, ce dont vous avez besoin dans la callback
    None # fonction qui supprime les user_datas
)
notif.show()
Gtk.main()
