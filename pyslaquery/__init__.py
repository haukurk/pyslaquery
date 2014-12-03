import logging
from pyslaquery.utils import RequestsHelper


class SlackBase(object):
    HELPER = RequestsHelper("https://slack.com/api/")

    def __init__(self, token):
        self.token = token


class SlackQueryClient(SlackBase):

    def __init__(self, token):
        super(SlackQueryClient, self).__init__(token)

    def get_messages_for_channel(self, channel, text, **params):
        """search.messages
        """
        method = 'chat.postMessage'
        params.update({
            'channel': channel,
            'text': text,
        })
        return self.HELPER.create_post_request(method, params).json()


class SlackHandler(logging.Handler):
    """A logging handler that posts messages to a Slack channel!
    References:
    http://docs.python.org/2/library/logging.html#handler-objects
    """
    def __init__(self, token, channel, **kwargs):
        super(SlackHandler, self).__init__()
        self.client = SlackQueryClient(token)
        self.channel = channel
        self._kwargs = kwargs

    def emit(self, record):
        message = self.format(record)
        self.client.chat_post_message(self.channel,
                                      message,
                                      **self._kwargs)