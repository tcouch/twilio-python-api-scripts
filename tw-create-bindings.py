#!/usr/bin/env python3

from  twilio.rest import Client
import uuid
import argparse
import csv
import sys
import yaml

def main():
    parser = argparse.ArgumentParser(
        description="Create bindings for a list of phone numbers in Twilio")
    f_help = "CSV file containing list of phone numbers"
    parser.add_argument('-f','--file',help=f_help)
    args = parser.parse_args(sys.argv[1:])
    in_file = args.file
    tw_conf = get_config()
    account_sid=tw_conf["TWILIO_ACCOUNT_SID"]
    auth_token=tw_conf["TWILIO_AUTH_TOKEN"]
    service_sid=tw_conf["TWILIO_NOTIFY_SERVICE_SID"]
    message_service_sid=tw_conf["TWILIO_MESSAGE_SERVICE_SID"]
    client = Client(account_sid,auth_token)
    numbers_list = get_phone_numbers(in_file)
    output_list = []
    for phone_no in numbers_list:
        phone_no, id = bind_phone_number(phone_no,client,service_sid)
        output_list.append({
            'phone_no': phone_no,
            'id': id
        })
    output_file = in_file[:-4] + '_output.csv'
    with open(output_file, 'w',newline='') as f:
        fc = csv.DictWriter(f,fieldnames=output_list[0].keys())
        fc.writeheader()
        fc.writerows(output_list)

def get_config():
    with open('twilio.config') as conf_file:
        tw_conf = yaml.load(conf_file, Loader=yaml.BaseLoader)
    return tw_conf

def get_phone_numbers(in_file) -> 'list':
    numbers_list = []
    with open(in_file) as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                pass
            else:
                for phone_no in row:
                    numbers_list.append(phone_no)
    return numbers_list

def bind_phone_number(phone_no,client,service_sid) -> 'phone_no,id':
    if phone_number_is_valid(phone_no,client):
        id = uuid.uuid4()
        binding = client.notify.services(service_sid) \
                     .bindings \
                     .create(
                         identity=id,
                         binding_type='sms',
                         address=phone_no
                     )
    else: id = None
    return phone_no,id

def phone_number_is_valid(phone_no,client) -> 'bool':
    try:
        client.lookups.v1.phone_numbers(phone_no).fetch()
        return True
    except:
        print("Invalid phone number {0}. Skipping...".format(phone_no))
        return False

if __name__ == '__main__':
    main()
