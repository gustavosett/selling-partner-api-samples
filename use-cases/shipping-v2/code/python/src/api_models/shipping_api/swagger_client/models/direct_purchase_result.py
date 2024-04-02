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

class DirectPurchaseResult(object):
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
        'shipment_id': 'ShipmentId',
        'package_document_detail_list': 'PackageDocumentDetailList'
    }

    attribute_map = {
        'shipment_id': 'shipmentId',
        'package_document_detail_list': 'packageDocumentDetailList'
    }

    def __init__(self, shipment_id=None, package_document_detail_list=None):  # noqa: E501
        """DirectPurchaseResult - a model defined in Swagger"""  # noqa: E501
        self._shipment_id = None
        self._package_document_detail_list = None
        self.discriminator = None
        self.shipment_id = shipment_id
        if package_document_detail_list is not None:
            self.package_document_detail_list = package_document_detail_list

    @property
    def shipment_id(self):
        """Gets the shipment_id of this DirectPurchaseResult.  # noqa: E501


        :return: The shipment_id of this DirectPurchaseResult.  # noqa: E501
        :rtype: ShipmentId
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this DirectPurchaseResult.


        :param shipment_id: The shipment_id of this DirectPurchaseResult.  # noqa: E501
        :type: ShipmentId
        """
        if shipment_id is None:
            raise ValueError("Invalid value for `shipment_id`, must not be `None`")  # noqa: E501

        self._shipment_id = shipment_id

    @property
    def package_document_detail_list(self):
        """Gets the package_document_detail_list of this DirectPurchaseResult.  # noqa: E501


        :return: The package_document_detail_list of this DirectPurchaseResult.  # noqa: E501
        :rtype: PackageDocumentDetailList
        """
        return self._package_document_detail_list

    @package_document_detail_list.setter
    def package_document_detail_list(self, package_document_detail_list):
        """Sets the package_document_detail_list of this DirectPurchaseResult.


        :param package_document_detail_list: The package_document_detail_list of this DirectPurchaseResult.  # noqa: E501
        :type: PackageDocumentDetailList
        """

        self._package_document_detail_list = package_document_detail_list

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
        if issubclass(DirectPurchaseResult, dict):
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
        if not isinstance(other, DirectPurchaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
