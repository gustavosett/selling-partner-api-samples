# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.  # noqa: E501

    OpenAPI spec version: v2
    Contact: swa-api-core@amazon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetCarrierAccountsResponse(object):
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
        'active_accounts': 'ActiveAccounts'
    }

    attribute_map = {
        'active_accounts': 'activeAccounts'
    }

    def __init__(self, active_accounts=None):  # noqa: E501
        """GetCarrierAccountsResponse - a model defined in Swagger"""  # noqa: E501
        self._active_accounts = None
        self.discriminator = None
        self.active_accounts = active_accounts

    @property
    def active_accounts(self):
        """Gets the active_accounts of this GetCarrierAccountsResponse.  # noqa: E501


        :return: The active_accounts of this GetCarrierAccountsResponse.  # noqa: E501
        :rtype: ActiveAccounts
        """
        return self._active_accounts

    @active_accounts.setter
    def active_accounts(self, active_accounts):
        """Sets the active_accounts of this GetCarrierAccountsResponse.


        :param active_accounts: The active_accounts of this GetCarrierAccountsResponse.  # noqa: E501
        :type: ActiveAccounts
        """
        if active_accounts is None:
            raise ValueError("Invalid value for `active_accounts`, must not be `None`")  # noqa: E501

        self._active_accounts = active_accounts

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
        if issubclass(GetCarrierAccountsResponse, dict):
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
        if not isinstance(other, GetCarrierAccountsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
