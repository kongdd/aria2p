"""
Aria2p package.

This package provides a command-line tool and a Python library to interact with an `aria2c` daemon process through
JSON-RPC.

If you read this message, you probably want to learn about the library and not the command-line tool:
please refer to the README.md included in this package to get the link to the official documentation.
"""


from .api import API
from .client import JSONRPCClient, JSONRPCError
from .downloads import BitTorrent, Download, File
from .options import Options
from .stats import Stats

__all__ = ["API", "JSONRPCError", "JSONRPCClient", "Download", "BitTorrent", "File", "Options", "Stats"]

# TODO: write aria2, aria2c, Aria2, Aria2c consistently
# TODO: write all docstrings
# TODO: write tests
