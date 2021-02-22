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
* Visit https://www.twilio.com/try-twilio
* Create a copy of twilio.config.example called twilio.config
* From the [dashboard](https://www.twilio.com/console) copy your ACCOUNT SID and AUTH TOKEN and enter them in twilio.config

# Buy a number
All products and services > SUPER NETWORK > Phone Numbers > Buy a number
* Make sure you get a GB one!

# Set up a messaging service
All products and services > COMMUNICATIONS CLOUD > Programmable Messaging > Messaging services > Create Messaging Service
* Copy the messaging service SID (e.g. "MG#################################") into twilio.config

# Set up a notify service
All products and services > ENGAGEMENT CLOUD > Notify > Services > +
* Give it a friendly name and create
* Copy the notify service SID (e.g. "IS###################################") into twilio.config 
* Click service friendly name
* Under Messaging Service SID select the messaging service from above
* Save

# Run tw-create-bindings.py
* Copy the csv file containing the list of numbers you want to bind to the notify service (e.g. **my-list-of-numbers.csv**) to this project directory and run:
```
python tw-create-bindings.py -f my-list-of-numbers.csv
```

# Text all bindings:
```
notification = client.notify.services("IS###################################")\
    .notifications.create(tag=["all"],body="Please take our survey")
```

