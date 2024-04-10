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

class GetRatesRequest(object):
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
        'ship_to': 'Address',
        'ship_from': 'Address',
        'return_to': 'Address',
        'ship_date': 'datetime',
        'shipper_instruction': 'ShipperInstruction',
        'packages': 'PackageList',
        'value_added_services': 'ValueAddedServiceDetails',
        'tax_details': 'TaxDetailList',
        'channel_details': 'ChannelDetails',
        'client_reference_details': 'ClientReferenceDetails',
        'shipment_type': 'ShipmentType',
        'destination_access_point_details': 'AccessPointDetails'
    }

    attribute_map = {
        'ship_to': 'shipTo',
        'ship_from': 'shipFrom',
        'return_to': 'returnTo',
        'ship_date': 'shipDate',
        'shipper_instruction': 'shipperInstruction',
        'packages': 'packages',
        'value_added_services': 'valueAddedServices',
        'tax_details': 'taxDetails',
        'channel_details': 'channelDetails',
        'client_reference_details': 'clientReferenceDetails',
        'shipment_type': 'shipmentType',
        'destination_access_point_details': 'destinationAccessPointDetails'
    }

    def __init__(self, ship_to=None, ship_from=None, return_to=None, ship_date=None, shipper_instruction=None, packages=None, value_added_services=None, tax_details=None, channel_details=None, client_reference_details=None, shipment_type=None, destination_access_point_details=None):  # noqa: E501
        """GetRatesRequest - a model defined in Swagger"""  # noqa: E501
        self._ship_to = None
        self._ship_from = None
        self._return_to = None
        self._ship_date = None
        self._shipper_instruction = None
        self._packages = None
        self._value_added_services = None
        self._tax_details = None
        self._channel_details = None
        self._client_reference_details = None
        self._shipment_type = None
        self._destination_access_point_details = None
        self.discriminator = None
        if ship_to is not None:
            self.ship_to = ship_to
        self.ship_from = ship_from
        if return_to is not None:
            self.return_to = return_to
        if ship_date is not None:
            self.ship_date = ship_date
        if shipper_instruction is not None:
            self.shipper_instruction = shipper_instruction
        self.packages = packages
        if value_added_services is not None:
            self.value_added_services = value_added_services
        if tax_details is not None:
            self.tax_details = tax_details
        self.channel_details = channel_details
        if client_reference_details is not None:
            self.client_reference_details = client_reference_details
        if shipment_type is not None:
            self.shipment_type = shipment_type
        if destination_access_point_details is not None:
            self.destination_access_point_details = destination_access_point_details

    @property
    def ship_to(self):
        """Gets the ship_to of this GetRatesRequest.  # noqa: E501


        :return: The ship_to of this GetRatesRequest.  # noqa: E501
        :rtype: Address
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """Sets the ship_to of this GetRatesRequest.


        :param ship_to: The ship_to of this GetRatesRequest.  # noqa: E501
        :type: Address
        """

        self._ship_to = ship_to

    @property
    def ship_from(self):
        """Gets the ship_from of this GetRatesRequest.  # noqa: E501


        :return: The ship_from of this GetRatesRequest.  # noqa: E501
        :rtype: Address
        """
        return self._ship_from

    @ship_from.setter
    def ship_from(self, ship_from):
        """Sets the ship_from of this GetRatesRequest.


        :param ship_from: The ship_from of this GetRatesRequest.  # noqa: E501
        :type: Address
        """
        if ship_from is None:
            raise ValueError("Invalid value for `ship_from`, must not be `None`")  # noqa: E501

        self._ship_from = ship_from

    @property
    def return_to(self):
        """Gets the return_to of this GetRatesRequest.  # noqa: E501


        :return: The return_to of this GetRatesRequest.  # noqa: E501
        :rtype: Address
        """
        return self._return_to

    @return_to.setter
    def return_to(self, return_to):
        """Sets the return_to of this GetRatesRequest.


        :param return_to: The return_to of this GetRatesRequest.  # noqa: E501
        :type: Address
        """

        self._return_to = return_to

    @property
    def ship_date(self):
        """Gets the ship_date of this GetRatesRequest.  # noqa: E501

        The ship date and time (the requested pickup). This defaults to the current date and time.  # noqa: E501

        :return: The ship_date of this GetRatesRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this GetRatesRequest.

        The ship date and time (the requested pickup). This defaults to the current date and time.  # noqa: E501

        :param ship_date: The ship_date of this GetRatesRequest.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def shipper_instruction(self):
        """Gets the shipper_instruction of this GetRatesRequest.  # noqa: E501


        :return: The shipper_instruction of this GetRatesRequest.  # noqa: E501
        :rtype: ShipperInstruction
        """
        return self._shipper_instruction

    @shipper_instruction.setter
    def shipper_instruction(self, shipper_instruction):
        """Sets the shipper_instruction of this GetRatesRequest.


        :param shipper_instruction: The shipper_instruction of this GetRatesRequest.  # noqa: E501
        :type: ShipperInstruction
        """

        self._shipper_instruction = shipper_instruction

    @property
    def packages(self):
        """Gets the packages of this GetRatesRequest.  # noqa: E501


        :return: The packages of this GetRatesRequest.  # noqa: E501
        :rtype: PackageList
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this GetRatesRequest.


        :param packages: The packages of this GetRatesRequest.  # noqa: E501
        :type: PackageList
        """
        if packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def value_added_services(self):
        """Gets the value_added_services of this GetRatesRequest.  # noqa: E501


        :return: The value_added_services of this GetRatesRequest.  # noqa: E501
        :rtype: ValueAddedServiceDetails
        """
        return self._value_added_services

    @value_added_services.setter
    def value_added_services(self, value_added_services):
        """Sets the value_added_services of this GetRatesRequest.


        :param value_added_services: The value_added_services of this GetRatesRequest.  # noqa: E501
        :type: ValueAddedServiceDetails
        """

        self._value_added_services = value_added_services

    @property
    def tax_details(self):
        """Gets the tax_details of this GetRatesRequest.  # noqa: E501


        :return: The tax_details of this GetRatesRequest.  # noqa: E501
        :rtype: TaxDetailList
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """Sets the tax_details of this GetRatesRequest.


        :param tax_details: The tax_details of this GetRatesRequest.  # noqa: E501
        :type: TaxDetailList
        """

        self._tax_details = tax_details

    @property
    def channel_details(self):
        """Gets the channel_details of this GetRatesRequest.  # noqa: E501


        :return: The channel_details of this GetRatesRequest.  # noqa: E501
        :rtype: ChannelDetails
        """
        return self._channel_details

    @channel_details.setter
    def channel_details(self, channel_details):
        """Sets the channel_details of this GetRatesRequest.


        :param channel_details: The channel_details of this GetRatesRequest.  # noqa: E501
        :type: ChannelDetails
        """
        if channel_details is None:
            raise ValueError("Invalid value for `channel_details`, must not be `None`")  # noqa: E501

        self._channel_details = channel_details

    @property
    def client_reference_details(self):
        """Gets the client_reference_details of this GetRatesRequest.  # noqa: E501


        :return: The client_reference_details of this GetRatesRequest.  # noqa: E501
        :rtype: ClientReferenceDetails
        """
        return self._client_reference_details

    @client_reference_details.setter
    def client_reference_details(self, client_reference_details):
        """Sets the client_reference_details of this GetRatesRequest.


        :param client_reference_details: The client_reference_details of this GetRatesRequest.  # noqa: E501
        :type: ClientReferenceDetails
        """

        self._client_reference_details = client_reference_details

    @property
    def shipment_type(self):
        """Gets the shipment_type of this GetRatesRequest.  # noqa: E501


        :return: The shipment_type of this GetRatesRequest.  # noqa: E501
        :rtype: ShipmentType
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this GetRatesRequest.


        :param shipment_type: The shipment_type of this GetRatesRequest.  # noqa: E501
        :type: ShipmentType
        """

        self._shipment_type = shipment_type

    @property
    def destination_access_point_details(self):
        """Gets the destination_access_point_details of this GetRatesRequest.  # noqa: E501


        :return: The destination_access_point_details of this GetRatesRequest.  # noqa: E501
        :rtype: AccessPointDetails
        """
        return self._destination_access_point_details

    @destination_access_point_details.setter
    def destination_access_point_details(self, destination_access_point_details):
        """Sets the destination_access_point_details of this GetRatesRequest.


        :param destination_access_point_details: The destination_access_point_details of this GetRatesRequest.  # noqa: E501
        :type: AccessPointDetails
        """

        self._destination_access_point_details = destination_access_point_details

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
        if issubclass(GetRatesRequest, dict):
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
        if not isinstance(other, GetRatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other