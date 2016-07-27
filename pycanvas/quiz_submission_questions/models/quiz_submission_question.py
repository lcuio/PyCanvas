# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from ...base_model import BaseModel
from pprint import pformat
from six import iteritems
import re


class QuizSubmissionQuestion(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, flagged=None, answer=None):
        """
        QuizSubmissionQuestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'flagged': 'bool',
            'answer': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'flagged': 'flagged',
            'answer': 'answer'
        }

        self._id = id
        self._flagged = flagged
        self._answer = answer

    @property
    def id(self):
        """
        Gets the id of this QuizSubmissionQuestion.
        The ID of the QuizQuestion this answer is for.

        :return: The id of this QuizSubmissionQuestion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QuizSubmissionQuestion.
        The ID of the QuizQuestion this answer is for.

        :param id: The id of this QuizSubmissionQuestion.
        :type: int
        """

        self._id = id

    @property
    def flagged(self):
        """
        Gets the flagged of this QuizSubmissionQuestion.
        Whether this question is flagged.

        :return: The flagged of this QuizSubmissionQuestion.
        :rtype: bool
        """
        return self._flagged

    @flagged.setter
    def flagged(self, flagged):
        """
        Sets the flagged of this QuizSubmissionQuestion.
        Whether this question is flagged.

        :param flagged: The flagged of this QuizSubmissionQuestion.
        :type: bool
        """

        self._flagged = flagged

    @property
    def answer(self):
        """
        Gets the answer of this QuizSubmissionQuestion.
        The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information.

        :return: The answer of this QuizSubmissionQuestion.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """
        Sets the answer of this QuizSubmissionQuestion.
        The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information.

        :param answer: The answer of this QuizSubmissionQuestion.
        :type: str
        """

        self._answer = answer

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other