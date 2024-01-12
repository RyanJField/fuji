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


class DataContentMetadataOutput:
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
    swagger_types = {"object_type": "str", "data_content_descriptor": "list[DataContentMetadataOutputInner]"}

    attribute_map = {"object_type": "object_type", "data_content_descriptor": "data_content_descriptor"}

    def __init__(self, object_type=None, data_content_descriptor=None):
        """DataContentMetadataOutput - a model defined in Swagger"""
        self._object_type = None
        self._data_content_descriptor = None
        self.discriminator = None
        if object_type is not None:
            self.object_type = object_type
        if data_content_descriptor is not None:
            self.data_content_descriptor = data_content_descriptor

    @property
    def object_type(self):
        """Gets the object_type of this DataContentMetadataOutput.  # noqa: E501


        :return: The object_type of this DataContentMetadataOutput.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DataContentMetadataOutput.


        :param object_type: The object_type of this DataContentMetadataOutput.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def data_content_descriptor(self):
        """Gets the data_content_descriptor of this DataContentMetadataOutput.  # noqa: E501


        :return: The data_content_descriptor of this DataContentMetadataOutput.  # noqa: E501
        :rtype: list[DataContentMetadataOutputInner]
        """
        return self._data_content_descriptor

    @data_content_descriptor.setter
    def data_content_descriptor(self, data_content_descriptor):
        """Sets the data_content_descriptor of this DataContentMetadataOutput.


        :param data_content_descriptor: The data_content_descriptor of this DataContentMetadataOutput.  # noqa: E501
        :type: list[DataContentMetadataOutputInner]
        """

        self._data_content_descriptor = data_content_descriptor

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
        if issubclass(DataContentMetadataOutput, dict):
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
        if not isinstance(other, DataContentMetadataOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
