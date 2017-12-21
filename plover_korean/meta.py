'''
Meta plugins for Korean support in Plover.
'''

from collections import namedtuple
import hgtk


RULE_PARTICLE_TOPIC = '는,은'
RULE_PARTICLE_SUBJECT = '가,이'
RULE_PARTICLE_OBJECT = '를,을'
RULE_PARTICLE_AND_FORMAL = '와,과'

ParticleRuleInfo = namedtuple(
    'ParticleRuleInfo', [
        # The particle to use when the previous word ends in a vowel.
        'vowel',
        # The particle to use when the previous word ends in a consonant.
        'consonant',
        # For what last consonant of the previous word should the
        # 'consonant' case be treated as the 'vowel' case.
        # Example: 'ㄹ' for the consonant = '으로', vowel = '로' particle.
        'except_consonant'
    ]
)

def initialize_particle_action(context):
    action = context.new_action()
    action.prev_attach = True

    last_word = context.last_action.word or ''

    return (action, last_word)

def parse_particle_args(meta_args: str) -> ParticleRuleInfo:
    args_list = meta_args.split(',', 2)

    try:
        vowel = args_list[0]
    except IndexError:
        vowel = ''

    try:
        consonant = args_list[1]
    except IndexError:
        consonant = ''

    try:
        except_consonant = args_list[2]
    except IndexError:
        except_consonant = ''

    return ParticleRuleInfo(
        vowel=vowel,
        consonant=consonant,
        except_consonant=except_consonant
    )

def apply_particle_generic(context, meta_args: str):
    (action, last_word) = initialize_particle_action(context)

    rule_info = parse_particle_args(meta_args)

    last_syllable = ''
    if len(last_word) >= 1:
        last_syllable = last_word[-1]

    # TODO: Order here is pretty strict and fragile - could probably be refactored
    can_determine_particle = (last_syllable and
                              hgtk.checker.is_hangul(last_syllable))

    if (can_determine_particle and
            hgtk.checker.has_batchim(last_syllable) and
            (hgtk.letter.decompose(last_syllable)[-1] != rule_info.except_consonant)):
        action.text = rule_info.consonant
    elif can_determine_particle:
        action.text = rule_info.vowel
    # TODO: Is this good default behavior? Should it just choose one?
    else:
        action.text = f'{rule_info.consonant}({rule_info.vowel})'

    # For now, build into every particle that a space follows it
    action.text = action.text + ' '

    return action

def apply_particle_topic(context, _):
    return apply_particle_generic(context, RULE_PARTICLE_TOPIC)

def apply_particle_subject(context, _):
    return apply_particle_generic(context, RULE_PARTICLE_SUBJECT)

def apply_particle_object(context, _):
    return apply_particle_generic(context, RULE_PARTICLE_OBJECT)

def apply_particle_and_formal(context, _):
    return apply_particle_generic(context, RULE_PARTICLE_AND_FORMAL)
