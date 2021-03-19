# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server.models.debug import Debug  # noqa: F401,E501
from fuji_server.models.fair_result_common import FAIRResultCommon  # noqa: F401,E501
from fuji_server.models.fair_result_common_score import FAIRResultCommonScore  # noqa: F401,E501
from fuji_server.models.fair_result_evaluation_criterium import FAIRResultEvaluationCriterium  # noqa: F401,E501
from fuji_server.models.metadata_preserved_output import MetadataPreservedOutput  # noqa: F401,E501
from fuji_server import util


class MetadataPreserved(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, metric_identifier: str=None, metric_name: str=None, metric_tests: Dict[str, FAIRResultEvaluationCriterium]=None, test_status: str='fail', score: FAIRResultCommonScore=None, maturity: str='incomplete', output: MetadataPreservedOutput=None, test_debug: Debug=None):  # noqa: E501
        """MetadataPreserved - a model defined in Swagger

        :param id: The id of this MetadataPreserved.  # noqa: E501
        :type id: int
        :param metric_identifier: The metric_identifier of this MetadataPreserved.  # noqa: E501
        :type metric_identifier: str
        :param metric_name: The metric_name of this MetadataPreserved.  # noqa: E501
        :type metric_name: str
        :param metric_tests: The metric_tests of this MetadataPreserved.  # noqa: E501
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        :param test_status: The test_status of this MetadataPreserved.  # noqa: E501
        :type test_status: str
        :param score: The score of this MetadataPreserved.  # noqa: E501
        :type score: FAIRResultCommonScore
        :param maturity: The maturity of this MetadataPreserved.  # noqa: E501
        :type maturity: str
        :param output: The output of this MetadataPreserved.  # noqa: E501
        :type output: MetadataPreservedOutput
        :param test_debug: The test_debug of this MetadataPreserved.  # noqa: E501
        :type test_debug: Debug
        """
        self.swagger_types = {
            'id': int,
            'metric_identifier': str,
            'metric_name': str,
            'metric_tests': Dict[str, FAIRResultEvaluationCriterium],
            'test_status': str,
            'score': FAIRResultCommonScore,
            'maturity': str,
            'output': MetadataPreservedOutput,
            'test_debug': Debug
        }

        self.attribute_map = {
            'id': 'id',
            'metric_identifier': 'metric_identifier',
            'metric_name': 'metric_name',
            'metric_tests': 'metric_tests',
            'test_status': 'test_status',
            'score': 'score',
            'maturity': 'maturity',
            'output': 'output',
            'test_debug': 'test_debug'
        }
        self._id = id
        self._metric_identifier = metric_identifier
        self._metric_name = metric_name
        self._metric_tests = metric_tests
        self._test_status = test_status
        self._score = score
        self._maturity = maturity
        self._output = output
        self._test_debug = test_debug

    @classmethod
    def from_dict(cls, dikt) -> 'MetadataPreserved':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MetadataPreserved of this MetadataPreserved.  # noqa: E501
        :rtype: MetadataPreserved
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this MetadataPreserved.


        :return: The id of this MetadataPreserved.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this MetadataPreserved.


        :param id: The id of this MetadataPreserved.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metric_identifier(self) -> str:
        """Gets the metric_identifier of this MetadataPreserved.


        :return: The metric_identifier of this MetadataPreserved.
        :rtype: str
        """
        return self._metric_identifier

    @metric_identifier.setter
    def metric_identifier(self, metric_identifier: str):
        """Sets the metric_identifier of this MetadataPreserved.


        :param metric_identifier: The metric_identifier of this MetadataPreserved.
        :type metric_identifier: str
        """
        if metric_identifier is None:
            raise ValueError("Invalid value for `metric_identifier`, must not be `None`")  # noqa: E501

        self._metric_identifier = metric_identifier

    @property
    def metric_name(self) -> str:
        """Gets the metric_name of this MetadataPreserved.


        :return: The metric_name of this MetadataPreserved.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
        """Sets the metric_name of this MetadataPreserved.


        :param metric_name: The metric_name of this MetadataPreserved.
        :type metric_name: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def metric_tests(self) -> Dict[str, FAIRResultEvaluationCriterium]:
        """Gets the metric_tests of this MetadataPreserved.


        :return: The metric_tests of this MetadataPreserved.
        :rtype: Dict[str, FAIRResultEvaluationCriterium]
        """
        return self._metric_tests

    @metric_tests.setter
    def metric_tests(self, metric_tests: Dict[str, FAIRResultEvaluationCriterium]):
        """Sets the metric_tests of this MetadataPreserved.


        :param metric_tests: The metric_tests of this MetadataPreserved.
        :type metric_tests: Dict[str, FAIRResultEvaluationCriterium]
        """

        self._metric_tests = metric_tests

    @property
    def test_status(self) -> str:
        """Gets the test_status of this MetadataPreserved.


        :return: The test_status of this MetadataPreserved.
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status: str):
        """Sets the test_status of this MetadataPreserved.


        :param test_status: The test_status of this MetadataPreserved.
        :type test_status: str
        """
        allowed_values = ["pass", "fail", "indeterminate"]  # noqa: E501
        if test_status not in allowed_values:
            raise ValueError(
                "Invalid value for `test_status` ({0}), must be one of {1}"
                .format(test_status, allowed_values)
            )

        self._test_status = test_status

    @property
    def score(self) -> FAIRResultCommonScore:
        """Gets the score of this MetadataPreserved.


        :return: The score of this MetadataPreserved.
        :rtype: FAIRResultCommonScore
        """
        return self._score

    @score.setter
    def score(self, score: FAIRResultCommonScore):
        """Sets the score of this MetadataPreserved.


        :param score: The score of this MetadataPreserved.
        :type score: FAIRResultCommonScore
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def maturity(self) -> str:
        """Gets the maturity of this MetadataPreserved.


        :return: The maturity of this MetadataPreserved.
        :rtype: str
        """
        return self._maturity

    @maturity.setter
    def maturity(self, maturity: str):
        """Sets the maturity of this MetadataPreserved.


        :param maturity: The maturity of this MetadataPreserved.
        :type maturity: str
        """
        allowed_values = ["incomplete", "initial", "managed", "defined", "quantitatively managed", "optimizing"]  # noqa: E501
        if maturity not in allowed_values:
            raise ValueError(
                "Invalid value for `maturity` ({0}), must be one of {1}"
                .format(maturity, allowed_values)
            )

        self._maturity = maturity

    @property
    def output(self) -> MetadataPreservedOutput:
        """Gets the output of this MetadataPreserved.


        :return: The output of this MetadataPreserved.
        :rtype: MetadataPreservedOutput
        """
        return self._output

    @output.setter
    def output(self, output: MetadataPreservedOutput):
        """Sets the output of this MetadataPreserved.


        :param output: The output of this MetadataPreserved.
        :type output: MetadataPreservedOutput
        """

        self._output = output

    @property
    def test_debug(self) -> Debug:
        """Gets the test_debug of this MetadataPreserved.


        :return: The test_debug of this MetadataPreserved.
        :rtype: Debug
        """
        return self._test_debug

    @test_debug.setter
    def test_debug(self, test_debug: Debug):
        """Sets the test_debug of this MetadataPreserved.


        :param test_debug: The test_debug of this MetadataPreserved.
        :type test_debug: Debug
        """

        self._test_debug = test_debug
