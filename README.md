# Plover Korean

Korean plugins for [Plover](https://github.com/openstenoproject/plover).

Currently contains:

- [System Overview - CAS-based Layout](#system-overview-cas-based-layout)
- [System Overview - Sorizava-based Layout](#system-overview-sorizava-based-layout)
- [Meta Plugins](#meta-plugins)

## Installation

*This plugin has not been released on PyPI yet, so locally installing from source is currently the only option*

Download the latest version of Plover for your operating system from the [releases page](https://github.com/openstenoproject/plover/releases). Only versions 4.0.0.dev7 and higher are supported.

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the "plover-korean" plugin entry in the list
4. Click install
5. Restart Plover

The same method can be used for updating and uninstalling the plugin.

If you have issues with character misalignment in places like the Paper Tape in the Plover GUI try installing [Nanum Gothic Coding](https://fonts.google.com/earlyaccess#Nanum+Gothic+Coding), a monospaced sans-serif Korean font, and setting Plover's font to that where possible. The majority of monospaced fonts do not have CJK language support which is why this issue comes up for things relying on monospaced plain text display.

## System Overview - CAS-based Layout

![CAS Layout](https://i.imgur.com/T9Kfc07.png)

See the reference guide for this system [here](https://github.com/nsmarkop/plover_korean_notes).

## System Overview - Sorizava-based Layout

![Sorizava Layout](https://i.imgur.com/kpEL3mE.png)

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
ko_particle_neun | ~는/은
ko_particle_ga   | ~가/이
ko_particle_reul | ~를/을
ko_particle_da   | ~다/이다
ko_particle_ra   | ~라/이라
ko_particle_ya   | ~야/아
ko_particle_wa   | ~와/과
ko_particle_rang | ~랑/이랑
ko_particle_na   | ~나/이나
ko_particle_ro   | ~로/으로
ko_particle_myeo | ~며/이며

If support for a particular variable particle is not currently implemented, [**please open an issue on GitHub for support to be added**](https://github.com/nsmarkop/plover_korean/issues). However, there is one additional meta plugin that can be used for when this occurs: "ko_particle_generic". It has three plugin arguments:

1. The particle to be used for words ending in vowels.
2. The particle to be used for words ending in consonants.
3. (optional) The final consonant of words where the consonant case should be treated as the vowel case.

For example, an entry that replicates the "ko_particle_neun" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:는,은}"
}
```

An entry that replicates the "ko_particle_ro" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:로,으로,ㄹ}"
}
```

All particles will attach to the previous entry.

One limitation of these particles is that if they are being attached to something that is not written in Hangeul they cannot accurately determine which particle variation needs to be used. When that occurs both variations will be output instead in the format "consonant_option(vowel_option)". This is open to change based on usage and feedback.
