# Nautilus as a file chooser very basic demo

Just a very crappy demo of using Nautilus instead of the Gtk File Chooser
with portals. Only the critically reqauired basics for opening files are supported.
(However you get an icon view with thumbnails!)

## Run

* First, build Nautilus, but the version in `nautilus-filechooser` directory with flatpak
and install it.

* Have dbus-python, pygobject installed.

* Go to `portal/data` and run install.sh as superuser, this messes up your install a bit though,
and it is tested only on a Debian 10 vm. If you aren't using XFCE it also might not work as
that is specified as the "desktop" in the .portal file.

* Kill all other competing xdg-desktop-portal backends that implement the file chooser.

* Reboot/restart xdg-desktop-portal.

* That's it,
now run an application that can use the portal APIs for its file chooser. In GTK, `GtkFileChooserNative`
supports this, and should be used by modern applications anyway. If GTK is not running in Flatpak,
you also have to set the `GTK_USE_PORTAL` environment variable to `1`. (Note that only opening is supported)
