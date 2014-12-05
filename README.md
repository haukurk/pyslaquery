pyslaquery
==========
A simple wrapper for querying messages, channels and other information from Slack channels.


The API is located at https://slack.com/api

## Installation

    pip install git+git://github.com/haukurk/pyslaquery.git
	
or

	pip install pyslaquery
	
## Example of usage

### Basic search

Get latest messages from the channel `#general`

from pyslaquery import SlackQueryClient
client = SlackQueryClient('xoxp-3137381152-3137381170-3136966963-ac68cc')
messages = client.get_messages_for_channel('breaking-news')


	>>> from pyslaquery import SlackQueryClient
	>>> client = SlackQueryClient('Authorization Token')
	>>> client.get_messages_for_channel('breaking-news')
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
	
#### Search options

You can limit how many messages you get:

    >>> client.get_messages_for_channel('breaking-news', limit=1)

You can include messages with subtype (messages like when a user joined the channel etc.)

    >>> client.get_messages_for_channel('breaking-news', limit=1, no_subtypes=False)

### List Channels

You can easily list your channels:

    >>> client.get_channel_list
    
You can easily get informations about a channel:

    >>> client.get_channel_info("general")


## Exceptions 

List of exceptions that the wrapper can raise

*SlackAPIError*: When Slack API returns a error of any kind.

