'''
Meta plugins for Korean support in Plover.
'''

from collections import namedtuple
import plover_korean.hangeul as hangeul


# Constants for particle rules.
RULE_PARTICLE_NEUN = '는,은'
RULE_PARTICLE_GA = '가,이'
RULE_PARTICLE_REUL = '를,을'

RULE_PARTICLE_DA = '다,이다'
RULE_PARTICLE_RA = '라,이라'
RULE_PARTICLE_YA = '야,아'

RULE_PARTICLE_WA = '와,과'
RULE_PARTICLE_RANG = '랑,이랑'
RULE_PARTICLE_NA = "나,이나"

RULE_PARTICLE_RO = '로,으로,ㄹ'
RULE_PARTICLE_MYEO = '며,이며'

ParticleRuleInfo = namedtuple(
    'ParticleRuleInfo', [
        # The particle to use when the previous word ends in a vowel.
        'vowel',
        # The particle to use when the previous word ends in a consonant.
        'consonant',
        # For what final consonant of the previous word should the
        # 'consonant' case be treated as the 'vowel' case.
        # Example: 'ㄹ' for the consonant = '으로', vowel = '로' particle.
        'except_consonant'
    ]
)

def parse_particle_args(particle_info: str) -> ParticleRuleInfo:
    '''
    Parses raw particle information into a ParticleRuleInfo structure.

    :param particle_info: The generic particle information.
                          Comma-delimited string format corresponding to ParticleRuleInfo
                          like 'vowel,consonant,except_consonant'. Both 'vowel' and
                          'consonant' must be provided.
    :type particle_info: str

    :return: The parsed particle rule info if possible to parse.
    :rtype: ParticleRuleInfo

    :raises ValueError: Unable to parse the provided particle information.
    '''

    args_list = particle_info.split(',', 2)

    try:
        vowel = args_list[0]
        if not hangeul.is_hangeul(vowel):
            vowel = ''
    except IndexError:
        vowel = ''

    try:
        consonant = args_list[1]
        if not hangeul.is_hangeul(consonant):
            consonant = ''
    except IndexError:
        consonant = ''

    try:
        except_consonant = args_list[2]
        if not hangeul.is_letter(except_consonant):
            except_consonant = ''
    except IndexError:
        except_consonant = ''

    if not vowel and not consonant:
        raise ValueError('Both a vowel and consonant particle must be provided.')

    return ParticleRuleInfo(
        vowel=vowel,
        consonant=consonant,
        except_consonant=except_consonant
    )

def format_unresolved_particle(rule_info: ParticleRuleInfo):
    '''
    When a choice of one particle cannot be made, formats the choices for output.

    :param rule_info: The particle rule info in use.
    :type rule_info: ParticleRuleInfo

    :return: Formatted string for output.
    :rtype: str
    '''

    return f'{rule_info.consonant}({rule_info.vowel})'

def apply_particle_generic(context, meta_args: str):
    '''
    Attaches the provided generic particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :param meta_args: The arguments containing the generic particle information.
                      Comma-delimited string format corresponding to ParticleRuleInfo
                      like 'vowel,consonant,except_consonant'. Both 'vowel' and
                      'consonant' must be provided.
    :type meta_args: str

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    try:
        rule_info = parse_particle_args(meta_args)
    except ValueError:
        return context.new_action()

    action = context.new_action()
    action.prev_attach = True
    action.next_attach = True

    last_word = context.last_action.word or ''

    if (hangeul.ends_in_consonant(last_word) and
            not hangeul.is_last_consonant(last_word, rule_info.except_consonant)):
        action.text = rule_info.consonant
    elif hangeul.ends_in_vowel(last_word):
        action.text = rule_info.vowel
    else:
        action.text = format_unresolved_particle(rule_info)

    return action

def apply_particle_neun(context, _):
    '''
    Attaches the topic particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_NEUN)

def apply_particle_ga(context, _):
    '''
    Attaches the subject particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_GA)

def apply_particle_reul(context, _):
    '''
    Attaches the object particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_REUL)

def apply_particle_da(context, _):
    '''
    Attaches the verb / copula particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_DA)

def apply_particle_ra(context, _):
    '''
    Attaches the contraction of 라서 to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_RA)

def apply_particle_ya(context, _):
    '''
    Attaches the vocative name particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_YA)

def apply_particle_wa(context, _):
    '''
    Attaches the formal 'and' particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_WA)

def apply_particle_rang(context, _):
    '''
    Attaches the informal 'and' particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_RANG)

def apply_particle_na(context, _):
    '''
    Attaches the 'or' particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_NA)

def apply_particle_ro(context, _):
    '''
    Attaches the direction particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_RO)

def apply_particle_myeo(context, _):
    '''
    Attaches the quasi 'and' / same time particle to the last word in the context
    to be executed as the next action.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    return apply_particle_generic(context, RULE_PARTICLE_MYEO)
