pyslaquery - A simple wrapper for querying (and posting) messages from Slack channels.
==========

The wrapper's sole purpose is to query the Slack API and get latest messages in a channel.


The API is located at https://api.slack.com

## Installation

    pip install git+git://github.com/haukurk/pyslaquery.git
	
or

	pip install pyslaquery
	
## Example of usage

Get latest messages from the channel `#general`

	>>> from pyslaquery import SlackQueryClient
	>>> client = SlackQueryClient('Authorization Token')
	>>> client.get_latest_messages('general')
	{
	"ok": true,
	"messages": [
		{
		"type": "message",
		"user": "U0341B750",
		"text": "Test Message 1",
		"ts": "1417641989.000009"
		},
		{
		"type": "message",
		"user": "U0341B750",
		"text": "Test Message 2",
		"ts": "1417641976.000008"
		}
	],
	"has_more": false
	}
	
## Exceptions 

List of exceptions that the wrapper can raise

*SlackAPIError*: When Slack API returns a error of any kind.

