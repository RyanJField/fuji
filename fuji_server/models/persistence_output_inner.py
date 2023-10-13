from fuji_server import util
from fuji_server.models.base_model_ import Model


class PersistenceOutputInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        pid: str | None = None,
        pid_scheme: str | None = None,
        resolvable_status: bool = False,
        resolved_url: str | None = None,
    ):
        """PersistenceOutputInner - a model defined in Swagger

        :param pid: The pid of this PersistenceOutputInner.  # noqa: E501
        :type pid: str
        :param pid_scheme: The pid_scheme of this PersistenceOutputInner.  # noqa: E501
        :type pid_scheme: str
        :param resolvable_status: The resolvable_status of this PersistenceOutputInner.  # noqa: E501
        :type resolvable_status: bool
        :param resolved_url: The resolved_url of this PersistenceOutputInner.  # noqa: E501
        :type resolved_url: str
        """
        self.swagger_types = {"pid": str, "pid_scheme": str, "resolvable_status": bool, "resolved_url": str}

        self.attribute_map = {
            "pid": "pid",
            "pid_scheme": "pid_scheme",
            "resolvable_status": "resolvable_status",
            "resolved_url": "resolved_url",
        }
        self._pid = pid
        self._pid_scheme = pid_scheme
        self._resolvable_status = resolvable_status
        self._resolved_url = resolved_url

    @classmethod
    def from_dict(cls, dikt) -> "PersistenceOutputInner":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Persistence_output_inner of this PersistenceOutputInner.  # noqa: E501
        :rtype: PersistenceOutputInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pid(self) -> str:
        """Gets the pid of this PersistenceOutputInner.


        :return: The pid of this PersistenceOutputInner.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid: str):
        """Sets the pid of this PersistenceOutputInner.


        :param pid: The pid of this PersistenceOutputInner.
        :type pid: str
        """

        self._pid = pid

    @property
    def pid_scheme(self) -> str:
        """Gets the pid_scheme of this PersistenceOutputInner.


        :return: The pid_scheme of this PersistenceOutputInner.
        :rtype: str
        """
        return self._pid_scheme

    @pid_scheme.setter
    def pid_scheme(self, pid_scheme: str):
        """Sets the pid_scheme of this PersistenceOutputInner.


        :param pid_scheme: The pid_scheme of this PersistenceOutputInner.
        :type pid_scheme: str
        """

        self._pid_scheme = pid_scheme

    @property
    def resolvable_status(self) -> bool:
        """Gets the resolvable_status of this PersistenceOutputInner.


        :return: The resolvable_status of this PersistenceOutputInner.
        :rtype: bool
        """
        return self._resolvable_status

    @resolvable_status.setter
    def resolvable_status(self, resolvable_status: bool):
        """Sets the resolvable_status of this PersistenceOutputInner.


        :param resolvable_status: The resolvable_status of this PersistenceOutputInner.
        :type resolvable_status: bool
        """

        self._resolvable_status = resolvable_status

    @property
    def resolved_url(self) -> str:
        """Gets the resolved_url of this PersistenceOutputInner.


        :return: The resolved_url of this PersistenceOutputInner.
        :rtype: str
        """
        return self._resolved_url

    @resolved_url.setter
    def resolved_url(self, resolved_url: str):
        """Sets the resolved_url of this PersistenceOutputInner.


        :param resolved_url: The resolved_url of this PersistenceOutputInner.
        :type resolved_url: str
        """

        self._resolved_url = resolved_url
