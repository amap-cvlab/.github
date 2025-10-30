# Alibaba AMAP CV Lab

[中文阅读](README_zh.md)

# 👋 About Us

The Alibaba AMAP CV Lab focuses on cutting-edge research and innovative applications centered around computer vision technology, dedicated to building the core technological capabilities of the spatiotemporal internet. 
Positioned at the intersection of the physical and digital worlds, we empower smart mobility, daily life, and virtual spaces through AI-driven understanding and generation.

As the core technical driving force behind AMAP, our research spans the entire chain from perception to generation, and from human-centric intelligence to world modeling. 
We are structured into six major research domains:
- 🗺️ Map & Autonomous Driving: Integrating multimodal perception with high-definition map generation to enable spatial semantic understanding and regulation-aware intelligent driving.
- 🧍 Human-Centric AI: Building AI systems that understand human emotion, identity, and behavior to achieve natural visual generation and interaction.
- 🧭 Embodied Intelligence: Studying agents that perceive, plan, and act within both virtual and physical environments, unifying vision, language, and motion intelligence.
- 🌐 World Modeling: Constructing dynamic, interactive models of the world to empower AI with the ability to understand, predict, and generate complex environments.
- 🧊 3D Generation & Reconstruction: Advancing 3D scene modeling, rendering, and generation with continuous level-of-detail control and physically realistic synthesis.
- 🧠 General Deep Learning: Exploring general representation learning, model optimization, and multimodal alignment as foundational algorithms for spatiotemporal intelligence.

The AMAP CV Lab stands at the forefront of computer vision research and application, serving as a key technological practitioner in Alibaba’s spatial intelligent internet.
We believe that AI’s ability to understand the world defines the future of intelligent mobility and everyday life.

---

_We welcome contributions, issues, and feedback!_  
Feel free to ⭐ the repos below to stay updated.

# 🔈 Latest News

- 🏛 **Sep, 2025** – Our paper [**FutureSightDrive**](https://miv-xjtu.github.io/FSDrive.github.io/) is accepted by NeurIPS 2025 (Spotlight).
- 🏛 **Jul, 2025** – Our paper [**FantasyTalking**](https://fantasy-amap.github.io/fantasy-talking/) is accepted by ACM MM 2025.
- 🏛 **Jun, 2025** – Our paper [**SeqGrowGraph**](https://openaccess.thecvf.com/content/ICCV2025/papers/Xie_SeqGrowGraph_Learning_Lane_Topology_as_a_Chain_of_Graph_Expansions_ICCV_2025_paper.pdf) is accepted by ICCV 2025.
- 📢 **May, 2025** – We released the full project of [**FSDrive**](https://miv-xjtu.github.io/FSDrive.github.io/).
- 🏛 **Apr, 2025** – Our paper [**G3PT**](https://arxiv.org/abs/2409.06322) is accepted by IJCAI 2025.
- 📢 **Apr, 2025** – We released the inference code and model weights of [**FantasyTalking**](https://fantasy-amap.github.io/fantasy-talking/), [**FantasyID**](https://fantasy-amap.github.io/fantasy-id/).

# 🔧 Public Technologies

## 🗺️ Map & Autonomous Driving

The core of our research lies in integrating perception, mapping, and decision-making for intelligent transportation. We develop next-generation 3D map engines, traffic rule reasoning, and scene-level behavior modeling, enabling AI to understand spatial context and make interpretable decisions in real-world urban environments.
<br><br>

### 🚘 FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving

[![Project](https://img.shields.io/badge/🌐%20%20Project-FSDrive-blue.svg)](https://miv-xjtu.github.io/FSDrive.github.io/)
[![arXiv](https://img.shields.io/badge/Arxiv-2505.17685-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2505.17685)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/MIV-XJTU/FSDrive)
![GitHub Stars](https://img.shields.io/github/stars/MIV-XJTU/FSDrive)

The first VLA for autonomous driving visual reasoning, which proposes spatio-temporal CoT to think visually about trajectory planning and unifies visual generation and understanding with minimal data.
<br><br>

### 📑 SeqGrowGraph: Learning Lane Topology as a Chain of Graph Expansions

[![arXiv](https://img.shields.io/badge/Arxiv-2507.04822v1-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2507.04822v1)

A generative framework that reframes lane network learning as a process of incrementally building an adjacency matrix.
<br><br>

### 🚗 Driving by the Rules: A Benchmark for Integrating Traffic Sign Regulations into Vectorized HD Map

[![Project](https://img.shields.io/badge/🌐%20%20Project-MapDR-blue.svg)](https://amap-cvlab.github.io/DriveByTheRules/)
[![arXiv](https://img.shields.io/badge/Arxiv-2410.23780-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2410.23780)

Benchmark and multi-modal approach for integrating lane-level traffic sign regulations into vectorized HD maps.
<br><br>

## 🤖 Human-Centric AI

Centered on generative AI, our digital human research advances from driven generation to autonomous action. Through the Fantasy AIGC model family, we achieve expressive, identity-consistent, and physically realistic video generation via multimodal diffusion and 3D-aware modeling.
<br><br>

### 🗣️ FantasyTalking: Realistic Talking Portrait Generation via Coherent Motion Synthesis

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyTalking-blue.svg)](https://fantasy-amap.github.io/fantasy-talking/)
[![arXiv](https://img.shields.io/badge/Arxiv-2504.04842-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2504.04842)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-talking)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-talking)
[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/acvlab/FantasyTalking)
[![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-FFD21E.svg)](https://huggingface.co/spaces/acvlab/FantasyTalking)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/amap_cvlab/FantasyTalking)

The first Wan-based high-fidelity audio-driven avatar system that synchronizes facial expressions, lip motion, and body gestures in dynamic scenes through dual-stage audio-visual alignment and controllable motion modulation.
<br><br>

### 🤡 FantasyPortrait: Enhancing Multi-Character Portrait Animation with Expression-Augmented Diffusion Transformers

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyPortrait-blue.svg)](https://fantasy-amap.github.io/fantasy-portrait/)
[![arXiv](https://img.shields.io/badge/Arxiv-2507.12956-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2507.12956)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-portrait)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-portrait)

A novel expression-driven video-generation method that pairs emotion-enhanced learning with masked cross-attention, enabling the creation of high-quality, richly expressive animations for both single and multi-portrait scenarios.
<br><br>

### 🗣️ FantasyTalking2: Timestep-Layer Adaptive Preference Optimization for Audio-Driven Portrait Animation

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyTalking2-blue.svg)](https://fantasy-amap.github.io/fantasy-talking2/)
[![arXiv](https://img.shields.io/badge/Arxiv-2508.11255v1-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2508.11255v1)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-talking2)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-talking2)

A novel Timestep-Layer Adaptive Multi-Expert Preference Optimization (TLPO) method enhances the quality of audio-driven avatar in three dimensions: lip-sync, motion naturalness, and visual quality.
<br><br>

### 🆔 FantasyID: Face Knowledge Enhanced ID-Preserving Video Generation

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyID-blue.svg)](https://fantasy-amap.github.io/fantasy-id/)
[![arXiv](https://img.shields.io/badge/Arxiv-2502.13995-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2502.13995)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-id)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-id)
[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/acvlab/FantasyID)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/amap_cvlab/FantasyID)

A tuning-free text-to-video model that leverages 3D facial priors, multi-view augmentation, and layer-aware guidance injection to deliver dynamic, identity-preserving video generation.
<br><br>

### 🗿 FantasyHSI: Video-Generation-Centric 4D Human Synthesis In Any Scene through A Graph-based Multi-Agent Framework

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyHSI-blue.svg)](https://fantasy-amap.github.io/fantasy-hsi/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.01232-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.01232)
[![GitHub](https://img.shields.io/badge/Code%20%28Comming%20Soon%29-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-hsi)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-hsi)

A graph-based multi-agent framework that grounds video generation within 3D world dynamics, enabling digital humans to perceive, plan, and act autonomously, thus serving as the technical bridge that links human modeling to world modeling through unified perception–action reasoning.
<br><br>

### 💃🏻 HumanRig: Learning Automatic Rigging for Humanoid Characters in Animation

[![Project](https://img.shields.io/badge/🌐%20%20Project-HumanRig-blue.svg)](https://c8241998.github.io/HumanRig/)
[![arXiv](https://img.shields.io/badge/Arxiv-2412.02317-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2412.02317)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/c8241998/HumanRig)
![GitHub Stars](https://img.shields.io/github/stars/c8241998/HumanRig)
[![HuggingFace Dataset](https://img.shields.io/badge/🤗-HuggingFace%20Dataset-FFD21E.svg)](https://huggingface.co/datasets/jellyczd/HumanRig)

The first dataset for automatic rigging of 3D generated digital humans and a transformer-based end-to-end automatic rigging algorithm.
<br><br>

## 🧭 Embodied AI

We study perception, reasoning, and action of intelligent agents in both virtual and physical environments. By integrating vision-language models and reinforcement learning, we build embodied agents capable of environmental perception, goal planning, and task execution, forming a unified cognitive foundation for robots and digital humans.
<br><br>

### CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

[![Project](https://img.shields.io/badge/🌐%20%20Project-CE-Nav-blue.svg)](https://ce-nav.github.io/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.23203-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.23203)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/CE-Nav)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/CE-Nav)

A novel cross-embodiment local navigation framework, which can serve as a "one brain, multiple forms", plug-and-play fast system.
<br><br>

### OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation

[![arXiv](https://img.shields.io/badge/Arxiv-2509.25687-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.25687)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/OmniNav)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/OmniNav)

OmniNav is a unified embodied navigation framework that combines a lightweight, real-time (up to 5 Hz) continuous waypoint policy with a fast–slow planning architecture and large-scale vision-language multi-task training to robustly handle instruction-, object-, and point-goal navigation and frontier exploration, achieving state-of-the-art performance and real-world validation.
<br><br>

### 🧠 JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

[![Project](https://img.shields.io/badge/🌐%20%20Project-JanusVLN-blue.svg)](https://miv-xjtu.github.io/JanusVLN.github.io/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.22548-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.22548)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/MIV-XJTU/JanusVLN)
![GitHub Stars](https://img.shields.io/github/stars/MIV-XJTU/JanusVLN)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/misstl/JanusVLN_Extra)

The first visual-language navigation agent with dual implicit memory decouples visual semantics and spatial perception and models them respectively as compact implicit neural representations.
<br><br>

### Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA

[![arXiv](https://img.shields.io/badge/Arxiv-2509.26251-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.26251)

A Robust Vision-Language-Action Framework with Structural Perception and Explicit Dynamics Reasoning.
<br><br>

## 🌐 World Modeling

We aim to construct dynamic, interactive world models for understanding, predicting, and generating physically consistent spatiotemporal phenomena. By leveraging multimodal modeling and generative learning, our research enables a perception-to-simulation loop that empowers AI to comprehend and recreate the real world.
<br><br>

### 🌏 FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction

[![arXiv](https://img.shields.io/badge/Arxiv-2509.21657-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.21657)

A unified world model integrating video priors and geometric grounding for synthesizing explorable and geometrically consistent 3D scenes.
<br><br>

### World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training

[![arXiv](https://img.shields.io/badge/Arxiv-2509.24948-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.24948)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/junjxiao/world-env)
![GitHub Stars](https://img.shields.io/github/stars/junjxiao/world-env)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/junjxiao/world-env)

A novel framework leveraging world model as a virtual environment for VLA post training.
<br><br>

## 🧊 3D Generation & Reconstruction

Our research in 3D generation and reconstruction covers Gaussian Splatting, NeRF, and 3D-aware diffusion, aiming for real-time rendering, continuous level-of-detail control, and semantically consistent 3D scene synthesis.
<br><br>

### 🧸 G3PT: Unleash the Power of Autoregressive Modeling in 3D Generative Tasks

[![arXiv](https://img.shields.io/badge/Arxiv-2409.06322-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2409.06322)

The first native 3D generation foundational model based on next-scale autoregression.
<br><br>

### 🏙 Global-Guided Focal Neural Radiance Field for Large-Scale Scene Representation

[![Project](https://img.shields.io/badge/🌐%20%20Project-GF-NeRF-blue.svg)](https://shaomq2187.github.io/GF-NeRF/)
[![arXiv](https://img.shields.io/badge/Arxiv-2403.12839-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2403.12839)

GF-NeRF introduces a global-guided two-stage architecture to achieve consistent and high-fidelity large-scale scene rendering without relying on prior scene knowledge.
<br><br>

### 💠 CLoD-GS: Continuous Level-of-Detail Gaussian Splatting for Real-Time Rendering

[![arXiv](https://img.shields.io/badge/Arxiv-2510.09997-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2510.09997)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/CLoD-GS)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/CLoD-GS)

CLoD-GS equips 3D Gaussian Splatting with learnable distance-adaptive opacity, enabling smooth, storage-efficient, artifact-free continuous level-of-detail rendering from a single model.
<br><br>

## 🧠 General Deep Learning

We focus on general representation learning and model optimization as the foundation for multimodal and cross-domain AI systems. Our research includes Transformer architecture optimization, distributed training, model compression, and preference alignment (DPO, RLHF) to enhance generalization and interpretability.
<br><br>

### 🎙️ A Study on the Adverse Impact of Synthetic Speech on Speech Recognition


Performance analysis and novel solution exploration for speech recognition under synthetic speech interference.
<br><br>

### Doubly-Fused ViT: Fuse Information from Dual Vision Transformer Streams

[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/ginobilinie/DFvT)
![GitHub Stars](https://img.shields.io/github/stars/ginobilinie/DFvT)

DFvT introduces a doubly-fused Vision Transformer that combines efficient global context modeling with fine-grained spatial detail preservation to achieve high accuracy and efficiency.
<br><br>

### SCMT: Self-Correction Mean Teacher for Semi-supervised Object Detection


A self-correction mean teacher architecture that mitigates the impact of noisy pseudo-labels, offering a novel technological breakthrough in the field of semi-supervised object detection.
<br><br>

### DPOSE: Online Keypoint-CAM Guided Inference for Driver Pose Estimation


An optimization scheme for a proprietary HPE task in DMS scenarios which involves a pose-wise hard mining strategy for distribution balance and an online keypoint-aligned Grad-CAM loss to constrain activations to semantic regions.
<br><br>
