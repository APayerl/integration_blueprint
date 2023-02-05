"""Constants for integration_blueprint."""
# Base component constants
NAME = "Vafab Miljö hämtningsdag"
DOMAIN = "vafab_environment_pickup_day"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by https://vafabmiljo.se"
ISSUE_URL = "https://github.com/APayerl/vafab_environment_pickup_day/issues"

# Icons
ICON = "mdi:format-quote-close"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_ADDRESS = "address"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
