pyslaquery
==========
A really simple wrapper around Slack API, for querying information from Slack channels and users.


*tags: query, Slack API, python.


The API is located at https://slack.com/api

## Installation

    pip install git+git://github.com/haukurk/pyslaquery.git
	
or

	pip install pyslaquery
	
## Example of usage

### Basic search

Get latest messages from the channel `#general`

	>>> from pyslaquery import SlackQueryClient
	>>> client = SlackQueryClient('Authorization Token')
	>>> client.get_messages_for_channel('breaking-news')
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
	
#### Search options

You can limit how many messages you get:

    >>> client.get_messages_for_channel('breaking-news', limit=1)

You can include messages with subtype (messages like when a user joined the channel etc.)

    >>> client.get_messages_for_channel('breaking-news', limit=1, no_subtypes=False)
    
You can resolve user id's.

    >>> client.get_messages_for_channel('breaking-news', resolve_usernames=True)

### Other Examples

List your channels:

    >>> client.get_channel_list
    
Query informations about a channel:

    >>> client.get_channel_info("general")

Query information about a user, from its id:

    >>> client.get_user_info("USD426733")

## Exceptions 

List of exceptions that the wrapper can raise

*SlackAPIError*: When Slack API returns a error of any kind.

