import gtk, webkit
class WebBrowser(gtk.Window):
	def __init__(self):
		super(WebBrowser, self).__init__()
		self.connect('destroy', gtk.main_quit)
		self.vbox = gtk.VBox()
		self.add(self.vbox)
		self.addressbar = gtk.Entry()
		self.vbox.pack_start(self.addressbar, expand=False, fill=False)
		self.addressbar.connect('activate', self.location_entered)
		self.scroller = gtk.ScrolledWindow()
		self.vbox.add(self.scroller)
		self.webpage = webkit.WebView()
		self.scroller.add(self.webpage)
		self.show_all()
	def location_entered(self, addressbar):
		self.webpage.open(addressbar.props.text)
webbrowser = WebBrowser()
gtk.main()
