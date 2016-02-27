#!/usr/bin/env python

from lifxlan import *
import dbus, gobject, sys
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

bus = dbus.SystemBus()
redshift = bus.get_object('dk.jonls.redshift.dbus', '/dk/jonls/Redshift')
iface = dbus.Interface(redshift, 'dk.jonls.Redshift')
lifxlan = LifxLAN(broadcast_ip=sys.argv[1])

def temperature_handler(temperature):
	sys.stdout.write('.')
	sys.stdout.flush()

	lifxlan.set_color_all_lights([0, 0, 65535, temperature], rapid=True)

iface.connect_to_signal('Temperature', temperature_handler)
print('Ready!')
gobject.MainLoop().run()

