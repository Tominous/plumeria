"""A list of common configuration options that might be used by plugins."""

from plumeria import config
from plumeria.config.types import boolstr, dateformatstr

nsfw = config.create("common", "nsfw", type=boolstr, fallback=False, comment="Whether to allow NSFW functions",
                     scoped=True, private=False)

short_date_time_format = config.create("common", "date_time_short", type=dateformatstr,
                                       fallback="%b %m, %Y %I:%M %p %Z", comment="Short date and time format",
                                       scoped=True, private=False)

config.add(nsfw)
config.add(short_date_time_format)
