<div align="center">

<img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/banner.jpg" alt="Yeying Lab: Game World Models" width="100%">

**Real-time interactive game world models.** *Press a key, and the model draws the next frame of the game world.*

[Homepage](https://jinyeying.github.io/) · [Join us](#join-us)

**13 projects · 11 papers · 12 open-source codebases · 9 models · 6 datasets**

[![Total stars](https://img.shields.io/github/stars/YeyingLab?style=social)](https://github.com/YeyingLab)

</div>

https://github.com/user-attachments/assets/e070b091-178b-4faf-be39-83f433563232

Yeying Lab is led by [Yeying Jin](https://jinyeying.github.io/), Staff Researcher at Tencent and Adjunct Faculty at NUS ECE.
We build video world models that players can steer, edit and play in real time: agents that run the game while a video model renders it, action and language control that stays spatially consistent, and NPCs that read the game state and react to players.

> These are technical explorations, not commercial games.

## Agentic gameplay and real-time world editing

| Project | In one line | Links |
|---|---|---|
| **MaLiang**<br><sub>Painting Playable Game Worlds from Numbers</sub> | Paint a map, and the world follows. | [![Code](https://img.shields.io/github/stars/YeyingLab/MaLiang?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/MaLiang) · [Model](https://github.com/YeyingLab/MaLiang/releases/tag/v1.0-models) |
| **Wizard**<br><sub>Manipulate Any World in Real Time via Agentic Control</sub> | Manipulates any world in real time. | [arXiv](https://arxiv.org/abs/2610.40339) · [Project](https://wyzardwu.github.io/wizard/) · [![Code](https://img.shields.io/github/stars/YeyingLab/Wizard?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/Wizard) · [🤗 Model](https://huggingface.co/datasets/yuzhewu207/wizard/tree/main/weights) · [🤗 Data](https://huggingface.co/datasets/yuzhewu207/wizard) |
| **UnboundRun** | Renders endless parkour at 40 fps. | Coming soon |
| **GameCrafter**<br><sub>An Agentic Framework for Multi-Gameplay Game World Generation</sub> | Builds worlds from a prompt. | [Paper](https://github.com/YeyingLab/GameCrafter/blob/main/paper/GameCrafter.pdf) · [Project](https://teawhite.cn/GameCrafter/) · [![Code](https://img.shields.io/github/stars/YeyingLab/GameCrafter?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/GameCrafter) |
| **GameDirector**<br><sub>Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models</sub> | Splits logic from rendering. | [arXiv](https://arxiv.org/abs/2609.25652) · [Project](https://jimntu.github.io/gamedirector/) · [![Code](https://img.shields.io/github/stars/Jimntu/GameDirector_code?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/Jimntu/GameDirector_code) · [🤗 Model](https://huggingface.co/onepiece1999/GameDirector) · [🤗 Data](https://huggingface.co/datasets/onepiece1999/GameDirector-Training-Data) |

## Spatially consistent action and language control

| Project | In one line | Links |
|---|---|---|
| **SCOPE**<br><sub>Simulating Cross-game Operations in Playable Environments for FPS World Models</sub> | Learns first-person action control. | [arXiv](https://arxiv.org/abs/2605.23345) · [Project](https://z2tong.github.io/SCOPE/) · [![Code](https://img.shields.io/github/stars/z2tong/SCOPE?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/z2tong/SCOPE) · [🤗 Model](https://huggingface.co/zizhaotong/SCOPE) · [🤗 Data](https://huggingface.co/collections/zizhaotong/crossfps) |
| **ActionRoPE**<br><sub>Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models</sub> | Keeps revisited scenes stable. | [arXiv](https://arxiv.org/abs/2610.25861) · [Project](https://teawhite.cn/ActionRoPE/) · [![Code](https://img.shields.io/github/stars/YeyingLab/ActionRoPE?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/ActionRoPE) · [🤗 Model](https://huggingface.co/teawhite/ActionRoPE) |
| **H3-World**<br><sub>Turning Language Understanding into World Control</sub> | Turns language into world control. | [arXiv](https://arxiv.org/abs/2609.01560) · [Project](https://danzer1xxxxchan.github.io/H3-World/) · [![Code](https://img.shields.io/github/stars/YeyingLab/H3-World?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/H3-World) · [🤗 Model](https://huggingface.co/DANNY621/H3-World) |
| **Incantation**<br><sub>Natural Language as the Action Interface for Multi-Entity Video World Models</sub> | Commands many characters in plain language. | [arXiv](https://arxiv.org/abs/2605.18601) · [Project](https://matrixteam-ai.github.io/pages/Incanation) · [![Code](https://img.shields.io/github/stars/zhushangwen/Incantation?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/zhushangwen/Incantation) · [Play](https://www.reactor.inc/incantation) · [🤗 Model](https://huggingface.co/MatrixTeam/Incantation_preview_margit) · [🤗 Data](https://huggingface.co/datasets/MatrixTeam/incantation-elden-ring-scenes) |

## State-aware gameplay and NPC behavior

| Project | In one line | Links |
|---|---|---|
| **WorldMind**<br><sub>Decoupled Game World Model for State-Aware NPC Behavior</sub> | Makes NPCs reason, then act. | [arXiv](https://arxiv.org/abs/2608.21439) · [Project](https://teawhite.cn/worldmind_projectpage/) · [![Code](https://img.shields.io/github/stars/YeyingLab/WorldMind?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/WorldMind) |
| **ReactiveGWM**<br><sub>Flexible Control and NPC Reactivity in Game World Models</sub> | Lets NPCs react to players. | [arXiv](https://arxiv.org/abs/2605.15256) · [Project](https://inv-wzq.github.io/ReactiveGWM/) · [![Code](https://img.shields.io/github/stars/YeyingLab/ReactiveGWM?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/ReactiveGWM) · [🤗 Model](https://huggingface.co/INV-WZQ/ReactiveGWM-Models) · [🤗 Data](https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets) |
| **StatePlay**<br><sub>State-Aware Game World Models for Mechanics-Consistent Generation</sub> | Models frames and game states. | [arXiv](https://arxiv.org/abs/2607.26754) · [Project](https://jimntu.github.io/stateplay_page/) · [![Code](https://img.shields.io/github/stars/Jimntu/StatePlay?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/Jimntu/StatePlay) · [🤗 Model](https://huggingface.co/onepiece1999/StatePlay) · [🤗 Data](https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset) |

<sub>SCOPE and Incantation are joint projects with external collaborators.</sub>

## Beyond games: agentic video

| Project | In one line | Links |
|---|---|---|
| **StoryEngine**<br><sub>A State-Grounded Agentic Framework for Video Storytelling</sub> | Turns a story into a multi-shot video. | [arXiv](https://arxiv.org/abs/2609.33627) · [Project](https://yeyinglab.github.io/StoryEngine/) · [![Code](https://img.shields.io/github/stars/YeyingLab/StoryEngine?style=flat&logo=github&label=Code%20%E2%98%85&color=f5c518&labelColor=24292f)](https://github.com/YeyingLab/StoryEngine) |

## Join us

We're hiring 6-month research interns in world models and coding agents, in Singapore and through [Tencent campus recruiting](https://join.qq.com/post_detail.html?postid=1210646470286783493) in China. [Details](https://zhuanlan.zhihu.com/p/2070315664162689467)
