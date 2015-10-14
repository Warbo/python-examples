# Web browser in 20 lines of Python (excluding comments)
# Made by Chris Warburton whilst consulting the example browser of
# PyWebKitGTK by Jan Alonzo <jmalonzo@unpluggable.com>,
# One Laptop Per Child and Red Hat, Inc.
# This is Public Domain. Chop it, mix it, fiddle around, it's meant for
# learning.

import gtk, webkit

# Define a web browser as a type of window
class WebBrowser(gtk.Window):

	def __init__(self):
		# Set up the regular window stuff
		super(WebBrowser, self).__init__()

		# When the window closes we want the program to stop
		self.connect('destroy', gtk.main_quit)

		# We need 2 things stacked vertically, so make a box which
		# stacks things vertically, then add it to the window
		self.vbox = gtk.VBox()
		self.add(self.vbox)

		# Make a text entry box to input a new address and add it to
		# the vertically stacking box so that it only expands across
		self.addressbar = gtk.Entry()
		self.vbox.pack_start(self.addressbar, expand=False, fill=False)
		# When an address is entered run "location_entered"
		self.addressbar.connect('activate', self.location_entered)

		# The page may be too big for the window, so make a box which
		# can scroll and add it to the vertically stacking box
		self.scroller = gtk.ScrolledWindow()
		self.vbox.add(self.scroller)

		# Make the actual page viewer and put it in the scrolling box
		self.webpage = webkit.WebView()
		self.scroller.add(self.webpage)

		# Finally make everything visible
		self.show_all()

	def location_entered(self, addressbar):
		# This is run when an address is entered and tells the webpage
		# viewer to load the new address
		self.webpage.open(addressbar.props.text)

# Make one of the web browsers we just defined
webbrowser = WebBrowser()

# Run the program
gtk.main()
