# -*- coding: utf-8 -*-
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model repository."""

from typing import List, Type

from neural_insights.components.model.model import Model
from neural_insights.components.model.onnxrt.model import OnnxrtModel
from neural_insights.components.model.pytorch.model import PyTorchScriptModel
from neural_insights.components.model.tensorflow.frozen_pb import FrozenPbModel
from neural_insights.components.model.tensorflow.keras import KerasModel
from neural_insights.components.model.tensorflow.meta_graph import MetaGraphModel
from neural_insights.components.model.tensorflow.saved_model import SavedModelModel
from neural_insights.utils.exceptions import NotFoundException
from neural_insights.utils.logger import log


class ModelRepository:
    """Model repository."""

    def __init__(self) -> None:
        """Initialize class."""
        self.model_types: List[Type[Model]] = [
            FrozenPbModel,
            KerasModel,
            MetaGraphModel,
            OnnxrtModel,
            SavedModelModel,
            PyTorchScriptModel,
        ]

    def get_model(self, path: str) -> Model:
        """Get Model for given path."""
        for model_type in self.model_types:
            supports_path = model_type.supports_path(path)
            log.debug(f"{model_type.__name__}: {supports_path}")
            if model_type.supports_path(path):
                return model_type(path)

        raise NotFoundException(f"Unable to find Model for path {path}")

    def get_frameworks(self) -> List[str]:
        """Get list of supported frameworks."""
        unique_frameworks = {model.get_framework_name() for model in self.model_types}
        return sorted(unique_frameworks)

    @staticmethod
    def get_framework_from_path(model_path: str) -> str:
        """Get framework name from model extension.

        :param model_path: Path to model.
        """
        model_repository = ModelRepository()
        try:
            model = model_repository.get_model(model_path)
            return model.get_framework_name()
        except NotFoundException:
            raise NotFoundException("Framework was not recognized.")

    @staticmethod
    def get_supported_frameworks() -> List[str]:
        """Get list of supported frameworks."""
        return ModelRepository().get_frameworks()

    @staticmethod
    def is_model_path(path: str) -> bool:
        """Check if provided path is for model."""
        try:
            ModelRepository().get_model(path)
            return True
        except NotFoundException:
            return False
