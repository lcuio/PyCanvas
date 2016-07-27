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


class Migrator(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, requires_file_upload=None, name=None, required_settings=None):
        """
        Migrator - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'requires_file_upload': 'bool',
            'name': 'str',
            'required_settings': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'requires_file_upload': 'requires_file_upload',
            'name': 'name',
            'required_settings': 'required_settings'
        }

        self._type = type
        self._requires_file_upload = requires_file_upload
        self._name = name
        self._required_settings = required_settings

    @property
    def type(self):
        """
        Gets the type of this Migrator.
        The value to pass to the create endpoint

        :return: The type of this Migrator.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Migrator.
        The value to pass to the create endpoint

        :param type: The type of this Migrator.
        :type: str
        """

        self._type = type

    @property
    def requires_file_upload(self):
        """
        Gets the requires_file_upload of this Migrator.
        Whether this endpoint requires a file upload

        :return: The requires_file_upload of this Migrator.
        :rtype: bool
        """
        return self._requires_file_upload

    @requires_file_upload.setter
    def requires_file_upload(self, requires_file_upload):
        """
        Sets the requires_file_upload of this Migrator.
        Whether this endpoint requires a file upload

        :param requires_file_upload: The requires_file_upload of this Migrator.
        :type: bool
        """

        self._requires_file_upload = requires_file_upload

    @property
    def name(self):
        """
        Gets the name of this Migrator.
        Description of the package type expected

        :return: The name of this Migrator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Migrator.
        Description of the package type expected

        :param name: The name of this Migrator.
        :type: str
        """

        self._name = name

    @property
    def required_settings(self):
        """
        Gets the required_settings of this Migrator.
        A list of fields this system requires

        :return: The required_settings of this Migrator.
        :rtype: list[str]
        """
        return self._required_settings

    @required_settings.setter
    def required_settings(self, required_settings):
        """
        Sets the required_settings of this Migrator.
        A list of fields this system requires

        :param required_settings: The required_settings of this Migrator.
        :type: list[str]
        """

        self._required_settings = required_settings

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