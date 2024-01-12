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


class DataContentMetadataOutputInner:
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
    swagger_types = {"descriptor": "str", "descriptor_value": "str", "matches_content": "bool"}

    attribute_map = {
        "descriptor": "descriptor",
        "descriptor_value": "descriptor_value",
        "matches_content": "matches_content",
    }

    def __init__(self, descriptor=None, descriptor_value=None, matches_content=False):
        """DataContentMetadataOutputInner - a model defined in Swagger"""
        self._descriptor = None
        self._descriptor_value = None
        self._matches_content = None
        self.discriminator = None
        if descriptor is not None:
            self.descriptor = descriptor
        if descriptor_value is not None:
            self.descriptor_value = descriptor_value
        if matches_content is not None:
            self.matches_content = matches_content

    @property
    def descriptor(self):
        """Gets the descriptor of this DataContentMetadataOutputInner.  # noqa: E501


        :return: The descriptor of this DataContentMetadataOutputInner.  # noqa: E501
        :rtype: str
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """Sets the descriptor of this DataContentMetadataOutputInner.


        :param descriptor: The descriptor of this DataContentMetadataOutputInner.  # noqa: E501
        :type: str
        """

        self._descriptor = descriptor

    @property
    def descriptor_value(self):
        """Gets the descriptor_value of this DataContentMetadataOutputInner.  # noqa: E501


        :return: The descriptor_value of this DataContentMetadataOutputInner.  # noqa: E501
        :rtype: str
        """
        return self._descriptor_value

    @descriptor_value.setter
    def descriptor_value(self, descriptor_value):
        """Sets the descriptor_value of this DataContentMetadataOutputInner.


        :param descriptor_value: The descriptor_value of this DataContentMetadataOutputInner.  # noqa: E501
        :type: str
        """

        self._descriptor_value = descriptor_value

    @property
    def matches_content(self):
        """Gets the matches_content of this DataContentMetadataOutputInner.  # noqa: E501


        :return: The matches_content of this DataContentMetadataOutputInner.  # noqa: E501
        :rtype: bool
        """
        return self._matches_content

    @matches_content.setter
    def matches_content(self, matches_content):
        """Sets the matches_content of this DataContentMetadataOutputInner.


        :param matches_content: The matches_content of this DataContentMetadataOutputInner.  # noqa: E501
        :type: bool
        """

        self._matches_content = matches_content

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
        if issubclass(DataContentMetadataOutputInner, dict):
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
        if not isinstance(other, DataContentMetadataOutputInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
