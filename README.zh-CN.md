# 你好世界 :wink:

这是我进行与 github 操作/工作流、问题表单、模板相关的所有实验的存储库，首先在这里测试对项目的任何非代码相关贡献。

### 我现在有什么？

-   检查生产网站上损坏的链接并为此创建问题的操作。
-   贡献者的新问题表单，如错误报告问题模板等。

# 你好

如果原始 README 更改，则测试此操作是否也会更改 README 的本地化版本。

<h1 align="center">
  <img src="images/nerd-fonts-logo.svg" alt="Nerd Fonts Logo" />
</h1>
<h2 align="center">
  <img alt="Iconic font aggregator, collection, and patcher" src="images/project-subtitle-phrase.svg">
</h2>

<div align="center">
[Releases][release]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Fonts](#patched-fonts)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Font Patcher](#font-patcher)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Wiki Documentation][wiki]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Stickers][stickers]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[VimDevIcons][vim-devicons]

[![GitHub release][img-version-badge]][repo][![Gitter][img-gitter-badge]][gitter][![Build Status][img-travis-ci]][travis-ci][![Code of Conduct][coc-badge]][coc][![PRs Welcome][prs-badge]][prs]<a href="#patched-fonts" title=""><img src="https://raw.githubusercontent.com/wiki/ryanoasis/nerd-fonts/images/faux-shield-badge-os-logos.svg?sanitize=true" alt="Nerd Fonts - OS Support"></a>[![Twitter][twitter-badge]][twitter-intent]

</div>

**书呆子字体**是一个用大量字形（图标）修补开发人员目标字体的项目。特别是从流行的“标志性字体”中添加大量额外字形，例如[字体真棒➶][font-awesome],[神兽➶][vorillaz-devicons],[八角形 ➶][octicons]， 和[其他](#glyph-sets).

以下 Sankey 流程图显示了当前包含的字形集：

<p align="center">
  <img src="images/sankey-glyphs-combined-diagram.svg" alt="@SankeyMATIC Diagram" />
</p>

<sub><i>使用创建的图表<a href="http://sankeymatic.com/" title="SankeyMATIC (BETA): A Sankey diagram builder for everyone">@SankeyMATIC</a></i></sub>

## 重要通知

-   `master`分支文件路径是**不是**认为稳定。[验证您的存储库 URI 引用](#unstable-file-paths)
-   克隆这个存储库是**不是**受到推崇的 （[由于回购规模](#option-5-clone-the-repo)) 除非你打算[为发展做贡献](#contributing)

## 目录

[**TL; 博士**](#tldr)

[**安装选项**](#font-installation)

-   [**1 - 手册**](#option-1-download-and-install-manually)
-   [**2 - 发布存档下载**](#option-2-release-archive-download)
-   [**3 - 安装脚本**](#option-3-install-script)
-   [**4 - 自制字体 (macOS (OS X))**](#option-4-homebrew-fonts)
-   [**5 - 克隆回购**](#option-5-clone-the-repo)
-   [**6 - Ad Hoc Curl 下载**](#option-6-ad-hoc-curl-download)
-   [**7 - Arch 用户存储库 (AUR) (Arch Linux)**](#option-7-unofficial-arch-user-repository-aur)
-   [**8 - 修补你自己的字体**](#option-8-patch-your-own-font)

[**特征**](#features)

-   [**字形/图标集**](#glyph-sets)
-   [**修补字体**](#patched-fonts)
-   [**组合**](#combinations)
-   [**字体修补程序**](#font-patcher)

[**开发者/贡献者**](#font-patcher)

-   [**字体修补程序**](#font-patcher)
-   [**必须修补所有字体修补程序！**](#gotta-patch-em-all)
-   [**其他要修补的好字体**](#other-good-fonts-to-patch)
-   [**贡献**](#contributing)

[**项目动机**](#project-motivation)

**附加信息**

-   [**master 上的文件路径不稳定**](#unstable-file-paths)
-   [**变更日志**](#changelog)
-   [**执照**](#license)

## TL; 博士

Nerd Fonts 采用流行的编程字体并添加了一堆 Glyphs。
  还有一个[字体修补程序](#font-patcher)如果您想要的字体尚未修补，则可用。
  有关更多高级信息，请参阅[维基][wiki].如果您正在寻找 Vim 插件，请参阅[Vim 开发图标 ➶][vim-devicons].

### 各种字体下载选项

_如果你..._

-   `Option 1.`想要**迅速地**抢一个**个人字体**从下载[`patched-fonts/`目录](#patched-fonts)
-   `Option 2.`想下载一个**字体系列**变体包（粗体、斜体等）见[下载档案](#option-2-release-archive-download)
-   `Option 3.`想要**自动化**安装或使用**脚本**见[安装脚本](#option-3-install-script)
-   `Option 4.`在...上**苹果系统**并想使用**家酿**看[自制字体](#option-4-homebrew-fonts)
-   `Option 5.`想**完全控制**然后看[克隆 repo](#option-5-clone-the-repo)
-   `Option 6.`想要使用**`curl`命令**或用于**脚本**看[临时卷曲下载](#option-6-ad-hoc-curl-download)
-   `Option 7.`在...上**拱形Linux**并想使用**和包装**看[非官方 Arch 用户存储库](#option-7-unofficial-arch-user-repository-aur)
-   `Option 8.`想要修补自己的字体，请参阅[字体修补程序](#option-8-patch-your-own-font)

## 特征

-   一种[FontForge Python 脚本](#font-patcher)修补任何字体
    -   包括创建选项**等宽（固定间距，固定宽度）**_或者_**双倍宽度（非等宽）**字形
    -   有关更多详细信息，请参阅[**字体修补程序**](#font-patcher)部分
-   **`51`**已经[修补字体系列](#patched-fonts)
-   超过**`1,444,400`**修补字体的独特组合/变化[（更多细节）](#combinations)
-   超过**`2,824`**字形/图标组合[（更多细节）](#combinations)
    -   当前的字形集包括：[带有额外符号的电力线][ryanoasis-powerline-extra-symbols],[字体真棒][font-awesome],[材料设计图标][font-material-design-icons],[天气][font-weather],[神像][vorillaz-devicons],[八角形][octicons],[字体标志][font-linux]（以前[字体 Linux][font-linux]),[小丸子][gabrielelana-pomicons]
-   **等宽（固定间距，固定宽度）**_或者_**双倍宽度（非等宽）**每种字体的字形版本
    -   这是指 Nerd Font 字形本身不一定是整个字体
-   提供的开发人员/贡献者[bash脚本](#gotta-patch-em-all)重新修补所有字体

## 字形集

:mag: :mag: 您现在可以轻松搜索字形[N二代fonts.com][Cheat Sheet]通过[备忘单][]

看[Wiki: Glyph Sets and Codepoints 了解更多细节][wiki-glyph-sets-codepoints]

### shell 中的图标名称

看[Wiki：shell 中的图标名称][wiki-icon-names-in-shell]

## 修补字体

| 字体名称                                              | 字体名称和存储库                          | \*射频网 | 电磁尺寸 | 地位               |
| :------------------------------------------------ | :-------------------------------- | :---- | :--- | :--------------- |
| [3270 书呆子字体][p-3270]                              | [3270][f-3270]                    | 不     | 1000 | ![w]![m2]![l]    |
| [龙舌兰][p-agave]                                    | [龙舌兰][f-agave]                    | 不     | 2048 | ![w]![m2]![l]    |
| [匿名书呆子字体][p-anonymous-pro]                        | [匿名专业版][f-a-pro]                  | 不     | 2048 | ![w]![m2]![l]    |
| [有摩][p-arimo]                                     | [有摩][f-arimo]                     | 不     | 2048 | ![w]![m2]![l]    |
| [Aurulent Sans Mono Nerd 字体][p-aurulent]          |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [大蓝终端][p-bigblueterm]                             |                                   | 不     | 1200 | ![w]![m2]![l]    |
| [Bitstream Vera Sans Mono Nerd 字体][p-bitstream]   |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [布莱克斯\*][p-blex]                                  | [IBM Plex Mono][f-ibm-plex]       | 是的    | 1000 | ![w]![m2]![l]    |
| [Caskaydia Cove Nerd 字体\*][p-cascadia]            | [卡斯卡迪亚代码][f-cascadia]             | 是的    | 2048 | ![w]![m2]![l]    |
| [代码新罗马书呆子字体][p-code-nr]                           |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Cousin Nerd 字体][p-cousine]                       | [表哥][f-cousine]                   | 不     | 1000 | ![w]![m2]![l]    |
| [爸爸时间单声道][p-daddytimemono]                        | [爸爸时间单声道][f-daddytimemono]        | 不     | 1024 | ![w]![m2]![l]    |
| [Dejav 的个人价值 rd 电话 t][p-dejavu]                   |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Droid Sans Mono Nerd 字体][p-droid]                |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [异想天开的 Sans Nerd 字体][p-fantasque]                 | [梦幻般的没有][f-fant]                  | 不     | 2048 | ![w]![m2]![l]    |
| [Fira Code Nerd 字体][p-fira-code]                  | [费拉代码][f-fira-code]               | 不     | 1000 | ![w]![m2]![l]    |
| [Fila 人价值 rd 电话 t][p-fira-mono]                   | [公平的][f-fira-mono]                | 不     | 1000 | ![w]![m2]![l]    |
| [人的价值 rd 电话 t][p-go-mono]                         | [人][f-go-mono]                    | 不     | 1000 | ![w]![m2]![l]    |
| [Gohu Nerd 字体][p-gohu]                            | [悟空TTF][f-gohu2],[悟空][f-gohu]     | 不     | 1000 | ![w]![m2]![l]    |
| [Hack Nerd 字体][p-hack]                            | [黑客][f-hack]                      | 不     | 2048 | ![w]![m2]![l]    |
| [Hasklug 书呆子字体\*][p-hasklig]                      | [仓促][f-hasklig]                   | 是的    | 1000 | ![w]![m2]![l]    |
| [重数据 Mono Nerd 字体][p-heavy-data]                  |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Hurmit Nerd 字体][p-hermit]                        |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [我在写\*][p-im-writing]                             | [作家][f-ia-writer]                 | 是的    | 1000 | ![w]![m2]![l]    |
| [Inconsolata Nerd 字体][p-inconsolata]              |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [Inconsolata Go Nerd 字体][p-inconsolata-go]        |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [Inconsolata LGC Nerd 字体][p-inconsolata-lgc]      |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [Iosevka Nerd 字体][p-iosevka]                      | [约瑟夫卡][f-iosevka]                 | 不     | 1000 | [#83][s-iosevka] |
| [JetBrains 单声道][p-jetbrains-mono]                 | [JetBrains 单声道][f-jetbrains-mono] | 不     | 1000 | ![w]![m2]![l]    |
| [Lekton Nerd 字体][p-lekton]                        |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [Iterachion Monone rd 字体 \*][p-liberation]        | [解放][f-liberation]                | 是的    | 2048 | ![w]![m2]![l]    |
| [Lilex Nerd 字体][p-lilex]                          | [百合][f-lilex]                     | 不     | 2000 | ![w2]![m2]![l]   |
| [Meslo Nerd 字体][p-meslo]                          |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Monofur Nerd 字体][p-monofur]                      |                                   | 不     | 2400 | ![w]![m2]![l]    |
| [Monoid 书呆子字体][p-monoid]                          |                                   | 不     | 1536 | ![w]![m2]![l]    |
| [树值 rd 电话 t][p-mononoki]                          | [事物之树][f-mononoki]                | 不     | 1024 | ![w]![m2]![l]    |
| [M+ (MPlus) 书呆子字体][p-mplus]                       |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [已知][p-noto]                                      |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [开放阅读障碍][p-opendyslexic]                          |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [立交桥][p-overpass]                                 |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [ProFont（Windows 调整）书呆子字体][p-profont]             |                                   | 不     | 1200 | ![w]![m2]![l]    |
| [ProFont (x11) 书呆子字体][p-profont]                  |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [ProggyClean Nerd 字体][p-proggy-clean]             |                                   | 不     | 2048 | 不完善              |
| [机器人和人][p-roboto]                                 |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Sauce Code Nerd 字体][p-source-code-pro]           | [来源][f-source]                    | 是的    | 1000 | ![w]![m2]![l]    |
| [Shu Re tech mono nerd font\*][p-share-tech-mono] | [时尚手ch人][f-share]                 | 是的    | 1000 | ![w]![m2]![l]    |
| [Space Mono Nerd 字体][p-space-mono]                | [太空单声道][f-space]                  | 不     | 1000 | ![w]![m2]![l]    |
| [Teriness Nerd 字体\*][p-terminus]                  | [总站字体][f-terminus]                | 是的    | 1000 | ![w]![m2]![l]    |
| [蒂诺斯][p-tinos]                                    |                                   | 不     | 2048 | ![w]![m2]![l]    |
| [Ubuntu 书呆子字体][p-ubuntu]                          |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [Ubunz 人价值 rd 电话 t][p-ubuntu-mono]                |                                   | 不     | 1000 | ![w]![m2]![l]    |
| [维克多·莫诺][p-victor]                                | [维克多·莫诺][f-victor]                | 不     | 1000 | ![w]![m2]![l]    |

<sub>_\*RFN = 保留字体名称_</sub>

## 组合

-   超过**`1,485,000`**修补字体的独特变体/组合（Power Set）：
    -   **`50`**修补字体
    -   **`719`**修补字体系列
    -   **`2,876`**“完整”变体/组合
    -   **`'1,485,410'`**_可能的_变化/组合
    -   -   **`1,488,286`**计算组合总数 (2,876 + 1,428,110)
-   每种字体的组合是[变化](#variations)

### 变化

-   没有给出标志（默认为只有**Seti-OY + 布什**和**[神像][vorillaz-devicons]**)
-   **双倍的_（可变/比例）_**或者**单身的_（固定/等宽）_**宽度字形
-   [字体真棒][font-awesome]
-   [字体真棒扩展][font-awesome-extension]
-   [材料设计图标][font-material-design-icons]
-   [天气][font-weather]
-   [GitHub Octicons][octicons]
-   [字体标志][font-linux]（以前[字体 Linux][font-linux])
-   [电力线额外符号][ryanoasis-powerline-extra-symbols]
-   [IEC 电源符号][website-iecpower]
-   [小丸子][gabrielelana-pomicons]
-   Windows 兼容性

## 字体安装

### `Option 1: Download and Install Manually`

> 最佳选择**迅速地**得到一个特定的**个人字体**.

具体下载[修补字体](#patched-fonts)你的选择

### `Option 2: Release Archive Download`

> 如果你想要一个最好的选择**档案**或完成**字体系列**变体（粗体、斜体等）。

字体可作为包下载[最新发布](https://github.com/ryanoasis/nerd-fonts/releases/latest)

### `Option 3: Install Script`

> 如果你愿意，最好的选择**自动化**安装或用于**脚本**.

_笔记_:**需要克隆**截至目前的回购

#### 所有字体：

-   安装所有打过补丁的字体（_警告：这是很多字体加起来很大_)

```sh
./install.sh
```

或者，在 Powershell 中（仅限 Windows）：

```pwsh
./install.ps1
```

#### 单一字体：

-   安装您选择的单个字体

```sh
./install.sh <FontName>
./install.sh Hack
./install.sh HeavyData
```

或者，在 Powershell 中（仅限 Windows）：

```pwsh
./install.ps1 <FontName>
./install.ps1 Hack
./install.ps1 HeavyData
```

### `Option 4: Homebrew Fonts`

> 如果打开，最好的选择**苹果系统**并想使用**家酿**.

所有字体均可通过[Homebrew Cask 字体](https://github.com/Homebrew/homebrew-cask-fonts)在 macOS (OS X) 上

```sh
brew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
```

### `Option 5: Clone the Repo`

> 最佳选择**完全控制**,**全部**或者**一些**的字体，或**贡献**发展。

此存储库的完整克隆是**不是**如果您只对有限的一组字体感兴趣，则不需要也不高效（主要是由于存储库大小）。

如果您确实想克隆整个 repo，请确保_浅_克隆：

```sh
git clone --depth 1
```

如果要克隆子目录，请使用`git sparse-checkout`.下面的例子需要`Git v2.26`:

```sh
git clone --filter=blob:none --sparse git@github.com:ryanoasis/nerd-fonts
cd nerd-fonts
git sparse-checkout add patched-fonts/JetBrainsMono
```

### `Option 6: Ad Hoc Curl Download`

> 选项如果你想使用**`curl`命令**或用于**脚本**.

#### Linux

```sh
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

_笔记：_弃用的替代路径：`~/.fonts`

#### macOS (OS X)

```sh
cd ~/Library/Fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

### `Option 7: Unofficial Arch User Repository (AUR)`

> 选项**拱形Linux**并想使用**和包装**.

以下字体可通过[和包装](https://aur.archlinux.org/)在 Arch Linux 上：

-   [书呆子字体完整（双宽）](https://aur.archlinux.org/packages/nerd-fonts-complete/)
-   [Nerd Fonts Complete（单宽）（过时）](https://aur.archlinux.org/packages/nerd-fonts-complete-mono-glyphs/)
-   [书呆子字体 DejaVu 完成](https://aur.archlinux.org/packages/nerd-fonts-dejavu-complete/)
-   [书呆子字体源代码专业版完整](https://aur.archlinux.org/packages/nerd-fonts-source-code-pro/)
-   [书呆子字体 Git（过时）](https://aur.archlinux.org/packages/nerd-fonts-git/)
-   [书呆子字体 Fira 代码](https://aur.archlinux.org/packages/nerd-fonts-fira-code/)
-   [书呆子字体总站](https://aur.archlinux.org/packages/nerd-fonts-terminus/)
-   [书呆子字体解放单声道](https://aur.archlinux.org/packages/nerd-fonts-liberation-mono/)
-   [根 rd 电话 ts 人](https://aur.archlinux.org/packages/nerd-fonts-go-mono/)
-   [书呆子字体匿名专业版](https://aur.archlinux.org/packages/nerd-fonts-anonymous-pro/)
-   [根 rd 电话 ts 门](https://aur.archlinux.org/packages/nerd-fonts-noto/)
-   [书呆子字体 Inconsolata](https://aur.archlinux.org/packages/nerd-fonts-inconsolata/)

### `Option 8: Patch Your Own Font`

> 的选项**修补**您的**自己的字体**或完全**定制**修补的字体。

使用提供的 Python 命令行脚本从您自己的字体生成修补字体以获得额外的新字形

看：[字体修补程序](#font-patcher)用途

-   如果您这样做，请使用此选项**不是**想使用其中之一[提供的字体](#patched-fonts)
-   您仍然需要将生成的字体复制到系统上正确的字体目录

<h2 align="center" id="font-patcher">
	<img src="images/nerd-fonts-patcher-logo.png" alt="Nerd Fonts Patcher">
</h2>

修补您自己选择的字体以用于[Vim 开发图标 ➶][vim-devicons]:

-   要求：Python 2（或 Python 3），`python-fontforge`包（版本`20141231`或稍后，请参阅
    这[安装说明](http://designwithfontforge.com/en-US/Installing_Fontforge.html))

-   OSX 上的替代安装方法：`brew install fontforge`

-   Linux 上的替代方法：使用[应用图片](https://github.com/fontforge/fontforge/releases)

-   使用 Docker 的替代方法：[码头工人中心](https://hub.docker.com/r/nerdfonts/patcher)

-   用法：

        ./font-patcher PATH_TO_FONT

-   替代用法：使用脚本标志使用 FontForge 二进制文件执行修补程序：

        ./fontforge -script font-patcher PATH_TO_FONT

-   使用 AppImage 修补字体：

    _笔记_:`chmod u+x`下载后的 AppImage。所有提供的路径都需要**绝对**并且需要明确的输出路径！如果所有内容都位于同一目录中，则可以使用`$PWD`速记。

        ./FontForge.AppImage -script $PWD/font-patcher $PWD/BaseFont.ttf -out /tmp

-   使用 Docker 修补字体：

        docker run -v /path/to/fonts:/in -v /path/for/output:/out nerdfonts/patcher [OPTIONS]

完整选项：

    usage: font-patcher [-h] [-v] [-s] [-l] [-q] [-w] [-c] [--fontawesome]
                        [--fontawesomeextension] [--fontlinux] [--octicons]
                        [--powersymbols] [--pomicons] [--powerline]
                        [--powerlineextra] [--material] [--weather]
                        [--custom [CUSTOM]] [--postprocess [POSTPROCESS]]
                        [--removeligs] [--configfile [CONFIGFILE]]
                        [--progressbars | --no-progressbars] [--careful]
                        [-ext [EXTENSION]] [-out [OUTPUTDIR]]
                        font

    Nerd Fonts Font Patcher: patches a given font with programming and development related glyphs

    * Website: https://www.nerdfonts.com
    * Version: 2.0.0
    * Development Website: https://github.com/ryanoasis/nerd-fonts
    * Changelog: https://github.com/ryanoasis/nerd-fonts/blob/master/changelog.md

    positional arguments:
      font                  The path to the font to patch (e.g., Inconsolata.otf)

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -s, --mono, --use-single-width-glyphs
                            Whether to generate the glyphs as single-width not double-width (default is double-width)
      -l, --adjust-line-height
                            Whether to adjust line heights (attempt to center powerline separators more evenly)
      -q, --quiet, --shutup
                            Do not generate verbose output
      -w, --windows         Limit the internal font name to 31 characters (for Windows compatibility)
      -c, --complete        Add all available Glyphs
      --fontawesome         Add Font Awesome Glyphs (http://fontawesome.io/)
      --fontawesomeextension
                            Add Font Awesome Extension Glyphs (https://andrelzgava.github.io/font-awesome-extension/)
      --fontlinux, --fontlogos
                            Add Font Linux and other open source Glyphs (https://github.com/Lukas-W/font-logos)
      --octicons            Add Octicons Glyphs (https://octicons.github.com)
      --powersymbols        Add IEC Power Symbols (https://unicodepowersymbol.com/)
      --pomicons            Add Pomicon Glyphs (https://github.com/gabrielelana/pomicons)
      --powerline           Add Powerline Glyphs
      --powerlineextra      Add Powerline Glyphs (https://github.com/ryanoasis/powerline-extra-symbols)
      --material, --materialdesignicons, --mdi
                            Add Material Design Icons (https://github.com/templarian/MaterialDesign)
      --weather, --weathericons
                            Add Weather Icons (https://github.com/erikflowers/weather-icons)
      --custom [CUSTOM]     Specify a custom symbol font. All new glyphs will be copied, with no scaling applied.
      --postprocess [POSTPROCESS]
                            Specify a Script for Post Processing
      --removeligs, --removeligatures
                            Removes ligatures specified in JSON configuration file
      --configfile [CONFIGFILE]
                            Specify a file path for JSON configuration file (see sample: src/config.sample.json)
      --progressbars        Show percentage completion progress bars per Glyph Set
      --no-progressbars     Don't show percentage completion progress bars per Glyph Set
      --careful             Do not overwrite existing glyphs if detected
      -ext [EXTENSION], --extension [EXTENSION]
                            Change font file type to create (e.g., ttf, otf)
      -out [OUTPUTDIR], --outputdir [OUTPUTDIR]
                            The directory to output the patched font file to

#### 例子

    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf
    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf -s -q
    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf --use-single-width-glyphs --quiet
    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf -w
    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf --windows --quiet
    ./font-patcher Droid\ Sans\ Mono\ for\ Powerline.otf --windows --pomicons --quiet

    ./font-patcher Inconsolata.otf --fontawesome
    ./font-patcher Inconsolata.otf --fontawesome --octicons --pomicons
    ./font-patcher Inconsolata.otf

    ./FontForge.AppImage -script /tmp/nerdfonts/font-patcher /tmp/nerdfonts/CascadiaMonoPL-Semibold.ttf --fontawesome -out /tmp
    ./FontForge.AppImage -script $PWD/font-patcher $PWD/CascadiaMonoPL-Semibold.ttf --octicons -out $HOME

    docker run --rm -v ~/myfont/patchme:/in -v ~/myfont/patched:/out nerdfonts/patcher
    docker run --rm -v ~/Desktop/myfont/patchme:/in -v ~/Desktop/myfont/patched:/out nerdfonts/patcher --fontawesome

<a name="gotta-patch-em-all"></a>

## 必须修补所有字体修补程序！

-   供贡献者或开发者使用

-   重新打补丁**全部**未修补目录中的字体：

        ./gotta-patch-em-all-font-patcher\!.sh

-   可以选择限制为特定的字体名称模式：

        ./gotta-patch-em-all-font-patcher\!.sh Hermit

## 贡献

看[contributing.面对](contributing.md)

## 不稳定的文件路径

:warning: 警告: 文件路径可能会根据版本（尤其是**重大的**版本颠簸）

参考**释放**分支和_不是_这~~掌握~~分支，因为每个版本的路径都会发生变化

-   例如：
    -   :white_check_mark: 使用：<code>https\\://github.com/ryanoasis/nerd-fonts/blob/<b>0.9.0</b>/patched-fonts/hermit/medium/complete/hu RMIT%20medium%20nerd%20font%20complete.喔套房</code>
    -   :x: 而不是：<code>https\\://github.com/ryanoasis/nerd-fonts/blob/<del>掌握</del>/patched-fonts/hermit/medium/complete/hu RMIT%20medium%20nerd%20font%20complete.喔套房</code>

## 其他要修补的好字体

由于许可证而无法提供或共享的要修补的其他好字体列表：

-   [输入单声道][input-mono]（许可证限制）
    -   可能带有外部托管:)
-   [事情为][pragmatapro]（不是免费的）
-   [控制台][consolas]（所有权）
-   [歌剧和人][operator]（不是免费的）
-   [感谢 Mono][dank]（不是免费的）

## 项目动机

看[维基：项目目的][wiki-project-purpose]

## 变更日志

看[change log.面对](changelog.md)

## 执照

[和](LICENSE)© 瑞安 L 麦金太尔

<!--
Repo References
-->

[vim-devicons]: https://github.com/ryanoasis/vim-devicons "VimDevIcons Vim Plugin (external link) ➶"

[vorillaz-devicons]: https://vorillaz.github.io/devicons/

[font-awesome]: https://github.com/FortAwesome/Font-Awesome

[font-awesome-extension]: https://github.com/AndreLZGava/font-awesome-extension

[font-material-design-icons]: https://github.com/Templarian/MaterialDesign

[font-weather]: https://github.com/erikflowers/weather-icons

[octicons]: https://github.com/primer/octicons

[font-linux]: https://github.com/Lukas-W/font-logos

[gabrielelana-pomicons]: https://github.com/gabrielelana/pomicons

[Seti-UI]: https://atom.io/themes/seti-ui

[ryanoasis-powerline-extra-symbols]: https://github.com/ryanoasis/powerline-extra-symbols

[wiki]: https://github.com/ryanoasis/nerd-fonts/wiki

[wiki-project-purpose]: https://github.com/ryanoasis/nerd-fonts/wiki/Project-Purpose

[wiki-glyph-sets-codepoints]: https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points

[wiki-icon-names-in-shell]: https://github.com/ryanoasis/nerd-fonts/wiki/Icon-Names-in-Shell

[repo]: https://github.com/ryanoasis/nerd-fonts

[gitter]: https://gitter.im/ryanoasis/nerd-fonts

[code-climate]: https://codeclimate.com/github/ryanoasis/nerd-fonts

[travis-ci]: https://travis-ci.org/ryanoasis/nerd-fonts

[twitter-intent]: https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fryanoasis%2Fnerd-fonts&via=%40nerdfonts&text=Nerd%20Fonts%20-%20Iconic%20font%20aggregator%2C%20collection%2C%20and%20patcher&hashtags=iconfont%20font%20github

<!--
Website References
-->

[website-iecpower]: https://unicodepowersymbol.com/

[Cheat Sheet]: https://nerdfonts.com/cheat-sheet

[stickers]: https://www.redbubble.com/people/ryanoasis/works/30764810-nerd-fonts-iconic-font-aggregator

<!--
Link References
-->

[badge-version]: https://badge.fury.io/gh/ryanoasis%2Fnerd-fonts

[badge-gitter]: https://gitter.im/ryanoasis/nerd-fonts?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

[img-version-badge]: https://img.shields.io/github/release/ryanoasis/nerd-fonts.svg?style=for-the-badge

[img-gitter-badge]: https://img.shields.io/gitter/room/nwjs/nw.js.svg?style=for-the-badge

[img-code-climate-badge]: https://img.shields.io/codeclimate/issues/ryanoasis/nerd-fonts.svg?style=for-the-badge

[img-travis-ci]: https://img.shields.io/travis/ryanoasis/nerd-fonts.svg?branch=master&style=for-the-badge

[coc-badge]: https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=for-the-badge

[prs-badge]: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIGlkPSJzdmcyIiB3aWR0aD0iNjQ1IiBoZWlnaHQ9IjU4NSIgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPiA8ZyBpZD0ibGF5ZXIxIj4gIDxwYXRoIGlkPSJwYXRoMjQxNyIgZD0ibTI5Ny4zIDU1MC44N2MtMTMuNzc1LTE1LjQzNi00OC4xNzEtNDUuNTMtNzYuNDM1LTY2Ljg3NC04My43NDQtNjMuMjQyLTk1LjE0Mi03Mi4zOTQtMTI5LjE0LTEwMy43LTYyLjY4NS01Ny43Mi04OS4zMDYtMTE1LjcxLTg5LjIxNC0xOTQuMzQgMC4wNDQ1MTItMzguMzg0IDIuNjYwOC01My4xNzIgMTMuNDEtNzUuNzk3IDE4LjIzNy0zOC4zODYgNDUuMS02Ni45MDkgNzkuNDQ1LTg0LjM1NSAyNC4zMjUtMTIuMzU2IDM2LjMyMy0xNy44NDUgNzYuOTQ0LTE4LjA3IDQyLjQ5My0wLjIzNDgzIDUxLjQzOSA0LjcxOTcgNzYuNDM1IDE4LjQ1MiAzMC40MjUgMTYuNzE0IDYxLjc0IDUyLjQzNiA2OC4yMTMgNzcuODExbDMuOTk4MSAxNS42NzIgOS44NTk2LTIxLjU4NWM1NS43MTYtMTIxLjk3IDIzMy42LTEyMC4xNSAyOTUuNSAzLjAzMTYgMTkuNjM4IDM5LjA3NiAyMS43OTQgMTIyLjUxIDQuMzgwMSAxNjkuNTEtMjIuNzE1IDYxLjMwOS02NS4zOCAxMDguMDUtMTY0LjAxIDE3OS42OC02NC42ODEgNDYuOTc0LTEzNy44OCAxMTguMDUtMTQyLjk4IDEyOC4wMy01LjkxNTUgMTEuNTg4LTAuMjgyMTYgMS44MTU5LTI2LjQwOC0yNy40NjF6IiBmaWxsPSIjZGQ1MDRmIi8%2BIDwvZz48L3N2Zz4%3D

[twitter-badge]: https://img.shields.io/twitter/url/http/shields.io.svg?style=for-the-badge&logo=twitter

[os-badge]: https://img.shields.io/badge/-OS-brightgreen.svg?style=for-the-badge&logoWidth=80&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIHdpZHRoPSIzOS43NDFtbSIgaGVpZ2h0PSIxMy4zNzdtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMzkuNzQxMjggMTMuMzc3MTI3IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48bWV0YWRhdGE%2BPHJkZjpSREY%2BPGNjOldvcmsgcmRmOmFib3V0PSIiPjxkYzpmb3JtYXQ%2BaW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PjxkYzp0eXBlIHJkZjpyZXNvdXJjZT0iaHR0cDovL3B1cmwub3JnL2RjL2RjbWl0eXBlL1N0aWxsSW1hZ2UiLz48ZGM6dGl0bGUvPjwvY2M6V29yaz48L3JkZjpSREY%2BPC9tZXRhZGF0YT48ZyB0cmFuc2Zvcm09Im1hdHJpeCguMzMwODMgMCAwIC4zMzA4MyAyNi41MDggLTEuNzc0MikiPjxwb2x5Z29uIHBvaW50cz0iMTcuNCAzOC4zIDIxLjUgNDAuNiAyNy43IDQwLjYgMzMuNSAzNi4yIDM2LjEgMjkuMyAzMC4xIDIyIDI4LjQgMTcuOSAyMC4xIDE4LjIgMjAuMiAyMC41IDE4LjYgMjMuNSAxNi4xIDI4LjQgMTUuNiAzMi41IiBmaWxsPSIjZWNlZmYxIi8%2BPHBhdGggZD0ibTM0LjMgMjMuOWMtMS42LTIuMy0yLjktMy43LTMuNi02LjZzMC4yLTIuMS0wLjQtNC42Yy0wLjMtMS4zLTAuOC0yLjItMS4zLTIuOS0wLjYtMC43LTEuMy0xLjEtMS43LTEuMi0wLjktMC41LTMtMS4zLTUuNiAwLjEtMi43IDEuNC0yLjQgNC40LTEuOSAxMC41IDAgMC40LTAuMSAwLjktMC4zIDEuMy0wLjQgMC45LTEuMSAxLjctMS43IDIuNC0wLjcgMS0xLjQgMi0xLjkgMy4xLTEuMiAyLjMtMi4zIDUuMi0yIDYuMyAwLjUtMC4xIDYuOCA5LjUgNi44IDkuNyAwLjQtMC4xIDIuMS0wLjEgMy42LTAuMSAyLjEtMC4xIDMuMy0wLjIgNSAwLjIgMC0wLjMtMC4xLTAuNi0wLjEtMC45IDAtMC42IDAuMS0xLjEgMC4yLTEuOCAwLjEtMC41IDAuMi0xIDAuMy0xLjYtMSAwLjktMi44IDEuOS00LjUgMi4yLTEuNSAwLjMtNC0wLjItNS4yLTEuNyAwLjEgMCAwLjMgMCAwLjQtMC4xIDAuMy0wLjEgMC42LTAuMiAwLjctMC40IDAuMy0wLjUgMC4xLTEtMC4xLTEuM3MtMS43LTEuNC0yLjQtMi0xLjEtMC45LTEuNS0xLjNsLTAuOC0wLjhjLTAuMi0wLjItMC4zLTAuNC0wLjQtMC41LTAuMi0wLjUtMC4zLTEuMS0wLjItMS45IDAuMS0xLjEgMC41LTIgMS0zIDAuMi0wLjQgMC43LTEuMiAwLjctMS4ycy0xLjcgNC4yLTAuOCA1LjVjMCAwIDAuMS0xLjMgMC41LTIuNiAwLjMtMC45IDAuOC0yLjIgMS40LTIuOXMyLjEtMy4zIDIuMi00LjljMC0wLjcgMC4xLTEuNCAwLjEtMS45LTAuNC0wLjQgNi42LTEuNCA3LTAuMyAwLjEgMC40IDEuNSA0IDIuMyA1LjkgMC40IDAuOSAwLjkgMS43IDEuMiAyLjcgMC4zIDEuMSAwLjUgMi42IDAuNSA0LjEgMCAwLjMgMCAwLjgtMC4xIDEuMyAwLjIgMCA0LjEtNC4yLTAuNS03LjcgMCAwIDIuOCAxLjMgMi45IDMuOSAwLjEgMi4xLTAuOCAzLjgtMSA0LjEgMC4xIDAgMi4xIDAuOSAyLjIgMC45IDAuNCAwIDEuMi0wLjMgMS4yLTAuMyAwLjEtMC4zIDAuNC0xLjEgMC40LTEuNCAwLjctMi4zLTEtNi0yLjYtOC4zeiIgZmlsbD0iIzI2MzIzOCIvPjxnIGZpbGw9IiNlY2VmZjEiPjxlbGxpcHNlIGN4PSIyMS42IiBjeT0iMTUuMyIgcng9IjEuMyIgcnk9IjIiLz48ZWxsaXBzZSBjeD0iMjYuMSIgY3k9IjE1LjIiIHJ4PSIxLjciIHJ5PSIyLjMiLz48L2c%2BPGcgZmlsbD0iIzIxMjEyMSI%2BPGVsbGlwc2UgdHJhbnNmb3JtPSJtYXRyaXgoLS4xMjU0IC0uOTkyMSAuOTkyMSAtLjEyNTQgOC45NzU0IDM4Ljk5NykiIGN4PSIyMS43IiBjeT0iMTUuNSIgcng9IjEuMiIgcnk9Ii43Ii8%2BPGVsbGlwc2UgY3g9IjI2IiBjeT0iMTUuNiIgcng9IjEiIHJ5PSIxLjMiLz48L2c%2BPGcgZmlsbD0iI2ZmYzEwNyI%2BPHBhdGggZD0ibTM5LjMgMzcuNmMtMC40LTAuMi0xLjEtMC41LTEuNy0xLjQtMC4zLTAuNS0wLjItMS45LTAuNy0yLjUtMC4zLTAuNC0wLjctMC4yLTAuOC0wLjItMC45IDAuMi0zIDEuNi00LjQgMC0wLjItMC4yLTAuNS0wLjUtMS0wLjVzLTAuNyAwLjItMC45IDAuNi0wLjIgMC43LTAuMiAxLjdjMCAwLjggMCAxLjctMC4xIDIuNC0wLjIgMS43LTAuNSAyLjctMC41IDMuNyAwIDEuMSAwLjMgMS44IDAuNyAyLjEgMC4zIDAuMyAwLjggMC41IDEuOSAwLjVzMS44LTAuNCAyLjUtMS4xYzAuNS0wLjUgMC45LTAuNyAyLjMtMS43IDEuMS0wLjcgMi44LTEuNiAzLjEtMS45IDAuMi0wLjIgMC41LTAuMyAwLjUtMC45IDAtMC41LTAuNC0wLjctMC43LTAuOHoiLz48cGF0aCBkPSJtMTkuMiAzNy45Yy0xLTEuNi0xLjEtMS45LTEuOC0yLjktMC42LTEtMS45LTIuOS0yLjctMi45LTAuNiAwLTAuOSAwLjMtMS4zIDAuN3MtMC44IDEuMy0xLjUgMS44Yy0wLjYgMC41LTIuMyAwLjQtMi43IDFzMC40IDEuNSAwLjQgM2MwIDAuNi0wLjUgMS0wLjYgMS40LTAuMSAwLjUtMC4yIDAuOCAwIDEuMiAwLjQgMC42IDAuOSAwLjggNC4zIDEuNSAxLjggMC40IDMuNSAxLjQgNC42IDEuNXMzIDAgMy0yLjdjMC4xLTEuNi0wLjgtMi0xLjctMy42eiIvPjxwYXRoIGQ9Im0yMS4xIDE5LjhjLTAuNi0wLjQtMS4xLTAuOC0xLjEtMS40czAuNC0wLjggMS0xLjNjMC4xLTAuMSAxLjItMS4xIDIuMy0xLjFzMi40IDAuNyAyLjkgMC45YzAuOSAwLjIgMS44IDAuNCAxLjcgMS4xLTAuMSAxLTAuMiAxLjItMS4yIDEuNy0wLjcgMC4yLTIgMS4zLTIuOSAxLjMtMC40IDAtMSAwLTEuNC0wLjEtMC4zLTAuMS0wLjgtMC42LTEuMy0xLjF6Ii8%2BPC9nPjxnIGZpbGw9IiM2MzQ3MDMiPjxwYXRoIGQ9Im0yMC45IDE5YzAuMiAwLjIgMC41IDAuNCAwLjggMC41IDAuMiAwLjEgMC41IDAuMiAwLjUgMC4yaDAuOWMwLjUgMCAxLjItMC4yIDEuOS0wLjYgMC43LTAuMyAwLjgtMC41IDEuMy0wLjcgMC41LTAuMyAxLTAuNiAwLjgtMC43cy0wLjQgMC0xLjEgMC40Yy0wLjYgMC40LTEuMSAwLjYtMS43IDAuOS0wLjMgMC4xLTAuNyAwLjMtMSAwLjNoLTAuOWMtMC4zIDAtMC41LTAuMS0wLjgtMC4yLTAuMi0wLjEtMC4zLTAuMi0wLjQtMC4yLTAuMi0wLjEtMC42LTAuNS0wLjgtMC42IDAgMC0wLjIgMC0wLjEgMC4xbDAuNiAwLjZ6Ii8%2BPHBhdGggZD0ibTIzLjkgMTYuOGMwLjEgMC4yIDAuMyAwLjIgMC40IDAuM3MwLjIgMC4xIDAuMiAwLjFjMC4xLTAuMSAwLTAuMy0wLjEtMC4zIDAtMC4yLTAuNS0wLjItMC41LTAuMXoiLz48cGF0aCBkPSJtMjIuMyAxN2MwIDAuMSAwLjIgMC4yIDAuMiAwLjEgMC4xLTAuMSAwLjItMC4yIDAuMy0wLjIgMC4yLTAuMSAwLjEtMC4yLTAuMi0wLjItMC4yIDAuMS0wLjIgMC4yLTAuMyAwLjN6Ii8%2BPC9nPjxwYXRoIGQ9Im0zMiAzNC43djAuM2MwLjIgMC40IDAuNyAwLjUgMS4xIDAuNSAwLjYgMCAxLjItMC40IDEuNS0wLjggMC0wLjEgMC4xLTAuMiAwLjItMC4zIDAuMi0wLjMgMC4zLTAuNSAwLjQtMC42IDAgMC0wLjEtMC4xLTAuMS0wLjItMC4xLTAuMi0wLjQtMC40LTAuOC0wLjUtMC4zLTAuMS0wLjgtMC4yLTEtMC4yLTAuOS0wLjEtMS40IDAuMi0xLjcgMC41IDAgMCAwLjEgMCAwLjEgMC4xIDAuMiAwLjIgMC4zIDAuNCAwLjMgMC43IDAuMSAwLjIgMCAwLjMgMCAwLjV6IiBmaWxsPSIjNDU1YTY0Ii8%2BPC9nPjxnIHRyYW5zZm9ybT0ibWF0cml4KC4xMzk0NSAwIDAgLjEzOTQ1IDAgMS4xNjIzKSI%2BPHBhdGggZD0ibTAgMTIuNDAyIDM1LjY4Ny00Ljg2MDIgMC4wMTU2IDM0LjQyMy0zNS42NyAwLjIwMzEzeiIgZmlsbD0iI2Y4NjgyYyIvPjxwYXRoIGQ9Im0zOS45OTYgNi45MDU5IDQ3LjMxOC02LjkwNnY0MS41MjdsLTQ3LjMxOCAwLjM3NTY1eiIgZmlsbD0iIzkxYzMwMCIvPjxwYXRoIGQ9Im0zNS42NyA0NS45MzEgMC4wMjc3IDM0LjQ1My0zNS42Ny00LjkwNDEtMmUtMyAtMjkuNzh6IiBmaWxsPSIjMDBiNGYxIi8%2BPHBhdGggZD0ibTg3LjMyNiA0Ni4yNTUtMC4wMTExIDQxLjM0LTQ3LjMxOC02LjY3ODQtMC4wNjYzLTM0LjczOXoiIGZpbGw9IiNmZmMzMDAiLz48L2c%2BPHBhdGggZD0ibTI2LjEzNyAxMC4yODRjLTAuMTk5NTggMC40NjEwNi0wLjQzNTgxIDAuODg1NDctMC43MDk1MiAxLjI3NTctMC4zNzMwOCAwLjUzMTkzLTAuNjc4NTYgMC45MDAxMy0wLjkxMzk4IDEuMTA0Ni0wLjM2NDk0IDAuMzM1NjItMC43NTU5NSAwLjUwNzUtMS4xNzQ2IDAuNTE3MjctMC4zMDA1OSAwLTAuNjYzMDgtMC4wODU1My0xLjA4NS0wLjI1OTA0LTAuNDIzMzUtMC4xNzI2OS0wLjgxMjQtMC4yNTgyMy0xLjE2ODEtMC4yNTgyMy0wLjM3MzA4IDAtMC43NzMyMiAwLjA4NTU0LTEuMjAxMiAwLjI1ODIzLTAuNDI4NjQgMC4xNzM1MS0wLjc3Mzk1IDAuMjYzOTMtMS4wMzggMC4yNzI4OS0wLjQwMTUyIDAuMDE3MTItMC44MDE3My0wLjE1OTY2LTEuMjAxMi0wLjUzMTEyLTAuMjU0OTctMC4yMjIzOC0wLjU3Mzg4LTAuNjAzNjItMC45NTU5My0xLjE0MzctMC40MDk5LTAuNTc2NzQtMC43NDY5MS0xLjI0NTUtMS4wMTA5LTIuMDA4LTAuMjgyNzUtMC44MjM1Ni0wLjQyNDQ5LTEuNjIxMS0wLjQyNDQ5LTIuMzkzMSAwLTAuODg0NDEgMC4xOTExLTEuNjQ3MiAwLjU3Mzg4LTIuMjg2NCAwLjMwMDgzLTAuNTEzNDQgMC43MDEwNC0wLjkxODQ2IDEuMjAxOS0xLjIxNTggMC41MDA5LTAuMjk3MzMgMS4wNDIxLTAuNDQ4ODQgMS42MjUtMC40NTg1NCAwLjMxODkxIDAgMC43MzcxMyAwLjA5ODY1IDEuMjU2OCAwLjI5MjUyIDAuNTE4MjUgMC4xOTQ1MyAwLjg1MTAxIDAuMjkzMTggMC45OTY5IDAuMjkzMTggMC4xMDkwOCAwIDAuNDc4NzQtMC4xMTUzNSAxLjEwNTQtMC4zNDUzMSAwLjU5MjYyLTAuMjEzMjYgMS4wOTI4LTAuMzAxNTYgMS41MDI1LTAuMjY2NzggMS4xMTAzIDAuMDg5NiAxLjk0NDQgMC41MjcyOSAyLjQ5OTIgMS4zMTU4LTAuOTkyOTkgMC42MDE2Ni0xLjQ4NDIgMS40NDQ0LTEuNDc0NCAyLjUyNTQgOWUtMyAwLjg0MjA1IDAuMzE0NDMgMS41NDI4IDAuOTE0NzkgMi4wOTkxIDAuMjcyMDggMC4yNTgyMiAwLjU3NTkyIDAuNDU3OCAwLjkxMzk4IDAuNTk5NTQtMC4wNzMzMiAwLjIxMjYxLTAuMTUwNyAwLjQxNjI2LTAuMjMyOTggMC42MTE3NnptLTIuNTQ2NC0xMC4wMmMwIDAuNjYtMC4yNDExMiAxLjI3NjItMC43MjE3MyAxLjg0NjYtMC41OCAwLjY3ODA3LTEuMjgxNSAxLjA2OTktMi4wNDIzIDEuMDA4MS0wLjAwOTctMC4wNzkxOC0wLjAxNTMtMC4xNjI1MS0wLjAxNTMtMC4yNTAwOCAwLTAuNjMzNiAwLjI3NTgyLTEuMzExNyAwLjc2NTY0LTEuODY2MSAwLjI0NDU0LTAuMjgwNzEgMC41NTU1NS0wLjUxNDEyIDAuOTMyNzEtMC43MDAzMSAwLjM3NjM1LTAuMTgzNDEgMC43MzIzMy0wLjI4NDg1IDEuMDY3MS0wLjMwMjIxIDAuMDA5OCAwLjA4ODIzIDAuMDEzODUgMC4xNzY0NyAwLjAxMzg1IDAuMjY0eiIgc3Ryb2tlLXdpZHRoPSIuMDgxNDYiLz48L3N2Zz4%3D

[consolas]: https://docs.microsoft.com/en-us/typography/font-list/consolas

[input-mono]: http://input.djr.com/download/

[pragmatapro]: https://www.fsd.it/shop/fonts/pragmatapro/

[operator]: https://www.typography.com/fonts/operator/

[dank]: https://dank.sh/

[release]: https://github.com/ryanoasis/nerd-fonts/releases/latest "Latest Release (external link) ➶"

[coc]: https://github.com/ryanoasis/nerd-fonts/blob/master/code_of_conduct.md "Contributor Covenant Code of Conduct"

[prs]: http://makeapullrequest.com "Make a Pull Request (external link) ➶"

<!--
Font repos
-->

[f-arimo]: https://github.com/google/fonts/tree/master/apache/arimo

[f-hack]: https://github.com/chrissimpkins/Hack

[f-a-pro]: https://www.marksimonson.com/fonts/view/anonymous-pro

[f-3270]: https://github.com/rbanffy/3270font

[f-cascadia]: https://github.com/microsoft/cascadia-code

[f-cousine]: https://fonts.google.com/specimen/Cousine

[f-source]: https://github.com/adobe-fonts/source-code-pro

[f-liberation]: https://pagure.io/liberation-fonts

[f-lilex]: https://github.com/mishamyrt/Lilex

[f-terminus]: http://terminus-font.sourceforge.net

[f-fira-mono]: https://github.com/mozilla/Fira

[f-fira-code]: https://github.com/tonsky/FiraCode

[f-monoid]: https://github.com/larsenwork/monoid

[f-iosevka]: https://github.com/be5invis/Iosevka

[f-jetbrains-mono]: https://github.com/JetBrains/JetBrainsMono

[f-fant]: https://github.com/belluzj/fantasque-sans

[f-share]: https://fonts.google.com/specimen/Share+Tech+Mono

[f-space]: https://fonts.google.com/specimen/Space+Mono

[f-go-mono]: https://go.googlesource.com/image/+/master/font/gofont/ttfs/

[f-gohu]: http://font.gohu.org/

[f-gohu2]: https://github.com/koemaeda/gohufont-ttf

[f-mononoki]: https://madmalik.github.io/mononoki/

[f-hasklig]: https://github.com/i-tu/Hasklig

[f-ibm-plex]: https://github.com/IBM/plex

[f-victor]: https://github.com/rubjo/victor-mono

[f-daddytimemono]: https://github.com/BourgeoisBear/DaddyTimeMono

[f-agave]: https://github.com/agarick/agave

[f-ia-writer]: https://github.com/iaolo/iA-Fonts

<!--
Patched Font internal links
-->

[p-3270]: patched-fonts/3270

[p-anonymous-pro]: patched-fonts/AnonymousPro

[p-aurulent]: patched-fonts/AurulentSansMono

[p-arimo]: patched-fonts/Arimo

[p-bigblueterm]: patched-fonts/BigBlueTerminal

[p-bitstream]: patched-fonts/BitstreamVeraSansMono

[p-blex]: patched-fonts/IBMPlexMono

[p-cascadia]: patched-fonts/CascadiaCode

[p-cousine]: patched-fonts/Cousine

[p-dejavu]: patched-fonts/DejaVuSansMono

[p-droid]: patched-fonts/DroidSansMono

[p-fantasque]: patched-fonts/FantasqueSansMono

[p-fira-code]: patched-fonts/FiraCode

[p-fira-mono]: patched-fonts/FiraMono

[p-heavy-data]: patched-fonts/HeavyData

[p-hermit]: patched-fonts/Hermit

[p-inconsolata]: patched-fonts/Inconsolata

[p-inconsolata-go]: patched-fonts/InconsolataGo

[p-inconsolata-lgc]: patched-fonts/InconsolataLGC

[p-iosevka]: patched-fonts/Iosevka

[p-jetbrains-mono]: patched-fonts/JetBrainsMono

[p-hack]: patched-fonts/Hack

[p-lekton]: patched-fonts/Lekton

[p-liberation]: patched-fonts/LiberationMono

[p-lilex]: patched-fonts/Lilex

[p-meslo]: patched-fonts/Meslo

[p-monofur]: patched-fonts/Monofur

[p-monoid]: patched-fonts/Monoid

[p-mplus]: patched-fonts/MPlus

[p-noto]: patched-fonts/Noto

[p-opendyslexic]: patched-fonts/OpenDyslexic

[p-overpass]: patched-fonts/Overpass

[p-profont]: patched-fonts/ProFont

[p-proggy-clean]: patched-fonts/ProggyClean

[p-roboto]: patched-fonts/RobotoMono

[p-source-code-pro]: patched-fonts/SourceCodePro

[p-terminus]: patched-fonts/Terminus

[p-tinos]: patched-fonts/Tinos

[p-ubuntu]: patched-fonts/Ubuntu

[p-ubuntu-mono]: patched-fonts/UbuntuMono

[p-share-tech-mono]: patched-fonts/ShareTechMono

[p-space-mono]: patched-fonts/SpaceMono

[p-go-mono]: patched-fonts/Go-Mono

[p-gohu]: patched-fonts/Gohu

[p-mononoki]: patched-fonts/Mononoki

[p-code-nr]: patched-fonts/CodeNewRoman

[p-hasklig]: patched-fonts/Hasklig

[p-victor]: patched-fonts/VictorMono

[p-daddytimemono]: patched-fonts/DaddyTimeMono

[p-agave]: patched-fonts/Agave

[p-im-writing]: patched-fonts/iA-Writer

<!--
Quick Link Images
-->

[ql-1]: images/nerd-fonts-character-logo-md.png "Latest Release (external link) ➶"

[ql-2]: images/nerd-fonts-character-logo-md.png "↓ View Patched Fonts List ↓"

[ql-3]: images/nerd-fonts-patcher-logo-md.png "↓ Font Patcher Details ↓"

[ql-4]: https://raw.githubusercontent.com/wiki/ryanoasis/vim-devicons/screenshots/v1.0.0/branding-logo-sm.png "VimDevIcons Vim Plugin (external link) ➶"

[ql-5]: images/nerd-fonts-character-logo-md.png "Font Package Archive (Zip) Downloads (external link) ➶"

<!--
Patched Font Statuses
-->

[w-top]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/windows-pass-sm.png "↓ Windows Compatibility Status ↓"

[l-top]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/linux-pass-sm.png "↓ Linux Compatibility Status ↓"

[m-top]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/mac-pass-sm.png "↓ macOS (OSX) Compatibility Status ↓"

[w]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/windows-pass-sm.png "Windows status is working ☺"

[l]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/linux-pass-sm.png "Linux status is working ☺"

[m]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/mac-pass-sm.png "macOS (OSX) status is working ☺"

[w2]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/windows-unknown-sm.png "Windows status is Unknown/Un-tested"

[l2]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/linux-unknown-sm.png "Linux status is Unknown/Un-tested"

[m2]: https://github.com/ryanoasis/nerd-fonts/wiki/screenshots/v1.0.x/mac-unknown-sm.png "macOS (OSX) status is Unknown/Un-tested"

[s-iosevka]: https://github.com/ryanoasis/nerd-fonts/issues/83
