"""Sample API Client."""
import logging
import asyncio
import socket
from typing import Optional
import aiohttp
import async_timeout

from .TypeObj import RhService, SearchAddressResult

TIMEOUT = 10

_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class IntegrationBlueprintApiClient:
    """API data retrieval"""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        """Sample API Client."""
        self._session = session
        self.protocol = "https://"
        self.domain = "services.vafabmiljo.se"
        self.path = "/FutureWebVKFHus/SimpleWastePickup"
        self.base_path = self.protocol + self.domain + self.path

    async def async_get_address(self, address) -> str:
        """Use to get address string used to query real data"""
        url = self.base_path + "/SearchAdress"
        query = await self.api_wrapper(
            "post", url, data={"searchText": address}, headers=HEADERS
        )
        response = query.json()
        obj = SearchAddressResult.from_dict(response)
        _LOGGER.warning(response)
        _LOGGER.warning("Address: %s, Response: %s", address, obj)
        return obj.buildings[0]

    async def async_get_data(self, address) -> list[RhService]:
        """Get data from the API."""

        url = self.base_path + "/GetWastePickupSchedule"
        params = {"address": address}
        return RhService.from_dict(await self.api_wrapper("get", url, params=params))

    async def api_wrapper(
        self,
        method: str,
        url: str,
        data: dict = None,
        headers: dict = None,
        params: dict = None,
    ) -> dict:
        """Get information from the API."""
        if data is None:
            data = {}
        if headers is None:
            headers = {}
        if params is None:
            params = {}

        try:
            async with async_timeout.timeout(TIMEOUT):
                match method:
                    case "get":
                        response = await self._session.get(
                            url, headers=headers, params=params
                        )
                        return await response.json()
                    case "post":
                        response = await self._session.post(
                            url, headers=headers, json=data
                        )
                        return await response.json()

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
