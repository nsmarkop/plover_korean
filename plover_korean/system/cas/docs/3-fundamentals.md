# Fundamentals

Before getting into the theory, there are a few things to cover as background knowledge.

## Spacing

Spacing in this system is often explicit and the `*` key serves as the space key for the user when used alone for this purpose. Automatic spaces by the system all the time like those used in the standard English system do not work well with this theory due to it being based off of syllable blocks at its core rather than words, however once you start getting into particle usage and more you can start to rely on it.

How this is implemented in practice with the [Korean plugin](https://github.com/nsmarkop/plover_korean) for [Plover](https://github.com/openstenoproject/plover) is that each dictionary entry must end with an attach operator: `{^}`. Any entry that does not end with an attach operator should be considered an "explicit" space. Attach operators will be shown for dictionary entries mentioned here.

Keep the spacing rules in mind when adding new entries to your personal dictionary.

## Suppressing Spaces

Sometimes a space will be added when you don't want it to be. You can refer to Plover's [dictionary format wiki page](https://github.com/openstenoproject/plover/wiki/Dictionary-Format) for syntax to use in dictionary entries to overcome this. In the default dictionary, TODO: create a stroke like D-LS to go with *.

## Undo

In order to undo what you've typed, you can use the `-ㅂㄴ` stroke.