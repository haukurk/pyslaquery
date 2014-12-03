import requests
from pyslaquery import exception as pyslaquery_exceptions


class RequestsHelper(object):
    """
    Logic abstraction around requests module.
    """

    def __init__(self, base):
        self.base = base

    def create_post_request(self, method, params):
        """
        Create POST request to the Slack API
        :param method: Slack API method
        :param params: params to include with the request
        :return: requests.Response object
        """
        url = "%s/%s" % (self.base, method)
        result = requests.post(url, data=params, verify=False)

        if not result.json()['ok']:
            raise pyslaquery_exceptions.SlackAPIError(result['error'])

    def create_get_request(self, method, params):
        url = "%s/%s" % (self.base, method)
        result = requests.post(url, data=params, verify=False)

        if not result.json()['ok']:
            raise pyslaquery_exceptions.SlackAPIError(result['error'])