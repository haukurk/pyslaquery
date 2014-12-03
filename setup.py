from distutils.core import setup

setup(
    name="pyslaquery",
    version="0.1.0",
    description="A Python wrapper for querying and posting messages from Slack Channels",
    author="@haukurk",
    author_email="haukur@hauxi.is",
    packages=["pyslaquery"],
    install_requires=["requests"],
)