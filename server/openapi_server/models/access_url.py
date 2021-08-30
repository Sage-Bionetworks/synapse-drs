# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AccessURL(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, url=None, headers=None):  # noqa: E501
        """AccessURL - a model defined in OpenAPI

        :param url: The url of this AccessURL.  # noqa: E501
        :type url: str
        :param headers: The headers of this AccessURL.  # noqa: E501
        :type headers: List[str]
        """
        self.openapi_types = {
            'url': str,
            'headers': List[str]
        }

        self.attribute_map = {
            'url': 'url',
            'headers': 'headers'
        }

        self._url = url
        self._headers = headers

    @classmethod
    def from_dict(cls, dikt) -> 'AccessURL':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessURL of this AccessURL.  # noqa: E501
        :rtype: AccessURL
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self):
        """Gets the url of this AccessURL.

        A fully resolvable URL that can be used to fetch the actual object bytes.  # noqa: E501

        :return: The url of this AccessURL.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AccessURL.

        A fully resolvable URL that can be used to fetch the actual object bytes.  # noqa: E501

        :param url: The url of this AccessURL.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this AccessURL.

        An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.  # noqa: E501

        :return: The headers of this AccessURL.
        :rtype: List[str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this AccessURL.

        An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.  # noqa: E501

        :param headers: The headers of this AccessURL.
        :type headers: List[str]
        """

        self._headers = headers
