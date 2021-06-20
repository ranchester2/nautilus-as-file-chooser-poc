mkdir -p /usr/share/xdg-desktop-portal/portals/
cp nautilus.portal /usr/share/xdg-desktop-portal/portals/nautilus.portal

mkdir -p /usr/share/dbus-1/services/
cp org.freedesktop.impl.portal.desktop.nautilus.service /usr/share/dbus-1/services/

cp xdg-desktop-portal-nautilus.desktop /usr/share/applications/

mkdir -p /usr/lib/systemd/user/
cp xdg-desktop-portal-nautilus.service /usr/lib/systemd/user

rm -rvf /usr/libexec/naut-portal-packages/
mkdir -p /usr/libexec/naut-portal-packages/nautilus
touch /usr/libexec/naut-portal-packages/nautilus/__init__.py
cp ../defs.py ../file_chooser.py /usr/libexec/naut-portal-packages/nautilus/
cp ../nautilus_portal.py /usr/libexec/xdg-desktop-portal-nautilus
chmod +x /usr/libexec/xdg-desktop-portal-nautilus