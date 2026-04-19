# 阿里巴巴 高德视觉技术中心

[For English](README.md)

# 👋 团队介绍

高德视觉技术中心专注于以计算机视觉为核心的前沿研究与创新应用，致力于打造时空互联网领域的核心技术能力。
我们立足于现实世界与数字世界的交汇点，以AI驱动真实世界的智能化理解与生成，赋能智慧出行、生活服务与虚拟空间构建。
作为业界领航者，团队不仅在计算机视觉领域持续深耕，更将计算机视觉及AI技术应用在自主导航、高德打车、生活服务等多元化场景。
作为高德地图的核心技术驱动部门，我们的研究方向涵盖从感知到生成、从人本智能到世界建模的全链条技术体系，形成了六大研究领域：
- 🗺️ 地图与自动驾驶（Map & Autonomous Driving）：融合多模态感知与高精地图生成，探索空间语义理解与规则感知下的智能出行。
- 🕺🏻 数字人（Human-Centric AI）：构建以人为中心的AI系统，让模型理解情感、身份与行为，实现自然的视觉生成与交互。
- 🧭 具身智能（Embodied AI）：研究智能体在虚拟与真实世界中的感知、规划与行动，推动视觉语言与运动智能的统一。
- 🌐 世界模型（World Modeling）：构建动态可交互的世界建模框架，让AI具备对环境的理解、预测与生成能力。
- 🧊 3D生成与重建（3D Generation & Reconstruction）：聚焦三维场景的建模、渲染与生成，实现连续细节控制与真实感表达。
- 🧠 通用深度学习（General Deep Learning）：探索通用表征、模型优化与多模态对齐，为时空智能提供底层算法支撑。

高德视觉技术中心始终站在计算机视觉研究与应用的创新高地，是高德空间智能互联网的重要技术实践者。我们相信，**AI对世界的理解能力，将决定未来出行与生活的智能化水平**。

---

*欢迎贡献、提交 issue 和反馈！*  
欢迎给我们的仓库点个 ⭐ 保持关注。

# 🔈 最新动态

* 🏛 **2025 年 11月** – 我们共有 **5 篇论文** 入选 AAAI 2026，包括 1 篇 Oral，涵盖自动驾驶、以及来自视频生成与数字人：[**UniMapGen**](https://arxiv.org/abs/2509.22262) (*Oral*), [**PriorDrive**](), [**Persistent Autoregressive Mapping**](https://arxiv.org/pdf/2509.22756), [**FantasyTalking2**](https://fantasy-amap.github.io/fantasy-talking2/), [**FantasyHSI**](https://fantasy-amap.github.io/fantasy-hsi/)
* 🏛 **2025 年 9 月** – 我们的论文 [**FutureSightDrive**](https://miv-xjtu.github.io/FSDrive.github.io/) 被 NeurIPS 2025 接收，并选为 Spotlight。
* 🏛 **2025 年 7 月** – 我们的论文 [**FantasyTalking**](https://arxiv.org/pdf/2504.04842) 被 ACM MM 2025 接收。
* 🏛 **2025 年 6 月** – 我们的论文 [**SeqGrowGraph**](https://arxiv.org/pdf/2507.04822v1) 被 ICCV 2025 接收。
* 📢 **2025 年 5 月** – 我们发布了 [**FSDrive**](https://miv-xjtu.github.io/FSDrive.github.io/) 的完整项目。
* 🏛 **2025 年 4 月** – 我们的论文 [**G3PT**](https://arxiv.org/abs/2409.06322) 被 IJCAI 2025 接收。
* 📢 **2025 年 4 月** – 我们发布了 [**FantasyTalking**](https://fantasy-amap.github.io/fantasy-talking/)、[**FantasyID**](https://fantasy-amap.github.io/fantasy-id/) 的推理代码和模型权重。

# 🔧 公开技术

## 🗺️ 地图与自动驾驶

融合感知、地图与决策的核心技术，推动高精地图、自动驾驶感知与时空智能的深度融合。团队聚焦于构建下一代 3D 地图引擎、交通规则理解与场景级行为建模，让 AI 在真实城市道路中具备空间理解与可解释决策能力。
<br><br>

### 🚘 FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving

[![Project](https://img.shields.io/badge/🌐%20%20Project-FSDrive-blue.svg)](https://miv-xjtu.github.io/FSDrive.github.io/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-NeurIPS%202025%20%28Spotlight%29-green.svg)](https://neurips.cc/virtual/2025/poster/116)
[![arXiv](https://img.shields.io/badge/Arxiv-2505.17685-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2505.17685)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/MIV-XJTU/FSDrive)
![GitHub Stars](https://img.shields.io/github/stars/MIV-XJTU/FSDrive)

在自动驾驶方向首次提出一种时空思维链的推理方法，提出了视觉生成与理解统一的预训练范式，允许模型可视化地思考，基于当前观察和预测的未来世界进行轨迹规划。
<br><br>

### 🗺 UniMapGen: A Generative Framework for Large-Scale Map Construction from Multi-modal Data

[![Project](https://img.shields.io/badge/🌐%20%20Project-UniMapGen-blue.svg)](https://amap-cvlab.github.io/UniMapGen/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-AAAI%202026%20%28Oral%29-green.svg)](https://arxiv.org/pdf/2509.22262)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.22262-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.22262)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/UniMapGen)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/UniMapGen)

一个生成式统一框架，可以通过自回归方式从多模态输入中生成平滑且拓扑一致的矢量化地图，实现可扩展的、对遮挡具有鲁棒性的大规模城市地图构建，同时无需昂贵的现场数据采集。
<br><br>

### 🛣️ PriorDrive: Enhancing Online HD Mapping with Unified Vector Priors

[![Project](https://img.shields.io/badge/🌐%20%20Project-PriorDrive-blue.svg)](https://miv-xjtu.github.io/PriorDrive/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-AAAI%202026-green.svg)](https://arxiv.org/abs/2409.05352)
[![arXiv](https://img.shields.io/badge/Arxiv-2409.05352-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2409.05352)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/MIV-XJTU/PriorDrive)
![GitHub Stars](https://img.shields.io/github/stars/MIV-XJTU/PriorDrive)

首个能够统一编码并融合多种矢量化先验地图（如SD地图、过期HD地图、历史地图），以增强在线高精地图构建的框架。
<br><br>

### 🚥 Persistent Autoregressive Mapping with Traffic Rules for Autonomous Driving

[![Project](https://img.shields.io/badge/🌐%20%20Project-PAMR-blue.svg)](https://miv-xjtu.github.io/PAMR/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.22756-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.22756)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/https://github.com/MIV-XJTU/PAMR)
![GitHub Stars](https://img.shields.io/github/stars/https://github.com/MIV-XJTU/PAMR)

本文提出一种融合几何与规则的生成式联合推理范式（PAMR），它以自回归方式统一构建车道向量与持久化交通规则，赋予车辆跨越长时序的场景记忆与规则遵循能力。
<br><br>

### 📑 SeqGrowGraph: Learning Lane Topology as a Chain of Graph Expansions

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-ICCV%202025-green.svg)](https://openaccess.thecvf.com/content/ICCV2025/papers/Xie_SeqGrowGraph_Learning_Lane_Topology_as_a_Chain_of_Graph_Expansions_ICCV_2025_paper.pdf)
[![arXiv](https://img.shields.io/badge/Arxiv-2507.04822v1-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2507.04822v1)

一种以增量式构建邻接矩阵过程重新阐释车道网学习的生成框架。
<br><br>

### 🚗 Driving by the Rules: A Benchmark for Integrating Traffic Sign Regulations into Vectorized HD Map

[![Project](https://img.shields.io/badge/🌐%20%20Project-MapDR-blue.svg)](https://amap-cvlab.github.io/DriveByTheRules/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-CVPR%202025%20%28Highlight%29-green.svg)](https://openaccess.thecvf.com/content/CVPR2025/papers/Chang_Driving_by_the_Rules_A_Benchmark_for_Integrating_Traffic_Sign_CVPR_2025_paper.pdf)
[![arXiv](https://img.shields.io/badge/Arxiv-2410.23780-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2410.23780)

交通标志中的车道级交通规则理解与绑路评测基准及多模态解决方案。
<br><br>

## 🕺🏻 数字人

以生成式AI为核心，探索数字人从“被驱动”到“自主行动”的进化。团队提出 [Fantasy AIGC 系列模型](https://github.com/Fantasy-AMAP)，覆盖表情驱动、语音驱动、身份保持与动作生成，实现情感丰富、身份一致、物理合理的高保真数字人视频生成。
<br><br>

### 🗣️ FantasyTalking: Realistic Talking Portrait Generation via Coherent Motion Synthesis

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyTalking-blue.svg)](https://fantasy-amap.github.io/fantasy-talking/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-ACM%20MM%202025-green.svg)](https://dl.acm.org/doi/10.1145/3746027.3755217)
[![arXiv](https://img.shields.io/badge/Arxiv-2504.04842-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2504.04842)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-talking)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-talking)
[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/acvlab/FantasyTalking)
[![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-FFD21E.svg)](https://huggingface.co/spaces/acvlab/FantasyTalking)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/amap_cvlab/FantasyTalking)

首个基于 Wan 的高保真音频驱动虚拟人系统，通过双阶段音视对齐与可控运动调制，实现动态场景下面部表情、唇动与身体姿态的精准同步。
<br><br>

### 🎙️ FantasyTalking2: Timestep-Layer Adaptive Preference Optimization for Audio-Driven Portrait Animation

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyTalking2-blue.svg)](https://fantasy-amap.github.io/fantasy-talking2/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-AAAI%202026-green.svg)](https://doi.org/10.48550/arXiv.2508.11255)
[![arXiv](https://img.shields.io/badge/Arxiv-2508.11255v1-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2508.11255v1)
[![GitHub](https://img.shields.io/badge/Code%20%28Comming%20Soon%29-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-talking2)

一种新颖的“时间步-网络层”自适应多专家偏好优化(TLPO)方法，在口型一致、动作自然、视觉效果三个维度上提升了音频驱动数字人动画的质量。
<br><br>

### 🗿 FantasyHSI: Video-Generation-Centric 4D Human Synthesis In Any Scene through A Graph-based Multi-Agent Framework

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyHSI-blue.svg)](https://fantasy-amap.github.io/fantasy-hsi/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-AAAI%202026-green.svg)](https://doi.org/10.48550/arXiv.2509.01232)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.01232-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.01232)
[![GitHub](https://img.shields.io/badge/Code%20%28Comming%20Soon%29-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-hsi)

一种基于图结构的多智能体框架，将视频生成与三维世界动态相融合，使数字人具备感知、规划与自主行动的能力，从而在技术层面上成为连接人与世界的统一“感知–行动”推理桥梁。
<br><br>

### 🤡 FantasyPortrait: Enhancing Multi-Character Portrait Animation with Expression-Augmented Diffusion Transformers

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyPortrait-blue.svg)](https://fantasy-amap.github.io/fantasy-portrait/)
[![arXiv](https://img.shields.io/badge/Arxiv-2507.12956-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2507.12956)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-portrait)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-portrait)

一种全新的表情驱动视频生成方法，将情绪增强学习与掩码交叉注意力相结合，可在单人或多人肖像场景中生成高质量且富有表现力的动画。
<br><br>

### 🆔 FantasyID: Face Knowledge Enhanced ID-Preserving Video Generation

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyID-blue.svg)](https://fantasy-amap.github.io/fantasy-id/)
[![arXiv](https://img.shields.io/badge/Arxiv-2502.13995-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2502.13995)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-id)
![GitHub Stars](https://img.shields.io/github/stars/Fantasy-AMAP/fantasy-id)
[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/acvlab/FantasyID)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/amap_cvlab/FantasyID)

以3D面部先验、多视角增强以及层感知注入的提升运动场景下的ID保持视频生成框架。
<br><br>

### 💃🏻 HumanRig: Learning Automatic Rigging for Humanoid Characters in Animation

[![Project](https://img.shields.io/badge/🌐%20%20Project-HumanRig-blue.svg)](https://c8241998.github.io/HumanRig/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-CVPR%202025%20%28Highlight%29-green.svg)](https://openaccess.thecvf.com/content/CVPR2025/papers/Chu_HumanRig_Learning_Automatic_Rigging_for_Humanoid_Character_in_a_Large_CVPR_2025_paper.pdf)
[![arXiv](https://img.shields.io/badge/Arxiv-2412.02317-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2412.02317)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/c8241998/HumanRig)
![GitHub Stars](https://img.shields.io/github/stars/c8241998/HumanRig)
[![HuggingFace Dataset](https://img.shields.io/badge/🤗-HuggingFace%20Dataset-FFD21E.svg)](https://huggingface.co/datasets/jellyczd/HumanRig)

首个面向3D生成数字人的自动绑骨数据集以及基于变换器的端到端自动绑骨算法。
<br><br>

## 🧭 具身智能

研究智能体在虚拟与物理环境中的感知、思考与行动机制。通过视觉语言模型与强化学习的结合，构建可在三维空间中感知环境、规划目标、执行任务的具身智能体，为机器人与虚拟人提供统一的认知框架。
<br><br>

### CE-Nav: Flow-Guided Reinforcement Refinement for Cross-Embodiment Local Navigation

[![Project](https://img.shields.io/badge/🌐%20%20Project-CE%20Nav-blue.svg)](https://ce-nav.github.io/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.23203-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.23203)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/CE-Nav)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/CE-Nav)

一个新颖的跨具身实体的局部导航框架，可用作一脑多形、可插拔的快系统。
<br><br>

### OmniNav: A Unified Framework for Prospective Exploration and Visual-Language Navigation

[![arXiv](https://img.shields.io/badge/Arxiv-2509.25687-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.25687)
[![GitHub](https://img.shields.io/badge/Code%20%28Comming%20Soon%29-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/OmniNav)

OmniNav提出统一的机器人导航框架，以低延迟的连续航点策略与快慢协同规划结合多任务、通用视觉语言数据增强理解能力，在指令目标、物体目标、点目标及前沿探索任务上实现更高精度、泛化与成功率，并获真实部署验证。
<br><br>

### 🧠 JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation

[![Project](https://img.shields.io/badge/🌐%20%20Project-JanusVLN-blue.svg)](https://miv-xjtu.github.io/JanusVLN.github.io/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.22548-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.22548)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/MIV-XJTU/JanusVLN)
![GitHub Stars](https://img.shields.io/github/stars/MIV-XJTU/JanusVLN)
[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/misstl/JanusVLN_Extra)

首个具备双重隐式记忆的视觉语言导航智能体，解耦视觉语义和空间感知，并分别建模为紧凑的隐式神经表示。
<br><br>

### Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA

[![arXiv](https://img.shields.io/badge/Arxiv-2509.26251-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.26251)

融合空间结构与动态推理的视觉-语言-动作新范式。
<br><br>

## 🌐 世界模型

致力于构建动态、可交互的世界模型，用于理解、预测与生成物理一致的时空过程。通过跨模态数据建模与生成式学习，实现从感知到模拟的闭环，让AI具备理解真实世界的能力。
<br><br>

### 🌏 FantasyWorld: Geometry-Consistent World Modeling via Unified Video and 3D Prediction

[![Project](https://img.shields.io/badge/🌐%20%20Project-FantasyWorld-blue.svg)](https://fantasy-amap.github.io/fantasy-world/)
[![arXiv](https://img.shields.io/badge/Arxiv-2509.21657-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.21657)
[![GitHub](https://img.shields.io/badge/Code%20%28Comming%20Soon%29-GitHub-181717.svg?logo=GitHub)](https://github.com/Fantasy-AMAP/fantasy-world)

一个统一视频先验信息和几何3D的世界模型，能够生成几何一致的、可探索的3D场景。
<br><br>

### World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training

[![arXiv](https://img.shields.io/badge/Arxiv-2509.24948-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2509.24948)

一个新颖的以世界模型为虚拟环境的VLA后训练框架。
<br><br>

## 🧊 3D生成与重建

探索3D世界的生成式建模与高保真重建。研究方向涵盖 Gaussian Splatting、NeRF、3D-aware diffusion 等技术，用于实现实时渲染、连续细节层次（LOD）控制与语义一致的三维场景生成。
<br><br>

### 🧸 G3PT: Unleash the Power of Autoregressive Modeling in 3D Generative Tasks

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-IJCAI%202025-green.svg)](https://www.ijcai.org/proceedings/2025/262)
[![arXiv](https://img.shields.io/badge/Arxiv-2409.06322-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2409.06322)

首个基于多尺度自回归的原生 3D 生成基座大模型。
<br><br>

### 🏙 Global-Guided Focal Neural Radiance Field for Large-Scale Scene Representation

[![Project](https://img.shields.io/badge/🌐%20%20Project-GF%20NeRF-blue.svg)](https://shaomq2187.github.io/GF-NeRF/)
[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-WACV%202025-green.svg)](https://ieeexplore.ieee.org/abstract/document/10943871)
[![arXiv](https://img.shields.io/badge/Arxiv-2403.12839-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2403.12839)

GF-NeRF 通过全局引导的双阶段架构，实现无需先验知识的大规模场景一致且高保真渲染。
<br><br>

### 💠 CLoD-GS: Continuous Level-of-Detail Gaussian Splatting for Real-Time Rendering

[![arXiv](https://img.shields.io/badge/Arxiv-2510.09997-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2510.09997)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/amap-cvlab/CLoD-GS)
![GitHub Stars](https://img.shields.io/github/stars/amap-cvlab/CLoD-GS)

CLoD-GS 通过引入可学习的距离自适应透明度，为 3D 高斯喷溅表示实现单一模型内平滑、无存储冗余、无跳变伪影的连续细节层次渲染。
<br><br>

## 🧠 通用深度学习

关注通用表示学习与模型优化，为多模态、跨任务AI系统提供统一基础。研究方向包括 Transformer架构优化、分布式训练、模型压缩 与 偏好对齐学习（DPO, RLHF），持续提升模型的泛化性与可解释性。
<br><br>

### 🎙️ A Study on the Adverse Impact of Synthetic Speech on Speech Recognition

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-ICASSP%202024-green.svg)](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10446991)

合成语音干扰下，语音识别性能分析和新方案探索。
<br><br>

### Doubly-Fused ViT: Fuse Information from Dual Vision Transformer Streams

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-ECCV%202022-green.svg)](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136830723.pdf)
[![GitHub](https://img.shields.io/badge/Code-GitHub-181717.svg?logo=GitHub)](https://github.com/ginobilinie/DFvT)
![GitHub Stars](https://img.shields.io/github/stars/ginobilinie/DFvT)

DFvT 提出一种双融合视觉Transformer架构，兼顾全局上下文建模与精细空间细节保留，在保证高效率的同时实现高精度表现。
<br><br>

### SCMT: Self-Correction Mean Teacher for Semi-supervised Object Detection

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-IJCAI%202022-green.svg)](https://www.ijcai.org/proceedings/2022/0207.pdf)

一种通过自我校正的教师架构来减少噪声伪标签影响的半监督目标检测新方法。
<br><br>

### DPOSE: Online Keypoint-CAM Guided Inference for Driver Pose Estimation

[![Conference](https://img.shields.io/badge/%F0%9F%8F%9B%20%20Conference-CVPR%20Workshop%202023-green.svg)](https://openaccess.thecvf.com/content/CVPR2023W/Precognition/papers/Guo_DPOSE_Online_Keypoint-CAM_Guided_Inference_for_Driver_Pose_Estimation_With_CVPRW_2023_paper.pdf)

针对DMS场景下的HPE任务，提出包含困难样本挖掘与在线关键点对齐Grad-CAM损失的优化方案。
<br><br>
