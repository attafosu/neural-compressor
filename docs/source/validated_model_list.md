
Validated Models
======
Intel® Neural Compressor validated examples with multiple compression techniques. The typical examples link can be found in [example tables](https://github.com/intel/neural-compressor/blob/master/examples/README.md), and the performance/accuracy results is available here.

1. [Validated Quantization Examples](#Validated-Quantization-Examples)

    1.1. [TensorFlow Models with Intel TensorFlow 2.11.0](#tensorflow-models-with-Intel-tensorflow-2110)

    1.2. [PyTorch Models with Torch 1.13.0+cpu in PTQ Mode](#pytorch-models-with-torch-1130cpu-in-qat-mode)

    1.3. [PyTorch Models with Torch 1.13.0+cpu in QAT Mode](#pytorch-models-with-torch-1130cpu-in-qat-mode)

    1.4. [PyTorch Models with Torch and Intel® Extension for PyTorch* 1.13.0+cpu](#pytorch-models-with-torch-and-intel-extension-for-pytorch-1130cpu)
    
    1.5. [ONNX Models with ONNX Runtime 1.13.1](#onnx-models-with-onnx-runtime-1131)

    1.6. [MXNet Models with MXNet 1.9.1](#mxnet-models-with-mxnet-191)

2. [Validated Pruning Examples](#Validated-Pruning-Examples)

3. [Validated Knowledge Distillation Examples](#Validated-Knowledge-Distillation-Examples)

4. [Validated ONNX QDQ INT8 Models on Multiple Hardware through ONNX Runtime](#validated-onnx-qdq-int8-models-on-multiple-hardware-through-onnx-runtime)

## Validated Quantization Examples

> Notes: v2.2 release data will be updated in 1-2 weeks after the release. 

Performance results test on ​​01/04/2023 with Intel Xeon Platinum 8380 Scalable processor, using 1 socket, 4 cores/instance, 8 instances and batch size 1. 

Performance varies by use, configuration and other factors. See [platform configuration](./platform_configuration.md) for configuration details. For more complete information about performance and benchmark results, visit www.intel.com/benchmarks

### TensorFlow Models with Intel TensorFlow 2.11.0

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput(samples/sec)<br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>BERT base MRPC</td>
    <td>CKPT</td>
    <td>86.52%</td>
    <td>86.52%</td>
    <td>0.00%</td>
    <td>170.44 </td>
    <td>93.69 </td>
    <td>1.82x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD</td>
    <td>pb</td>
    <td>92.40 </td>
    <td>92.99 </td>
    <td>-0.63%</td>
    <td>18.39 </td>
    <td>9.92 </td>
    <td>1.85x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD (ONNX Model Zoo)</td>
    <td>pb</td>
    <td>92.41 </td>
    <td>92.98 </td>
    <td>-0.61%</td>
    <td>20.41 </td>
    <td>11.16 </td>
    <td>1.83x</td>
  </tr>
  <tr>
    <td>Densenet 121</td>
    <td>pb</td>
    <td>73.61%</td>
    <td>72.89%</td>
    <td>0.99%</td>
    <td>274.61 </td>
    <td>148.72 </td>
    <td>1.85x</td>
  </tr>
  <tr>
    <td>Densenet 161</td>
    <td>pb</td>
    <td>76.30%</td>
    <td>76.29%</td>
    <td>0.01%</td>
    <td>132.35 </td>
    <td>95.24 </td>
    <td>1.39x</td>
  </tr>
  <tr>
    <td>Densenet 169</td>
    <td>pb</td>
    <td>74.38%</td>
    <td>74.65%</td>
    <td>-0.36%</td>
    <td>191.31 </td>
    <td>118.99 </td>
    <td>1.61x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>pb</td>
    <td>37.44%</td>
    <td>38.31%</td>
    <td>-2.27%</td>
    <td>3.31 </td>
    <td>1.81 </td>
    <td>1.83x</td>
  </tr>
  <tr>
    <td>Faster R-CNN Inception ResNet V2</td>
    <td>SavedModel</td>
    <td>37.55%</td>
    <td>38.31%</td>
    <td>-1.98%</td>
    <td>3.32 </td>
    <td>1.81 </td>
    <td>1.84x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet101</td>
    <td>pb</td>
    <td>30.33%</td>
    <td>30.39%</td>
    <td>-0.20%</td>
    <td>42.57 </td>
    <td>13.25 </td>
    <td>3.21x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet101</td>
    <td>SavedModel</td>
    <td>30.33%</td>
    <td>30.39%</td>
    <td>-0.20%</td>
    <td>43.41 </td>
    <td>11.73 </td>
    <td>3.70x</td>
  </tr>
  <tr>
    <td>Faster R-CNN ResNet50</td>
    <td>pb</td>
    <td>26.64%</td>
    <td>26.59%</td>
    <td>0.19%</td>
    <td>51.70 </td>
    <td>16.45 </td>
    <td>3.14x</td>
  </tr>
  <tr>
    <td>Inception ResNet V2</td>
    <td>pb</td>
    <td>80.34%</td>
    <td>80.40%</td>
    <td>-0.07%</td>
    <td>139.29 </td>
    <td>76.65 </td>
    <td>1.82x</td>
  </tr>
  <tr>
    <td>Inception ResNet V2</td>
    <td>keras</td>
    <td>80.35%</td>
    <td>80.40%</td>
    <td>-0.05%</td>
    <td>99.42 </td>
    <td>54.50 </td>
    <td>1.82x</td>
  </tr>
  <tr>
    <td>Inception V1</td>
    <td>pb</td>
    <td>70.44%</td>
    <td>69.74%</td>
    <td>1.00%</td>
    <td>955.20 </td>
    <td>328.15 </td>
    <td>2.91x</td>
  </tr>
  <tr>
    <td>Inception V2</td>
    <td>pb</td>
    <td>74.34%</td>
    <td>73.97%</td>
    <td>0.50%</td>
    <td>709.92 </td>
    <td>282.40 </td>
    <td>2.51x</td>
  </tr>
  <tr>
    <td>Inception V3</td>
    <td>pb</td>
    <td>76.71%</td>
    <td>76.75%</td>
    <td>-0.05%</td>
    <td>337.09 </td>
    <td>160.07 </td>
    <td>2.11x</td>
  </tr>
  <tr>
    <td>Inception V3</td>
    <td>keras</td>
    <td>77.73%</td>
    <td>77.83%</td>
    <td>-0.13%</td>
    <td>438.52 </td>
    <td>204.76 </td>
    <td>2.14x</td>
  </tr>
  <tr>
    <td>Inception V4</td>
    <td>pb</td>
    <td>80.18%</td>
    <td>80.27%</td>
    <td>-0.11%</td>
    <td>223.02 </td>
    <td>105.44 </td>
    <td>2.12x</td>
  </tr>
  <tr>
    <td>Mask R-CNN Inception V2</td>
    <td>pb</td>
    <td>28.50%</td>
    <td>28.73%</td>
    <td>-0.80%</td>
    <td>69.42 </td>
    <td>33.00 </td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>Mask R-CNN Inception V2</td>
    <td>CKPT</td>
    <td>28.50%</td>
    <td>28.73%</td>
    <td>-0.80%</td>
    <td>69.47 </td>
    <td>32.88 </td>
    <td>2.11x</td>
  </tr>
  <tr>
    <td>MobileNet V1</td>
    <td>pb</td>
    <td>71.85%</td>
    <td>70.96%</td>
    <td>1.25%</td>
    <td>1347.65 </td>
    <td>439.05 </td>
    <td>3.07x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>pb</td>
    <td>72.56%</td>
    <td>71.76%</td>
    <td>1.11%</td>
    <td>1192.01 </td>
    <td>492.92 </td>
    <td>2.42x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>keras</td>
    <td>71.10%</td>
    <td>71.76%</td>
    <td>-0.91%</td>
    <td>412.75 </td>
    <td>376.34 </td>
    <td>1.10x</td>
  </tr>
  <tr>
    <td>MobileNet V3</td>
    <td>pb</td>
    <td>74.00%</td>
    <td>75.31%</td>
    <td>-1.74%</td>
    <td>662.07 </td>
    <td>397.69 </td>
    <td>1.66x</td>
  </tr>
  <tr>
    <td>ResNet101</td>
    <td>pb</td>
    <td>77.50%</td>
    <td>76.45%</td>
    <td>1.37%</td>
    <td>299.23 </td>
    <td>154.67 </td>
    <td>1.93x</td>
  </tr>
  <tr>
    <td>ResNet101</td>
    <td>keras</td>
    <td>61.38%</td>
    <td>61.47%</td>
    <td>-0.16%</td>
    <td>476.39 </td>
    <td>227.24 </td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>ResNet50 fashion</td>
    <td>keras</td>
    <td>78.04%</td>
    <td>78.12%</td>
    <td>-0.10%</td>
    <td>2734.43 </td>
    <td>1299.73 </td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.0</td>
    <td>pb</td>
    <td>74.12%</td>
    <td>74.27%</td>
    <td>-0.20%</td>
    <td>498.76 </td>
    <td>178.72 </td>
    <td>2.79x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.5</td>
    <td>pb</td>
    <td>76.23%</td>
    <td>76.46%</td>
    <td>-0.30%</td>
    <td>427.46 </td>
    <td>173.25 </td>
    <td>2.47x</td>
  </tr>
  <tr>
    <td>ResNetV2 101</td>
    <td>pb</td>
    <td>72.65%</td>
    <td>71.87%</td>
    <td>1.09%</td>
    <td>194.11 </td>
    <td>146.42 </td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>ResNetV2 101</td>
    <td>keras</td>
    <td>71.48%</td>
    <td>71.57%</td>
    <td>-0.12%</td>
    <td>237.09 </td>
    <td>187.24 </td>
    <td>1.27x</td>
  </tr>
  <tr>
    <td>ResNetV2 152</td>
    <td>pb</td>
    <td>73.07%</td>
    <td>72.37%</td>
    <td>0.97%</td>
    <td>155.04 </td>
    <td>112.01 </td>
    <td>1.38x</td>
  </tr>
  <tr>
    <td>ResNetV2 50</td>
    <td>pb</td>
    <td>70.44%</td>
    <td>69.64%</td>
    <td>1.15%</td>
    <td>302.55 </td>
    <td>215.50 </td>
    <td>1.40x</td>
  </tr>
  <tr>
    <td>ResNet v2 50</td>
    <td>keras</td>
    <td>69.20%</td>
    <td>69.03%</td>
    <td>0.25%</td>
    <td>346.99 </td>
    <td>312.15 </td>
    <td>1.11x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>pb</td>
    <td>23.12%</td>
    <td>23.13%</td>
    <td>-0.04%</td>
    <td>277.10 </td>
    <td>173.61 </td>
    <td>1.60x</td>
  </tr>
  <tr>
    <td>SSD MobileNet v1</td>
    <td>CKPT</td>
    <td>23.10%</td>
    <td>23.13%</td>
    <td>-0.13%</td>
    <td>273.51 </td>
    <td>118.46 </td>
    <td>2.31x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>pb</td>
    <td>21.70%</td>
    <td>22.09%</td>
    <td>-1.77%</td>
    <td>33.95 </td>
    <td>8.81 </td>
    <td>3.85x</td>
  </tr>
  <tr>
    <td>SSD ResNet50 V1</td>
    <td>pb</td>
    <td>37.75%</td>
    <td>38.00%</td>
    <td>-0.66%</td>
    <td>34.11 </td>
    <td>15.67 </td>
    <td>2.18x</td>
  </tr>
  <tr>
    <td>SSD ResNet50 v1</td>
    <td>CKPT</td>
    <td>37.82%</td>
    <td>38.00%</td>
    <td>-0.47%</td>
    <td>34.57 </td>
    <td>13.68 </td>
    <td>2.53x</td>
  </tr>
  <tr>
    <td>Transformer lt MLPerf</td>
    <td>pb</td>
    <td>27.12 </td>
    <td>27.17 </td>
    <td>-0.18%</td>
    <td>3.26 </td>
    <td>2.63 </td>
    <td>1.24x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>pb</td>
    <td>72.64%</td>
    <td>70.89%</td>
    <td>2.47%</td>
    <td>219.11 </td>
    <td>91.30 </td>
    <td>2.40x</td>
  </tr>
  <tr>
    <td>VGG19</td>
    <td>pb</td>
    <td>72.69%</td>
    <td>71.01%</td>
    <td>2.37%</td>
    <td>193.61 </td>
    <td>78.47 </td>
    <td>2.47x</td>
  </tr>
  <tr>
    <td>Wide Deep large DS</td>
    <td>pb</td>
    <td>77.75%</td>
    <td>77.67%</td>
    <td>0.10%</td>
    <td>11506.91 </td>
    <td>9665.07 </td>
    <td>1.19x</td>
  </tr>
  <tr>
    <td>Xception</td>
    <td>keras</td>
    <td>78.43%</td>
    <td>78.94%</td>
    <td>-0.65%</td>
    <td>262.83 </td>
    <td>137.35 </td>
    <td>1.91x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Torch 1.13.0+cpu in PTQ Mode

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput (samples/sec) <br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ALBERT base MRPC</td>
    <td>EAGER</td>
    <td>88.85%</td>
    <td>88.50%</td>
    <td>0.40%</td>
    <td>25.68 </td>
    <td>21.58 </td>
    <td>1.19x</td>
  </tr>
  <tr>
    <td>Barthez MRPC</td>
    <td>EAGER</td>
    <td>83.92%</td>
    <td>83.81%</td>
    <td>0.14%</td>
    <td>143.37 </td>
    <td>70.96 </td>
    <td>2.02x</td>
  </tr>
  <tr>
    <td>BERT base COLA</td>
    <td>FX</td>
    <td>58.80%</td>
    <td>58.84%</td>
    <td>-0.07%</td>
    <td>223.51 </td>
    <td>101.39 </td>
    <td>2.20x</td>
  </tr>
  <tr>
    <td>BERT base MRPC</td>
    <td>FX</td>
    <td>89.90%</td>
    <td>90.69%</td>
    <td>-0.88%</td>
    <td>209.80 </td>
    <td>100.96 </td>
    <td>2.08x</td>
  </tr>
  <tr>
    <td>BERT base RTE</td>
    <td>FX</td>
    <td>69.31%</td>
    <td>69.68%</td>
    <td>-0.52%</td>
    <td>221.92 </td>
    <td>101.36 </td>
    <td>2.19x</td>
  </tr>
  <tr>
    <td>BERT base SST-2</td>
    <td>FX</td>
    <td>91.06%</td>
    <td>91.86%</td>
    <td>-0.87%</td>
    <td>224.19 </td>
    <td>101.23 </td>
    <td>2.21x</td>
  </tr>
  <tr>
    <td>BERT base STSB</td>
    <td>FX</td>
    <td>89.10%</td>
    <td>89.75%</td>
    <td>-0.72%</td>
    <td>218.04 </td>
    <td>101.15 </td>
    <td>2.16x</td>
  </tr>
  <tr>
    <td>BERT large COLA</td>
    <td>FX</td>
    <td>64.12%</td>
    <td>62.57%</td>
    <td>2.48%</td>
    <td>75.42 </td>
    <td>29.32 </td>
    <td>2.57x</td>
  </tr>
  <tr>
    <td>BERT large MRPC</td>
    <td>FX</td>
    <td>89.50%</td>
    <td>90.38%</td>
    <td>-0.97%</td>
    <td>75.10 </td>
    <td>29.41 </td>
    <td>2.55x</td>
  </tr>
  <tr>
    <td>BERT large QNLI</td>
    <td>FX</td>
    <td>90.90%</td>
    <td>91.82%</td>
    <td>-1.00%</td>
    <td>74.80 </td>
    <td>29.17 </td>
    <td>2.56x</td>
  </tr>
  <tr>
    <td>BERT large RTE</td>
    <td>FX</td>
    <td>73.29%</td>
    <td>74.01%</td>
    <td>-0.97%</td>
    <td>40.38 </td>
    <td>29.28 </td>
    <td>1.38x</td>
  </tr>
  <tr>
    <td>BERT large SQuAD</td>
    <td>FX</td>
    <td>92.61 </td>
    <td>93.16 </td>
    <td>-0.58%</td>
    <td>18.53 </td>
    <td>9.82 </td>
    <td>1.89x</td>
  </tr>
  <tr>
    <td>BlendCNN</td>
    <td>EAGER</td>
    <td>68.40%</td>
    <td>68.40%</td>
    <td>0.00%</td>
    <td>4885.60 </td>
    <td>3715.36 </td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>CamemBERT base MRPC</td>
    <td>EAGER</td>
    <td>86.70%</td>
    <td>86.82%</td>
    <td>-0.14%</td>
    <td>206.00 </td>
    <td>98.50 </td>
    <td>2.09x</td>
  </tr>
  <tr>
    <td>Ctrl MRPC</td>
    <td>EAGER</td>
    <td>81.87%</td>
    <td>82.00%</td>
    <td>-0.15%</td>
    <td>19.39 </td>
    <td>7.19 </td>
    <td>2.70x</td>
  </tr>
  <tr>
    <td>Deberta MRPC</td>
    <td>EAGER</td>
    <td>90.88%</td>
    <td>90.91%</td>
    <td>-0.04%</td>
    <td>125.42 </td>
    <td>67.67 </td>
    <td>1.85x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>EAGER</td>
    <td>88.23%</td>
    <td>89.16%</td>
    <td>-1.05%</td>
    <td>366.27 </td>
    <td>197.76 </td>
    <td>1.85x</td>
  </tr>
  <tr>
    <td>DistilBERT base MRPC</td>
    <td>FX</td>
    <td>88.54%</td>
    <td>89.16%</td>
    <td>-0.69%</td>
    <td>399.63 </td>
    <td>197.47 </td>
    <td>2.02x</td>
  </tr>
  <tr>
    <td>FlauBERT MRPC</td>
    <td>EAGER</td>
    <td>79.87%</td>
    <td>80.19%</td>
    <td>-0.40%</td>
    <td>592.53 </td>
    <td>385.01 </td>
    <td>1.54x</td>
  </tr>
  <tr>
    <td>GPT J WikiText</td>
    <td>FX</td>
    <td>3.36 </td>
    <td>2.34 </td>
    <td>43.84%</td>
    <td>0.52 </td>
    <td>0.20 </td>
    <td>2.60x</td>
  </tr>
  <tr>
    <td>HuBERT</td>
    <td>EAGER</td>
    <td>97.63%</td>
    <td>97.84%</td>
    <td>-0.21%</td>
    <td>10.00 </td>
    <td>7.26 </td>
    <td>1.38x</td>
  </tr>
  <tr>
    <td>Inception V3</td>
    <td>EAGER</td>
    <td>69.43%</td>
    <td>69.52%</td>
    <td>-0.13%</td>
    <td>446.65 </td>
    <td>181.41 </td>
    <td>2.46x</td>
  </tr>
  <tr>
    <td>Layoutlm MRPC</td>
    <td>EAGER</td>
    <td>81.22%</td>
    <td>78.01%</td>
    <td>4.12%</td>
    <td>204.22 </td>
    <td>96.26 </td>
    <td>2.12x</td>
  </tr>
  <tr>
    <td>Longformer MRPC</td>
    <td>EAGER</td>
    <td>91.01%</td>
    <td>91.46%</td>
    <td>-0.49%</td>
    <td>18.68 </td>
    <td>14.25 </td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>Mask R-CNN</td>
    <td>FX</td>
    <td>37.60%</td>
    <td>37.80%</td>
    <td>-0.53%</td>
    <td>7.20 </td>
    <td>4.77 </td>
    <td>1.51x</td>
  </tr>
  <tr>
    <td>Mbart wnli</td>
    <td>EAGER</td>
    <td>56.34%</td>
    <td>56.34%</td>
    <td>0.00%</td>
    <td>56.32 </td>
    <td>24.77 </td>
    <td>2.27x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>EAGER</td>
    <td>70.54%</td>
    <td>71.84%</td>
    <td>-1.81%</td>
    <td>625.38 </td>
    <td>451.25 </td>
    <td>1.39x</td>
  </tr>
  <tr>
    <td>lvwerra/pegasus-samsum</td>
    <td>EAGER</td>
    <td>42.10 </td>
    <td>42.67 </td>
    <td>-1.35%</td>
    <td>3.58 </td>
    <td>1.06 </td>
    <td>3.38x</td>
  </tr>
  <tr>
    <td>Peleenet</td>
    <td>EAGER</td>
    <td>71.64%</td>
    <td>72.10%</td>
    <td>-0.64%</td>
    <td>402.33 </td>
    <td>312.37 </td>
    <td>1.29x</td>
  </tr>
  <tr>
    <td>Pokemon Diffusers</td>
    <td>FX</td>
    <td>275.80 </td>
    <td>334.48 </td>
    <td>-17.54%</td>
    <td>0.03 </td>
    <td>0.02 </td>
    <td>1.48x</td>
  </tr>
  <tr>
    <td>Reformer Crime and Punishment</td>
    <td>EAGER</td>
    <td>1.88 </td>
    <td>1.87 </td>
    <td>0.43%</td>
    <td>162.34 </td>
    <td>153.65 </td>
    <td>1.06x</td>
  </tr>
  <tr>
    <td>ResNet18</td>
    <td>EAGER</td>
    <td>69.57%</td>
    <td>69.76%</td>
    <td>-0.27%</td>
    <td>657.72 </td>
    <td>327.69 </td>
    <td>2.01x</td>
  </tr>
  <tr>
    <td>ResNet18</td>
    <td>FX</td>
    <td>69.62%</td>
    <td>69.76%</td>
    <td>-0.20%</td>
    <td>812.99 </td>
    <td>344.99 </td>
    <td>2.36x</td>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>EAGER</td>
    <td>75.98%</td>
    <td>76.15%</td>
    <td>-0.21%</td>
    <td>360.16 </td>
    <td>161.44 </td>
    <td>2.23x</td>
  </tr>
  <tr>
    <td>Resnext101 32x8d</td>
    <td>EAGER</td>
    <td>79.08%</td>
    <td>79.31%</td>
    <td>-0.29%</td>
    <td>182.84 </td>
    <td>60.55 </td>
    <td>3.02x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC</td>
    <td>EAGER</td>
    <td>88.25%</td>
    <td>88.18%</td>
    <td>0.08%</td>
    <td>207.41 </td>
    <td>98.71 </td>
    <td>2.10x</td>
  </tr>
  <tr>
    <td>SqueezeBERT MRPC</td>
    <td>EAGER</td>
    <td>86.87%</td>
    <td>87.65%</td>
    <td>-0.89%</td>
    <td>195.00 </td>
    <td>150.09 </td>
    <td>1.30x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>FX</td>
    <td>19.47 </td>
    <td>19.63 </td>
    <td>-0.83%</td>
    <td>18.56 </td>
    <td>6.75 </td>
    <td>2.75x</td>
  </tr>
  <tr>
    <td>Transfo-xl MRPC</td>
    <td>EAGER</td>
    <td>81.97%</td>
    <td>81.20%</td>
    <td>0.94%</td>
    <td>9.73 </td>
    <td>6.92 </td>
    <td>1.41x</td>
  </tr>
  <tr>
    <td>Wave2Vec2</td>
    <td>FX</td>
    <td>95.71%</td>
    <td>96.60%</td>
    <td>-0.92%</td>
    <td>23.78 </td>
    <td>19.45 </td>
    <td>1.22x</td>
  </tr>
  <tr>
    <td>Xlm Roberta MRPC</td>
    <td>EAGER</td>
    <td>88.24%</td>
    <td>88.24%</td>
    <td>0.00%</td>
    <td>102.19 </td>
    <td>102.58 </td>
    <td>1.00x</td>
  </tr>
  <tr>
    <td>Xlm Roberta-base MRPC</td>
    <td>EAGER</td>
    <td>88.03%</td>
    <td>88.62%</td>
    <td>-0.67%</td>
    <td>115.16 </td>
    <td>98.75 </td>
    <td>1.17x</td>
  </tr>
  <tr>
    <td>YOLO V3</td>
    <td>EAGER</td>
    <td>24.60%</td>
    <td>24.54%</td>
    <td>0.21%</td>
    <td>76.15 </td>
    <td>31.80 </td>
    <td>2.39x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Torch 1.13.0+cpu in QAT Mode

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput (samples/sec) <br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>BERT base MRPC</td>
    <td>FX</td>
    <td>89.20%</td>
    <td>89.50%</td>
    <td>-0.34%</td>
    <td>232.16</td>
    <td>101.89</td>
    <td>2.28x</td>
  </tr>
  <tr>
    <td class="tg-zk71">ResNet 18</td>
    <td>EAGER</td>
    <td>69.68%</td>
    <td>69.76%</td>
    <td>-0.12%</td>
    <td>664.99</td>
    <td>329.15</td>
    <td>2.02x</td>
  </tr>
  <tr>
    <td class="tg-zk71">ResNet 18</td>
    <td>FX</td>
    <td>69.84%</td>
    <td>69.76%</td>
    <td>0.12%</td>
    <td>832.32</td>
    <td>338.48</td>
    <td>2.46x</td>
  </tr>
  <tr>
    <td class="tg-zk71">ResNet 50</td>
    <td>EAGER</td>
    <td>76.03%</td>
    <td>76.15%</td>
    <td>-0.15%</td>
    <td>433.83</td>
    <td>164.98</td>
    <td>2.63x</td>
  </tr>
</tbody>
</table>

### PyTorch Models with Torch and Intel® Extension for PyTorch* 1.13.0+cpu

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput (samples/sec) <br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>ResNet50</td>
    <td>IPEX</td>
    <td>76.01%</td>
    <td>76.15%</td>
    <td>-0.17%</td>
    <td>836.38</td>
    <td>207.89</td>
    <td>4.02x</td>
  </tr>
  <tr>
    <td>ResNet18</td>
    <td>IPEX</td>
    <td>69.65%</td>
    <td>69.76%</td>
    <td>-0.15%</td>
    <td>1396.52</td>
    <td>463.95</td>
    <td>3.01x</td>
  </tr>
  <tr>
    <td>SSD ResNet34</td>
    <td>IPEX</td>
    <td>19.93%</td>
    <td>20.00%</td>
    <td>-0.36%</td>
    <td>30.08</td>
    <td>7.66</td>
    <td>3.93x</td>
  </tr>
  <tr>
    <td>BERT large</td>
    <td>IPEX</td>
    <td>92.81</td>
    <td>93.16</td>
    <td>-0.37%</td>
    <td>46.44</td>
    <td>6.73</td>
    <td>6.90x</td>
  </tr>
  <tr>
    <td>Distilbert base</td>
    <td>IPEX</td>
    <td>85.97</td>
    <td>86.84</td>
    <td>-0.99%</td>
    <td>159.90</td>
    <td>68.95</td>
    <td>2.32x</td>
  </tr>
</tbody>
</table>

### ONNX Models with ONNX Runtime 1.13.1

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Example</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput(samples/sec) <br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center"> 
  <tr>
    <td>AlexNet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>54.73%</td>
    <td>54.79%</td>
    <td>-0.11%</td>
    <td>968.22 </td>
    <td>473.31 </td>
    <td>2.05x</td>
  </tr>
  <tr>
    <td>AlexNet (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>54.71%</td>
    <td>54.79%</td>
    <td>-0.15%</td>
    <td>958.75 </td>
    <td>477.77 </td>
    <td>2.01x</td>
  </tr>
  <tr>
    <td>ArcFace (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>99.80%</td>
    <td>99.80%</td>
    <td>0.00%</td>
    <td>225.10 </td>
    <td>126.56 </td>
    <td>1.78x</td>
  </tr>
  <tr>
    <td>BERT base MRPC DYNAMIC</td>
    <td>QLinear</td>
    <td>85.29%</td>
    <td>86.03%</td>
    <td>-0.86%</td>
    <td>298.33 </td>
    <td>124.67 </td>
    <td>2.39x</td>
  </tr>
  <tr>
    <td>BERT base MRPC STATIC</td>
    <td>QLinear</td>
    <td>85.54%</td>
    <td>86.03%</td>
    <td>-0.57%</td>
    <td>624.43 </td>
    <td>254.64 </td>
    <td>2.45x</td>
  </tr>
  <tr>
    <td>BERT SQuAD model zoo DYNAMIC (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>80.44 </td>
    <td>80.67 </td>
    <td>-0.29%</td>
    <td>97.81 </td>
    <td>52.75 </td>
    <td>1.85x</td>
  </tr>
  <tr>
    <td>Caffenet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>56.21%</td>
    <td>56.30%</td>
    <td>-0.16%</td>
    <td>1432.98 </td>
    <td>540.28 </td>
    <td>2.65x</td>
  </tr>
  <tr>
    <td>Caffenet (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>56.25%</td>
    <td>56.30%</td>
    <td>-0.09%</td>
    <td>1460.21 </td>
    <td>540.81 </td>
    <td>2.70x</td>
  </tr>
  <tr>
    <td>Densenet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>60.53%</td>
    <td>60.96%</td>
    <td>-0.71%</td>
    <td>357.41 </td>
    <td>265.22 </td>
    <td>1.35x</td>
  </tr>
  <tr>
    <td>Distilbert base MRPC</td>
    <td>QLinear</td>
    <td>85.54%</td>
    <td>84.56%</td>
    <td>1.16%</td>
    <td>1365.72 </td>
    <td>477.62 </td>
    <td>2.86x</td>
  </tr>
  <tr>
    <td>Distilbert base MRPC</td>
    <td>QDQ</td>
    <td>84.56%</td>
    <td>84.56%</td>
    <td>0.00%</td>
    <td>524.96 </td>
    <td>476.39 </td>
    <td>1.10x</td>
  </tr>
  <tr>
    <td>DUC (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>81.62%</td>
    <td>81.92%</td>
    <td>-0.37%</td>
    <td>5.66 </td>
    <td>2.82 </td>
    <td>2.01x</td>
  </tr>
  <tr>
    <td>EfficientNet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>77.57%</td>
    <td>77.70%</td>
    <td>-0.17%</td>
    <td>1211.10 </td>
    <td>758.41 </td>
    <td>1.60x</td>
  </tr>
  <tr>
    <td>EfficientNet (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>77.61%</td>
    <td>77.70%</td>
    <td>-0.12%</td>
    <td>856.64 </td>
    <td>762.48 </td>
    <td>1.12x</td>
  </tr>
  <tr>
    <td>Emotion Ferplus (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>8.00%</td>
    <td>8.00%</td>
    <td>0.00%</td>
    <td>925.43 </td>
    <td>694.99 </td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>Faster R-CNN (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>34.09%</td>
    <td>34.37%</td>
    <td>-0.81%</td>
    <td>13.82 </td>
    <td>5.89 </td>
    <td>2.35x</td>
  </tr>
  <tr>
    <td>Faster R-CNN (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>33.90%</td>
    <td>34.37%</td>
    <td>-1.37%</td>
    <td>9.59 </td>
    <td>6.09 </td>
    <td>1.57x</td>
  </tr>
  <tr>
    <td>FCN (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>64.54%</td>
    <td>64.98%</td>
    <td>-0.68%</td>
    <td>40.49 </td>
    <td>11.92 </td>
    <td>3.40x</td>
  </tr>
  <tr>
    <td>FCN (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>64.40%</td>
    <td>64.98%</td>
    <td>-0.89%</td>
    <td>26.87 </td>
    <td>11.92 </td>
    <td>2.25x</td>
  </tr>
  <tr>
    <td>GoogleNet-12 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>67.71%</td>
    <td>67.79%</td>
    <td>-0.12%</td>
    <td>771.39 </td>
    <td>571.35 </td>
    <td>1.35x</td>
  </tr>
  <tr>
    <td>GoogleNet-12 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>67.73%</td>
    <td>67.79%</td>
    <td>-0.09%</td>
    <td>763.79 </td>
    <td>579.95 </td>
    <td>1.32x</td>
  </tr>
  <tr>
    <td>HF ALBERT-base-V2 DYNAMIC</td>
    <td>QLinear</td>
    <td>91.40%</td>
    <td>92.32%</td>
    <td>-1.00%</td>
    <td>156.96 </td>
    <td>105.89 </td>
    <td>1.48x</td>
  </tr>
  <tr>
    <td>HF BERT-base-multilingual-cased DYNAMIC</td>
    <td>QLinear</td>
    <td>88.70 </td>
    <td>89.13 </td>
    <td>-0.48%</td>
    <td>47.68 </td>
    <td>23.95 </td>
    <td>1.99x</td>
  </tr>
  <tr>
    <td>HF BERT-base-uncased DYNAMIC</td>
    <td>QLinear</td>
    <td>89.58%</td>
    <td>90.42%</td>
    <td>-0.93%</td>
    <td>199.37 </td>
    <td>104.85 </td>
    <td>1.90x</td>
  </tr>
  <tr>
    <td>HF CamemBERT-base DYNAMIC</td>
    <td>QLinear</td>
    <td>88.47%</td>
    <td>89.28%</td>
    <td>-0.91%</td>
    <td>182.60 </td>
    <td>105.45 </td>
    <td>1.73x</td>
  </tr>
  <tr>
    <td>HF Distilbert-base-uncased DYNAMIC</td>
    <td>QLinear</td>
    <td>90.37%</td>
    <td>91.06%</td>
    <td>-0.76%</td>
    <td>449.71 </td>
    <td>164.21 </td>
    <td>2.74x</td>
  </tr>
  <tr>
    <td>HF minilm-l12-h384-uncased DYNAMIC</td>
    <td>QLinear</td>
    <td>91.07%</td>
    <td>90.97%</td>
    <td>0.11%</td>
    <td>466.59 </td>
    <td>247.71 </td>
    <td>1.88x</td>
  </tr>
  <tr>
    <td>HF minilm-l6-h384-uncased DYNAMIC</td>
    <td>QLinear</td>
    <td>89.91%</td>
    <td>90.14%</td>
    <td>-0.26%</td>
    <td>523.59 </td>
    <td>354.05 </td>
    <td>1.48x</td>
  </tr>
  <tr>
    <td>HF Roberta-base DYNAMIC</td>
    <td>QLinear</td>
    <td>90.85%</td>
    <td>91.38%</td>
    <td>-0.58%</td>
    <td>183.59 </td>
    <td>107.70 </td>
    <td>1.70x</td>
  </tr>
  <tr>
    <td>HF Spanbert DYNAMIC</td>
    <td>QLinear</td>
    <td>91.40 </td>
    <td>91.98 </td>
    <td>-0.63%</td>
    <td>48.36 </td>
    <td>24.03 </td>
    <td>2.01x</td>
  </tr>
  <tr>
    <td>HF Xlm Roberta-base DYNAMIC</td>
    <td>QLinear</td>
    <td>89.45%</td>
    <td>90.10%</td>
    <td>-0.72%</td>
    <td>208.16 </td>
    <td>64.60 </td>
    <td>3.22x</td>
  </tr>
  <tr>
    <td>Inception V1 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>67.21%</td>
    <td>67.24%</td>
    <td>-0.04%</td>
    <td>795.38 </td>
    <td>600.03 </td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>Inception v1 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>67.21%</td>
    <td>67.24%</td>
    <td>-0.04%</td>
    <td>780.70 </td>
    <td>591.81 </td>
    <td>1.32x</td>
  </tr>
  <tr>
    <td>Mask R-CNN (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>33.13%</td>
    <td>33.72%</td>
    <td>-1.75%</td>
    <td>11.61 </td>
    <td>5.58 </td>
    <td>2.08x</td>
  </tr>
  <tr>
    <td>Mask R-CNN (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>33.28%</td>
    <td>33.72%</td>
    <td>-1.30%</td>
    <td>8.64 </td>
    <td>5.53 </td>
    <td>1.56x</td>
  </tr>
  <tr>
    <td>MobileBERT MRPC</td>
    <td>QLinear</td>
    <td>86.27%</td>
    <td>86.27%</td>
    <td>0.00%</td>
    <td>591.94 </td>
    <td>515.49 </td>
    <td>1.15x</td>
  </tr>
  <tr>
    <td>MobileBERT SQuAD MLPerf DYNAMIC</td>
    <td>QLinear</td>
    <td>89.82 </td>
    <td>90.03 </td>
    <td>-0.23%</td>
    <td>85.66 </td>
    <td>74.12 </td>
    <td>1.16x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>QLinear</td>
    <td>65.59%</td>
    <td>66.89%</td>
    <td>-1.94%</td>
    <td>2370.93 </td>
    <td>1526.33 </td>
    <td>1.55x</td>
  </tr>
  <tr>
    <td>MobileNet V2</td>
    <td>QDQ</td>
    <td>65.82%</td>
    <td>66.89%</td>
    <td>-1.60%</td>
    <td>2216.02 </td>
    <td>1506.85 </td>
    <td>1.47x</td>
  </tr>
  <tr>
    <td>MobileNet V3 MLPerf</td>
    <td>QLinear</td>
    <td>75.58%</td>
    <td>75.74%</td>
    <td>-0.21%</td>
    <td>2078.85 </td>
    <td>1028.31 </td>
    <td>2.02x</td>
  </tr>
  <tr>
    <td>MobileNet V3 MLPerf</td>
    <td>QDQ</td>
    <td>75.57%</td>
    <td>75.74%</td>
    <td>-0.22%</td>
    <td>1762.62 </td>
    <td>999.31 </td>
    <td>1.76x</td>
  </tr>
  <tr>
    <td>MobileNetV2-12 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>68.38%</td>
    <td>69.48%</td>
    <td>-1.58%</td>
    <td>2615.52 </td>
    <td>1645.08 </td>
    <td>1.59x</td>
  </tr>
  <tr>
    <td>MobileNetV2-12 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>68.51%</td>
    <td>69.48%</td>
    <td>-1.40%</td>
    <td>2461.25 </td>
    <td>1674.36 </td>
    <td>1.47x</td>
  </tr>
  <tr>
    <td>ResNet v1.5 MLPerf</td>
    <td>QLinear</td>
    <td>76.15%</td>
    <td>76.46%</td>
    <td>-0.41%</td>
    <td>766.33 </td>
    <td>431.92 </td>
    <td>1.77x</td>
  </tr>
  <tr>
    <td>ResNet v1.5 MLPerf</td>
    <td>QDQ</td>
    <td>76.14%</td>
    <td>76.46%</td>
    <td>-0.42%</td>
    <td>575.34 </td>
    <td>430.83 </td>
    <td>1.34x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.5</td>
    <td>QLinear</td>
    <td>72.26%</td>
    <td>72.29%</td>
    <td>-0.04%</td>
    <td>747.31 </td>
    <td>431.09 </td>
    <td>1.73x</td>
  </tr>
  <tr>
    <td>ResNet50 v1.5</td>
    <td>QDQ</td>
    <td>72.20%</td>
    <td>72.29%</td>
    <td>-0.12%</td>
    <td>564.21 </td>
    <td>431.50 </td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>ResNet50-v1-12 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>74.81%</td>
    <td>74.99%</td>
    <td>-0.24%</td>
    <td>594.29 </td>
    <td>449.21 </td>
    <td>1.32x</td>
  </tr>
  <tr>
    <td>ResNet50-v1-12 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>74.76%</td>
    <td>74.99%</td>
    <td>-0.31%</td>
    <td>590.51 </td>
    <td>449.93 </td>
    <td>1.31x</td>
  </tr>
  <tr>
    <td>Roberta base MRPC</td>
    <td>QLinear</td>
    <td>90.69%</td>
    <td>89.95%</td>
    <td>0.82%</td>
    <td>643.03 </td>
    <td>253.04 </td>
    <td>2.54x</td>
  </tr>
  <tr>
    <td>ShuffleNet V2-12 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>66.13%</td>
    <td>66.36%</td>
    <td>-0.35%</td>
    <td>2354.51 </td>
    <td>1461.47 </td>
    <td>1.61x</td>
  </tr>
  <tr>
    <td>ShuffleNet V2-12 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>66.12%</td>
    <td>66.36%</td>
    <td>-0.36%</td>
    <td>1850.09 </td>
    <td>1368.35 </td>
    <td>1.35x</td>
  </tr>
  <tr>
    <td>SqueezeNet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>56.54%</td>
    <td>56.87%</td>
    <td>-0.58%</td>
    <td>2484.36 </td>
    <td>1912.37 </td>
    <td>1.30x</td>
  </tr>
  <tr>
    <td>SqueezeNet (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>56.39%</td>
    <td>56.87%</td>
    <td>-0.83%</td>
    <td>2526.02 </td>
    <td>1911.32 </td>
    <td>1.32x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>QLinear</td>
    <td>22.44%</td>
    <td>23.10%</td>
    <td>-2.86%</td>
    <td>710.17 </td>
    <td>549.55 </td>
    <td>1.29x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1</td>
    <td>QDQ</td>
    <td>22.44%</td>
    <td>23.10%</td>
    <td>-2.86%</td>
    <td>622.58 </td>
    <td>497.42 </td>
    <td>1.25x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>22.96%</td>
    <td>23.02%</td>
    <td>-0.26%</td>
    <td>652.14 </td>
    <td>507.77 </td>
    <td>1.28x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>22.96%</td>
    <td>23.02%</td>
    <td>-0.26%</td>
    <td>573.30 </td>
    <td>470.42 </td>
    <td>1.22x</td>
  </tr>
  <tr>
    <td>SSD MobileNet V2</td>
    <td>QLinear</td>
    <td>24.03%</td>
    <td>24.67%</td>
    <td>-2.59%</td>
    <td>527.67 </td>
    <td>396.27 </td>
    <td>1.33x</td>
  </tr>
  <tr>
    <td>SSD-12 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>18.92%</td>
    <td>18.98%</td>
    <td>-0.32%</td>
    <td>31.24 </td>
    <td>8.77 </td>
    <td>3.56x</td>
  </tr>
  <tr>
    <td>SSD-12 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>18.63%</td>
    <td>18.98%</td>
    <td>-1.84%</td>
    <td>23.72 </td>
    <td>8.87 </td>
    <td>2.68x</td>
  </tr>
  <tr>
    <td>Tiny YOLO V3 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>11.82%</td>
    <td>12.42%</td>
    <td>-4.83%</td>
    <td>647.17 </td>
    <td>514.42 </td>
    <td>1.26x</td>
  </tr>
  <tr>
    <td>Ultraface (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>83.34%</td>
    <td>83.65%</td>
    <td>-0.37%</td>
    <td>314.50 </td>
    <td>125.56 </td>
    <td>2.50x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>QLinear</td>
    <td>66.67%</td>
    <td>66.69%</td>
    <td>-0.03%</td>
    <td>221.62 </td>
    <td>98.20 </td>
    <td>2.26x</td>
  </tr>
  <tr>
    <td>VGG16</td>
    <td>QDQ</td>
    <td>66.69%</td>
    <td>66.69%</td>
    <td>0.00%</td>
    <td>304.09 </td>
    <td>98.33 </td>
    <td>3.09x</td>
  </tr>
  <tr>
    <td>VGG16 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>72.32%</td>
    <td>72.40%</td>
    <td>-0.11%</td>
    <td>316.54 </td>
    <td>98.49 </td>
    <td>3.21x</td>
  </tr>
  <tr>
    <td>VGG16 (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>72.31%</td>
    <td>72.40%</td>
    <td>-0.12%</td>
    <td>315.61 </td>
    <td>98.46 </td>
    <td>3.21x</td>
  </tr>
  <tr>
    <td>YOLO V3 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>26.92%</td>
    <td>28.73%</td>
    <td>-6.30%</td>
    <td>119.63 </td>
    <td>53.37 </td>
    <td>2.24x</td>
  </tr>
  <tr>
    <td>YOLO V4 (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>32.33%</td>
    <td>33.71%</td>
    <td>-4.09%</td>
    <td>49.30 </td>
    <td>32.88 </td>
    <td>1.50x</td>
  </tr>
  <tr>
    <td>ZFNet (ONNX Model Zoo)</td>
    <td>QLinear</td>
    <td>55.84%</td>
    <td>55.96%</td>
    <td>-0.21%</td>
    <td>462.28 </td>
    <td>268.32 </td>
    <td>1.72x</td>
  </tr>
  <tr>
    <td>ZFNet (ONNX Model Zoo)</td>
    <td>QDQ</td>
    <td>55.86%</td>
    <td>55.96%</td>
    <td>-0.18%</td>
    <td>465.44 </td>
    <td>265.58 </td>
    <td>1.75x</td>
  </tr>
</tbody>
</table>

### MXNet Models with MXNet 1.9.1

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance<br>Throughput(samples/sec) <br></th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Accuracy Ratio<br>[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio<br>[INT8/FP32]</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>Inception V3</td>
    <td>77.77%</td>
    <td>77.65%</td>
    <td>0.16%</td>
    <td>94.24 </td>
    <td>58.05 </td>
    <td>1.62x</td>
  </tr>
  <tr>
    <td>MobileNet 1.0</td>
    <td>71.61%</td>
    <td>72.23%</td>
    <td>-0.86%</td>
    <td>436.46 </td>
    <td>314.81 </td>
    <td>1.39x</td>
  </tr>
  <tr>
    <td>MobileNet V2 1.0</td>
    <td>70.75%</td>
    <td>70.87%</td>
    <td>-0.16%</td>
    <td>270.78 </td>
    <td>229.21 </td>
    <td>1.18x</td>
  </tr>
  <tr>
    <td>ResNet 152 V1</td>
    <td>78.30%</td>
    <td>78.54%</td>
    <td>-0.30%</td>
    <td>66.62 </td>
    <td>36.55 </td>
    <td>1.82x</td>
  </tr>
  <tr>
    <td>ResNet 18 V1</td>
    <td>70.01%</td>
    <td>70.14%</td>
    <td>-0.19%</td>
    <td>429.86 </td>
    <td>224.10 </td>
    <td>1.92x</td>
  </tr>
  <tr>
    <td>ResNet 50 V1</td>
    <td>75.94%</td>
    <td>76.33%</td>
    <td>-0.50%</td>
    <td>182.56 </td>
    <td>94.15 </td>
    <td>1.94x</td>
  </tr>
  <tr>
    <td>SqueezeNet 1.0</td>
    <td>56.82%</td>
    <td>56.97%</td>
    <td>-0.26%</td>
    <td>331.72 </td>
    <td>242.76 </td>
    <td>1.37x</td>
  </tr>
  <tr>
    <td>SSD MobileNet 1.0</td>
    <td>74.94%</td>
    <td>75.54%</td>
    <td>-0.79%</td>
    <td>53.66 </td>
    <td>27.16 </td>
    <td>1.98x</td>
  </tr>
  <tr>
    <td>SSD ResNet50 V1</td>
    <td>80.19%</td>
    <td>80.23%</td>
    <td>-0.05%</td>
    <td>37.63 </td>
    <td>16.80 </td>
    <td>2.24x</td>
  </tr>
</tbody>
</table>

## Validated Pruning Examples

<table class="docutils">
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th rowspan="2">Task</br>Dataset</th>
    <th rowspan="2">Dense Accuracy<br>Sparse Accuracy</th>
    <th rowspan="2">Relative Drop</th>
    <th rowspan="2">Sparsity ratio<br>Sparsity Pattern</th>
    <th rowspan="2">Comments<br>Balanced<br>or unbalanced ratio</th>
  </tr>
  <tr>
  </tr>
</thead>
<tbody>  
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=76.2</td>
    <td>-0.80%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=76.2</td>
    <td>-0.80%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=76.87</br>f1=77.62</td>
    <td>+0.98%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=86.90</br>f1=86.15</td>
    <td>-0.86%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=86.90</br>f1=87.50</td>
    <td>+0.69%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=88.59</br>f1=87.78</td>
    <td>-0.92%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-base-uncased</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=88.59</br>f1=89.40</td>
    <td>+0.91%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.23</br>f1=90.91</td>
    <td>-0.35%</td>
    <td>80%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.23</br>f1=91.67</td>
    <td>+0.48%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=87.22</td>
    <td>-0.34%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=87.33</td>
    <td>-0.22%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>balanced</td>  
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=86.89</td>
    <td>-0.72%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>MRPC</td>
    <td>f1=87.52</br>f1=86.8</td>
    <td>-0.83%</td>
    <td>60%</br>structured per channel</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>text classification</br>MRPC</td>
    <td>f1=90.26</br>f1=89.85</td>
    <td>-0.46%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Distilbert-base-uncased</td>
    <td>text classification</br>MRPC</td>
    <td>f1=90.26</br>f1=90.88</td>
    <td>+0.69%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=86.92</td>
    <td>-0.79%</td>
    <td>90%</br>structured 4x1</td>
    <td>snip momentum</br>unbalanced</td>  
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=87.73</td>
    <td>+0.14%</td>
    <td>50%</br>structured 2:4</td>
    <td>snip momentum</br>balanced</td>
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Mini</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy=87.61</br>accuracy=86.92</td>
    <td>-0.79%</td>
    <td>50%</br>structured per channel</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>ResNet50</td>
    <td>image recognition</br>ImageNet</td>
    <td>top1 acc = 78.95</br>top1 acc = 80.10</td>
    <td>-1.43%</td>
    <td>75%</br>structured 2x1</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  <tr>
    <td>YOLO-v5s6</td>
    <td>object detection</br>COCO</td>
    <td>AP0.50:0.95/AP0.50=0.404/0.6</br>AP0.50:0.95/AP0.50=0.393/0.584</td>
    <td>-2.72%</td>
    <td>80%</br>unstructured</td>
    <td>snip momentum</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Large</td>
    <td>question answering</br>SQuAD-v1.1</td>
    <td>f1=91.34</br>f1=90.7</td>
    <td>-0.07%</td>
    <td>80%</br>structured 2x1</td>
    <td>group lasso</br>unbalanced</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>MNLI</td>
    <td>[m, mm] = [84.57, 84.79]</br>[m, mm] = [82.45, 83.27]</td>
    <td>[-2.51%, -1.80%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>MNLI</td>
    <td>[m, mm] = [84.57, 84.79]</br>[m, mm] = [83.20, 84.11]</td>
    <td>[-1.62%, -0.80%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  </tr>  
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 91.51</td>
    <td>-0.88%</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>    
  </tr>
  <tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 92.20</td>
    <td>-0.13%</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>       
  </tr>
  <tr>  
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>SST-2</td>
    <td>accuracy = 92.32</br>accuracy = 91.97</td>
    <td>-0.38%</td>
    <td>20%</br>unstructured</td>
    <td>gradient sensitivity</br>balanced</td>       
  </tr>
  <tr>  
  </tr>  
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QQP</td>
    <td>[accuracy, f1] = [91.10, 88.05]</br>[accuracy, f1] = [90.48, 87.06]</td>
    <td>[-0.68%, -1.12%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QQP</td>
    <td>[accuracy, f1] = [91.10, 88.05]</br>[accuracy, f1] = [90.92, 87.78]</td>
    <td>[-0.20%, -0.31%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>   
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QNLI</td>
    <td>accuracy = 91.54</br>accuracy = 90.39</td>
    <td>-1.26%</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>        
  </tr>
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>text classification</br>QNLI</td>
    <td>accuracy = 91.54</br>accuracy = 90.87</td>
    <td>-0.73%</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>      
  </tr>
  <tr>
  </tr>   
  <tr>
    <td>Bert-Base</td>
    <td>question answering</td>
    <td>[em, f1] = [79.34, 87.10]</br>[em, f1] = [77.27, 85.75]</td>
    <td>[-2.61%, -1.54%]</td>
    <td>70%</br>unstructured</td>
    <td>Prune once for all</br>balanced</td>   
  </tr>  
  <tr>
  </tr>
  <tr>
    <td>Bert-Base</td>
    <td>question answering</td>
    <td>[em, f1] = [79.34, 87.10]</br>[em, f1] = [78.03, 86.50]</td>
    <td>[-1.65%, -0.69%]</td>
    <td>50%</br>structured 1:2</td>
    <td>Prune once for all</br>balanced</td>       
  </tr>  
  <tr>
  </tr>  
</tbody>
</table>

## Validated Knowledge Distillation Examples

|  Example Name       | Dataset   | Student<br>(Metrics)                 | Teacher<br>(Metrics)               | Student With Distillation<br>(Metrics Improvement)  | Student With <br>Distributed Distillation<br>(Metrics Improvement)  |
|---------------------|-----------|--------------------------------------|------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| MobileNet example   | CIFAR-10  | MobileNetV2-0.35<br>(0.7965 ACC)     | WideResNet40-2<br>(0.9522 ACC)     |   0.8178 ACC<br>(0.0213 ACC)                        |   0.8235 ACC<br>(0.027 ACC)                        |
| CNN example         | CIFAR-100 | CNN-2<br>(0.5494 ACC)                | CNN-10<br>(0.7153 ACC)             |   0.5540 ACC<br>(0.0046 ACC)                        |   0.5523 ACC<br>(0.0029 ACC)                        |
| VGG example         | CIFAR-100 | VGG-8-BN<br>(0.7022 ACC)             | VGG-13-BN<br>(0.7415 ACC)          |   0.7025 ACC<br>(0.0003 ACC)                        |   NA                        |
| ResNet example      | ImageNet  | ResNet18<br>(0.6739 ACC)             | ResNet50<br>(0.7399 ACC)           |   0.6845 ACC<br>(0.0106 ACC)                        |   NA                        |
| BlendCnn example    |   MRPC    | BlendCnn<br>(0.7034 ACC)             | BERT-Base<br>(0.8382 ACC)          |   0.7034 ACC<br>(0 ACC)                             |   NA                        |
| BiLSTM example      |  SST-2    | BiLSTM<br>(0.8314 ACC)               | RoBERTa-Base<br>(0.9403 ACC)       |   0.9048 ACC<br>(0.0734 ACC)                        |   NA                        |
|DistilBERT example   |  SQuAD    | DistilBERT<br>(0.7323/0.8256 EM/F1)  | BERT-Base<br>(0.8084/0.8814 EM/F1) |   0.7442/0.8371 EM/F1<br>(0.0119/0.0115 EM/F1)      |   NA                        |
|TinyBERT example     |  MNLI     | TinyBERT<br>(0.8018/0.8044 m/mm)     | BERT-Base<br>(0.8363/0.8411 m/mm)  |   0.8025/0.8074 m/mm<br>(0.0007/0.0030 m/mm)        |   NA                        |
|BERT-3 example       |  QQP      | BERT-3<br>(0.8626/0.8213 EM/F1)      | BERT-Base<br>(0.9091/0.8782 EM/F1) |   0.8684/0.8259 EM/F1<br>(0.0058/0.0046 EM/F1)      |   NA                        |
|DistilRoBERTa example|  COLA     | DistilRoBERTa<br>(0.6057 ACC)        | RoBERTa-Large<br>(0.6455 ACC)      |   0.6187 ACC<br>(0.0130 ACC)                        |   NA                        |

## Validated ONNX QDQ INT8 Models on Multiple Hardware through ONNX Runtime

<table class="docutils">
<thead>
  <tr>
    <th class="tg-y3we">Model (ONNX QDQ)</th>
    <th class="tg-pm1l">AWS c6i.2xlarge (Intel)<br>CPU Execution Provider</th>
    <th class="tg-pm1l">AWS c6a.2xlarge (AMD)<br>CPU Execution Provider</th>
    <th class="tg-pm1l">AWS c6g.2xlarge (ARM)<br>CPU Execution Provider</th>
    <th class="tg-8d8j">NVidia A100<br>CUDA Execution<br>Provider</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-cwad">ResNet50</td>
    <td class="tg-pm1l">74.76%</td>
    <td class="tg-pm1l">68.95%</td>
    <td class="tg-pm1l">74.76%</td>
    <td class="tg-6q5x">74.75%</td>
  </tr>
  <tr>
    <td class="tg-cwad">BERT-base</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-6q5x">84.31%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ResNet50 V1.5</td>
    <td class="tg-pm1l">72.20%</td>
    <td class="tg-pm1l">67.70%</td>
    <td class="tg-pm1l">72.20%</td>
    <td class="tg-6q5x">72.29%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V2</td>
    <td class="tg-pm1l">65.82%</td>
    <td class="tg-pm1l">58.56%</td>
    <td class="tg-pm1l">65.83%</td>
    <td class="tg-pm1l">65.63%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD MobileNet V1</td>
    <td class="tg-pm1l">22.45%</td>
    <td class="tg-pm1l">16.53%</td>
    <td class="tg-pm1l">22.45%</td>
    <td class="tg-pm1l">22.35%</td>
  </tr>
  <tr>
    <td class="tg-cwad">DistilBERT base MRPC</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">83.82%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-6q5x">84.56%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SqueezeNet</td>
    <td class="tg-pm1l">56.54%</td>
    <td class="tg-pm1l">53.52%</td>
    <td class="tg-pm1l">56.54%</td>
    <td class="tg-6q5x">56.55%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD</td>
    <td class="tg-pm1l">18.63%</td>
    <td class="tg-pm1l">18.54%</td>
    <td class="tg-pm1l">18.63%</td>
    <td class="tg-6q5x">18.61%</td>
  </tr>
  <tr>
    <td class="tg-cwad">AlexNet</td>
    <td class="tg-pm1l">54.71%</td>
    <td class="tg-pm1l">47.06%</td>
    <td class="tg-pm1l">54.71%</td>
    <td class="tg-pm1l">54.79%</td>
  </tr>
  <tr>
    <td class="tg-cwad">CaffeNet</td>
    <td class="tg-pm1l">56.25%</td>
    <td class="tg-pm1l">52.35%</td>
    <td class="tg-pm1l">56.27%</td>
    <td class="tg-pm1l">56.24%</td>
  </tr>
  <tr>
    <td class="tg-cwad">GoogleNet</td>
    <td class="tg-pm1l">67.73%</td>
    <td class="tg-pm1l">63.56%</td>
    <td class="tg-pm1l">67.72%</td>
    <td class="tg-6q5x">67.76%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ZFNet</td>
    <td class="tg-pm1l">55.86%</td>
    <td class="tg-pm1l">45.09%</td>
    <td class="tg-pm1l">55.86%</td>
    <td class="tg-pm1l">55.89%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Inception V1</td>
    <td class="tg-pm1l">67.21%</td>
    <td class="tg-pm1l">63.03%</td>
    <td class="tg-pm1l">67.20%</td>
    <td class="tg-6q5x">67.21%</td>
  </tr>
  <tr>
    <td class="tg-cwad">SSD MobileNet V1 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">22.86%</td>
    <td class="tg-pm1l">16.94%</td>
    <td class="tg-pm1l">22.80%</td>
    <td class="tg-pm1l">22.87%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Mobile bert MRPC</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">84.56%</td>
    <td class="tg-pm1l">85.54%</td>
    <td class="tg-pm1l">85.54%</td>
  </tr>
  <tr>
    <td class="tg-cwad">Roberta base MRPC</td>
    <td class="tg-pm1l">89.46%</td>
    <td class="tg-pm1l">90.44%</td>
    <td class="tg-pm1l">89.71%</td>
    <td class="tg-pm1l">89.71%</td>
  </tr>
  <tr>
    <td class="tg-cwad">ResNet50 V1.5 MLPerf</td>
    <td class="tg-pm1l">76.14%</td>
    <td class="tg-pm1l">72.80%</td>
    <td class="tg-pm1l">76.14%</td>
    <td class="tg-6q5x">76.17%</td>
  </tr>
  <tr>
    <td class="tg-cwad">VGG16</td>
    <td class="tg-pm1l">66.69%</td>
    <td class="tg-pm1l">64.25%</td>
    <td class="tg-pm1l">66.69%</td>
    <td class="tg-pm1l">66.64%</td>
  </tr>
  <tr>
    <td class="tg-cwad">VGG16 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">72.31%</td>
    <td class="tg-pm1l">69.35%</td>
    <td class="tg-pm1l">72.32%</td>
    <td class="tg-pm1l">72.34%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V3 MLPerf</td>
    <td class="tg-pm1l">75.57%</td>
    <td class="tg-pm1l">70.78%</td>
    <td class="tg-pm1l">75.56%</td>
    <td class="tg-6q5x">75.52%</td>
  </tr>
  <tr>
    <td class="tg-cwad">EfficientNet</td>
    <td class="tg-pm1l">77.61%</td>
    <td class="tg-pm1l">76.52%</td>
    <td class="tg-pm1l">77.56%</td>
    <td class="tg-pm1l">77.60%</td>
  </tr>
  <tr>
    <td class="tg-cwad">MobileNet V2 (ONNX Model Zoo)</td>
    <td class="tg-pm1l">68.51%</td>
    <td class="tg-pm1l">62.48%</td>
    <td class="tg-pm1l">68.58%</td>
    <td class="tg-pm1l">68.48%</td>
  </tr>
  <tr>
    <td class="tg-413a">ShuffleNet V2</td>
    <td class="tg-pm1l">66.12%</td>
    <td class="tg-pm1l">58.41%</td>
    <td class="tg-pm1l">66.11%</td>
    <td class="tg-pm1l">66.11%</td>
  </tr>
</tbody>
</table>

