import json
import os
import argparse
from OmniParser.omniparser import Omniparser

def parse_jsonl(data, data_name):
    with open(data_name, mode='w') as writer:
        for j in range(len(data)):
            jsonresponse=json.dumps(data[j], ensure_ascii=False)
            writer.write(jsonresponse+'\n')

def main():
    parser = argparse.ArgumentParser(description="Run DeskVision Detector module.")
    parser.add_argument("--image_path", type=str, default="images/")
    parser.add_argument("--annotated_path", type=str, default='annotated_images/')
    parser.add_argument("--output_file", type=str, default='Deskvision_detector.jsonl')
    args = parser.parse_args()

    image_paths = args.image_path
    files = os.listdir(image_files)
    file_path = [image_files+x for x in files]
    res = []
    config = {
        'som_model_path': 'OmniParser/weights/icon_detect_v2/model.pt',
        'device': 'cuda',
        'imgsz': 640,
        'iou_threshold': 0.1,
        'box_threshold': 0.15
    }
    parser = Omniparser(config)
    for i in range(len(file_path)):
        image_path = file_path[i]
        save_path = args.annotated_path + str(i)+'.png'
        try:
            label_coordinates = parser.parse(image_path, save_path, deskvision=True)
        except:
            continue
        boxes = []
        for id, bbox in label_coordinates.items():
            bbox = [int(bbox[0]), int(bbox[1]), int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])]
            boxes.append({'id': id, 'bbox': bbox})
        res.append({'ori_path':image_path, 'annotated_path':save_path, 'boxes':boxes})
        if i%500 == 0:
            parse_jsonl(res, args.output_file)

    parse_jsonl(res, args.output_file)
    
if __name__ == "__main__":
    main()