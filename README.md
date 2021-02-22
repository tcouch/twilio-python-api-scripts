# Setup Python with the Twilio client
## Using venv
```
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt
```

## Using conda
```
conda env create -n twilio-env -f environment.yml
```

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
```
python tw-create-bindings.py -f my-list-of-numbers.csv
```

# Text all bindings:
```
notification = client.notify.services("IS###################################")\
    .notifications.create(tag=["all"],body="Please take our survey")
```

