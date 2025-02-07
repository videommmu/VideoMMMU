# <img src="./assets/pyramid-chart.png" alt="Video-MMMU Icon" style="height: 30px; vertical-align: middle;"> Video-MMMU: Evaluating Knowledge Acquisition from Multi-Discipline Professional Videos


🏠 [LMMs-Lab Homepage](https://lmms-lab.framer.ai) | <a href="https://emoji.gg/emoji/1684-discord-thread"><img src="https://cdn3.emoji.gg/emojis/1684-discord-thread.png" width="14px" height="14px" alt="Discord_Thread"></a> [discord/lmms-eval](https://discord.gg/zdkwKUqrPy) | 🎓 [Project Page](https://videommmu.github.io/) |📝 [Arxiv Paper](https://arxiv.org/abs/2501.13826)

---

## Annoucement
- [2025-1] 🎉🎉 We introduce [VideoMMMU](https://videommmu.github.io/), a massive, multi-modal, multi-disciplinary video benchmark that evaluates the knowledge acquisition capability from educational videos.

## Evaluation
The evaluation of VideoMMMU is integrated into [LMMs-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval/tree/main). Below is a detailed instruction of the evaluation.

## Installation

For formal usage, you can install the package from PyPI by running the following command:
```bash
pip install lmms-eval
```

For development, you can install the package by cloning the repository and running the following command:
```bash
git clone https://github.com/EvolvingLMMs-Lab/lmms-eval
cd lmms-eval
pip install -e .
```

If you want to test LLaVA, you will have to clone their repo from [LLaVA](https://github.com/haotian-liu/LLaVA) and
```bash
git clone https://github.com/LLaVA-VL/LLaVA-NeXT
cd LLaVA-NeXT
pip install -e .
```

## Command

**Evaluation of LLaVA-OneVision on VideoMMMU**

```bash
accelerate launch --num_processes=1 --main_process_port 12345 -m lmms_eval \
--model llava_onevision \
--model_args pretrained=lmms-lab/llava-onevision-qwen2-7b-ov,conv_template=qwen_1_5,model_name=llava_qwen,max_frames_num=32,torch_dype=bfloat16 \
    --tasks video_mmmu \
    --batch_size 1 \
    --log_samples \
    --log_samples_suffix debug \
    --output_path ./logs/
```

**Evaluate a single track of VideoMMMU**

```bash
accelerate launch --num_processes=1 --main_process_port 12345 -m lmms_eval \
--model llava_onevision \
--model_args pretrained=lmms-lab/llava-onevision-qwen2-7b-ov,conv_template=qwen_1_5,model_name=llava_qwen,max_frames_num=32,torch_dype=bfloat16 \
    --tasks video_mmmu_perception \
    --batch_size 1 \
    --log_samples \
    --log_samples_suffix debug \
    --output_path ./logs/
```

**Evaluate the question_only track of VideoMMMU (Knowledge Acquisition Experiment)**

```bash
accelerate launch --num_processes=1 --main_process_port 12345 -m lmms_eval \
--model llava_onevision \
--model_args pretrained=lmms-lab/llava-onevision-qwen2-7b-ov,conv_template=qwen_1_5,model_name=llava_qwen,max_frames_num=1,torch_dype=bfloat16 \
    --tasks video_mmmu_adaptation_question_only \
    --batch_size 1 \
    --log_samples \
    --log_samples_suffix debug \
    --output_path ./logs/
```

## Citation

```shell
@article{hu2025videommmu,
    title={Video-MMMU: Evaluating Knowledge Acquisition from Multi-Discipline Professional Videos},
    author={Kairui Hu and Penghao Wu and Fanyi Pu and Wang Xiao and Yuanhan Zhang and Xiang Yue and Bo Li and Ziwei Liu},
    booktitle={arXiv preprint arXiv:2501.13826},
    year={2025},
    url={https://arxiv.org/abs/2501.13826}
}

