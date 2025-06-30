<p align="center">
<a href="./README.zh.md">简体中文</a>|<a href="./README.md">English</a>
</p>  

<div align="center">

[\[🤗DeskVision-Captioner\]](https://huggingface.co/DanHuang/DeskVision-Captioner/tree/main)

</div>

# DeskVision 数据生成pipeline
## 环境准备
```shell
cd OmniParser
conda create -n omni python=3.10
pip install -r requirements.txt
conda activate omni
```

## Detector
1. 运行 Detector.py，使用 OmniParser、PaddleOCR 等模块解析图片中的可交互 UI 元素，并保存打标记后的图片。其中，[OmniParser](https://github.com/microsoft/OmniParser)需要自行下载，并实现omniparser.py。
```python
python Detector.py --image_path 'images' --annotated_path 'annotated_images' --output_file 'Deskvision_detector.jsonl'
```

## Captioner
1. 使用下面的 shell 脚本，启动 Captioner 模型服务。
```shell
bash deploy.sh
```
2. 运行 Captioner。
```python
python Captioner.py --detector_path 'Deskvision_detector.jsonl' --output_file 'Deskvision.jsonl'
```