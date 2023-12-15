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


class ItemOfferByMarketplace(object):
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
        'marketplace_id': 'str',
        'offer_type': 'str',
        'price': 'Money',
        'points': 'Points'
    }

    attribute_map = {
        'marketplace_id': 'marketplaceId',
        'offer_type': 'offerType',
        'price': 'price',
        'points': 'points'
    }

    def __init__(self, marketplace_id=None, offer_type=None, price=None, points=None, _configuration=None):  # noqa: E501
        """ItemOfferByMarketplace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._marketplace_id = None
        self._offer_type = None
        self._price = None
        self._points = None
        self.discriminator = None

        self.marketplace_id = marketplace_id
        self.offer_type = offer_type
        self.price = price
        if points is not None:
            self.points = points

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ItemOfferByMarketplace.  # noqa: E501

        Amazon marketplace identifier.  # noqa: E501

        :return: The marketplace_id of this ItemOfferByMarketplace.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ItemOfferByMarketplace.

        Amazon marketplace identifier.  # noqa: E501

        :param marketplace_id: The marketplace_id of this ItemOfferByMarketplace.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and marketplace_id is None:
            raise ValueError("Invalid value for `marketplace_id`, must not be `None`")  # noqa: E501

        self._marketplace_id = marketplace_id

    @property
    def offer_type(self):
        """Gets the offer_type of this ItemOfferByMarketplace.  # noqa: E501

        Type of offer for the listings item.  # noqa: E501

        :return: The offer_type of this ItemOfferByMarketplace.  # noqa: E501
        :rtype: str
        """
        return self._offer_type

    @offer_type.setter
    def offer_type(self, offer_type):
        """Sets the offer_type of this ItemOfferByMarketplace.

        Type of offer for the listings item.  # noqa: E501

        :param offer_type: The offer_type of this ItemOfferByMarketplace.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and offer_type is None:
            raise ValueError("Invalid value for `offer_type`, must not be `None`")  # noqa: E501
        allowed_values = ["B2C", "B2B"]  # noqa: E501
        if (self._configuration.client_side_validation and
                offer_type not in allowed_values):
            raise ValueError(
                "Invalid value for `offer_type` ({0}), must be one of {1}"  # noqa: E501
                .format(offer_type, allowed_values)
            )

        self._offer_type = offer_type

    @property
    def price(self):
        """Gets the price of this ItemOfferByMarketplace.  # noqa: E501

        Purchase price of the listings item  # noqa: E501

        :return: The price of this ItemOfferByMarketplace.  # noqa: E501
        :rtype: Money
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ItemOfferByMarketplace.

        Purchase price of the listings item  # noqa: E501

        :param price: The price of this ItemOfferByMarketplace.  # noqa: E501
        :type: Money
        """
        if self._configuration.client_side_validation and price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def points(self):
        """Gets the points of this ItemOfferByMarketplace.  # noqa: E501


        :return: The points of this ItemOfferByMarketplace.  # noqa: E501
        :rtype: Points
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this ItemOfferByMarketplace.


        :param points: The points of this ItemOfferByMarketplace.  # noqa: E501
        :type: Points
        """

        self._points = points

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
        if issubclass(ItemOfferByMarketplace, dict):
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
        if not isinstance(other, ItemOfferByMarketplace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemOfferByMarketplace):
            return True

        return self.to_dict() != other.to_dict()
