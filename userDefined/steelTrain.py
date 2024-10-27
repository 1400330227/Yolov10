from ultralytics import YOLOv10

# 模型配置文件
model_yaml_path = "ultralytics/cfg/models/v10/yolov10n.yaml"
# 数据集配置文件
data_yaml_path = 'datasets/steelPlate/data.yaml'
# 预训练模型
pre_model_name = './models/yolov10n.pt'

if __name__ == '__main__':
    model = YOLOv10(model_yaml_path).load(pre_model_name)
    results = model.train(data=data_yaml_path, epochs=15, batch=4, name='train_v10')