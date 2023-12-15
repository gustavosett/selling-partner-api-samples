# coding: utf-8

"""
    Selling Partner API for Listings Items

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.  For more information, see the [Listings Items API Use Case Guide](doc:listings-items-api-v2021-08-01-use-case-guide).  # noqa: E501

    OpenAPI spec version: 2021-08-01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.api_models.listings_api.swagger_client.configuration import Configuration


class ListingsItemPatchRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'product_type': 'str',
        'patches': 'list[PatchOperation]'
    }

    attribute_map = {
        'product_type': 'productType',
        'patches': 'patches'
    }

    def __init__(self, product_type=None, patches=None, _configuration=None):  # noqa: E501
        """ListingsItemPatchRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_type = None
        self._patches = None
        self.discriminator = None

        self.product_type = product_type
        self.patches = patches

    @property
    def product_type(self):
        """Gets the product_type of this ListingsItemPatchRequest.  # noqa: E501

        The Amazon product type of the listings item.  # noqa: E501

        :return: The product_type of this ListingsItemPatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ListingsItemPatchRequest.

        The Amazon product type of the listings item.  # noqa: E501

        :param product_type: The product_type of this ListingsItemPatchRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def patches(self):
        """Gets the patches of this ListingsItemPatchRequest.  # noqa: E501

        One or more JSON Patch operations to perform on the listings item.  # noqa: E501

        :return: The patches of this ListingsItemPatchRequest.  # noqa: E501
        :rtype: list[PatchOperation]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this ListingsItemPatchRequest.

        One or more JSON Patch operations to perform on the listings item.  # noqa: E501

        :param patches: The patches of this ListingsItemPatchRequest.  # noqa: E501
        :type: list[PatchOperation]
        """
        if self._configuration.client_side_validation and patches is None:
            raise ValueError("Invalid value for `patches`, must not be `None`")  # noqa: E501

        self._patches = patches

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ListingsItemPatchRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListingsItemPatchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListingsItemPatchRequest):
            return True

        return self.to_dict() != other.to_dict()
