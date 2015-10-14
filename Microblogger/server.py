# Blogging server in 17 lines (not counting comments)
# Note, you can only post blog entries from an account that is
# in the server accounts roster

import xmpp, time

# This function is run automatically when an incoming message arrives
def xmpp_message(con, event):
	# Handle messages but not protocol overhead like logon/off
	if event.getType() == 'chat' and event.getBody() is not None:
		changed_site = []		# Start with a clean HTML file
		# Add the current HTML file to it
		for line in open('blog.html', 'r').readlines():
			changed_site.append(line)
			# Add a timestamp and the new post above the previous posts, starting after the following comment
			if line.find('<!--Blog Posts Start Here-->') > -1:
				changed_site.append('		<h2>' + time.strftime('%Y-%m-%d %H:%M:%S') + '</h2>\n		<p>' + event.getBody() + '</p>\n\n')
		# Replace the old HTML file with the new one
		open('blog.html','w').writelines(changed_site)

# This logs onto XMPP as 'username@server' with password 'password'
client = xmpp.Client('server',debug=[])
client.connect()
client.auth('username','password',resource='microblog')
# Declare which function we want to run on incoming messages
client.RegisterHandler('message',xmpp_message)
# Tell the world that we are online
client.sendInitPresence()

# Look for messages every second
while True:
	client.Process(1)
	time.sleep(1)
