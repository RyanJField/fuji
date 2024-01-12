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

from swagger_client.models.fair_result_common import FAIRResultCommon


class IdentifierIncluded(FAIRResultCommon):
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
    swagger_types = {"output": "IdentifierIncludedOutput", "test_debug": "Debug"}
    if hasattr(FAIRResultCommon, "swagger_types"):
        swagger_types.update(FAIRResultCommon.swagger_types)

    attribute_map = {"output": "output", "test_debug": "test_debug"}
    if hasattr(FAIRResultCommon, "attribute_map"):
        attribute_map.update(FAIRResultCommon.attribute_map)

    def __init__(self, output=None, test_debug=None, *args, **kwargs):
        """IdentifierIncluded - a model defined in Swagger"""
        self._output = None
        self._test_debug = None
        self.discriminator = None
        if output is not None:
            self.output = output
        if test_debug is not None:
            self.test_debug = test_debug
        FAIRResultCommon.__init__(self, *args, **kwargs)

    @property
    def output(self):
        """Gets the output of this IdentifierIncluded.  # noqa: E501


        :return: The output of this IdentifierIncluded.  # noqa: E501
        :rtype: IdentifierIncludedOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this IdentifierIncluded.


        :param output: The output of this IdentifierIncluded.  # noqa: E501
        :type: IdentifierIncludedOutput
        """

        self._output = output

    @property
    def test_debug(self):
        """Gets the test_debug of this IdentifierIncluded.  # noqa: E501


        :return: The test_debug of this IdentifierIncluded.  # noqa: E501
        :rtype: Debug
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug):
        """Sets the test_debug of this IdentifierIncluded.


        :param test_debug: The test_debug of this IdentifierIncluded.  # noqa: E501
        :type: Debug
        """

        self._test_debug = test_debug

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
        if issubclass(IdentifierIncluded, dict):
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
        if not isinstance(other, IdentifierIncluded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
