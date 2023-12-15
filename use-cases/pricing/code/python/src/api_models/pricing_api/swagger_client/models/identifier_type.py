# coding: utf-8

"""
    Selling Partner API for Pricing

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.api_models.pricing_api.swagger_client.configuration import Configuration


class IdentifierType(object):
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
        'marketplace_asin': 'ASINIdentifier',
        'sku_identifier': 'SellerSKUIdentifier'
    }

    attribute_map = {
        'marketplace_asin': 'MarketplaceASIN',
        'sku_identifier': 'SKUIdentifier'
    }

    def __init__(self, marketplace_asin=None, sku_identifier=None, _configuration=None):  # noqa: E501
        """IdentifierType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._marketplace_asin = None
        self._sku_identifier = None
        self.discriminator = None

        self.marketplace_asin = marketplace_asin
        if sku_identifier is not None:
            self.sku_identifier = sku_identifier

    @property
    def marketplace_asin(self):
        """Gets the marketplace_asin of this IdentifierType.  # noqa: E501

        Indicates the item is identified by MarketPlaceId and ASIN.  # noqa: E501

        :return: The marketplace_asin of this IdentifierType.  # noqa: E501
        :rtype: ASINIdentifier
        """
        return self._marketplace_asin

    @marketplace_asin.setter
    def marketplace_asin(self, marketplace_asin):
        """Sets the marketplace_asin of this IdentifierType.

        Indicates the item is identified by MarketPlaceId and ASIN.  # noqa: E501

        :param marketplace_asin: The marketplace_asin of this IdentifierType.  # noqa: E501
        :type: ASINIdentifier
        """
        if self._configuration.client_side_validation and marketplace_asin is None:
            raise ValueError("Invalid value for `marketplace_asin`, must not be `None`")  # noqa: E501

        self._marketplace_asin = marketplace_asin

    @property
    def sku_identifier(self):
        """Gets the sku_identifier of this IdentifierType.  # noqa: E501

        Indicates the item is identified by MarketPlaceId, SellerId, and SellerSKU.  # noqa: E501

        :return: The sku_identifier of this IdentifierType.  # noqa: E501
        :rtype: SellerSKUIdentifier
        """
        return self._sku_identifier

    @sku_identifier.setter
    def sku_identifier(self, sku_identifier):
        """Sets the sku_identifier of this IdentifierType.

        Indicates the item is identified by MarketPlaceId, SellerId, and SellerSKU.  # noqa: E501

        :param sku_identifier: The sku_identifier of this IdentifierType.  # noqa: E501
        :type: SellerSKUIdentifier
        """

        self._sku_identifier = sku_identifier

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
        if issubclass(IdentifierType, dict):
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
        if not isinstance(other, IdentifierType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentifierType):
            return True

        return self.to_dict() != other.to_dict()
