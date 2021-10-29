#  Copyright (c) ZenML GmbH 2021. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
from zenml.integrations.registry import integration_registry
from zenml.logger import get_logger
from zenml.utils.source_utils import LazyLoader

logger = get_logger(__name__)

# Google Cloud Platform
gcp = LazyLoader("zenml.integrations.gcp.integration")
integration_registry.register_integration("gcp", gcp)

# Tensorflow
tensorflow = LazyLoader("zenml.integrations.tensorflow")
integration_registry.register_integration("tensorflow", tensorflow)

# sklearn
sklearn = LazyLoader("zenml.integrations.sklearn")
integration_registry.register_integration("sklearn", sklearn)

# Beam
beam = LazyLoader("zenml.integrations.beam")
integration_registry.register_integration("beam", beam)

# Pytorch
pytorch = LazyLoader("zenml.integrations.pytorch")
integration_registry.register_integration("pytorch", pytorch)

# Pytorch Lightning
pytorch_lightning = LazyLoader("zenml.integrations.pytorch_lightning")
integration_registry.register_integration(
    "pytorch_lightning", pytorch_lightning
)
