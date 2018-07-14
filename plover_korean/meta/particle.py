"""Meta plugins for Korean particles."""

from typing import Optional

from plover.formatting import _Context, _Action

from plover_korean.hangeul import (
    ParticleRuleInfo,
    load_raw_rule,
    attach_particle
)


def apply_particle(context: _Context,
                   rule_info: Optional[ParticleRuleInfo]) -> _Action:
    """Creates an action based on the particle rule info.

    The action will replace the last word in the context with the word plus
    the chosen particle based on the particle rule info.

    Args:
        context: The context of actions in Plover.
        rule_info: The particle rule information to use.

    Returns:
        An action with a particle attached to the last word in the context.
        If the rule info is invalid, a blank new action will be returned.
    """

    action: _Action = context.copy_last_action()

    if rule_info is None:
        return action

    last_word = ''.join(context.last_words(1))
    action.prev_replace = last_word
    action.prev_attach = True
    action.word = None
    action.text = attach_particle(last_word, rule_info)

    return action


def apply_particle_generic(context: _Context, args: str) -> _Action:
    """Creates an action based on the raw particle rule info.

    Args:
        context: The context of actions in Plover.
        args: The arguments containing the raw particle rule info.
            Format is a comma-delimited string corresponding to
            ParticleRuleInfo like 'vowel,consonant,except_consonant'.
            Both vowel and consonant must be provided.

    Returns:
        The next action for Plover to perform.
    """

    try:
        rule_info = load_raw_rule(args)
    except ValueError:
        pass

    return apply_particle(context, rule_info)


def apply_particle_neun(context: _Context, args: str) -> _Action:
    """Creates an action for the 는/은 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='는',
        consonant_particle='은',
        exception_consonant=None
    ))

def apply_particle_ga(context: _Context, args: str) -> _Action:
    """Creates an action for the 가/이 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='가',
        consonant_particle='이',
        exception_consonant=None
    ))


def apply_particle_reul(context: _Context, args: str) -> _Action:
    """Creates an action for the 를/을 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='를',
        consonant_particle='을',
        exception_consonant=None
    ))


def apply_particle_da(context: _Context, args: str) -> _Action:
    """Creates an action for the 다/이다 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='다',
        consonant_particle='이다',
        exception_consonant=None
    ))


def apply_particle_ra(context: _Context, args: str) -> _Action:
    """Creates an action for the 라/이라 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='라',
        consonant_particle='이라',
        exception_consonant=None
    ))


def apply_particle_ya(context: _Context, args: str) -> _Action:
    """Creates an action for the 야/아 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='야',
        consonant_particle='아',
        exception_consonant=None
    ))


def apply_particle_wa(context: _Context, args: str) -> _Action:
    """Creates an action for the 와/과 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='와',
        consonant_particle='과',
        exception_consonant=None
    ))


def apply_particle_rang(context: _Context, args: str) -> _Action:
    """Creates an action for the 랑/이랑 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='랑',
        consonant_particle='이랑',
        exception_consonant=None
    ))


def apply_particle_na(context: _Context, args: str) -> _Action:
    """Creates an action for the 나/이나 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='나',
        consonant_particle='이나',
        exception_consonant=None
    ))


def apply_particle_ro(context: _Context, args: str) -> _Action:
    """Creates an action for the 로/으로 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='로',
        consonant_particle='으로',
        exception_consonant='ㄹ'
    ))


def apply_particle_myeo(context: _Context, args: str) -> _Action:
    """Creates an action for the 며/이며 particle.

    Args:
        context: The context of actions in Plover.
        args: Unused arguments provided to the meta plugin.

    Returns:
        The next action for Plover to perform.
    """

    return apply_particle(context, ParticleRuleInfo(
        vowel_particle='며',
        consonant_particle='이며',
        exception_consonant=None
    ))
