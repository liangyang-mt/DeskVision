# DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents

<p align="center">
<a href="./README.md">English</a>|<a href="./README.zh.md">简体中文</a>
</p>  

<div align="center">

[\[💻Code\]](https://github.com/MooreThreads/GUIExplorer)[\[📝Paper\]](https://arxiv.org/abs/2503.11170) [\[🤗Models\]](https://huggingface.co/caca9527/GUIExplorer)[\[🤗Data\]](https://huggingface.co/datasets/caca9527/DeskVision)  

</div>

## 🤗 项目概述  

<div align=center><img width="60%" height="60%" src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/overview.png"/></div>


🔥🔥🔥 我们开源了自研的GUI多模态视觉理解大模型GUIExplorer以及用于训练该模型的DeskVision部分数据集（完整数据集正在整理并给出），该模型基于llava架构，不仅在开源GUI理解benchmark下取得与前沿方案相近甚至更优的视觉理解效果。在GUI理解功能上同时支持Visual Grounding，单步指令执行的能力。后续我们会继续开发该模型，使其具备交互对话能力，完备GUI Agent功能。

## 📝 开源计划

- [x] 推理代码
- [x] GUI理解预训练模型（7B）
- [x] Gradio demo（包含基础GUI理解功能 
- [x] 技术报告或论文  
- [x] 训练数据  
- [ ] 完整复杂指令多步执行Agent模型
- [ ] 训练代码  


## 🎞️ 示例 

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

**2. 单步指令执行**

<table class="center">

<tr>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/ins_1.png">
    </td>
    <td width=50% style="border: none">
        <img src="https://github.com/MooreThreads/GUIExplorer/blob/main/assets/ins_2.png">
    </td>
</tr>
</table>


**本项目也提供本地gradio demo部署代码，欢迎部署体验。**

## ⚒️ 安装

**1. 环境部署**

```bash  
git clone https://github.com/MooreThreads/GUIExplorer
cd GUIExplorer
conda create -n llava python=3.10 -y
conda activate llava
pip install --upgrade pip  # Enable PEP 660 support.
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -e ".[train]"
pip install -e ".[train]"       # 如果这条指令装库很慢，可以指定清华源（上面这条指令）
```

**2. 权重下载**

开源权重请访问[huggingface](https://huggingface.co/caca9527/GUIExplorer)下载，并将下载的模型权重放置在`./pretrained_weights`文件夹下。目前已提供7B预训练模型。

## 🚀 推理  
**1. 推理脚本** 

```shell
cd ./scripts/inference  
python infer.py --task xx --input_text xx --input_image xx
``` 

输入参数说明：  
|接口名 |输入值类型 | 默认值 | 物理意义 |  
|:-----|:----------|:---------|:-------|     
|task|str    |"grounding"|任务类型，目前支持"ocr", "grounding"和"instruction"|
|input_text|str  |""|输入文本。如果任务是"ocr"，输入待识别区域的绝对坐标"[x1,y1,x2,y2]"; "grounding"则输入待定位内容；其它则为指令；|
|input_image|str   |""|输入图像的路径|

输出说明：
ocr，定位或指令执行的可视化结果。

**2. 🎨 Gradio Demo**  

```shell 
cd ./scripts/inference
python demo.py
```  

该demo提供几个"grounding"和"instruction"的示例。

## 📝附录

## 数据集介绍

**1. DeskVision** 

我们开源了生成DeskVision数据的代码，其包含Detector和Captioner两个工具，具体使用方式详见```./scripts/DeskVision```。并且我们开源了基于这些工具下生成的DeskVision数据（部分），由于数据合法性原因，自建图片数据采用url方式呈现，具体数据内容详见[\[🤗Data\]](https://huggingface.co/datasets/caca9527/DeskVision)，更多数据后续会持续补充。我们也针对[OS-Atlas](https://osatlas.github.io/)开源的Desktop完整图片数据进行Region Caption生成，并也将相关annotations进行开源。 


**2. GUI理解benchmarks**

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


## Citation

如果你使用了我们的GUIExplorer或DeskVision数据集，麻烦引用我们的[\[📝Paper\]](https://arxiv.org/abs/2503.11170)：

```bibtex
@misc{xu2025deskvisionlargescaledesktop,
      title={DeskVision: Large Scale Desktop Region Captioning for Advanced GUI Agents}, 
      author={Yibin Xu and Liang Yang and Hao Chen and Hua Wang and Zhi Chen and Yaohua Tang},
      year={2025},
      eprint={2503.11170},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.11170}, 
}
```


## ⚖️ 声明

该项目所开源的代码，模型及数据集旨在用于学术研究，我们明确不对用户生成的内容承担任何责任。用户对使用模型和相关数据集时的行为承担全部责任。项目贡献者与用户的行为没有法律关系，也不承担任何责任。

## 🙏🏻 感谢
非常感谢[LLaVA-OneVision](https://llava-vl.github.io/blog/2024-08-05-llava-onevision/), [OS-Atlas](https://osatlas.github.io/), [SeeClick](https://github.com/njucckevin/SeeClick)等优秀的开源工作及数据集。

