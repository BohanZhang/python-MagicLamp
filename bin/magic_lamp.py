#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import appindicator

class MagicLamp:
    def __init__(self):
        self.ind = appindicator.Indicator ("magic-lamp-client", "magic-lamp-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon("distributor-logo")

        # create a menu
        self.menu = gtk.Menu()

        # create items for the menu - labels, checkboxes, radio buttons and images are supported:
        from utils.lunar_calendar import get_lunar_date
        import datetime
        today = datetime.datetime.today()
        lunar_data = get_lunar_date(today)
        lunar_char = '农历' + str(lunar_data[1]) + '月' + ''
        print lunar_char
        item = gtk.MenuItem(lunar_char)
        item.show()
        self.menu.append(item)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)

    def quit(self, widget, data=None):
        gtk.main_quit()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ml = MagicLamp()
    main()
