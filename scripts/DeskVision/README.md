<p align="center">
<a href="./README.zh.md">简体中文</a>|<a href="./README.md">English</a>
</p>  

<div align="center">

[\[🤗DeskVision-Captioner\]](https://huggingface.co/DanHuang/DeskVision-Captioner/tree/main)

</div>

# DeskVision Data Automatic Generation Pipeline
## Environment Preparation
```shell
cd OmniParser
conda create -n omni python=3.10
pip install -r requirements.txt
conda activate omni
```

## Detector
1. Run Detector.py, use modules such as OmniParser and PaddleOCR to parse interactive UI elements in the image, and save the annotated image. Among them, [OmniParser](https://github.com/microsoft/OmniParser) needs to be downloaded separately, and omniparser.py needs to be implemented.
```python
python Detector.py --image_path 'images' --annotated_path 'annotated_images' --output_file 'Deskvision_detector.jsonl'
```

## Captioner
1. Use the following shell script to start the Captioner model service.
```shell
bash deploy.sh
```
2. run Captioner.
```python
python Captioner.py --detector_path 'Deskvision_detector.jsonl' --output_file 'Deskvision.jsonl'
```