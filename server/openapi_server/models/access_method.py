# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_url import AccessURL
from openapi_server import util

from openapi_server.models.access_url import AccessURL  # noqa: E501

class AccessMethod(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, access_url=None, access_id=None, region=None):  # noqa: E501
        """AccessMethod - a model defined in OpenAPI

        :param type: The type of this AccessMethod.  # noqa: E501
        :type type: str
        :param access_url: The access_url of this AccessMethod.  # noqa: E501
        :type access_url: AccessURL
        :param access_id: The access_id of this AccessMethod.  # noqa: E501
        :type access_id: str
        :param region: The region of this AccessMethod.  # noqa: E501
        :type region: str
        """
        self.openapi_types = {
            'type': str,
            'access_url': AccessURL,
            'access_id': str,
            'region': str
        }

        self.attribute_map = {
            'type': 'type',
            'access_url': 'access_url',
            'access_id': 'access_id',
            'region': 'region'
        }

        self._type = type
        self._access_url = access_url
        self._access_id = access_id
        self._region = region

    @classmethod
    def from_dict(cls, dikt) -> 'AccessMethod':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessMethod of this AccessMethod.  # noqa: E501
        :rtype: AccessMethod
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this AccessMethod.

        Type of the access method.  # noqa: E501

        :return: The type of this AccessMethod.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccessMethod.

        Type of the access method.  # noqa: E501

        :param type: The type of this AccessMethod.
        :type type: str
        """
        allowed_values = ["s3", "gs", "ftp", "gsiftp", "globus", "htsget", "https", "file"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def access_url(self):
        """Gets the access_url of this AccessMethod.


        :return: The access_url of this AccessMethod.
        :rtype: AccessURL
        """
        return self._access_url

    @access_url.setter
    def access_url(self, access_url):
        """Sets the access_url of this AccessMethod.


        :param access_url: The access_url of this AccessMethod.
        :type access_url: AccessURL
        """

        self._access_url = access_url

    @property
    def access_id(self):
        """Gets the access_id of this AccessMethod.

        An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided.  # noqa: E501

        :return: The access_id of this AccessMethod.
        :rtype: str
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """Sets the access_id of this AccessMethod.

        An arbitrary string to be passed to the `/access` method to get an `AccessURL`. This string must be unique within the scope of a single object. Note that at least one of `access_url` and `access_id` must be provided.  # noqa: E501

        :param access_id: The access_id of this AccessMethod.
        :type access_id: str
        """

        self._access_id = access_id

    @property
    def region(self):
        """Gets the region of this AccessMethod.

        Name of the region in the cloud service provider that the object belongs to.  # noqa: E501

        :return: The region of this AccessMethod.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AccessMethod.

        Name of the region in the cloud service provider that the object belongs to.  # noqa: E501

        :param region: The region of this AccessMethod.
        :type region: str
        """

        self._region = region
