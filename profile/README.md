<div align="center">

<img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/banner.jpg" alt="Yeying Lab: Game World Models" width="100%">

**Real-time interactive game world models.** *Press a key, and the model draws the next frame of the game world.*

[Homepage](https://jinyeying.github.io/) · [🤗 Hugging Face](https://huggingface.co/collections/yeyingjin/yeying-lab-6b09480206e083c253ed2163) · [Agentic gameplay](#agentic-gameplay-and-real-time-world-editing) · [Coding agents](#coding-agents-and-world-model-infrastructure) · [Action & language control](#spatially-consistent-action-and-language-control) · [NPC behavior](#state-aware-gameplay-and-npc-behavior) · [Agentic video](#beyond-games-agentic-video) · [Virtual try-on](#beyond-games-virtual-try-on) · [Join us](https://zhuanlan.zhihu.com/p/2070315664162689467)

**16 projects · 14 papers · 15 open-source codebases · 11 models · 9 datasets**

<a href="https://github.com/YeyingLab"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/orgstars-yeyinglab.svg" alt="Total GitHub stars"></a> <a href="https://huggingface.co/collections/yeyingjin/yeying-lab-6b09480206e083c253ed2163"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/sumhfdl-data-yeyinglab.svg" alt="Total Hugging Face dataset downloads"></a> <a href="https://huggingface.co/collections/yeyingjin/yeying-lab-6b09480206e083c253ed2163"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/sumhfdl-model-yeyinglab.svg" alt="Total Hugging Face model downloads"></a> <a href="https://huggingface.co/collections/yeyingjin/yeying-lab-6b09480206e083c253ed2163"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/sumhfpaper-yeyinglab.svg" alt="Total Hugging Face paper upvotes"></a>

</div>

https://github.com/user-attachments/assets/e070b091-178b-4faf-be39-83f433563232

Yeying Lab is led by [Yeying Jin](https://jinyeying.github.io/) (Tencent · NUS).

📢 We're hiring 6-month research interns in world models and coding agents, in Singapore and in China. [Details](https://zhuanlan.zhihu.com/p/2070315664162689467) · [Apply on LinkedIn (Singapore, world models)](https://www.linkedin.com/jobs/view/4471500956/)

## Agentic gameplay and real-time world editing

<table>
<tr>
<td width="50%" valign="top">
<a href="https://yeyinglab.github.io/MaLiang/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/maliang.gif" width="100%" alt="MaLiang demo"></a>
<p><b>MaLiang</b>&nbsp; <img src="https://img.shields.io/badge/Code%20%26%20models-released-2ea44f?style=flat-square" alt="Code & models released" align="absmiddle"><br><sub><i>Painting Playable Game Worlds from Numbers</i></sub></p>
<p>Paint a map, and the world follows: a 4-step causal video model streams the game world in real time.</p>
<p><a href="https://yeyinglab.github.io/MaLiang/">Project</a> · <a href="https://github.com/YeyingLab/MaLiang"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-maliang.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/15y6u87/MaLiang"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-15y6u87-maliang.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/15y6u87/MaLiang-Data"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-15y6u87-maliang-data.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://wyzardwu.github.io/wizard/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/wizard.gif" width="100%" alt="Wizard demo"></a>
<p><b>Wizard</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Manipulate Any World in Real Time via Agentic Control</i></sub></p>
<p>Reshape any world in plain language; a video model renders the edits at 24 FPS in 2 steps.</p>
<p><a href="https://arxiv.org/abs/2610.40339">arXiv</a> · <a href="https://wyzardwu.github.io/wizard/">Project</a> · <a href="https://huggingface.co/papers/2610.40339"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2610.40339.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/Wizard"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-wizard.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/yuzhewu207/Wizard"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-yuzhewu207-wizard.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/yuzhewu207/wizard"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-yuzhewu207-wizard.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
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
<a href="https://jimntu.github.io/gamedirector/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/gamedirector.gif" width="100%" alt="GameDirector demo"></a>
<p><b>GameDirector</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models</i></sub></p>
<p>An agent runs the rules, states and NPC tactics while a world model renders them: boss action quality +39.9%.</p>
<p><a href="https://arxiv.org/abs/2609.25652">arXiv</a> · <a href="https://jimntu.github.io/gamedirector/">Project</a> · <a href="https://huggingface.co/papers/2609.25652"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2609.25652.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/GameDirector"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-gamedirector.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/onepiece1999/GameDirector"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-onepiece1999-gamedirector.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/onepiece1999/GameDirector-Training-Data"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-onepiece1999-gamedirector-training-data.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
</table>

## Coding agents and world-model infrastructure

<table>
<tr>
<td width="50%" valign="top">
<a href="https://teawhite.cn/GameCrafter/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/gamecrafter.gif" width="100%" alt="GameCrafter demo"></a>
<p><b>GameCrafter</b>&nbsp; <img src="https://img.shields.io/badge/Preprint-2026-6e7781?style=flat-square" alt="Preprint 2026" align="absmiddle"><br><sub><i>An Agentic Framework for Multi-Gameplay Game World Generation</i></sub></p>
<p>Coding agents turn one prompt into a playable multi-gameplay 3D world; best overall score (87.77) on a ten-task benchmark.</p>
<p><a href="https://github.com/YeyingLab/GameCrafter/blob/main/paper/GameCrafter.pdf">Paper</a> · <a href="https://teawhite.cn/GameCrafter/">Project</a> · <a href="https://github.com/YeyingLab/GameCrafter"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-gamecrafter.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/teawhite/GameCrafter"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-teawhite-gamecrafter.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://openenvision.org/WorldFoundry"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/worldfoundry.jpg" width="100%" alt="WorldFoundry demo"></a>
<p><b>WorldFoundry</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Towards Unified Infrastructure for World Intelligence</i></sub></p>
<p>One framework to run and evaluate world models: 270 models, 74 benchmarks and 62 metrics across video, 3D, 4D, interactive and embodied worlds. #2 on Hugging Face Daily Papers.</p>
<p><a href="https://arxiv.org/abs/2611.10771">arXiv</a> · <a href="https://openenvision.org/WorldFoundry">Project</a> · <a href="https://huggingface.co/papers/2611.10771"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2611.10771.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/OpenEnvision/WorldFoundry"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-openenvision-worldfoundry.svg" alt="GitHub stars" align="absmiddle"></a></p>
</td>
</tr>
</table>

## Spatially consistent action and language control

<table>
<tr>
<td width="50%" valign="top">
<a href="https://yeyinglab.github.io/SCOPE/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/scope.gif" width="100%" alt="SCOPE demo"></a>
<p><b>SCOPE</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Simulating Cross-game Operations in Playable Environments for FPS World Models</i></sub></p>
<p>An FPS world model trained on CrossFPS, the first multi-game FPS dataset: 69K clips, 7 titles, 10-DoF controls.</p>
<p><a href="https://arxiv.org/abs/2605.23345">arXiv</a> · <a href="https://yeyinglab.github.io/SCOPE/">Project</a> · <a href="https://huggingface.co/papers/2605.23345"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2605.23345.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/SCOPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-scope.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/zizhaotong/SCOPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-zizhaotong-scope.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/collections/zizhaotong/crossfps"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-collection-zizhaotong-crossfps.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://danzer1xxxxchan.github.io/H3-World/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/h3world.gif" width="100%" alt="H3-World demo"></a>
<p><b>H3-World</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Turning Language Understanding into World Control</i></sub></p>
<p>Turns a video model's language understanding into character and camera control, training only 0.199% of parameters.</p>
<p><a href="https://arxiv.org/abs/2609.01560">arXiv</a> · <a href="https://danzer1xxxxchan.github.io/H3-World/">Project</a> · <a href="https://huggingface.co/papers/2609.01560"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2609.01560.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/H3-World"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-h3-world.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/DANNY621/H3-World"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-danny621-h3-world.svg" alt="Hugging Face model downloads" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://teawhite.cn/ActionRoPE/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/actionrope.gif" width="100%" alt="ActionRoPE demo"></a>
<p><b>ActionRoPE</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Action as Coordinates for Spatially Consistent Control in Planar-Camera Game World Models</i></sub></p>
<p>Actions become world-coordinate rotary positions: 66% less revisit drift, on 1.3B–33B backbones.</p>
<p><a href="https://arxiv.org/abs/2610.25861">arXiv</a> · <a href="https://teawhite.cn/ActionRoPE/">Project</a> · <a href="https://huggingface.co/papers/2610.25861"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2610.25861.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/ActionRoPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-actionrope.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/teawhite/ActionRoPE"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-teawhite-actionrope.svg" alt="Hugging Face model likes" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://matrixteam-ai.github.io/pages/Incanation"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/incantation.gif" width="100%" alt="Incantation demo"></a>
<p><b>Incantation</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Natural Language as the Action Interface for Multi-Entity Video World Models</i></sub></p>
<p>Command many characters in plain language: 89% cross-entity transfer success vs. 43% for action-ID baselines.</p>
<p><a href="https://arxiv.org/abs/2605.18601">arXiv</a> · <a href="https://matrixteam-ai.github.io/pages/Incanation">Project</a> · <a href="https://www.reactor.inc/incantation">Play</a> · <a href="https://huggingface.co/papers/2605.18601"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2605.18601.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/zhushangwen/Incantation"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-zhushangwen-incantation.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/MatrixTeam/Incantation_preview_margit">🤗 Model</a> · <a href="https://huggingface.co/datasets/MatrixTeam/incantation-elden-ring-scenes"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-matrixteam-incantation-elden-ring-scenes.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/MatrixTeam/incantation_pro_dataset"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-prodata-matrixteam-incantation_pro_dataset.svg" alt="Hugging Face dataset downloads (pro)" align="absmiddle"></a></p>
</td>
</tr>
</table>

## State-aware gameplay and NPC behavior

<table>
<tr>
<td width="50%" valign="top">
<a href="https://inv-wzq.github.io/ReactiveGWM/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/reactivegwm.gif" width="100%" alt="ReactiveGWM demo"></a>
<p><b>ReactiveGWM</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Flexible Control and NPC Reactivity in Game World Models</i></sub></p>
<p>NPCs follow Offense / Defense / Control strategies and transfer zero-shot to unseen games.</p>
<p><a href="https://arxiv.org/abs/2605.15256">arXiv</a> · <a href="https://inv-wzq.github.io/ReactiveGWM/">Project</a> · <a href="https://huggingface.co/papers/2605.15256"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2605.15256.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/ReactiveGWM"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-reactivegwm.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/INV-WZQ/ReactiveGWM-Models"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hflike-model-inv-wzq-reactivegwm-models.svg" alt="Hugging Face model likes" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/INV-WZQ/ReactiveGWM-Datasets"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-inv-wzq-reactivegwm-datasets.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://jimntu.github.io/stateplay_page/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/stateplay.gif" width="100%" alt="StatePlay demo"></a>
<p><b>StatePlay</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>State-Aware Game World Models for Mechanics-Consistent Generation</i></sub></p>
<p>Generates frames together with game states (health, meters, timers): +18.6% mechanics fidelity.</p>
<p><a href="https://arxiv.org/abs/2607.26754">arXiv</a> · <a href="https://jimntu.github.io/stateplay_page/">Project</a> · <a href="https://huggingface.co/papers/2607.26754"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2607.26754.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/StatePlay"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-stateplay.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/onepiece1999/StatePlay"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-onepiece1999-stateplay.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/onepiece1999/StatePlay-Dataset"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-onepiece1999-stateplay-dataset.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="middle">
<a href="https://teawhite.cn/worldmind_projectpage/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/worldmind.gif" width="100%" alt="WorldMind demo"></a>
</td>
<td width="50%" valign="middle">
<p><b>WorldMind</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>Decoupled Game World Model for State-Aware NPC Behavior</i></sub></p>
<p>The first decoupled game world model for NPC behavior, from understanding to generation; preferred in ~70% of comparisons.</p>
<p><a href="https://arxiv.org/abs/2608.21439">arXiv</a> · <a href="https://teawhite.cn/worldmind_projectpage/">Project</a> · <a href="https://huggingface.co/papers/2608.21439"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2608.21439.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/WorldMind"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-worldmind.svg" alt="GitHub stars" align="absmiddle"></a></p>
</td>
</tr>
</table>

## Beyond games: agentic video

<table>
<tr>
<td width="50%" valign="middle">
<a href="https://yeyinglab.github.io/StoryEngine/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/storyengine.gif" width="100%" alt="StoryEngine demo"></a>
</td>
<td width="50%" valign="middle">
<p><b>StoryEngine</b>&nbsp; <img src="https://img.shields.io/badge/arXiv-2026-b31b1b?style=flat-square" alt="arXiv 2026" align="absmiddle"><br><sub><i>A State-Grounded Agentic Framework for Video Storytelling</i></sub></p>
<p>Turns a story into a multi-shot video, with every shot grounded in an explicit story state.</p>
<p><a href="https://arxiv.org/abs/2609.33627">arXiv</a> · <a href="https://yeyinglab.github.io/StoryEngine/">Project</a> · <a href="https://huggingface.co/papers/2609.33627"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2609.33627.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/StoryEngine"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-storyengine.svg" alt="GitHub stars" align="absmiddle"></a></p>
</td>
</tr>
</table>

## Beyond games: virtual try-on

<table>
<tr>
<td width="50%" valign="top">
<a href="https://yeyinglab.github.io/BooM-VVT/"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/boomvvt.gif" width="100%" alt="BooM-VVT demo"></a>
<p><b>BooM-VVT</b>&nbsp; <img src="https://img.shields.io/badge/ACM%20MM-2026-1f6feb?style=flat-square" alt="ACM MM 2026" align="absmiddle"><br><sub><i>Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data</i></sub></p>
<p>Dresses a person in any garment across a whole video without masks, trained with image-level pseudo data.</p>
<p><a href="https://arxiv.org/abs/2609.04120">arXiv</a> · <a href="https://yeyinglab.github.io/BooM-VVT/">Project</a> · <a href="https://huggingface.co/papers/2609.04120"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2609.04120.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/BooM-VVT"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-boom-vvt.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/zwpro/boomvvt"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-zwpro-boomvvt.svg" alt="Hugging Face model downloads" align="absmiddle"></a> · <a href="https://huggingface.co/datasets/zwpro/OmniView"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-data-zwpro-omniview.svg" alt="Hugging Face dataset downloads" align="absmiddle"></a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/YeyingLab/UniFit"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/assets/unifit.gif" width="100%" alt="UniFit demo"></a>
<p><b>UniFit</b>&nbsp; <img src="https://img.shields.io/badge/AAAI-2026-0b5394?style=flat-square" alt="AAAI 2026" align="absmiddle"><br><sub><i>Towards Universal Virtual Try-on with MLLM-Guided Semantic Alignment</i></sub></p>
<p>One model for many try-on tasks (multi-garment, model-to-model, model-free), aligned by a multimodal LLM.</p>
<p><a href="https://arxiv.org/abs/2511.15831">arXiv</a> · <a href="https://ojs.aaai.org/index.php/AAAI/article/view/38279">Paper</a> · <a href="https://huggingface.co/papers/2511.15831"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfpaper-2511.15831.svg" alt="Hugging Face paper upvotes" align="absmiddle"></a> · <a href="https://github.com/YeyingLab/UniFit"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/stars-yeyinglab-unifit.svg" alt="GitHub stars" align="absmiddle"></a> · <a href="https://huggingface.co/zwpro/UniFit"><img src="https://raw.githubusercontent.com/YeyingLab/.github/main/profile/badges/hfdl-model-zwpro-unifit.svg" alt="Hugging Face model downloads" align="absmiddle"></a></p>
</td>
</tr>
</table>
