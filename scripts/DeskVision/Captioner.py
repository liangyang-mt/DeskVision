import json
import base64
import argparse
from openai import OpenAI

def encode_image(image_path):
      with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
def parse_jsonl(data, data_name):
    with open(data_name, mode='w') as writer:
        for j in range(len(data)):
            jsonresponse=json.dumps(data[j], ensure_ascii=False)
            writer.write(jsonresponse+'\n')

def main():
    parser = argparse.ArgumentParser(description="Run DeskVision Detector module.")
    parser.add_argument("--detector_path", type=str, default="Deskvision_detector.jsonl")
    parser.add_argument("--output_file", type=str, default='Deskvision.jsonl')
    args = parser.parse_args()
    
    data = []
    with open(args.detector_path) as f:
        for item in f:
            data.append(json.loads(item))

    client = OpenAI(
        base_url="http://localhost:8001/v1",
        api_key="sk-xxx")

    res = []
    for i in range(len(data)):
        image_path = data[i]['annotated_path']
        region_caption = []
        base64_image = encode_image(image_path)
        boxes = data[i]['boxes']
        num = len(boxes)-1
        if num!=0:
            prompt = (
                f'请仔细观察上面标注过图像，找到每个编号过的边界框(ID: 0-{num})，'
                '并生成这些区域 UI 元素的描述。UI 元素的描述应该包括这个 UI 元素的类型(按钮、输入框、图标、下拉框等)，'
                '以及任何可见的文字，并且简单明了。\n'
                '你的输出必须严格遵守 JSON 格式: '
                '{{"caption_pairs": [{{"id": "...", "caption": "..."}} , ...]}}'
            )
        else:
            promot = '用光栅顺序扫描上面标注过图像，找到每个编号过的边界框(ID: 0)，并生成这些区域 UI 元素的描述。UI 元素的描述应该包括这个 UI 元素的类型(按钮、输入框、图标、下拉框等)，以及任何可见的文字，并且简单明了。\n你的输出必须严格遵守 JSON 格式: {"caption_pairs": [{"id": "...", "caption": "..."} , ...]}'
        completion = client.chat.completions.create(
            model="captioner",
            messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": [
                    {"type": "image_url", 
                    "image_url": {
                        "url":  f"data:image/jpeg;base64,{base64_image}"}
                    },
                    {"type": 'text', "text": prompt}
                    ]
                }
                ],
            max_tokens=1024,
            temperature=0.5,
            extra_body={
                    "repetition_penalty": 1,
            },)
        json_str = completion.choices[0].message.content.replace('```json','').replace('```','').strip()
        try:
            caption_pairs = json.loads(json_str)['caption_pairs']
        except:
            continue
        if len(caption_pairs)!=len(boxes):
            continue
        for j in range(len(caption_pairs)):
            region_caption.append({'id':caption_pairs[j]['id'], 'caption':caption_pairs[j]['caption'], 'bbox':boxes[caption_pairs[j]['id']]})
        res.append({'ori_path':data[i]['ori_path'], 'annotated_path':image_path, 'region_captions':region_caption})
        if (len(res)-1)%500 == 0:
            parse_jsonl(res, args.output_file)

    parse_jsonl(res, args.output_file)