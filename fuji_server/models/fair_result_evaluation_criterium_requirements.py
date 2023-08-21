# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class FAIRResultEvaluationCriteriumRequirements(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, target: str=None, modality: str=None, required: List[str]=None, tested_on: str=None, comment: str=None):  # noqa: E501
        """FAIRResultEvaluationCriteriumRequirements - a model defined in Swagger

        :param target: The target of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :type target: str
        :param modality: The modality of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :type modality: str
        :param required: The required of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :type required: List[str]
        :param tested_on: The tested_on of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :type tested_on: str
        :param comment: The comment of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :type comment: str
        """
        self.swagger_types = {
            'target': str,
            'modality': str,
            'required': List[str],
            'tested_on': str,
            'comment': str
        }

        self.attribute_map = {
            'target': 'target',
            'modality': 'modality',
            'required': 'required',
            'tested_on': 'tested_on',
            'comment': 'comment'
        }
        self._target = target
        self._modality = modality
        self._required = required
        self._tested_on = tested_on
        self._comment = comment

    @classmethod
    def from_dict(cls, dikt) -> 'FAIRResultEvaluationCriteriumRequirements':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FAIRResultEvaluationCriteriumRequirements of this FAIRResultEvaluationCriteriumRequirements.  # noqa: E501
        :rtype: FAIRResultEvaluationCriteriumRequirements
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target(self) -> str:
        """Gets the target of this FAIRResultEvaluationCriteriumRequirements.


        :return: The target of this FAIRResultEvaluationCriteriumRequirements.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target: str):
        """Sets the target of this FAIRResultEvaluationCriteriumRequirements.


        :param target: The target of this FAIRResultEvaluationCriteriumRequirements.
        :type target: str
        """

        self._target = target

    @property
    def modality(self) -> str:
        """Gets the modality of this FAIRResultEvaluationCriteriumRequirements.


        :return: The modality of this FAIRResultEvaluationCriteriumRequirements.
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality: str):
        """Sets the modality of this FAIRResultEvaluationCriteriumRequirements.


        :param modality: The modality of this FAIRResultEvaluationCriteriumRequirements.
        :type modality: str
        """

        self._modality = modality

    @property
    def required(self) -> List[str]:
        """Gets the required of this FAIRResultEvaluationCriteriumRequirements.


        :return: The required of this FAIRResultEvaluationCriteriumRequirements.
        :rtype: List[str]
        """
        return self._required

    @required.setter
    def required(self, required: List[str]):
        """Sets the required of this FAIRResultEvaluationCriteriumRequirements.


        :param required: The required of this FAIRResultEvaluationCriteriumRequirements.
        :type required: List[str]
        """

        self._required = required

    @property
    def tested_on(self) -> str:
        """Gets the tested_on of this FAIRResultEvaluationCriteriumRequirements.


        :return: The tested_on of this FAIRResultEvaluationCriteriumRequirements.
        :rtype: str
        """
        return self._tested_on

    @tested_on.setter
    def tested_on(self, tested_on: str):
        """Sets the tested_on of this FAIRResultEvaluationCriteriumRequirements.


        :param tested_on: The tested_on of this FAIRResultEvaluationCriteriumRequirements.
        :type tested_on: str
        """

        self._tested_on = tested_on

    @property
    def comment(self) -> str:
        """Gets the comment of this FAIRResultEvaluationCriteriumRequirements.


        :return: The comment of this FAIRResultEvaluationCriteriumRequirements.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment: str):
        """Sets the comment of this FAIRResultEvaluationCriteriumRequirements.


        :param comment: The comment of this FAIRResultEvaluationCriteriumRequirements.
        :type comment: str
        """

        self._comment = comment
