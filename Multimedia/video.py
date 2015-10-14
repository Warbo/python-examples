import sys, os, pygtk, gtk, gobject, pygst, gst

class GTK_Main:

	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		#vbox = gtk.VBox()
		#window.add(vbox)
		#hbox = gtk.HBox()
		#vbox.pack_start(hbox, False)
		#self.entry = gtk.Entry()
		#hbox.add(self.entry)
		#self.button = gtk.Button("Start")
		#hbox.pack_start(self.button, False)
		#self.button.connect("clicked", self.start_stop)
		self.movie_window = gtk.DrawingArea()
		#vbox.add(self.movie_window)

		window.add(self.movie_window)

		window.show_all()

		self.player = gst.element_factory_make("playbin", "player")
		bus = self.player.get_bus()
		bus.add_signal_watch()
		bus.enable_sync_message_emission()
		bus.connect('message', self.on_message)
		bus.connect('sync-message::element', self.on_sync_message)


	def start_stop(self, w):
		#if self.button.get_label() == "Start":
		#	filepath = self.entry.get_text()
		#	if os.path.exists(filepath):
		#		self.button.set_label("Stop")
		#		self.player.set_property('uri', "file://" + filepath)
		#		self.player.set_state(gst.STATE_PLAYING)
		#else:
		#	self.player.set_state(gst.STATE_NULL)
		#	self.button.set_label("Start")
		self.player.set_property('uri', "file:///home/chris/Files/Music Videos/Sonata Arctica - Don't Say A Word")
		self.player.set_state(gst.STATE_PLAYING)

	def on_message(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS:
			self.player.set_state(gst.STATE_NULL)
			#self.button.set_label("Start")
		elif t == gst.MESSAGE_ERROR:
			self.player.set_state(gst.STATE_NULL)
			#self.button.set_label("Start")

	def on_sync_message(self, bus, message):
		if message.structure is None:
			return
		message_name = message.structure.get_name()
		if message_name == 'prepare-xwindow-id':
			imagesink = message.src
			imagesink.set_property('force-aspect-ratio', True)
			imagesink.set_xwindow_id(self.movie_window.window.xid)

GTK_Main()
gtk.gdk.threads_init()
gtk.main()
