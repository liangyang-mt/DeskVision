MODEL_PATH="Captioner-checkpoint"   
MODEL_NAME="captioner"
CUDA_VISIBLE_DEVICES=0,1,2,3
MAX_PIXELS=3156000
# deploy
vllm serve ${MODEL_PATH} \
    --port 8001 \
    --host 0.0.0.0 \
    --dtype bfloat16 \
    --tensor_parallel_size 4 \
    --limit-mm-per-prompt image=5 \
    --served-model-name "${MODEL_NAME}"