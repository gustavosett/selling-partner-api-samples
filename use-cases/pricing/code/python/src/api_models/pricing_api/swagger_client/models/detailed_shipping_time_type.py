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


class DetailedShippingTimeType(object):
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
        'minimum_hours': 'int',
        'maximum_hours': 'int',
        'available_date': 'str',
        'availability_type': 'str'
    }

    attribute_map = {
        'minimum_hours': 'minimumHours',
        'maximum_hours': 'maximumHours',
        'available_date': 'availableDate',
        'availability_type': 'availabilityType'
    }

    def __init__(self, minimum_hours=None, maximum_hours=None, available_date=None, availability_type=None, _configuration=None):  # noqa: E501
        """DetailedShippingTimeType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._minimum_hours = None
        self._maximum_hours = None
        self._available_date = None
        self._availability_type = None
        self.discriminator = None

        if minimum_hours is not None:
            self.minimum_hours = minimum_hours
        if maximum_hours is not None:
            self.maximum_hours = maximum_hours
        if available_date is not None:
            self.available_date = available_date
        if availability_type is not None:
            self.availability_type = availability_type

    @property
    def minimum_hours(self):
        """Gets the minimum_hours of this DetailedShippingTimeType.  # noqa: E501

        The minimum time, in hours, that the item will likely be shipped after the order has been placed.  # noqa: E501

        :return: The minimum_hours of this DetailedShippingTimeType.  # noqa: E501
        :rtype: int
        """
        return self._minimum_hours

    @minimum_hours.setter
    def minimum_hours(self, minimum_hours):
        """Sets the minimum_hours of this DetailedShippingTimeType.

        The minimum time, in hours, that the item will likely be shipped after the order has been placed.  # noqa: E501

        :param minimum_hours: The minimum_hours of this DetailedShippingTimeType.  # noqa: E501
        :type: int
        """

        self._minimum_hours = minimum_hours

    @property
    def maximum_hours(self):
        """Gets the maximum_hours of this DetailedShippingTimeType.  # noqa: E501

        The maximum time, in hours, that the item will likely be shipped after the order has been placed.  # noqa: E501

        :return: The maximum_hours of this DetailedShippingTimeType.  # noqa: E501
        :rtype: int
        """
        return self._maximum_hours

    @maximum_hours.setter
    def maximum_hours(self, maximum_hours):
        """Sets the maximum_hours of this DetailedShippingTimeType.

        The maximum time, in hours, that the item will likely be shipped after the order has been placed.  # noqa: E501

        :param maximum_hours: The maximum_hours of this DetailedShippingTimeType.  # noqa: E501
        :type: int
        """

        self._maximum_hours = maximum_hours

    @property
    def available_date(self):
        """Gets the available_date of this DetailedShippingTimeType.  # noqa: E501

        The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.  # noqa: E501

        :return: The available_date of this DetailedShippingTimeType.  # noqa: E501
        :rtype: str
        """
        return self._available_date

    @available_date.setter
    def available_date(self, available_date):
        """Sets the available_date of this DetailedShippingTimeType.

        The date when the item will be available for shipping. Only displayed for items that are not currently available for shipping.  # noqa: E501

        :param available_date: The available_date of this DetailedShippingTimeType.  # noqa: E501
        :type: str
        """

        self._available_date = available_date

    @property
    def availability_type(self):
        """Gets the availability_type of this DetailedShippingTimeType.  # noqa: E501

        Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.  # noqa: E501

        :return: The availability_type of this DetailedShippingTimeType.  # noqa: E501
        :rtype: str
        """
        return self._availability_type

    @availability_type.setter
    def availability_type(self, availability_type):
        """Sets the availability_type of this DetailedShippingTimeType.

        Indicates whether the item is available for shipping now, or on a known or an unknown date in the future. If known, the availableDate property indicates the date that the item will be available for shipping. Possible values: NOW, FUTURE_WITHOUT_DATE, FUTURE_WITH_DATE.  # noqa: E501

        :param availability_type: The availability_type of this DetailedShippingTimeType.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOW", "FUTURE_WITHOUT_DATE", "FUTURE_WITH_DATE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                availability_type not in allowed_values):
            raise ValueError(
                "Invalid value for `availability_type` ({0}), must be one of {1}"  # noqa: E501
                .format(availability_type, allowed_values)
            )

        self._availability_type = availability_type

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
        if issubclass(DetailedShippingTimeType, dict):
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
        if not isinstance(other, DetailedShippingTimeType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedShippingTimeType):
            return True

        return self.to_dict() != other.to_dict()
