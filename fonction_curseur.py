X = 600
Y = 600

import gtk
import gobject

def run():
    display = gtk.gdk.display_get_default()
    screen = gtk.gdk.screen_get_default()
    display.warp_pointer(screen, X, Y)
    gtk.main_quit()

gobject.idle_add(run)
gtk.main()