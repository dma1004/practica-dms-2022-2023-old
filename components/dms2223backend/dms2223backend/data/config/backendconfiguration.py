from typing import Dict

from dms2223common.data.config import ServiceConfiguration


class BackendConfiguration(ServiceConfiguration):
    """ Class responsible of storing a specific authentication service configuration.
    """

    def _component_name(self) -> str:
        """ The component name, to categorize the default config path.

        Returns:
            - str: A string identifying the component which will categorize the configuration.
        """

        return 'dms2223backend'

    def __init__(self):
        """ Initialization/constructor method.
        """

        ServiceConfiguration.__init__(self)

        self.set_authorized_api_keys([])

    def _set_values(self, values: Dict) -> None:
        """Sets/merges a collection of configuration values.

        Args:
            - values (Dict): A dictionary of configuration values.
        """
        ServiceConfiguration._set_values(self, values)

        if 'auth_service' in values:
            self.set_auth_service(values['auth_service'])

    def set_auth_service(self, auth_service: Dict) -> None:
        """Sets the connection parameters for the authentication service.

        Args:
            auth_service (Dict): Parameters to connect to the authentication service.

        Raises:
            - ValueError: If validation is not passed.
        """
        self._values['auth_service'] = auth_service

    def get_auth_service(self) -> Dict:
        """ Gets the authentication service configuration value.

        Returns:
            - Dict: A dictionary with the value of auth_service.
        """

        return self._values['auth_service']
