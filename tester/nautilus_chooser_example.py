import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("Nautilus File Chooser Example")

        self.set_default_size(500, 300)
        self.set_border_width(12)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        label = Gtk.Label(label="Please select a file here and see the dialog.")
        vbox.pack_start(label, False, False, 0)

        button = Gtk.FileChooserButton()
        vbox.pack_end(button, False, False, 0)

        self.add(vbox)
    
def on_activate(app):
    win = MainWindow()
    win.connect("destroy", lambda b : app.quit())
    app.add_window(win)
    win.show_all()
    win.present()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
