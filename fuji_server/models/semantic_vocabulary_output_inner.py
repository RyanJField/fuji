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


class SemanticVocabularyOutputInner:
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
    swagger_types = {"namespace": "str", "is_namespace_active": "bool"}

    attribute_map = {"namespace": "namespace", "is_namespace_active": "is_namespace_active"}

    def __init__(self, namespace=None, is_namespace_active=False):
        """SemanticVocabularyOutputInner - a model defined in Swagger"""
        self._namespace = None
        self._is_namespace_active = None
        self.discriminator = None
        if namespace is not None:
            self.namespace = namespace
        if is_namespace_active is not None:
            self.is_namespace_active = is_namespace_active

    @property
    def namespace(self):
        """Gets the namespace of this SemanticVocabularyOutputInner.  # noqa: E501


        :return: The namespace of this SemanticVocabularyOutputInner.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SemanticVocabularyOutputInner.


        :param namespace: The namespace of this SemanticVocabularyOutputInner.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def is_namespace_active(self):
        """Gets the is_namespace_active of this SemanticVocabularyOutputInner.  # noqa: E501


        :return: The is_namespace_active of this SemanticVocabularyOutputInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_namespace_active

    @is_namespace_active.setter
    def is_namespace_active(self, is_namespace_active):
        """Sets the is_namespace_active of this SemanticVocabularyOutputInner.


        :param is_namespace_active: The is_namespace_active of this SemanticVocabularyOutputInner.  # noqa: E501
        :type: bool
        """

        self._is_namespace_active = is_namespace_active

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
        if issubclass(SemanticVocabularyOutputInner, dict):
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
        if not isinstance(other, SemanticVocabularyOutputInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
