# Setup Python with the Twilio client
In: my.desktop.ucl.ac.uk
  Open: Anaconda3 (64-bit) > Anaconda Prompt
  In: Anaconda Prompt
    Type:
      conda create -n twilio
      conda activate twilio
      conda install pip
      pip install twilio yaml
      python # this starts python interpreter with ">>>" prompt
    In: Python interpreter
      Type:
        from twilio.rest import Client

# Setup Twilio trial account
https://www.twilio.com/try-twilio

# Buy a number
All products and services > SUPER NETWORK > Phone Numbers > Buy a number
* Make sure you get a GB one!

# Set up a messaging service
All products and services > COMMUNICATIONS CLOUD > Programmable Messaging > Messaging services > Create Messaging Service
* Make a note of the messaging service SID; e.g. "MG#################################"

# Set up a notify service
All products and services > ENGAGEMENT CLOUD > Notify > Services > +
* Give it a friendly name and create
* Make a note of the notify service SID; e.g. "IS###################################"
* Click service friendly name
* Under Messaging Service SID select the messaging service from above
* Save

# Run tw-create-bindings.py

# Text all bindings:
notification = client.notify.services("IS###################################")\
    .notifications.create(tag=["all"],body="Please take our survey")
