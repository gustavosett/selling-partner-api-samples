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

class AvailableValueAddedServiceGroup(object):
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
        'group_id': 'str',
        'group_description': 'str',
        'is_required': 'bool',
        'value_added_services': 'list[ValueAddedService]'
    }

    attribute_map = {
        'group_id': 'groupId',
        'group_description': 'groupDescription',
        'is_required': 'isRequired',
        'value_added_services': 'valueAddedServices'
    }

    def __init__(self, group_id=None, group_description=None, is_required=None, value_added_services=None):  # noqa: E501
        """AvailableValueAddedServiceGroup - a model defined in Swagger"""  # noqa: E501
        self._group_id = None
        self._group_description = None
        self._is_required = None
        self._value_added_services = None
        self.discriminator = None
        self.group_id = group_id
        self.group_description = group_description
        self.is_required = is_required
        if value_added_services is not None:
            self.value_added_services = value_added_services

    @property
    def group_id(self):
        """Gets the group_id of this AvailableValueAddedServiceGroup.  # noqa: E501

        The type of the value-added service group.  # noqa: E501

        :return: The group_id of this AvailableValueAddedServiceGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AvailableValueAddedServiceGroup.

        The type of the value-added service group.  # noqa: E501

        :param group_id: The group_id of this AvailableValueAddedServiceGroup.  # noqa: E501
        :type: str
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def group_description(self):
        """Gets the group_description of this AvailableValueAddedServiceGroup.  # noqa: E501

        The name of the value-added service group.  # noqa: E501

        :return: The group_description of this AvailableValueAddedServiceGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_description

    @group_description.setter
    def group_description(self, group_description):
        """Sets the group_description of this AvailableValueAddedServiceGroup.

        The name of the value-added service group.  # noqa: E501

        :param group_description: The group_description of this AvailableValueAddedServiceGroup.  # noqa: E501
        :type: str
        """
        if group_description is None:
            raise ValueError("Invalid value for `group_description`, must not be `None`")  # noqa: E501

        self._group_description = group_description

    @property
    def is_required(self):
        """Gets the is_required of this AvailableValueAddedServiceGroup.  # noqa: E501

        When true, one or more of the value-added services listed must be specified.  # noqa: E501

        :return: The is_required of this AvailableValueAddedServiceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this AvailableValueAddedServiceGroup.

        When true, one or more of the value-added services listed must be specified.  # noqa: E501

        :param is_required: The is_required of this AvailableValueAddedServiceGroup.  # noqa: E501
        :type: bool
        """
        if is_required is None:
            raise ValueError("Invalid value for `is_required`, must not be `None`")  # noqa: E501

        self._is_required = is_required

    @property
    def value_added_services(self):
        """Gets the value_added_services of this AvailableValueAddedServiceGroup.  # noqa: E501

        A list of optional value-added services available for purchase with a shipping service offering.  # noqa: E501

        :return: The value_added_services of this AvailableValueAddedServiceGroup.  # noqa: E501
        :rtype: list[ValueAddedService]
        """
        return self._value_added_services

    @value_added_services.setter
    def value_added_services(self, value_added_services):
        """Sets the value_added_services of this AvailableValueAddedServiceGroup.

        A list of optional value-added services available for purchase with a shipping service offering.  # noqa: E501

        :param value_added_services: The value_added_services of this AvailableValueAddedServiceGroup.  # noqa: E501
        :type: list[ValueAddedService]
        """

        self._value_added_services = value_added_services

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
        if issubclass(AvailableValueAddedServiceGroup, dict):
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
        if not isinstance(other, AvailableValueAddedServiceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
