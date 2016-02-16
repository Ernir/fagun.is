import json
import requests
from Fagun.settings import MAILCHIMP_API_KEY, \
    MAILCHIMP_ID, MAILCHIMP_SERVER


class MailChimp:
    """
    A class of helper methods for Mailchimp.
    Interfaces with version 3.0 of the Mailchimp API.
    """

    def __init__(self):
        self.mailchimp_id = MAILCHIMP_ID
        self.secret = MAILCHIMP_API_KEY
        self.server = MAILCHIMP_SERVER
        self.url_root = "https://{0}.api.mailchimp.com/3.0/".format(
            self.server
        )

    def add_member(self, email_address):
        """
        Adds one member to the defined mailing list.
        Returns the status code.
        """
        url = "{0}lists/{1}/members".format(
            self.url_root,
            self.mailchimp_id,
        )
        params = {
            "email_address": email_address,
            "status": "subscribed"
        }
        r = requests.post(
            url,
            auth=("apikey", self.secret),
            data=json.dumps(params)
        )
        return r.status_code


    def get_list(self):
        """
        Returns a list of the email addresses of all members signed up for
        the list.
        """
        url = "{0}lists/{1}/members".format(
            self.url_root,
            self.mailchimp_id,
        )
        params = {
            "fields": "members.email_address",
            "count": 10,  # The API is paginated
            "offset": 0
        }
        fetching = True
        addresses = []
        while fetching:  # ToDo: Error handling
            r = requests.get(
                url,
                auth=("apikey", self.secret),
                params=params
            )
            fetched_addresses = [  # Extracting just the addresses
                                   address["email_address"] for address in
                                   r.json()["members"]
            ]
            n = len(fetched_addresses)
            if not n > 0:
                fetching = False
            addresses += fetched_addresses
            params["offset"] += n  # Go to the next page of the API
        return addresses