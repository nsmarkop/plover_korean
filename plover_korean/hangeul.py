"""Korean script related functions and wrappers."""

from typing import NamedTuple, Optional, Dict

import hgtk


DELIM_RAW_RULE = ','


class ParticleRuleInfo(NamedTuple):
    """Stores Korean particle rule information.

    Attributes:
        vowel_particle: The particle to use when the previous word ends in a
            vowel.
        consonant_particle: The particle to use when the previous word ends in
            a consonant.
        exception_consonant: For what final consonant of the previous word
            should the consonant case be treated as the vowel case. For
            example: 'ㄹ' for the consonant = '으로', vowel = '로' particle.
    """

    vowel_particle: str
    consonant_particle: str
    exception_consonant: Optional[str]

    def get_hgtk_format(self) -> Dict[str, Optional[str]]:
        """Converts the rule info to the format used by hgtk.josa.

        Returns:
            A dictionary formatted like:

            {
                'has': vowel,
                'not': consonant,
                'except': exception
            }
        """

        return {
            'has': self.vowel_particle,
            'not': self.consonant_particle,
            'except': self.exception_consonant
        }

    def get_raw_format(self) -> str:
        """Converts the rule info to the raw rule format.

        Returns:
            A string formatted like vowel,consonant,exception.
        """

        delim = DELIM_RAW_RULE
        raw_rule = f'{self.vowel_particle}{delim}{self.consonant_particle}'

        if self.exception_consonant:
            raw_rule = f'{raw_rule}{delim}{self.exception_consonant}'

        return raw_rule


def load_raw_rule(raw_rule: str) -> ParticleRuleInfo:
    """Parses raw particle information into a ParticleRuleInfo.

    Args:
        raw_rule: The particle information. Format is a comma-delimited string
            corresponding to ParticleRuleInfo like
            'vowel,consonant,except_consonant'. Both vowel and consonant must
            be provided.

    Returns:
        The parsed particle rule info if it's possible to parse.

    Raises:
        ValueError: An error occurred parsing the particle information.
    """

    try:
        vowel, consonant, exception = raw_rule.split(DELIM_RAW_RULE, 2)
    except ValueError:
        exception = None
        vowel, consonant = raw_rule.split(DELIM_RAW_RULE, 2)

    return ParticleRuleInfo(
        vowel_particle=vowel,
        consonant_particle=consonant,
        exception_consonant=exception
    )


def format_unresolved_rule(rule_info: ParticleRuleInfo) -> str:
    """Formats an unresolved particle rule for display.

    Args:
        rule_info: The particle rule info to use.

    Returns:
        The formatted string.
    """

    return f'{rule_info.consonant_particle}({rule_info.vowel_particle})'


def attach_particle(word: str, rule_info: ParticleRuleInfo) -> str:
    """Attaches a particle to a word.

    Chooses a particle to use based on a word and a rule.
    If unable to determine a particle, the rule's consonant
    particle will be attached.

    Args:
        word: The word to choose a particle for.
        rule_info: The particle rule info to use.

    Returns:
        The word with the appropriate particle attached.
    """

    return hgtk.josa.attach(word, rule_info.get_hgtk_format())
