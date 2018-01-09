# Plover Korean

Korean plugin for [Plover](https://github.com/openstenoproject/plover). This plugin is still under development and breaking changes may happen frequently.

Currently contains:

- [System Overview - CAS-based Layout](#system-overview-cas-based-layout)
- [System Overview - Sorizava-based Layout](#system-overview-sorizava-based-layout)
- [Meta Plugins](#meta-plugins)

## Installation

*This plugin has not been released on PyPI yet, so locally installing from source is currently the only option*

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev6 and higher are supported.

Once installed, navigate to the Plugin Manager in the main Plover window. From there you should see the "plover-korean" plugin which you can select and install to use after restarting Plover. The same method can be used for updating and uninstalling the plugin.

If you run Plover from source you can alternatively install it directly with pip or you can check out a copy of this repository and install it locally with pip like so::

    pip install -e /path/to/repo

If you have issues with character misalignment in places like the Paper Tape in the Plover GUI try installing [Nanum Gothic Coding](https://fonts.google.com/earlyaccess#Nanum+Gothic+Coding), a monospaced sans-serif Korean font, and setting Plover's font to that where possible. The majority of monospaced fonts do not have CJK language support which is why this issue comes up for things relying on monospaced plain text display.

## Dictionaries

If you need to manually replace or update your dictionaries you can find the released ones [here](https://github.com/nsmarkop/plover_korean/tree/master/plover_korean/dictionaries). Each dictionary is prefixed with the system it applies to.

The released dictionaries are actually compiled versions of several separate dictionaries that are maintained [here](https://github.com/nsmarkop/plover_korean/tree/master/plover_korean/dictionaries_partial) if you want to use those directly.

## System Overview - CAS-based Layout

![CAS Layout](/images/layout_cas.png)

### Syllable Blocks

Syllable blocks form the foundation of the Korean language and as such the foundation of this system. Excluding the number row, the key layout is divided into three main sections:

- Initial consonant; stroked using the left hand.
- Medial vowel; stroked using the thumbs.
- Final consonant(s); stroked using the right hand.

To understand why this grouping can be used to easily represent every syllable in Korean you should be familiar with Korean syllable block construction which you can read about on [Wikipedia](https://en.wikipedia.org/wiki/Hangul#Morpho-syllabic_blocks).

#### Consonants

All base consonants are represented directly on both sides of the key layout; aspirated and tensed variations of them are written using combinations of the base consonants. To make the aspirated version of any consonant you add "ㅎ" to it like so (examples use the initial consonant group steno order for input):

Input | Output
----- | ------
ㅎㅈ    | ㅊ
ㅎㄱ    | ㅋ
ㅎㄷ    | ㅌ
ㅎㅂ    | ㅍ

To make the tensed version of any consonant you add "ㅇ" to it like so:

Input | Output
----- | ------
ㅈㅇ    | ㅉ
ㄱㅇ    | ㄲ
ㄷㅇ    | ㄸ
ㅇㅂ    | ㅃ
ㅇㅅ    | ㅆ

You can never have more than one initial consonant thus no conflicts exist in the initial position. For the final consonant position you can have multiple final consonants in the following cases:

- ㄳ
- ㄵ
- ㄶ
- ㄺ
- ㄻ
- ㄼ
- ㄽ
- ㄾ
- ㄿ
- ㅀ
- ㅄ

None of these cases conflict with the use of ㅎ and ㅇ for aspirated and tensed consonants which means both consonant postitions can be fully represented in a safe way.

If the initial consonant is "ㅇ" then it is left out of any strokes. Similarly, if there is no final consonant then nothing is needed in that position.

#### Vowels

Vowels are either used outright or constructed from their base parts for the complex vowels. The "\*" key is used as a modifier when just combining base vowels is not possible for the sound, like the "y" variation of vowels. "ㅖ" is a special case where an easier fingering not requiring pressing three vowel keys with one thumb is chosen over the standard pattern.

All vowels by themselves output their phonetic form so those will be used in the following table for examples:

Input  | Output
------ | ------
ㅗ      | 오
ㅏ      | 아
ㅜ      | 우
-ㅓ     | 어
-ㅣ     | 이
ㅏㅓ     | 으
ㅏㅣ     | 애
-ㅓㅣ    | 에
ㅗ*     | 요
ㅏ*     | 야
ㅜ*     | 유
-ㅓ*    | 여
ㅏ*ㅓ    | 얘
ㅗㅓㅣ    | 예
ㅏㅓㅣ    | 의
ㅗㅣ     | 외
ㅜㅣ     | 위
ㅗㅏ     | 와
ㅜㅓ     | 워
ㅗㅏㅣ    | 왜
ㅜㅓㅣ    | 웨

#### In Practice

To make syllable blocks you just combine the individual rules for the initial, medial, and final. Some examples:

Input         | Output
------------- | ------
ㅈㅏ            | 자
ㅈㅏㅁ           | 잠
ㅗㅅ            | 옷
-ㅓㄱ           | 억
ㅎㄱㅗㅇ          | 콩
ㄷㅇㅏㅇ          | 땅
ㅎㅗㅣ/ㅏㅓㅣ       | 회의
ㅅㅣ/ㄱㅗㅓㅣ       | 시계

One limitation of the system is that you cannot write consonants or vowels by themselves like "ㅈ" or "ㅏ". Instead you will need to write [letter names](https://en.wikipedia.org/wiki/Hangul#Letter_names) out phonetically like "지읒" via "ㅈㅣ/ㅏㅓㅈ" or "아" via "ㅏ" if the need ever arises. All Korean syllables use at least a consonant and a vowel which is why this is not currently supported.

### Spacing

The original CAS machines rely on manual spacing except when otherwise defined in dictionary entries. Plover is different in that by default it attempts to automatically handle spaces between strokes which can cause some issues in Korean due to how spacing works with particle attachment, verb conjugation, etc. when you are inputting things with combinations of briefs and individual syllable blocks.

The current approach to handle this for the system is to use the attach command, "{^}", in most dictionary entries to suppress the spacing. Some alternatives like a dictionary defined stroke for "{MODE:SET_SPACE:}" that would need to be used every time before typing or something on the core Plover side for letting systems define spacing rules are currently being looked into. It is possible that a way to take advantage of Plover's automatic spacing without relying on additional options will be found as well.

### Starter Strokes

A handful of useful strokes to know when getting started are listed below. Using the dictionary lookup in Plover or exploring [the dictionaries in this repository](/plover_korean/dictionaries_partial) are otherwise good ways to discover things.

Input     | Output
--------- | ------
\*        | Space
-ㅂㄴ       | Undo
-ㅂㄴㅅㅈ     | New line
1-ㅇ       | Period
1-ㄹ       | Comma
1-ㄱ       | Question mark
1-ㄷ       | Exclamation point

There are patterns to most things in the system, like "1-ㅇ" for a period with a space after it and "1*ㅇ" for a period without a space after it extending to commas and other symbols (other symbols which are stroked by just cycling through left hand number and right hand consonant combinations). I will be formalizing these in the dictionary and documenting them as development progresses.

### Briefs

The theory for constructing briefs is still being investigated and this will be updated with the patterns as time goes on.

## System Overview - Sorizava-based Layout

![Sorizava Layout](/images/layout_sorizava.png)

This system is not currently possible to use without modifications to setup.cfg to enable the system plugin and manually installing it for running Plover from source. It has not been tested and there is no plan to focus on dictionary work or resolving issues in the system for now, but it's here for future reference / development.

## Meta Plugins

Some behavior for Korean support cannot be implemented purely with normal dictionary entries and the current system plugin properties. Particularly, regex support for Korean syllable blocks does not work well so defining and executing on some grammatical rules needs to be done separately.

In order to use these meta plugins you need to add them with a dictionary entry like the example below:

``` json
{
    "ㄴㅣㄱ": "{:meta_plugin_name:meta_plugin_argument1,meta_plugin_argument2,...}"
}
```

Naturally if there are no arguments for the meta plugin, just the meta plugin name is sufficient.

All meta plugins here can be used in conjunction with the rest of the standard Plover dictionary formatting.

### Particles

While many particles are always the same when attached to words, some change their form depending on if the word they are attached to ends with a vowel or consonant. The following table lists the current plugins with that support that can be used:

Meta Plugin Name | Concept
---------------- | ----------
kr_particle_neun | ~는/은
kr_particle_ga   | ~가/이
kr_particle_reul | ~를/을
kr_particle_da   | ~다/이다
kr_particle_ra   | ~라/이라
kr_particle_ya   | ~야/아
kr_particle_wa   | ~와/과
kr_particle_rang | ~랑/이랑
kr_particle_na   | ~나/이나
kr_particle_ro   | ~로/으로
kr_particle_myeo | ~며/이며

If support for a particular variable particle is not currently implemented, [**please open an issue on GitHub for support to be added**](https://github.com/nsmarkop/plover_korean/issues). However, there is one additional meta plugin that can be used for when this occurs: "kr_particle_generic". It has three plugin arguments:

1. The particle to be used for words ending in vowels.
2. The particle to be used for words ending in consonants.
3. (optional) The final consonant of words where the consonant case should be treated as the vowel case.

For example, an entry that replicates the "kr_particle_neun" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:kr_particle_generic:는,은}"
}
```

An entry that replicates the "kr_particle_ro" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:kr_particle_generic:로,으로,ㄹ}"
}
```

All particles will attach to the previous and the next entries in Plover, so keep this in mind for things like needing to add explicit spacing after particles that should not have other particles or words attached directly after them.

One limitation of these plugins is that if they are being attached to something that is not written in Hangeul we cannot accurately determine which particle variation needs to be used. When that occurs both variations will be output instead in the format "consonant_option(vowel_option)". This is open to change based on usage and feedback.
