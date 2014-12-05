from pyslaquery.utils import find_channel_id, filter_out_message_subtypes
from pyslaquery.connection import SlackAPIConnection
from pyslaquery.exception import SlackAPIError


class SlackBase(object):
    _slackconnection = None

    def __init__(self, token):
        self._slackconnection = SlackAPIConnection("https://slack.com/api", token)


class SlackQueryClient(SlackBase):
    def __init__(self, token):
        super(SlackQueryClient, self).__init__(token)

    def get_messages_for_channel(self, req_channel, no_subtypes=True, count=10, **params):
        """
        Fetches history of messages and events from a channel.
        Method: channels.history

        :param req_channel: Channel to get messages from.
        :param no_subtypes: Show only plain messages, no messages with subtypes.
        :param count: Limit number of showned messages
        :param params: extra parameters to send with the request to the Slack API.
        return: dict object from the Slack API.
        """
        method = 'channels.history'

        channel_id = find_channel_id(self.get_channel_list(), req_channel)

        if channel_id is not None:
            params.update({
                'channel': channel_id,
                'count': count
            })
            channel_response = self._slackconnection.create_post_request(method, params).json()
            if no_subtypes is True:
                channel_response["messages"] = filter_out_message_subtypes(channel_response["messages"])
            return channel_response

        raise SlackAPIError("Could not find the channel specified.")

    def get_channel_list(self, **params):
        """
        Lists all channels in a Slack team.
        Method: channels.list

        return: dict object from the Slack API.
        """
        method = 'channels.list'
        return self._slackconnection.create_get_request(method, params).json()["channels"]

    def get_channel_info(self, req_channel, **params):
        """
        Gets information about a channel.
        Method: channels.info

        :param params: extra parameters to send with the request to the Slack API.
        :return: dict object from the Slack API.
        """
        method = 'channels.info'
        params.update({
            'channel': req_channel
        })
        return self._slackconnection.create_get_request(method, params).json()["channels"]