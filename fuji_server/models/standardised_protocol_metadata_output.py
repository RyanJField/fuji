"""
    F-UJI

    A Service for Evaluating Research Data Objects Based on <a href ='https://doi.org/10.5281/zenodo.3775793'>FAIRsFAIR Metrics</a>. <p> This work was supported by the <a href='https://www.fairsfair.eu/'>FAIRsFAIR</a> project (H2020-INFRAEOSC-2018-2020 Grant Agreement 831558).  # noqa: E501

    OpenAPI spec version: 3.0.1
    Contact: anusuriya.devaraju@googlemail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class StandardisedProtocolMetadataOutput:
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
    swagger_types = {"standard_metadata_protocol": "str"}

    attribute_map = {"standard_metadata_protocol": "standard_metadata_protocol"}

    def __init__(self, standard_metadata_protocol=None):
        """StandardisedProtocolMetadataOutput - a model defined in Swagger"""
        self._standard_metadata_protocol = None
        self.discriminator = None
        if standard_metadata_protocol is not None:
            self.standard_metadata_protocol = standard_metadata_protocol

    @property
    def standard_metadata_protocol(self):
        """Gets the standard_metadata_protocol of this StandardisedProtocolMetadataOutput.  # noqa: E501


        :return: The standard_metadata_protocol of this StandardisedProtocolMetadataOutput.  # noqa: E501
        :rtype: str
        """
        return self._standard_metadata_protocol

    @standard_metadata_protocol.setter
    def standard_metadata_protocol(self, standard_metadata_protocol):
        """Sets the standard_metadata_protocol of this StandardisedProtocolMetadataOutput.


        :param standard_metadata_protocol: The standard_metadata_protocol of this StandardisedProtocolMetadataOutput.  # noqa: E501
        :type: str
        """

        self._standard_metadata_protocol = standard_metadata_protocol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(StandardisedProtocolMetadataOutput, dict):
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
        if not isinstance(other, StandardisedProtocolMetadataOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
