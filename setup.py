from distutils.core import setup

setup(
    name="pyslaquery",
    version="0.1.7",
    description="A really simple wrapper around Slack API, for querying and from Slack Channels.",
    author="@haukurk",
    author_email="haukur@hauxi.is",
    packages=["pyslaquery"],
    install_requires=["requests"],
	url = 'https://github.com/haukurk/pyslaquery',
	download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
	keywords = ['slack', 'channels', 'query'], # arbitrary keywords
	classifiers = [],
)