# مرحبًا بالعالم: غمزة:

هذا هو المستودع حيث أقوم بجميع التجارب المتعلقة بإجراءات / سير عمل github ، ونماذج الإصدار ، والقوالب ، يتم اختبار أي مساهمة غير مرتبطة بالتعليمات البرمجية في المشروع أولاً هنا.

### ماذا لدي الآن؟

-   إجراء للتحقق من عدم وجود ارتباطات معطلة على موقع ويب خاص بالإنتاج ولإنشاء مشكلة لها.
-   نماذج المشكلات الجديدة للمساهمين مثل قالب مشكلة تقرير الخطأ والأشياء.

# أهلا

اختبار ما إذا كان هذا الإجراء يغير أيضًا الإصدار المترجم من README إذا تم تغيير README الأصلي.

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

**نيرد الخطوط**هو مشروع يقوم بتصحيح الخطوط المستهدفة للمطور بعدد كبير من الحروف الرسومية (الرموز). على وجه التحديد لإضافة عدد كبير من الحروف الرسومية الإضافية من "الخطوط الأيقونية" الشائعة مثل[رائع الخط ➶][font-awesome],[Devicons ➶][vorillaz-devicons],[Octicons ➶][octicons]، و[الآخرين](#glyph-sets).

يوضح مخطط تدفق Sankey التالي مجموعات الحروف الرسومية الحالية المضمنة:

<p align="center">
  <img src="images/sankey-glyphs-combined-diagram.svg" alt="@SankeyMATIC Diagram" />
</p>

<sub><i>تم إنشاء الرسم باستخدام<a href="http://sankeymatic.com/" title="SankeyMATIC (BETA): A Sankey diagram builder for everyone">تضمين التغريدة</a></i></sub>

## ملاحظات هامة

-   `master`مسارات الملفات الفرعية هي**ليس**تعتبر مستقرة.[تحقق من مراجع URI الخاصة بالمستودع](#unstable-file-paths)
-   استنساخ هذا المستودع هو**ليس**موصى به ([بسبب حجم الريبو](#option-5-clone-the-repo)) إلا إذا كنت ستفعل ذلك[المساهمة في التنمية](#contributing)

## جدول المحتويات

[**TL ؛ DR**](#tldr)

[**خيارات التثبيت**](#font-installation)

-   [**1 - يدوي**](#option-1-download-and-install-manually)
-   [**2 - إصدار تنزيل أرشيف**](#option-2-release-archive-download)
-   [**3 - تثبيت البرنامج النصي**](#option-3-install-script)
-   [**4 - Homebrew Fonts (macOS (OS X))**](#option-4-homebrew-fonts)
-   [**5 - استنساخ الريبو**](#option-5-clone-the-repo)
-   [**6 - تنزيل Ad Hoc Curl**](#option-6-ad-hoc-curl-download)
-   [**7 - مستودع مستخدم آرتش (AUR) (آرتش لينوكس)**](#option-7-unofficial-arch-user-repository-aur)
-   [**8 - تصحيح الخط الخاص بك**](#option-8-patch-your-own-font)

[**سمات**](#features)

-   [**مجموعات الحروف الرسومية / الأيقونة**](#glyph-sets)
-   [**خطوط مصححة**](#patched-fonts)
-   [**مجموعات**](#combinations)
-   [**الخط المرقع**](#font-patcher)

[**المطور / المساهم**](#font-patcher)

-   [**الخط المرقع**](#font-patcher)
-   [**فلدي تصحيح جميع الخطوط باتشر!**](#gotta-patch-em-all)
-   [**خطوط أخرى جيدة للتصحيح**](#other-good-fonts-to-patch)
-   [**المساهمة**](#contributing)

[**دافع المشروع**](#project-motivation)

**معلومات اضافية**

-   [**مسارات الملفات غير المستقرة على المستوى الرئيسي**](#unstable-file-paths)
-   [**التغيير**](#changelog)
-   [**رخصة**](#license)

## TL ؛ DR

تأخذ Nerd Fonts خطوط البرمجة الشائعة وتضيف مجموعة من الحروف الرسومية.
  هنالك أيضا[بتشر الخط](#font-patcher)متاح إذا لم يكن الخط الذي تريده مصححًا بالفعل.
  لمزيد من المعلومات عالية المستوى راجع[ويكي][wiki]. إذا كنت تبحث عن البرنامج المساعد Vim انظر[فيم DevIcons ➶][vim-devicons].

### خيارات تنزيل متنوعة للخطوط

_اذا أنت..._

-   `Option 1.`اريد ان**بسرعة**جرب أن**خط فردي**تنزيل من[`patched-fonts/`الدليل](#patched-fonts)
-   `Option 2.`تريد تنزيل ملف**خط العائلة**حزمة من الاختلافات (غامق ، مائل ، وما إلى ذلك) انظر[تنزيل أرشيف](#option-2-release-archive-download)
-   `Option 3.`اريد ان**أتمتة**التثبيت أو الاستخدام في**نصوص**انظر[تثبيت البرنامج النصي](#option-3-install-script)
-   `Option 4.`هي على**macOS**وتريد استخدامها**البيرة**ارى[الخطوط الرئيسية](#option-4-homebrew-fonts)
-   `Option 5.`يريد**السيطره الكامله**ثم انظر[استنساخ الريبو](#option-5-clone-the-repo)
-   `Option 6.`تريد استخدام**`curl`أمر**أو استخدامها في**نصوص**ارى[تنزيل Ad Hoc Curl](#option-6-ad-hoc-curl-download)
-   `Option 7.`هي على**قوس لينكس**وتريد استخدامها**والعبوات**ارى[مستودعات مستخدم Arch غير الرسمية](#option-7-unofficial-arch-user-repository-aur)
-   `Option 8.`تريد تصحيح الخط الخاص بك انظر[الخط المرقع](#option-8-patch-your-own-font)

## سمات

-   أ[برنامج FontForge Python النصي](#font-patcher)لتصحيح أي خط
    -   يتضمن خيارا للإنشاء**أحادي المسافة (خطوة ثابتة ، عرض ثابت)**_أو_**عرض مزدوج (غير أحادي المسافة)**الحروف الرسومية
    -   لمزيد من التفاصيل انظر[**الخط المرقع**](#font-patcher)الجزء
-   **`51`**بالفعل[عائلات الخطوط المصححة](#patched-fonts)
-   على**`1,444,400`**مجموعات / أشكال فريدة من الخطوط المصححة[(المزيد من التفاصيل)](#combinations)
-   على**`2,824`**الحروف الرسومية / الرموز مجتمعة[(المزيد من التفاصيل)](#combinations)
    -   تتضمن مجموعات الحروف الرسومية الحالية:[باورلاين مع رموز اضافية][ryanoasis-powerline-extra-symbols],[رائع الخط][font-awesome],[أيقونات تصميم المواد][font-material-design-icons],[طقس][font-weather],[Devicons][vorillaz-devicons],[أوكتيكونس][octicons],[شعارات الخطوط][font-linux](سابقا[لينكس الخط][font-linux]),[بوميونس][gabrielelana-pomicons]
-   **أحادي المسافة (خطوة ثابتة ، عرض ثابت)**_أو_**عرض مزدوج (غير أحادي المسافة)**نسخة الحروف الرسومية لكل خط
    -   يشير هذا إلى الحروف الرسومية Nerd Font نفسها وليس بالضرورة إلى الخط ككل
-   مطور / مساهم مقدم[نص باش](#gotta-patch-em-all)لإعادة تصحيح جميع الخطوط

## مجموعات الحروف الرسومية

: mag:: mag: يمكنك الآن البحث عن الحروف الرسومية بسهولة على[نردفنتس.كوم][Cheat Sheet]عبر[ورقة الغش][]

ارى[Wiki: مجموعات الحروف الرسومية والنقاط البرمجية لمزيد من التفاصيل][wiki-glyph-sets-codepoints]

### أسماء الأيقونات في shell

ارى[الويكي: أسماء الأيقونات في القشرة][wiki-icon-names-in-shell]

## خطوط مصححة

| اسم الخط                                                             | اسم الخط والمستودع                 | \*RFN | حجم EM | حالة             |
| :------------------------------------------------------------------- | :--------------------------------- | :---- | :----- | :--------------- |
| [3270 Nerd Font][p-3270]                                             | [٣٢٧٠][f-3270]                     | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [الأغاف][p-agave]                                                    | [الأغاف][f-agave]                  | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [مجهول الخط نيرد][p-anonymous-pro]                                   | [برو مجهول][f-a-pro]               | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [أريمو][p-arimo]                                                     | [أريمو][f-arimo]                   | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [Aurulent Sans Mono Nerd Font][p-aurulent]                           |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [BigBlueTerminal][p-bigblueterm]                                     |                                    | لا    | ١٢٠٠   | ![w]![m2]![l]    |
| [Bitstream Vera Sans Mono Nerd Font][p-bitstream]                    |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [بلكس \*][p-blex]                                                    | [IBM Plex Mono][f-ibm-plex]        | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [Caskaydia Cove Nerd Font \*][p-cascadia]                            | [كود كاسكاديا][f-cascadia]         | نعم   | ٢٠٤٨   | ![w]![m2]![l]    |
| [كود New Roman Nerd Font][p-code-nr]                                 |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [ابن عم الطالب الذي يذاكر كثيرا الخط][p-cousine]                     | [ابنة عم][f-cousine]               | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [DaddyTimeMono][p-daddytimemono]                                     | [DaddyTimeMono][f-daddytimemono]   | لا    | ١٠٢٤   | ![w]![m2]![l]    |
| [قيمة شخص Dejav rd phone t][p-dejavu]                                |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [Droid Sans Mono Nerd الخط][p-droid]                                 |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [غريب الاطوار بلا الخط الطالب الذي يذاكر كثيرا][p-fantasque]         | [رائع بدون][f-fant]                | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [فيرا كود نيرد الخط][p-fira-code]                                    | [كود فيرا][f-fira-code]            | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [شخص فيلا قيمة الهاتف rd][p-fira-mono]                               | [عدل][f-fira-mono]                 | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [قيمة الشخص هاتف rd][p-go-mono]                                      | [شخص][f-go-mono]                   | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [جوهو نيرد الخط][p-gohu]                                             | [Gohu TTF][f-gohu2],[جوهو][f-gohu] | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [هاك نيرد الخط][p-hack]                                              | [هاك][f-hack]                      | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [خط هاسكلوج نيرد \*][p-hasklig]                                      | [متسرع][f-hasklig]                 | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [البيانات الثقيلة أحادية الخط الطالب الذي يذاكر كثيرا][p-heavy-data] |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [هورميت نيرد الخط][p-hermit]                                         |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [انا اكتب\*][p-im-writing]                                           | [كاتب iA][f-ia-writer]             | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [خط Inconsolata الطالب الذي يذاكر كثيرا][p-inconsolata]              |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [Inconsolata Go Nerd الخط][p-inconsolata-go]                         |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [Inconsolata LGC Nerd الخط][p-inconsolata-lgc]                       |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [يوسيفكا نيرد الخط][p-iosevka]                                       | [يوسيفكا][f-iosevka]               | لا    | ١٠٠٠   | [#ضع][s-iosevka] |
| [JetBrains مونو][p-jetbrains-mono]                                   | [JetBrains مونو][f-jetbrains-mono] | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [ليكتون نيرد الخط][p-lekton]                                         |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [خط Iterachion Monone rd \*][p-liberation]                           | [تحرير][f-liberation]              | نعم   | ٢٠٤٨   | ![w]![m2]![l]    |
| [Lilex Nerd الخط][p-lilex]                                           | [ليلكس][f-lilex]                   | لا    | ٢٠٠٠   | ![w2]![m2]![l]   |
| [ميسلو نيرد الخط][p-meslo]                                           |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [Monofur الطالب الذي يذاكر كثيرا الخط][p-monofur]                    |                                    | لا    | ٢٤٠٠   | ![w]![m2]![l]    |
| [أحادي الخط الطالب الذي يذاكر كثيرا][p-monoid]                       |                                    | لا    | ١٥٣٦   | ![w]![m2]![l]    |
| [قيمة الشجرة rd phone t][p-mononoki]                                 | [شجرة الأشياء][f-mononoki]         | لا    | ١٠٢٤   | ![w]![m2]![l]    |
| [M + (MPlus) Nerd Font][p-mplus]                                     |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [معروف][p-noto]                                                      |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [مفتوح][p-opendyslexic]                                              |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [ممر علوي][p-overpass]                                               |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [ProFont (Windows tweaked) Nerd Font][p-profont]                     |                                    | لا    | ١٢٠٠   | ![w]![m2]![l]    |
| [ProFont (x11) Nerd Font][p-profont]                                 |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [ProggyClean Nerd الخط][p-proggy-clean]                              |                                    | لا    | ٢٠٤٨   | غير تام          |
| [روبو وشخص][p-roboto]                                                |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [كود صوص نيرد فونت][p-source-code-pro]                               | [مصدر][f-source]                   | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [Shure te ch thing ne rd font \*][p-share-tech-mono]                 | [من المألوف ch اليد ch][f-share]   | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [مساحة أحادية الخط الطالب الذي يذاكر كثيرا][p-space-mono]            | [الفضاء الأحادي][f-space]          | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [خط Terminess Nerd \*][p-terminus]                                   | [خط النهاية][f-terminus]           | نعم   | ١٠٠٠   | ![w]![m2]![l]    |
| [تينوس][p-tinos]                                                     |                                    | لا    | ٢٠٤٨   | ![w]![m2]![l]    |
| [Ubuntu Nerd Font][p-ubuntu]                                         |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [شخص Ubunz قيمة الهاتف rd t][p-ubuntu-mono]                          |                                    | لا    | ١٠٠٠   | ![w]![m2]![l]    |
| [فيكتور مونو][p-victor]                                              | [فيكتور مونو][f-victor]            | لا    | ١٠٠٠   | ![w]![m2]![l]    |

<sub>_\* RFN = اسم الخط المحجوز_</sub>

## مجموعات

-   على**`1,485,000`**الاختلافات / التركيبات الفريدة (مجموعة الطاقة) للخطوط المصححة:
    -   **`50`**محارف الخط مصححة
    -   **`719`**عائلات الخطوط المصححة
    -   **`2,876`**الاختلافات / المجموعات "كاملة"
    -   **`'1,485,410'`**_المستطاع_الاختلافات / المجموعات
    -   -   **`1,488,286`**إجمالي المجموعات المحسوبة (2،876 + 1،428،110)
-   مجموعات كل خط هي أي مجموعة من[الاختلافات](#variations)

### الاختلافات

-   لم يتم تقديم أعلام (الإعدادات الافتراضية على**Seti-OY + Bush**و**[Devicons][vorillaz-devicons]**)
-   **مزدوج_(متغير / متناسب)_**أو**غير مرتبطة_(ثابت / أحادي المسافة)_**عرض صور رمزية
-   [رائع الخط][font-awesome]
-   [ملحق Font Awesome][font-awesome-extension]
-   [أيقونات تصميم المواد][font-material-design-icons]
-   [طقس][font-weather]
-   [جيثب Octicons][octicons]
-   [شعارات الخطوط][font-linux](سابقا[لينكس الخط][font-linux])
-   [رموز باورلاين الإضافية][ryanoasis-powerline-extra-symbols]
-   [رموز الطاقة IEC][website-iecpower]
-   [بوميونس][gabrielelana-pomicons]
-   التوافق مع الويندوز

## تثبيت الخط

### `Option 1: Download and Install Manually`

> أفضل خيار لـ**بسرعة**الحصول على محدد**خط فردي**.

قم بتنزيل ملف[خط مصحح](#patched-fonts)من اختيارك

### `Option 2: Release Archive Download`

> أفضل خيار إذا كنت تريد**أرشيف**أو كاملة**خط العائلة**من الاختلافات (غامق ، مائل ، إلخ).

الخطوط متاحة للتنزيل كحزم في ملف[أحدث إصدار](https://github.com/ryanoasis/nerd-fonts/releases/latest)

### `Option 3: Install Script`

> أفضل خيار إذا كنت تريد**أتمتة**التثبيت أو للاستخدام في**نصوص**.

_ملحوظة_:**يتطلب الاستنساخ**الريبو اعتبارًا من الآن

#### كافة الخطوط:

-   يثبت كل الخطوط المصححة (_تحذير: هذا كثير من الخطوط تضيف ما يصل إلى حجم كبير_)

```sh
./install.sh
```

أو في Powershell (نظام التشغيل Windows فقط):

```pwsh
./install.ps1
```

#### خط واحد:

-   تثبيت خط واحد من اختيارك

```sh
./install.sh <FontName>
./install.sh Hack
./install.sh HeavyData
```

أو في Powershell (نظام التشغيل Windows فقط):

```pwsh
./install.ps1 <FontName>
./install.ps1 Hack
./install.ps1 HeavyData
```

### `Option 4: Homebrew Fonts`

> أفضل خيار إذا كان**macOS**وتريد استخدامها**البيرة**.

جميع الخطوط متوفرة عبر[Homebrew Cask الخطوط](https://github.com/Homebrew/homebrew-cask-fonts)على نظام macOS (OS X)

```sh
brew tap homebrew/cask-fonts
brew install --cask font-hack-nerd-font
```

### `Option 5: Clone the Repo`

> أفضل خيار لـ**سيطرة كاملة**,**الكل**أو**بعض**من الخطوط ، أو**المساهمة**في التنمية.

نسخة كاملة من هذا المستودع هو**ليس**مطلوب وغير فعال (غالبًا بسبب حجم المستودع) إذا كنت مهتمًا فقط بمجموعة محدودة من الخطوط.

إذا كنت ترغب في استنساخ الريبو بالكامل ، فتأكد من ذلك_بارز_استنساخ:

```sh
git clone --depth 1
```

إذا كنت تريد استنساخ دليل فرعي ، فاستخدم`git sparse-checkout`. المثال التالي يتطلب`Git v2.26`:

```sh
git clone --filter=blob:none --sparse git@github.com:ryanoasis/nerd-fonts
cd nerd-fonts
git sparse-checkout add patched-fonts/JetBrainsMono
```

### `Option 6: Ad Hoc Curl Download`

> الخيار إذا كنت تريد استخدام**`curl`أمر**أو للاستخدام في**نصوص**.

#### لينكس

```sh
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

_ملحوظة:_مسارات بديلة مهملة:`~/.fonts`

#### macOS (OS X)

```sh
cd ~/Library/Fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
```

### `Option 7: Unofficial Arch User Repository (AUR)`

> خيار**قوس لينكس**وترغب في استخدامها**والعبوات**.

الخطوط التالية متوفرة عبر[والعبوات](https://aur.archlinux.org/)على Arch Linux:

-   [اكتمل Nerd Fonts (مزدوج العرض)](https://aur.archlinux.org/packages/nerd-fonts-complete/)
-   [اكتمل Nerd Fonts (عرض واحد) (قديم)](https://aur.archlinux.org/packages/nerd-fonts-complete-mono-glyphs/)
-   [الطالب الذي يذاكر كثيرا الخطوط DejaVu كاملة](https://aur.archlinux.org/packages/nerd-fonts-dejavu-complete/)
-   [Nerd Fonts Source Code Pro كاملة](https://aur.archlinux.org/packages/nerd-fonts-source-code-pro/)
-   [Nerd Fonts Git (قديم)](https://aur.archlinux.org/packages/nerd-fonts-git/)
-   [نيرد الخطوط فيرا كود](https://aur.archlinux.org/packages/nerd-fonts-fira-code/)
-   [Nerd Fonts Terminus](https://aur.archlinux.org/packages/nerd-fonts-terminus/)
-   [الطالب الذي يذاكر كثيرا الخطوط التحرير مونو](https://aur.archlinux.org/packages/nerd-fonts-liberation-mono/)
-   [جذر الهاتف rd ts شخص](https://aur.archlinux.org/packages/nerd-fonts-go-mono/)
-   [الطالب الذي يذاكر كثيرا الخطوط مجهول برو](https://aur.archlinux.org/packages/nerd-fonts-anonymous-pro/)
-   [Root rd phone ts door](https://aur.archlinux.org/packages/nerd-fonts-noto/)
-   [الطالب الذي يذاكر كثيرا الخطوط Inconsolata](https://aur.archlinux.org/packages/nerd-fonts-inconsolata/)

### `Option 8: Patch Your Own Font`

> خيار**الترقيع**لك**الخط الخاص**أو بالكامل**التخصيص**الخط المصحح.

استخدم البرنامج النصي لسطر أوامر Python المقدم لإنشاء خط مصحح من الخط الخاص بك للحصول على الحروف الرسومية الجديدة الإضافية

ارى:[الخط المرقع](#font-patcher)للاستخدام

-   استخدم هذا الخيار إذا كنت تفعل ذلك**ليس**تريد استخدام أحد[الخطوط المقدمة](#patched-fonts)
-   ستظل بحاجة إلى نسخ الخط الذي تم إنشاؤه إلى دليل الخطوط الصحيح على نظامك

<h2 align="center" id="font-patcher">
	<img src="images/nerd-fonts-patcher-logo.png" alt="Nerd Fonts Patcher">
</h2>

تصحيح الخط الذي تختاره للاستخدام مع تنسيق[فيم DevIcons ➶][vim-devicons]:

-   يتطلب: Python 2 (أو Python 3) ،`python-fontforge`الحزمة (الإصدار`20141231`أو لاحقًا ، انظر
    ال[تعليمات التثبيت](http://designwithfontforge.com/en-US/Installing_Fontforge.html))

-   طريقة التثبيت البديلة على OSX:`brew install fontforge`

-   طريقة بديلة في Linux: استخدام امتداد[AppImage](https://github.com/fontforge/fontforge/releases)

-   طريقة بديلة باستخدام Docker:[ذكر حب](https://hub.docker.com/r/nerdfonts/patcher)

-   استعمال:

        ./font-patcher PATH_TO_FONT

-   الاستخدام البديل: نفِّذ أداة التصحيح باستخدام برنامج FontForge الثنائي باستخدام علامة البرنامج النصي:

        ./fontforge -script font-patcher PATH_TO_FONT

-   تصحيح الخطوط باستخدام AppImage:

    _ملحوظة_:`chmod u+x`AppImage بعد التنزيل. يجب أن تكون جميع المسارات المزودة**مطلق**ومسار إخراج واضح مطلوب! إذا كان كل شيء موجودًا في نفس الدليل ، فيمكنك استخدام ملحق`$PWD`الاختزال.

        ./FontForge.AppImage -script $PWD/font-patcher $PWD/BaseFont.ttf -out /tmp

-   خطوط الترقيع باستخدام Docker:

        docker run -v /path/to/fonts:/in -v /path/for/output:/out nerdfonts/patcher [OPTIONS]

خيارات كاملة:

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

#### أمثلة

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

## فلدي تصحيح جميع الخطوط باتشر!

-   لاستخدام المساهم أو المطور

-   إعادة البقع**الكل**الخطوط في الدليل غير المصحح:

        ./gotta-patch-em-all-font-patcher\!.sh

-   يمكن أن يقتصر اختياريًا على نمط اسم خط معين:

        ./gotta-patch-em-all-font-patcher\!.sh Hermit

## المساهمة

ارى[كونتريبتنج.مد](contributing.md)

## مسارات الملفات غير المستقرة

: تحذير: تحذير: قد تتغير مسارات الملفات بناءً على الإصدارات (خاصة ملفات**رائد**نسخة المطبات)

الرجوع إلى**إفراج**فرع و_ليس_ال~~رئيسي - سيد~~الفرع لأن المسارات عرضة للتغيير لكل إصدار

-   على سبيل المثال:
    -   : white_check_mark: استخدم:<code>https \\: //github.com/ryanoasis/nerd-fonts/blob/<b>٠.ص.٠</b>/بتشدفنتص/هرمية/مدعوم/سمبلت/هرمية%٢٠ميديوم%٢٠نيرد%٢٠فونت%٢٠سومبليتي.عطف</code>
    -   : x: بدلا من:<code>https \\: //github.com/ryanoasis/nerd-fonts/blob/<del>رئيسي - سيد</del>/بتشدفنتص/هرمية/مدعوم/سمبلت/هرمية%٢٠ميديوم%٢٠نيرد%٢٠فونت%٢٠سومبليتي.عطف</code>

## خطوط أخرى جيدة للتصحيح

قائمة بالخطوط الإضافية الجيدة للتصحيح والتي لا يمكن توفيرها أو مشاركتها بسبب ترخيصها:

-   [إدخال أحادي][input-mono](قيود الترخيص)
    -   ربما يأتي مع استضافة خارجية :)
-   [أشياء ل][pragmatapro](ليس حر)
-   [لوحات المفاتيح][consolas](امتلاكي)
-   [الاوبرا و r شخص][operator](ليس حر)
-   [بفضل مونو][dank](ليس حر)

## دافع المشروع

ارى[الويكي: الغرض من المشروع][wiki-project-purpose]

## التغيير

ارى[شانجلج.مد](changelog.md)

## رخصة

[مع](LICENSE)© ريان إل ماكنتاير

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
