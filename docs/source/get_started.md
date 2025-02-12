# Getting Started

1. [Quick Samples](#quick-samples)

2. [Validated Models](#validated-models)

## Quick Samples
### Quantization with Python API

```shell
# Install Intel Neural Compressor and TensorFlow
pip install neural-compressor
pip install tensorflow
# Prepare fp32 model
wget https://storage.googleapis.com/intel-optimized-tensorflow/models/v1_6/mobilenet_v1_1.0_224_frozen.pb
```
```python
from neural_compressor.config import PostTrainingQuantConfig
from neural_compressor.data import DataLoader
from neural_compressor.data import Datasets

dataset = Datasets('tensorflow')['dummy'](shape=(1, 224, 224, 3))
dataloader = DataLoader(framework='tensorflow', dataset=dataset)

from neural_compressor.quantization import fit
config = PostTrainingQuantConfig()
q_model = fit(
    model="./mobilenet_v1_1.0_224_frozen.pb",
    conf=config,
    calib_dataloader=dataloader,
    eval_dataloader=dataloader)
```

## Validated Models
Intel® Neural Compressor validated the quantization for 10K+ models from popular model hubs (e.g., HuggingFace Transformers, Torchvision, TensorFlow Model Hub, ONNX Model Zoo). 
Over 30 pruning, knowledge distillation and model export samples are also available. 
More details for validated typical models are available [here](/examples/README.md).
