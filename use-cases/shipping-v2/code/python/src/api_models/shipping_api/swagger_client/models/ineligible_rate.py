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

class IneligibleRate(object):
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
        'service_id': 'ServiceId',
        'service_name': 'ServiceName',
        'carrier_name': 'CarrierName',
        'carrier_id': 'CarrierId',
        'ineligibility_reasons': 'list[IneligibilityReason]'
    }

    attribute_map = {
        'service_id': 'serviceId',
        'service_name': 'serviceName',
        'carrier_name': 'carrierName',
        'carrier_id': 'carrierId',
        'ineligibility_reasons': 'ineligibilityReasons'
    }

    def __init__(self, service_id=None, service_name=None, carrier_name=None, carrier_id=None, ineligibility_reasons=None):  # noqa: E501
        """IneligibleRate - a model defined in Swagger"""  # noqa: E501
        self._service_id = None
        self._service_name = None
        self._carrier_name = None
        self._carrier_id = None
        self._ineligibility_reasons = None
        self.discriminator = None
        self.service_id = service_id
        self.service_name = service_name
        self.carrier_name = carrier_name
        self.carrier_id = carrier_id
        self.ineligibility_reasons = ineligibility_reasons

    @property
    def service_id(self):
        """Gets the service_id of this IneligibleRate.  # noqa: E501


        :return: The service_id of this IneligibleRate.  # noqa: E501
        :rtype: ServiceId
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this IneligibleRate.


        :param service_id: The service_id of this IneligibleRate.  # noqa: E501
        :type: ServiceId
        """
        if service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def service_name(self):
        """Gets the service_name of this IneligibleRate.  # noqa: E501


        :return: The service_name of this IneligibleRate.  # noqa: E501
        :rtype: ServiceName
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this IneligibleRate.


        :param service_name: The service_name of this IneligibleRate.  # noqa: E501
        :type: ServiceName
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

    @property
    def carrier_name(self):
        """Gets the carrier_name of this IneligibleRate.  # noqa: E501


        :return: The carrier_name of this IneligibleRate.  # noqa: E501
        :rtype: CarrierName
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this IneligibleRate.


        :param carrier_name: The carrier_name of this IneligibleRate.  # noqa: E501
        :type: CarrierName
        """
        if carrier_name is None:
            raise ValueError("Invalid value for `carrier_name`, must not be `None`")  # noqa: E501

        self._carrier_name = carrier_name

    @property
    def carrier_id(self):
        """Gets the carrier_id of this IneligibleRate.  # noqa: E501


        :return: The carrier_id of this IneligibleRate.  # noqa: E501
        :rtype: CarrierId
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this IneligibleRate.


        :param carrier_id: The carrier_id of this IneligibleRate.  # noqa: E501
        :type: CarrierId
        """
        if carrier_id is None:
            raise ValueError("Invalid value for `carrier_id`, must not be `None`")  # noqa: E501

        self._carrier_id = carrier_id

    @property
    def ineligibility_reasons(self):
        """Gets the ineligibility_reasons of this IneligibleRate.  # noqa: E501

        A list of reasons why a shipping service offering is ineligible.  # noqa: E501

        :return: The ineligibility_reasons of this IneligibleRate.  # noqa: E501
        :rtype: list[IneligibilityReason]
        """
        return self._ineligibility_reasons

    @ineligibility_reasons.setter
    def ineligibility_reasons(self, ineligibility_reasons):
        """Sets the ineligibility_reasons of this IneligibleRate.

        A list of reasons why a shipping service offering is ineligible.  # noqa: E501

        :param ineligibility_reasons: The ineligibility_reasons of this IneligibleRate.  # noqa: E501
        :type: list[IneligibilityReason]
        """
        if ineligibility_reasons is None:
            raise ValueError("Invalid value for `ineligibility_reasons`, must not be `None`")  # noqa: E501

        self._ineligibility_reasons = ineligibility_reasons

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
        if issubclass(IneligibleRate, dict):
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
        if not isinstance(other, IneligibleRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
