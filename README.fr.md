# Bonjour tout le monde :wink:

Il s'agit du référentiel où je fais toutes les expériences liées aux actions/workflows github, aux formulaires de problème, aux modèles. Toute contribution non liée au code au projet est d'abord testée ici.

### Qu'est-ce que j'ai en ce moment ?

-   une action pour vérifier les liens brisés sur un site Web de production et pour créer un problème pour le même.
-   Nouveaux formulaires de problème pour les contributeurs, comme le modèle de problème de rapport de bogue, etc.

# Bonjour

Tester si cette action modifie également la version localisée de README si le README d'origine est modifié.

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

**Polices de nerd**est un projet qui corrige les polices ciblées par les développeurs avec un nombre élevé de glyphes (icônes). Spécifiquement pour ajouter un grand nombre de glyphes supplémentaires à partir de « polices emblématiques » populaires telles que[Police géniale ➶][font-awesome],[Devicons ➶][vorillaz-devicons],[Octicons][octicons], et[autres](#glyph-sets).

L'organigramme de Sankey suivant montre les ensembles de glyphes actuels inclus :

<p align="center">
  <img src="images/sankey-glyphs-combined-diagram.svg" alt="@SankeyMATIC Diagram" />
</p>

<sub><i>Diagramme créé à l'aide de<a href="http://sankeymatic.com/" title="SankeyMATIC (BETA): A Sankey diagram builder for everyone">@SankeyMATIC</a></i></sub>

## Important Notices

-   `master`les chemins des fichiers de branche sont**ne pas**considéré comme stable.[Vérifier les références URI de votre référentiel](#unstable-file-paths)
-   le clonage de ce référentiel est**ne pas**conseillé ([en raison de la taille du dépôt](#option-5-clone-the-repo)) à moins que vous ne soyez[contribuer au développement](#contributing)

## Table des matières

[**TL ; DR**](#tldr)

[**Installation Options**](#font-installation)

-   [**1 - Manuel**](#option-1-download-and-install-manually)
-   [**2 - Télécharger l'archive de publication**](#option-2-release-archive-download)
-   [**3 - Script d'installation**](#option-3-install-script)
-   [**4 - Homebrew Fonts (macOS (OS X))**](#option-4-homebrew-fonts)
-   [**5 - Cloner le dépôt**](#option-5-clone-the-repo)
-   [**6 - Téléchargement Ad Hoc Curl**](#option-6-ad-hoc-curl-download)
-   [**7 - Référentiel utilisateur Arch (AUR) (Arch Linux)**](#option-7-unofficial-arch-user-repository-aur)
-   [**8 - Patchez votre propre police**](#option-8-patch-your-own-font)

[**Caractéristiques**](#features)

-   [**Ensembles de glyphes/icônes**](#glyph-sets)
-   [**Polices corrigées**](#patched-fonts)
-   [**Combinaisons**](#combinations)
-   [**Font Patcher**](#font-patcher)

[**Développeur / Contributeur**](#font-patcher)

-   [**Font Patcher**](#font-patcher)
-   [**Je dois les patcher tous les patcher de polices !**](#gotta-patch-em-all)
-   [**Autres bonnes polices à corriger**](#other-good-fonts-to-patch)
-   [**Contribuant**](#contributing)

[**Project Motivation**](#project-motivation)

**Information additionnelle**

-   [**Chemins de fichiers instables sur le maître**](#unstable-file-paths)
-   [**Journal des modifications**](#changelog)
-   [**Licence**](#license)

## TL ; DR

Nerd Fonts prend les polices de programmation populaires et ajoute un tas de glyphes.
  Il y a aussi[font patcher](#font-patcher)disponible si la police de votre choix n'est pas déjà corrigée.
  Pour plus d'informations de haut niveau, consultez le[wiki][wiki]. Si vous recherchez le plugin Vim voir[Vim DevIcons ➶][vim-devicons].

### Diverses options de téléchargement pour les polices

_Si tu..._

-   `Option 1.`vouloir**vite**saisir un**individual font**télécharger depuis le[`patched-fonts/`annuaire](#patched-fonts)
-   `Option 2.`voulez télécharger un**famille de polices**ensemble de variantes (gras, italique, etc.) voir[télécharger une archive](#option-2-release-archive-download)
-   `Option 3.`vouloir**automate**l'installation ou l'utilisation dans**scripts**voir le[Script d'installation](#option-3-install-script)
-   `Option 4.`sont sur**macOS**et souhaitez utiliser**Homebrew**voir[Polices Homebrew](#option-4-homebrew-fonts)
-   `Option 5.`vouloir**contrôle complet**alors voir[clonage du dépôt](#option-5-clone-the-repo)
-   `Option 6.`voulez utiliser le**`curl`commander**ou utiliser dans**scripts**voir[Téléchargement Ad Hoc Curl](#option-6-ad-hoc-curl-download)
-   `Option 7.`sont sur**Arch Linux**et souhaitez utiliser**et forfaits**voir[Dépôts d'utilisateurs Arch non officiels](#option-7-unofficial-arch-user-repository-aur)
-   `Option 8.`voulez patcher votre propre police voir le[Font Patcher](#option-8-patch-your-own-font)

## Caractéristiques

-   UNE[Script Python FontForge](#font-patcher)pour patcher n'importe quelle police
    -   Comprend une option pour créer**Monospace (pas fixe, largeur fixe)**_ou_**double largeur (non à espacement fixe)**glyphes
    -   Pour plus de détails voir le[**Font Patcher**](#font-patcher)section
-   **`51`**déjà[familles de polices corrigées](#patched-fonts)
-   Plus de**`1,444,400`**combinaisons/variations uniques de polices corrigées[(plus de détails)](#combinations)
-   Plus de**`2,824`**glyphes/icônes combinés[(plus de détails)](#combinations)
    -   Les ensembles de glyphes actuels incluent :[Powerline avec symboles supplémentaires][ryanoasis-powerline-extra-symbols],[Police géniale][font-awesome],[Icônes de conception matérielle][font-material-design-icons],[Temps][font-weather],[Devicons][vorillaz-devicons],[Octicons][octicons],[Font Logos][font-linux](Auparavant[Font Linux][font-linux]),[Pomicons][gabrielelana-pomicons]
-   **Monospace (pas fixe, largeur fixe)**_ou_**double largeur (non à espacement fixe)**version glyphes de chaque police
    -   Cela fait référence aux glyphes de la police Nerd eux-mêmes, pas nécessairement à la police dans son ensemble
-   Un développeur/contributeur fourni[script bash](#gotta-patch-em-all)pour re-patcher toutes les polices

## Ensembles de glyphes

:mag: :mag: Vous pouvez désormais rechercher facilement des glyphes sur[NerdFonts.com][Cheat Sheet]via le[Aidemémoire][]

Voir[Wiki : Ensembles de glyphes et points de code pour plus de détails][wiki-glyph-sets-codepoints]

### Noms des icônes dans le shell

Voir[Wiki : Noms des icônes dans le shell][wiki-icon-names-in-shell]

## Polices corrigées

| Nom de la police                                          | Nom de la police et référentiel         | \*RFN | Taille EM | Statut           |
| :-------------------------------------------------------- | :-------------------------------------- | :---- | :-------- | :--------------- |
| [3270 Nerd Font][p-3270]                                  | [3270][f-3270]                          | NON   | 1000      | ![w]![m2]![l]    |
| [Agave][p-agave]                                          | [Agave][f-agave]                        | NON   | 2048      | ![w]![m2]![l]    |
| [Anonymice Nerd Font][p-anonymous-pro]                    | [Anonyme Pro][f-a-pro]                  | NON   | 2048      | ![w]![m2]![l]    |
| [Arimo][p-arimo]                                          | [Arimo][f-arimo]                        | NON   | 2048      | ![w]![m2]![l]    |
| [Aurulent Sans Mono Nerd Font][p-aurulent]                |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [BigBlueTerminal][p-bigblueterm]                          |                                         | NON   | 1200      | ![w]![m2]![l]    |
| [Bitstream Vera Sans Mono Nerd Font][p-bitstream]         |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Blex\*][p-blex]                                          | [IBM Plex Mono][f-ibm-plex]             | OUI   | 1000      | ![w]![m2]![l]    |
| [Police Caskaydia Cove Nerd\*][p-cascadia]                | [Cascadia Code][f-cascadia]             | OUI   | 2048      | ![w]![m2]![l]    |
| [Code New Roman Nerd Police][p-code-nr]                   |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Cousine Nerd Font][p-cousine]                            | [Cousine][f-cousine]                    | NON   | 1000      | ![w]![m2]![l]    |
| [PapaTimeMono][p-daddytimemono]                           | [PapaTimeMono][f-daddytimemono]         | NON   | 1024      | ![w]![m2]![l]    |
| [DejaVu Sans Mono Nerd Font][p-dejavu]                    |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Droid Sans Mono Nerd Font][p-droid]                      |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Fantasque Sans Nerd Font][p-fantasque]                   | [Fantasque Sans][f-fant]                | NON   | 2048      | ![w]![m2]![l]    |
| [Fira Code Nerd Font][p-fira-code]                        | [Fira Code][f-fira-code]                | NON   | 1000      | ![w]![m2]![l]    |
| [Fira Mono Nerd Font][p-fira-mono]                        | [équitable][f-fira-mono]                | NON   | 1000      | ![w]![m2]![l]    |
| [Valeur de la personne rd téléphone t][p-go-mono]         | [Personne][f-go-mono]                   | NON   | 1000      | ![w]![m2]![l]    |
| [Gohu Nerd Font][p-gohu]                                  | [Gohu TTF][f-gohu2],[Gohu][f-gohu]      | NON   | 1000      | ![w]![m2]![l]    |
| [Hack Nerd Font][p-hack]                                  | [Pirater][f-hack]                       | NON   | 2048      | ![w]![m2]![l]    |
| [Hasklug Nerd Font\*][p-hasklig]                          | [Précipité][f-hasklig]                  | OUI   | 1000      | ![w]![m2]![l]    |
| [Cheveux vy valeur personne rd téléphone t][p-heavy-data] |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Hurmit Nerd Font][p-hermit]                              |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [J'écris\*][p-im-writing]                                 | [iA-Writer][f-ia-writer]                | OUI   | 1000      | ![w]![m2]![l]    |
| [Inconsolata Nerd Font][p-inconsolata]                    |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Police Inconsolata Go Nerd][p-inconsolata-go]            |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Inconsolata LGC Nerd Font][p-inconsolata-lgc]            |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Iosevka Nerd Font][p-iosevka]                            | [Iosevka][f-iosevka]                    | NON   | 1000      | [#83][s-iosevka] |
| [JetBrains Mono][p-jetbrains-mono]                        | [JetBrains Mono][f-jetbrains-mono]      | NON   | 1000      | ![w]![m2]![l]    |
| [Lekton Nerd Font][p-lekton]                              |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Literation Mono Nerd Font\*][p-liberation]               | [Libération][f-liberation]              | OUI   | 2048      | ![w]![m2]![l]    |
| [Lilex Nerd Font][p-lilex]                                | [Lilex][f-lilex]                        | NON   | 2000      | ![w2]![m2]![l]   |
| [Meslo Nerd Font][p-meslo]                                |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Monofur Nerd Font][p-monofur]                            |                                         | NON   | 2400      | ![w]![m2]![l]    |
| [Police Monoid Nerd][p-monoid]                            |                                         | NON   | 1536      | ![w]![m2]![l]    |
| [Mononoki Nerd Font][p-mononoki]                          | [Arbre des choses][f-mononoki]          | NON   | 1024      | ![w]![m2]![l]    |
| [M+ (MPlus) Nerd Font][p-mplus]                           |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Connu][p-noto]                                           |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [OuvertDyslexique][p-opendyslexic]                        |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Dépasser][p-overpass]                                    |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [ProFont (Windows tweaked) Nerd Font][p-profont]          |                                         | NON   | 1200      | ![w]![m2]![l]    |
| [ProFont (x11) Nerd Font][p-profont]                      |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Police ProggyClean Nerd][p-proggy-clean]                 |                                         | NON   | 2048      | Imparfait        |
| [Robot et personne][p-roboto]                             |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Sauce Code Nerd Font][p-source-code-pro]                 | [Source][f-source]                      | OUI   | 1000      | ![w]![m2]![l]    |
| [Police Shure tech thing nerd \*][p-share-tech-mono]      | [Personne à la mode à la main][f-share] | OUI   | 1000      | ![w]![m2]![l]    |
| [Space Mono Nerd Font][p-space-mono]                      | [Espace Mono][f-space]                  | NON   | 1000      | ![w]![m2]![l]    |
| [Terminess Nerd Font\*][p-terminus]                       | [Terminus Font][f-terminus]             | OUI   | 1000      | ![w]![m2]![l]    |
| [Tinos][p-tinos]                                          |                                         | NON   | 2048      | ![w]![m2]![l]    |
| [Ubuntu Nerd Font][p-ubuntu]                              |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Ubuntu Mono Nerd Font][p-ubuntu-mono]                    |                                         | NON   | 1000      | ![w]![m2]![l]    |
| [Victor Mono][p-victor]                                   | [Victor Mono][f-victor]                 | NON   | 1000      | ![w]![m2]![l]    |

<sub>_\*RFN = Nom de police réservé_</sub>

## Combinaisons

-   Plus de**`1,485,000`**variations/combinaisons uniques (Power Set) de polices corrigées :
    -   **`50`**polices de caractères corrigées
    -   **`719`**familles de polices corrigées
    -   **`2,876`**variantes/combinaisons « complètes »
    -   **`'1,485,410'`**_possible_variations/combinations
    -   -   **`1,488,286`**total des combinaisons calculées (2 876 + 1 428 110)
-   Les combinaisons pour chaque police sont n'importe quelle combinaison de[Variations](#variations)

### Variations

-   aucun indicateur donné (par défaut uniquement**Seti-UI + Custom**et**[Devicons][vorillaz-devicons]**)
-   **double_(variable/proportional)_**ou**Célibataire_(fixe/monospace)_**glyphes de largeur
-   [Police géniale][font-awesome]
-   [Extension de police géniale][font-awesome-extension]
-   [Icônes de conception matérielle][font-material-design-icons]
-   [Temps][font-weather]
-   [Octicons GitHub][octicons]
-   [Font Logos][font-linux](Auparavant[Font Linux][font-linux])
-   [Symboles supplémentaires Powerline][ryanoasis-powerline-extra-symbols]
-   [Symboles de puissance CEI][website-iecpower]
-   [Pomicons][gabrielelana-pomicons]
-   Compatibilité Windows

## Font Installation

### `Option 1: Download and Install Manually`

> Meilleure option pour**vite**obtenir un spécifique**individual font**.

Télécharger le spécifique[police corrigée](#patched-fonts)de votre choix

### `Option 2: Release Archive Download`

> Meilleure option si vous voulez un**archiver**ou compléter**famille de polices**de variations (gras, italique, etc.).

Les polices sont disponibles en téléchargement sous forme de packages dans le[dernière version](https://github.com/ryanoasis/nerd-fonts/releases/latest)

### `Option 3: Install Script`

> Meilleure option si vous voulez**automate**l'installation ou l'utilisation dans**scripts**.

_Note_:**Nécessite un clonage**le repo dès maintenant

#### Toutes les polices :

-   Installe toutes les polices corrigées (_Avertissement : il s'agit d'un grand nombre de polices qui s'ajoutent à une grande taille_)

```sh
./install.sh
```

ou, dans Powershell (Windows uniquement) :

```pwsh
./install.ps1
```

#### Single font:

-   Installe une seule police de votre choix

```sh
./install.sh <FontName>
./install.sh Hack
./install.sh HeavyData
```

ou, dans Powershell (Windows uniquement) :

```pwsh
./install.ps1 <FontName>
./install.ps1 Hack
./install.ps1 HeavyData
```

### `Option 4: Homebrew Fonts`

> Meilleure option si activé**macOS**et souhaitez utiliser**Homebrew**.

Toutes les polices sont disponibles via[Polices de Cask Homebrew](https://github.com/Homebrew/homebrew-cask-fonts)on macOS (OS X)

```sh
brew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
```

### `Option 5: Clone the Repo`

> Meilleure option pour**controle total**,**tous**ou**certains**des polices, ou**contribuant**au développement.

Un clone complet de ce référentiel est**ne pas**requis ni efficace (principalement en raison de la taille du référentiel) si vous n'êtes simplement intéressé que par un ensemble limité de polices.

Si vous souhaitez cloner l'intégralité du référentiel, assurez-vous de_peu profond_cloner:

```sh
git clone --depth 1
```

Si vous souhaitez cloner un sous-répertoire, utilisez`git sparse-checkout`. L'exemple suivant nécessite`Git v2.26`:

```sh
git clone --filter=blob:none --sparse git@github.com:ryanoasis/nerd-fonts
cd nerd-fonts
git sparse-checkout add patched-fonts/JetBrainsMono
```

### `Option 6: Ad Hoc Curl Download`

> Option si vous souhaitez utiliser le**`curl`commander**ou pour une utilisation dans**scripts**.

#### Linux

```sh
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

_Note:_chemins alternatifs obsolètes :`~/.fonts`

#### Mac OS X)

```sh
cd ~/Library/Fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

### `Option 7: Unofficial Arch User Repository (AUR)`

> Option pour**Arch Linux**et vouloir utiliser**et forfaits**.

Les polices suivantes sont disponibles via[et forfaits](https://aur.archlinux.org/)sur Arch Linux :

-   [Nerd Fonts Complete (double largeur)](https://aur.archlinux.org/packages/nerd-fonts-complete/)
-   [Nerd Fonts Complete (simple largeur) (obsolète)](https://aur.archlinux.org/packages/nerd-fonts-complete-mono-glyphs/)
-   [Nerd Fonts DejaVu Complete](https://aur.archlinux.org/packages/nerd-fonts-dejavu-complete/)
-   [Nerd Fonts Source Code Pro Complete](https://aur.archlinux.org/packages/nerd-fonts-source-code-pro/)
-   [Nerd Fonts Git (obsolète)](https://aur.archlinux.org/packages/nerd-fonts-git/)
-   [Nerd Fonts Fira Code](https://aur.archlinux.org/packages/nerd-fonts-fira-code/)
-   [Nerd Fonts Terminus](https://aur.archlinux.org/packages/nerd-fonts-terminus/)
-   [Nerd Fonts Liberation Mono](https://aur.archlinux.org/packages/nerd-fonts-liberation-mono/)
-   [Racine rd téléphone ts personne](https://aur.archlinux.org/packages/nerd-fonts-go-mono/)
-   [Nerd Fonts Anonymous Pro](https://aur.archlinux.org/packages/nerd-fonts-anonymous-pro/)
-   [Root rd phone ts door](https://aur.archlinux.org/packages/nerd-fonts-noto/)
-   [Nerd Fonts Inconsolata](https://aur.archlinux.org/packages/nerd-fonts-inconsolata/)

### `Option 8: Patch Your Own Font`

> L'option pour**patcher**ton**own font**ou entièrement**personnalisation**la police corrigée.

Utilisez le script de ligne de commande Python fourni pour générer une police corrigée à partir de votre propre police afin d'obtenir les nouveaux glyphes supplémentaires

Voir:[Font Patcher](#font-patcher)pour l'utilisation

-   utilisez cette option si vous**ne pas**voulez utiliser l'un des[polices fournies](#patched-fonts)
-   vous devrez toujours copier la police générée dans le bon répertoire de polices sur votre système

<h2 align="center" id="font-patcher">
	<img src="images/nerd-fonts-patcher-logo.png" alt="Nerd Fonts Patcher">
</h2>

Patcher la police de votre choix pour une utilisation avec le[Vim DevIcons ➶][vim-devicons]:

-   nécessite : Python 2 (ou Python 3),`python-fontforge`package (version`20141231`ou plus tard, voir
    les[instructions d'installation](http://designwithfontforge.com/en-US/Installing_Fontforge.html))

-   méthode d'installation alternative sur OSX :`brew install fontforge`

-   méthode alternative sous Linux : en utilisant le[AppImage](https://github.com/fontforge/fontforge/releases)

-   méthode alternative utilisant Docker :[Docker Hub](https://hub.docker.com/r/nerdfonts/patcher)

-   Usage:

        ./font-patcher PATH_TO_FONT

-   Utilisation alternative : exécutez le patcher avec le binaire FontForge à l'aide du drapeau de script :

        ./fontforge -script font-patcher PATH_TO_FONT

-   Correction des polices à l'aide de l'AppImage :

    _Note_:`chmod u+x`l'AppImage après le téléchargement. Tous les chemins fournis doivent être**absolu**et un chemin de sortie explicite est requis ! Si tout se trouve dans le même répertoire, vous pouvez utiliser le`$PWD`sténographie.

        ./FontForge.AppImage -script $PWD/font-patcher $PWD/BaseFont.ttf -out /tmp

-   Patcher des polices avec Docker :

        docker run -v /path/to/fonts:/in -v /path/for/output:/out nerdfonts/patcher [OPTIONS]

Toutes les options:

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

#### Exemples

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

## Je dois les patcher tous les patcher de polices !

-   à l'usage des contributeurs ou des développeurs

-   re-patchs**tous** fonts in the unpatched directory:

        ./gotta-patch-em-all-font-patcher\!.sh

-   peut éventuellement se limiter à un modèle de nom de police spécifique :

        ./gotta-patch-em-all-font-patcher\!.sh Hermit

## Contribuant

Voir[contributing.md](contributing.md)

## Chemins de fichiers instables

:warning: Attention : les chemins de fichiers peuvent changer en fonction des versions (en particulier**Majeur**version bumps)

Référencer le**Libération**succursale et_ne pas_les~~Maître~~branche car les chemins sont sujets à changement pour chaque version

-   Par exemple:
    -   :white_check_mark : Utilisez :<code>https\\://github.com/ryanoasis/nerd-fonts/blob/<b>0.9.0</b>/patched-fonts/Hermit/Medium/complete/Hurmit%20Medium%20Nerd%20Font%20Complete.otf</code>
    -   :x: Au lieu de :<code>https\\://github.com/ryanoasis/nerd-fonts/blob/<del>Maître</del>/patched-fonts/Hermit/Medium/complete/Hurmit%20Medium%20Nerd%20Font%20Complete.otf</code>

## Autres bonnes polices à corriger

Une liste de bonnes polices supplémentaires à corriger qui ne peuvent pas être fournies ou partagées en raison de leur licence :

-   [Entrée Mono][input-mono](license restriction)
    -   Peut-être à venir avec un hébergement externe :)
-   [Choses pour][pragmatapro](pas libre)
-   [Consoles][consolas](propriétaire)
-   [Opéra et r personne][operator](pas libre)
-   [Merci à Mono][dank](pas libre)

## Project Motivation

Voir[Wiki : Objectif du projet][wiki-project-purpose]

## Journal des modifications

Voir[changelog.md](changelog.md)

## Licence

[AVEC](LICENSE)© Ryan L McIntyre

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
