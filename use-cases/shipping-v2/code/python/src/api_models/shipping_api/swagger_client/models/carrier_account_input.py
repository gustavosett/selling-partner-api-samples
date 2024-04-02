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

class CarrierAccountInput(object):
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
        'description_localization_key': 'str',
        'name': 'str',
        'group_name': 'str',
        'input_type': 'InputType',
        'is_mandatory': 'bool',
        'is_confidential': 'bool',
        'is_hidden': 'bool',
        'validation_metadata': 'ValidationMetadataList'
    }

    attribute_map = {
        'description_localization_key': 'descriptionLocalizationKey',
        'name': 'name',
        'group_name': 'groupName',
        'input_type': 'inputType',
        'is_mandatory': 'isMandatory',
        'is_confidential': 'isConfidential',
        'is_hidden': 'isHidden',
        'validation_metadata': 'validationMetadata'
    }

    def __init__(self, description_localization_key=None, name=None, group_name=None, input_type=None, is_mandatory=None, is_confidential=None, is_hidden=None, validation_metadata=None):  # noqa: E501
        """CarrierAccountInput - a model defined in Swagger"""  # noqa: E501
        self._description_localization_key = None
        self._name = None
        self._group_name = None
        self._input_type = None
        self._is_mandatory = None
        self._is_confidential = None
        self._is_hidden = None
        self._validation_metadata = None
        self.discriminator = None
        if description_localization_key is not None:
            self.description_localization_key = description_localization_key
        if name is not None:
            self.name = name
        if group_name is not None:
            self.group_name = group_name
        if input_type is not None:
            self.input_type = input_type
        if is_mandatory is not None:
            self.is_mandatory = is_mandatory
        if is_confidential is not None:
            self.is_confidential = is_confidential
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if validation_metadata is not None:
            self.validation_metadata = validation_metadata

    @property
    def description_localization_key(self):
        """Gets the description_localization_key of this CarrierAccountInput.  # noqa: E501

        descriptionLocalizationKey value .  # noqa: E501

        :return: The description_localization_key of this CarrierAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._description_localization_key

    @description_localization_key.setter
    def description_localization_key(self, description_localization_key):
        """Sets the description_localization_key of this CarrierAccountInput.

        descriptionLocalizationKey value .  # noqa: E501

        :param description_localization_key: The description_localization_key of this CarrierAccountInput.  # noqa: E501
        :type: str
        """

        self._description_localization_key = description_localization_key

    @property
    def name(self):
        """Gets the name of this CarrierAccountInput.  # noqa: E501

        name value .  # noqa: E501

        :return: The name of this CarrierAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierAccountInput.

        name value .  # noqa: E501

        :param name: The name of this CarrierAccountInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group_name(self):
        """Gets the group_name of this CarrierAccountInput.  # noqa: E501

        groupName value .  # noqa: E501

        :return: The group_name of this CarrierAccountInput.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CarrierAccountInput.

        groupName value .  # noqa: E501

        :param group_name: The group_name of this CarrierAccountInput.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def input_type(self):
        """Gets the input_type of this CarrierAccountInput.  # noqa: E501


        :return: The input_type of this CarrierAccountInput.  # noqa: E501
        :rtype: InputType
        """
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        """Sets the input_type of this CarrierAccountInput.


        :param input_type: The input_type of this CarrierAccountInput.  # noqa: E501
        :type: InputType
        """

        self._input_type = input_type

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this CarrierAccountInput.  # noqa: E501

        mandatory or not  value .  # noqa: E501

        :return: The is_mandatory of this CarrierAccountInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this CarrierAccountInput.

        mandatory or not  value .  # noqa: E501

        :param is_mandatory: The is_mandatory of this CarrierAccountInput.  # noqa: E501
        :type: bool
        """

        self._is_mandatory = is_mandatory

    @property
    def is_confidential(self):
        """Gets the is_confidential of this CarrierAccountInput.  # noqa: E501

        is value is Confidential .  # noqa: E501

        :return: The is_confidential of this CarrierAccountInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_confidential

    @is_confidential.setter
    def is_confidential(self, is_confidential):
        """Sets the is_confidential of this CarrierAccountInput.

        is value is Confidential .  # noqa: E501

        :param is_confidential: The is_confidential of this CarrierAccountInput.  # noqa: E501
        :type: bool
        """

        self._is_confidential = is_confidential

    @property
    def is_hidden(self):
        """Gets the is_hidden of this CarrierAccountInput.  # noqa: E501

        is value is hidden .  # noqa: E501

        :return: The is_hidden of this CarrierAccountInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this CarrierAccountInput.

        is value is hidden .  # noqa: E501

        :param is_hidden: The is_hidden of this CarrierAccountInput.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def validation_metadata(self):
        """Gets the validation_metadata of this CarrierAccountInput.  # noqa: E501


        :return: The validation_metadata of this CarrierAccountInput.  # noqa: E501
        :rtype: ValidationMetadataList
        """
        return self._validation_metadata

    @validation_metadata.setter
    def validation_metadata(self, validation_metadata):
        """Sets the validation_metadata of this CarrierAccountInput.


        :param validation_metadata: The validation_metadata of this CarrierAccountInput.  # noqa: E501
        :type: ValidationMetadataList
        """

        self._validation_metadata = validation_metadata

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
        if issubclass(CarrierAccountInput, dict):
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
        if not isinstance(other, CarrierAccountInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
