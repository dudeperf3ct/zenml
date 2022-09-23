#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""AzureML step operator flavor."""

from typing import TYPE_CHECKING, Optional, Type

from zenml.integrations.azure import AZUREML_STEP_OPERATOR_FLAVOR
from zenml.step_operators.base_step_operator import (
    BaseStepOperatorConfig,
    BaseStepOperatorFlavor,
)
from zenml.utils import deprecation_utils
from zenml.utils.secret_utils import SecretField

if TYPE_CHECKING:
    from zenml.integrations.azure.step_operators import AzureMLStepOperator


class AzureMLStepOperatorConfig(BaseStepOperatorConfig):
    """Config for the AzureML step operator.

    Attributes:
        subscription_id: The Azure account's subscription ID
        resource_group: The resource group to which the AzureML workspace
            is deployed.
        workspace_name: The name of the AzureML Workspace.
        compute_target_name: The name of the configured ComputeTarget.
            An instance of it has to be created on the portal if it doesn't
            exist already.
        environment_name: The name of the environment if there
            already exists one.
        docker_base_image: The custom docker base image that the
            environment should use.
        tenant_id: The Azure Tenant ID.
        service_principal_id: The ID for the service principal that is created
            to allow apps to access secure resources.
        service_principal_password: Password for the service principal.
    """

    subscription_id: str
    resource_group: str
    workspace_name: str
    compute_target_name: str

    # Environment
    environment_name: Optional[str] = None
    docker_base_image: Optional[str] = None

    # Service principal authentication
    # https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication#configure-a-service-principal
    tenant_id: Optional[str] = SecretField()
    service_principal_id: Optional[str] = SecretField()
    service_principal_password: Optional[str] = SecretField()

    docker_parent_image: Optional[str] = None

    _deprecation_validator = deprecation_utils.deprecate_pydantic_attributes(
        "custom_docker_base_image_name", "docker_parent_image"
    )


class AzureMLStepOperatorFlavor(BaseStepOperatorFlavor):
    """Flavor for the AzureML step operator."""

    @property
    def name(self) -> str:
        """Name of the flavor.

        Returns:
            The name of the flavor.
        """
        return AZUREML_STEP_OPERATOR_FLAVOR

    @property
    def config_class(self) -> Type[AzureMLStepOperatorConfig]:
        """Returns AzureMLStepOperatorConfig config class.

        Returns:
                The config class.
        """
        return AzureMLStepOperatorConfig

    @property
    def implementation_class(self) -> Type["AzureMLStepOperator"]:
        """Implementation class.

        Returns:
            The implementation class.
        """
        from zenml.integrations.azure.step_operators import AzureMLStepOperator

        return AzureMLStepOperator