import dbus
import dbus.service
import logging
from nautilus.defs import UID_AS_PATH


class NautilusPortal(dbus.service.Object):
    def __init__(self, bus_name):
        super().__init__(
            bus_name, UID_AS_PATH
        )
        logging.info("created portal")

    @dbus.service.method(dbus_interface="org.freedesktop.impl.portal.FileChooser",
                         in_signature="osssa{sv}", out_signature="a{sv}")
    def OpenFile(self, handle: dbus.ObjectPath, app_id: str, parent_window: str, title: str, options: dict):
        logging.info("FileChooser works!")
