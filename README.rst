Plover Korean
=============

Korean stenography for
`Plover <https://github.com/openstenoproject/plover>`__.

-  `Korean Core - CAS-based System <#korean-core-cas-based-system>`__
-  `Korean Expanded - Sorizava-based
   System <#korean-expanded-sorizava-based-system>`__
-  `Meta Plugins <#meta-plugins>`__

Installation
------------

*This plugin has not been released on PyPI yet, so locally installing
from source is currently the only option*

If you have issues with character misalignment in places like the Paper
Tape in the Plover GUI try installing `Nanum Gothic
Coding <https://fonts.google.com/earlyaccess#Nanum+Gothic+Coding>`__, a
monospaced sans-serif Korean font, and setting Plover’s font to that
where possible. The majority of monospaced fonts do not have CJK
language support which is why this issue comes up for things relying on
monospaced plain text display.

Korean Core - CAS-based System
------------------------------

.. figure:: https://i.imgur.com/T9Kfc07.png
   :alt: CAS Layout

   CAS Layout

See the reference guide for this system
`here </plover_korean/system/cas/docs/README.md>`__.

Korean Expanded - Sorizava-based System
---------------------------------------

.. figure:: https://i.imgur.com/kpEL3mE.png
   :alt: Sorizava Layout

   Sorizava Layout

See the reference guide for this system
`here </plover_korean/system/sorizava/docs/README.md>`__.

Meta Plugins
------------

In order to use these meta plugins you need to add them with a
dictionary entry like the example below:

.. code:: json

    {
        "ㄴㅣㄱ": "{:meta_plugin_name:meta_plugin_argument1,meta_plugin_argument2,...}"
    }

If there are no arguments for the meta plugin, just
``{:meta_plugin_name}`` is sufficient.

Particles
~~~~~~~~~

Regex support for Korean syllable blocks does not work well so various
meta plugins have been created for contextually determining what
particle to attach to a word.

While many particles are always the same when attached to words, some
change their form depending on if the word they are attached to ends
with a vowel or consonant. The following table lists the current plugins
with that support that can be used:

+------------------+----------+
| Meta Plugin Name | Concept  |
+==================+==========+
| ko_particle_neun | ~는/은   |
+------------------+----------+
| ko_particle_ga   | ~가/이   |
+------------------+----------+
| ko_particle_reul | ~를/을   |
+------------------+----------+
| ko_particle_da   | ~다/이다 |
+------------------+----------+
| ko_particle_ra   | ~라/이라 |
+------------------+----------+
| ko_particle_ya   | ~야/아   |
+------------------+----------+
| ko_particle_wa   | ~와/과   |
+------------------+----------+
| ko_particle_rang | ~랑/이랑 |
+------------------+----------+
| ko_particle_na   | ~나/이나 |
+------------------+----------+
| ko_particle_ro   | ~로/으로 |
+------------------+----------+
| ko_particle_myeo | ~며/이며 |
+------------------+----------+

If support for a particular variable particle is not currently
implemented, `**please open an issue on GitHub for support to be
added** <https://github.com/nsmarkop/plover_korean/issues>`__. However,
there is one additional meta plugin that can be used for when this
occurs: “ko_particle_generic”. It has three plugin arguments:

1. The particle to be used for words ending in vowels.
2. The particle to be used for words ending in consonants.
3. (optional) The final consonant of words where the consonant case
   should be treated as the vowel case.

For example, an entry that replicates the “ko_particle_neun”
functionality would be:

.. code:: json

    {
        "ㄴㅣㄱ": "{:ko_particle_generic:는,은}"
    }

An entry that replicates the “ko_particle_ro” functionality would be:

.. code:: json

    {
        "ㄴㅣㄱ": "{:ko_particle_generic:로,으로,ㄹ}"
    }

If you attempt to use these plugins to attach particles to non-Korean
words they cannot accurately determine how to display and will fall back
to a default case.

License
-------

GPLv3+.
