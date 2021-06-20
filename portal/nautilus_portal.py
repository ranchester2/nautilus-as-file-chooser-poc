#!/usr/bin/env python3
from nautilus.file_chooser import NautilusPortal
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop
import dbus
import dbus.service
import logging
import os
import sys
sys.path.insert(1, "/usr/libexec/naut-portal-packages")


UID = "org.freedesktop.impl.portal.desktop.nautilus"
UID_AS_PATH = "/org/freedesktop/portal/desktop"


def main():
    logging.basicConfig(filename=f"{os.environ['HOME']}/portal.log",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.info("starting...")

    DBusGMainLoop(set_as_default=True)
    try:
        bus_name = dbus.service.BusName(
            UID, bus=dbus.SessionBus(), do_not_queue=True
        )
        logging.info("connected to bus")
    except dbus.exceptions.NameExistsException:
        logging.fatal(f"Service with id {UID} is already running")
        exit(1)
    loop = GLib.MainLoop()
    daemon = NautilusPortal(bus_name)
    try:
        loop.run()
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt received")
    except Exception as e:
        logging.error("Unhandled exception: {str(e)}")
    finally:
        loop.quit()


if __name__ == "__main__":
    main()
