<div align="center">

<img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/banner.jpg" alt="Yeying Lab: Game World Models" width="100%">

**Real-time interactive game world models.** *Press a key, and the model draws the next frame of the game world.*

[Homepage](https://jinyeying.github.io/) · [Agentic gameplay](#agentic-gameplay-and-real-time-world-editing) · [Action & language control](#spatially-consistent-action-and-language-control) · [NPC behavior](#state-aware-gameplay-and-npc-behavior) · [Agentic video](#beyond-games-agentic-video) · [Join us](#join-us)

**13 projects · 11 papers · 12 open-source codebases · 9 models · 6 datasets**

[![Total stars](https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/orgstars-yeyinglab.svg)](https://github.com/YeyingLab)

</div>

https://github.com/user-attachments/assets/e070b091-178b-4faf-be39-83f433563232

Yeying Lab is led by [Yeying Jin](https://jinyeying.github.io/), Staff Researcher at Tencent and Adjunct Faculty at NUS ECE.
We build video world models that players can steer, edit and play in real time: agents that run the game while a video model renders it, action and language control that stays spatially consistent, and NPCs that read the game state and react to players.

> These are technical explorations, not commercial games.

## Agentic gameplay and real-time world editing

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/YeyingLab/MaLiang"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/maliang.gif" width="100%" alt="MaLiang demo"></a>
<p><b>MaLiang</b>&nbsp; <img src="https://img.shields.io/badge/Code_%26_models-released-2ea44f?style=flat-square" alt="Code and models released" align="absmiddle"><br><sub><i>Painting Playable Game Worlds from Numbers</i></sub></p>
<p>Paint a map, and the world follows: a 4-step causal video model streams the game world in real time.</p>
<p><a href="https://github.com/YeyingLab/MaLiang"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-maliang.svg" alt="Code" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/MaLiang/releases/tag/v1.0-models">Model</a></p>
</td>
<td width="50%" valign="top">
<a href="https://wyzardwu.github.io/wizard/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/wizard.gif" width="100%" alt="Wizard demo"></a>
<p><b>Wizard</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Manipulate Any World in Real Time via Agentic Control</i></sub></p>
<p>Reshape any world in plain language; a video model renders the edits at 24 FPS in 2 steps.</p>
<p><sub>🎓 Co-first authors: <a href="https://nadia.sg/people/wu-yuzhe/">Yuzhe Wu</a>, <a href="https://jimntu.github.io/">Zijun Lin</a></sub></p>
<p><a href="https://arxiv.org/abs/2610.40339">arXiv</a> · <a href="https://wyzardwu.github.io/wizard/">Project</a> · <a href="https://github.com/YeyingLab/Wizard"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-wizard.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/yuzhewu207/wizard/tree/main/weights">🤗 Model</a> · <a href="https://huggingface.co/datasets/yuzhewu207/wizard"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-yuzhewu207-wizard.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="#"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/unboundrun.gif" width="100%" alt="UnboundRun demo"></a>
<p><b>UnboundRun</b>&nbsp; <img src="https://img.shields.io/badge/Coming-soon-f0883e?style=flat-square" alt="Coming soon" align="absmiddle"></p>
<p>Endless parkour in many art styles, rendered live at 40 fps.</p>
<p><i>Code coming soon</i></p>
</td>
<td width="50%" valign="top">
<a href="https://teawhite.cn/GameCrafter/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/gamecrafter.gif" width="100%" alt="GameCrafter demo"></a>
<p><b>GameCrafter</b>&nbsp; <img src="https://img.shields.io/badge/Preprint-2026-6e7781?style=flat-square" alt="Preprint 2026" align="absmiddle"><br><sub><i>An Agentic Framework for Multi-Gameplay Game World Generation</i></sub></p>
<p>One prompt builds a multi-gameplay 3D game world; best overall score (87.77) on a ten-task benchmark.</p>
<p><sub>🎓 Co-first authors: <a href="https://teawhite.cn/">Zhiyang Deng</a>, Xiyao Deng</sub></p>
<p><a href="https://github.com/YeyingLab/GameCrafter/blob/main/paper/GameCrafter.pdf">Paper</a> · <a href="https://teawhite.cn/GameCrafter/">Project</a> · <a href="https://github.com/YeyingLab/GameCrafter"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-gamecrafter.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/teawhite/GameCrafter"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-teawhite-gamecrafter.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://jimntu.github.io/gamedirector/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/gamedirector.gif" width="100%" alt="GameDirector demo"></a>
<p><b>GameDirector</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models</i></sub></p>
<p>An agent runs the rules, states and NPC tactics while a world model renders them: boss action quality +39.9%.</p>
<p><sub>🎓 Co-first authors: <a href="https://jimntu.github.io/">Zijun Lin</a>, <a href="https://teawhite.cn/">Zhiyang Deng</a></sub></p>
<p><a href="https://arxiv.org/abs/2609.25652">arXiv</a> · <a href="https://jimntu.github.io/gamedirector/">Project</a> · <a href="https://github.com/Jimntu/GameDirector_code"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-jimntu-gamedirector_code.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/onepiece1999/GameDirector"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-onepiece1999-gamedirector.svg" alt="Hugging Face model likes" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/onepiece1999/GameDirector-Training-Data"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-onepiece1999-gamedirector-training-data.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%"></td>
</tr>
</table>

## Spatially consistent action and language control

<table>
<tr>
<td width="50%" valign="top">
<a href="https://z2tong.github.io/SCOPE/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/scope.gif" width="100%" alt="SCOPE demo"></a>
<p><b>SCOPE</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Simulating Cross-game Operations in Playable Environments for FPS World Models</i></sub></p>
<p>An FPS world model trained on CrossFPS, the first multi-game FPS dataset: 69K clips, 7 titles, 10-DoF controls.</p>
<p><sub>🎓 First author: <a href="https://github.com/z2tong">Zizhao Tong</a></sub></p>
<p><a href="https://arxiv.org/abs/2605.23345">arXiv</a> · <a href="https://z2tong.github.io/SCOPE/">Project</a> · <a href="https://github.com/z2tong/SCOPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-z2tong-scope.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/zizhaotong/SCOPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-zizhaotong-scope.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/collections/zizhaotong/crossfps">🤗 Data</a></p>
</td>
<td width="50%" valign="top">
<a href="https://teawhite.cn/ActionRoPE/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/actionrope.gif" width="100%" alt="ActionRoPE demo"></a>
<p><b>ActionRoPE</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models</i></sub></p>
<p>Actions become world-coordinate rotary positions: 66% less revisit drift, on 1.3B–33B backbones.</p>
<p><sub>🎓 First author: <a href="https://teawhite.cn/">Zhiyang Deng</a></sub></p>
<p><a href="https://arxiv.org/abs/2610.25861">arXiv</a> · <a href="https://teawhite.cn/ActionRoPE/">Project</a> · <a href="https://github.com/YeyingLab/ActionRoPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-actionrope.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/teawhite/ActionRoPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-teawhite-actionrope.svg" alt="Hugging Face model likes" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://danzer1xxxxchan.github.io/H3-World/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/h3world.gif" width="100%" alt="H3-World demo"></a>
<p><b>H3-World</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Turning Language Understanding into World Control</i></sub></p>
<p>Turns a video model's language understanding into character and camera control, training only 0.199% of parameters.</p>
<p><sub>🎓 Co-first authors: <a href="https://danzer1xxxxchan.github.io/">Danze Chen</a>, <a href="https://inv-wzq.github.io/">Zeqing Wang</a></sub></p>
<p><a href="https://arxiv.org/abs/2609.01560">arXiv</a> · <a href="https://danzer1xxxxchan.github.io/H3-World/">Project</a> · <a href="https://github.com/YeyingLab/H3-World"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-h3-world.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/DANNY621/H3-World"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-danny621-h3-world.svg" alt="Hugging Face model likes" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://matrixteam-ai.github.io/pages/Incanation"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/incantation.gif" width="100%" alt="Incantation demo"></a>
<p><b>Incantation</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Natural Language as the Action Interface for Multi-Entity Video World Models</i></sub></p>
<p>Command many characters in plain language: 89% cross-entity transfer success vs. 43% for action-ID baselines.</p>
<p><sub>🎓 First author: <a href="https://github.com/zhushangwen">Shangwen Zhu</a></sub></p>
<p><a href="https://arxiv.org/abs/2605.18601">arXiv</a> · <a href="https://matrixteam-ai.github.io/pages/Incanation">Project</a> · <a href="https://github.com/zhushangwen/Incantation"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-zhushangwen-incantation.svg" alt="Code" align="absmiddle"></a> · <a href="https://www.reactor.inc/incantation">Play</a> · <a href="https://huggingface.co/MatrixTeam/Incantation_preview_margit">🤗 Model</a> · <a href="https://huggingface.co/datasets/MatrixTeam/incantation-elden-ring-scenes"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-matrixteam-incantation-elden-ring-scenes.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
</table>

<sub>SCOPE and Incantation are joint projects with external collaborators.</sub>

## State-aware gameplay and NPC behavior

<table>
<tr>
<td width="50%" valign="top">
<a href="https://teawhite.cn/worldmind_projectpage/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/worldmind.gif" width="100%" alt="WorldMind demo"></a>
<p><b>WorldMind</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Decoupled Game World Model for State-Aware NPC Behavior</i></sub></p>
<p>The first decoupled game world model for NPC behavior, from understanding to generation; preferred in ~70% of comparisons.</p>
<p><sub>🎓 First author: <a href="https://teawhite.cn/">Zhiyang Deng</a></sub></p>
<p><a href="https://arxiv.org/abs/2608.21439">arXiv</a> · <a href="https://teawhite.cn/worldmind_projectpage/">Project</a> · <a href="https://github.com/YeyingLab/WorldMind"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-worldmind.svg" alt="Code" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://inv-wzq.github.io/ReactiveGWM/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/reactivegwm.gif" width="100%" alt="ReactiveGWM demo"></a>
<p><b>ReactiveGWM</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Flexible Control and NPC Reactivity in Game World Models</i></sub></p>
<p>NPCs follow Offense / Defense / Control strategies and transfer zero-shot to unseen games.</p>
<p><sub>🎓 First author: <a href="https://inv-wzq.github.io/">Zeqing Wang</a></sub></p>
<p><a href="https://arxiv.org/abs/2605.15256">arXiv</a> · <a href="https://inv-wzq.github.io/ReactiveGWM/">Project</a> · <a href="https://github.com/YeyingLab/ReactiveGWM"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-reactivegwm.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/INV-WZQ/ReactiveGWM-Models"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-inv-wzq-reactivegwm-models.svg" alt="Hugging Face model likes" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-inv-wzq-reactivegwm-datasets.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://jimntu.github.io/stateplay_page/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/stateplay.gif" width="100%" alt="StatePlay demo"></a>
<p><b>StatePlay</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>State-Aware Game World Models for Mechanics-Consistent Generation</i></sub></p>
<p>Generates frames together with game states (health, meters, timers): +18.6% mechanics fidelity.</p>
<p><sub>🎓 First author: <a href="https://jimntu.github.io/">Zijun Lin</a></sub></p>
<p><a href="https://arxiv.org/abs/2607.26754">arXiv</a> · <a href="https://jimntu.github.io/stateplay_page/">Project</a> · <a href="https://github.com/Jimntu/StatePlay"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-jimntu-stateplay.svg" alt="Code" align="absmiddle"></a> · <a href="https://huggingface.co/onepiece1999/StatePlay"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-onepiece1999-stateplay.svg" alt="Hugging Face model likes" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-onepiece1999-stateplay-dataset.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%"></td>
</tr>
</table>

## Beyond games: agentic video

<table>
<tr>
<td width="50%" valign="top">
<a href="https://yeyinglab.github.io/StoryEngine/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/storyengine.gif" width="100%" alt="StoryEngine demo"></a>
<p><b>StoryEngine</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>A State-Grounded Agentic Framework for Video Storytelling</i></sub></p>
<p>Turns a story into a multi-shot video, with every shot grounded in an explicit story state.</p>
<p><sub>🎓 Co-first authors: <a href="https://github.com/wwwTaylor">Yingrui Wang</a>, <a href="https://inv-wzq.github.io/">Zeqing Wang</a></sub></p>
<p><a href="https://arxiv.org/abs/2609.33627">arXiv</a> · <a href="https://yeyinglab.github.io/StoryEngine/">Project</a> · <a href="https://github.com/YeyingLab/StoryEngine"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-storyengine.svg" alt="Code" align="absmiddle"></a></p>
</td>
<td width="50%"></td>
</tr>
</table>

## Join us

We're hiring 6-month research interns in world models and coding agents, in Singapore and through [Tencent campus recruiting](https://join.qq.com/post_detail.html?postid=1210646470286783493) in China. [Details](https://zhuanlan.zhihu.com/p/2070315664162689467)
