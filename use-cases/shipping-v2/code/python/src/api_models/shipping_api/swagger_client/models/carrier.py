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

class Carrier(object):
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
        'id': 'CarrierId',
        'name': 'CarrierName'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, id=None, name=None):  # noqa: E501
        """Carrier - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self.discriminator = None
        self.id = id
        self.name = name

    @property
    def id(self):
        """Gets the id of this Carrier.  # noqa: E501


        :return: The id of this Carrier.  # noqa: E501
        :rtype: CarrierId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Carrier.


        :param id: The id of this Carrier.  # noqa: E501
        :type: CarrierId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Carrier.  # noqa: E501


        :return: The name of this Carrier.  # noqa: E501
        :rtype: CarrierName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Carrier.


        :param name: The name of this Carrier.  # noqa: E501
        :type: CarrierName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(Carrier, dict):
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
        if not isinstance(other, Carrier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
