import logging
from pyslaquery.utils import RequestsHelper
from pyslaquery.exception import SlackAPIError


class SlackBase(object):
    HELPER = RequestsHelper("https://slack.com/api/")

    def __init__(self, token):
        self.token = token


class SlackQueryClient(SlackBase):
    def __init__(self, token):
        super(SlackQueryClient, self).__init__(token)

    def get_messages_for_channel(self, req_channel, **params):
        """channels.history
        """
        method = 'channels.history'

        channels = self.get_channel_list()

        for channel in channels:
            if channel["name"] == req_channel:
                params.update({
                    'token': self.token,
                    'channel': channel["id"],
                })
                return self.HELPER.create_post_request(method, params).json()

        raise SlackAPIError("Could not find the channel specified.")

    def get_channel_list(self, **params):
        """channels.list
        """
        method = 'channels.list'
        params.update({
            'token': self.token
        })
        return self.HELPER.create_get_request(method, params).json()["channels"]