# DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents

<p align="center">
<a href="./README.zh.md">简体中文</a>|<a href="./README.md">English</a>
</p>  

<div align="center">

[\[💻Code\]](https://github.com/MooreThreads/GUIExplorer)[\[📝Paper\]](https://arxiv.org/abs/2503.11170) [\[🤗Models\]](https://huggingface.co/caca9527/GUIExplorer)[\[🤗Data\]](https://huggingface.co/datasets/caca9527/DeskVision)  

</div>

## 🤗 Overview  

<div align=center><img width="760" height="300" src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/overview.png"/></div>

🔥🔥🔥 We have open-sourced our self-developed GUI multimodal visual understanding model GUIExplorer and part of the DeskVision dataset used to train the model (the complete dataset is being compiled and will be provided later). The model is based on the llava architecture and not only achieves visual understanding results similar to or even better than those of cutting-edge solutions under the open source GUI understanding benchmark, but also supports Visual Grounding and the ability to execute single-step instructions in terms of GUI understanding functions. We will continue to develop the model in the future to enable it to have interactive dialogue capabilities and complete GUI Agent functions.

## 📝 Release Plans

- [x] Inference scripts
- [x] Pre-trained model for GUI understanding (7B)
- [x] Gradio demo (supporting specified GUI understanding functions)  
- [x] Technical report or paper 
- [x] Training data  
- [ ] Complete multi-step execution Agent model of complex instructions   
- [ ] Training scripts

## 🎞️ Examples 


**1. Grounding**

<table class="center">

<tr>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/grounding_1.png">
    </td>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/grounding_2.png">
    </td>
</tr>
</table>

**2. single-step instruction execution**

<table class="center">

<tr>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/ins_1.png>
    </td>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/ins_2.png">
    </td>
</tr>
</table>


**This project also provides local gradio demo deployment code. Welcome to deploy and experience it.**

## ⚒️ Installation

**1. Build Environtment**

```bash  
git clone https://github.com/MooreThreads/GUIExplorer
cd GUIExplorer
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # Enable PEP 660 support.
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -e ".[train]"  
# If this command is very slow to load the library, you can specify the Tsinghua source (the above command)  
pip install -e ".[train]"       
```

**2. Download weights**

For open source weights, please visit [huggingface](https://huggingface.co/caca9527/GUIExplorer) to download, and place the downloaded model weights in the `./pretrained_weights` folder. Currently, 7B pre-trained models are provided.

## 🚀 Inference   
**1. Inference commands**

```shell
cd ./scripts/inference  
python infer.py --task xx --input_text xx --input_image xx
``` 

Input parameter description:    
|parameter name |type | default | parameter description |  
|:-----|:----------|:---------|:-------|     
|task|str    |"grounding"|Task type, currently supported "ocr", "grounding" and "instruction"|
|input_text|str  |""|Input text. If it is "ocr", enter the absolute coordinates "[x1,y1,x2,y2]" of the area to be identified; "grounding" means enter the content to be located; others are instructions;|
|input_image|str   |""|Input image path|

Output description:  
A visualization results of ocr, grounding or instruction execution.

**2. 🎨 Gradio Demo**

```shell 
cd ./scripts/inference
python demo.py
```  

The demo provides several examples of "grounding" and "instruction".

## 📝Appendix

## Dataset introduction

**1. DeskVision** 

We have open-sourced the code for generating DeskVision data, which includes two tools, Detector and Captioner. For details on how to use them, see ```./scripts/DeskVision```. We have also open-sourced (part of) the DeskVision data generated based on these tools. Due to data legitimacy reasons, self-built image data is presented in URL format. For details of the data content, see [\[🤗Data\]](https://huggingface.co/datasets/caca9527/DeskVision). More data will be added in the future. We also generate Region Captions for the open source Desktop complete image data of [OS-Atlas](https://osatlas.github.io/), and also open source the related annotations.

**2. GUI Understanding Benchmarks**  

**a. [ScreenSpot](https://huggingface.co/datasets/rootsautomation/ScreenSpot)**  

| Models      | Model Size | GUI Specific | Mobile Text | Mobile Icon/Widget | Desktop Text | Desktop Icon/Widget | Web Text | Web Icon/Widget | Average |
|------------|------------|--------------|-------------|--------------------|--------------|---------------------|----------|-----------------|---------|
| MiniGPT-v2 | 7B         | ❌            | 8.4        | 6.6               | 6.2         | 2.9                | 6.5     | 3.4            | 5.7    |
| GPT-4V     | -          | ❌            | 22.6       | 24.5              | 20.2        | 11.8               | 9.2     | 8.8            | 16.2   |
| Qwen2-VL    | 7B       |  ✅         | 61.34        | 39.29               | 51.01         | 44.98                | 33.04     | 21.84   | 42.89  |
| Fuyu       | 8B         | ✅            | 41.0       | 1.3               | 33.0        | 3.6                | 33.9    | 4.4            | 19.5   |
| CogAgent   | 18B        | ✅            | 67.0       | 24.0              | 74.2        | 20.0               | 70.4    | 28.6           | 47.4   |
| SeeClick   | 9.6B       | ✅            | 78.0       | 52.0              | 72.2        | 30.0               | 55.7    | 32.5           | 53.4   |
| UGround   | 7B       | ✅            | 82.8       | 60.3              | 82.5        | 63.6               | 80.4    | 70.4           | 73.3   |
| OmniParser(w. LS+ID)   | -       | ✅            | **93.9**       | 57              | 91.3        | 63.6               | 81.3    | 51           | 73   |
| OS-Atlas-Base   | 7B         | ✅            | 93.4       | 72.93              | **91.75**        | 62.86               | **90.87**    | 74.27           | 82.47   |
| GUIExplorer   | 7B         | ✅            | 89.01       | **77.29**              | 88.14        | **75.0**               | 82.61    | **81.55**           | **82.86**   |

**b. [GUIEnv](https://huggingface.co/datasets/yiye2023/GUIEnv)**

| Models      | Bbox2Text    |             | Text2Bbox    |              |              |              |
|------------|--------------|-------------|--------------|--------------|--------------|--------------|
|            | **EM Score**     | **F1 Score**    | **IoU@0.2**      | **IoU@0.5**      | **IoU@0.7**      | **Center@acc**   |
| MiniCPM-GUI      |   44.12      | 64.78       | 68.02       | 47.96       | 23.28       |   -        |
| SeeClick  |     5.19         | 8.59       | 53.34        |   24.58      | 5.55        |      56.85       |
| UGround  |     -         | -       | -        |   -      | -        |      63.76       |
| OS-Atlas-Base  |     42.33         | 60.51       | 76.33        |   59.68      | 41.9        |      75.76       |
| GUIExplorer  |     **54.60**         | **78.71**       | **88.51**        |   **82.56**      | **62.17**        |      **87.66**       |

