TAGS = r'[<{][/\\]?[a-z0-9.]+[}>]'
POSITION_TAGS = r'^{\\an[0-9]}'
FRONT_OPTIONAL_TAGS_WITH_HYPHEN = rf'^\s*({TAGS})?\s*-?\s*({TAGS})?'
TIME_LOOKAHEAD = r'(?![0-9]{2})'

SPEAKER = rf'({FRONT_OPTIONAL_TAGS_WITH_HYPHEN})\s*(Mc[A-Z][a-zA-Z]+|[A-Z0-9\&\[\]\.#\' ]+\s*|[A-Z][a-z]+):{TIME_LOOKAHEAD} ?'
SPEAKER_PARENTHESES = rf'({FRONT_OPTIONAL_TAGS_WITH_HYPHEN})\s*(?:[A-Z0-9\&\[\]\.#\' ]+\s*|[A-Z][a-z]+)(?: \([a-zA-Z ]+\)): ?'

DESCRIPTION_BRACKET = r'\[(?:[^\]]|\s)*\]'
DESCRIPTION_PARENTHESES = r'\((?:[^\)]|\s)*\)'
FULL_LINE_DESCIRPTION_BRACKET = rf'^-?\s*\[[^\]]+\]$'
NEW_LINE_DESCRIPTION_BRACKET = rf'^(?:{TAGS})?-?\s*{DESCRIPTION_BRACKET}(?:{TAGS})?$'
FRONT_DESCRIPTION_BRACKET = rf'^(?:{SPEAKER}|{SPEAKER_PARENTHESES})?({FRONT_OPTIONAL_TAGS_WITH_HYPHEN}){DESCRIPTION_BRACKET}:?'
END_DESCRIPTION_BRACKET = rf'\s*{DESCRIPTION_BRACKET}\s*$'
FULL_LINE_DESCIRPTION_PARENTHESES = rf'^-?\s*\([^\)]+\)$'
NEW_LINE_DESCRIPTION_PARENTHESES = rf'^(?:{TAGS})?-?\s*{DESCRIPTION_PARENTHESES}(?:{TAGS})?$'
FRONT_DESCRIPTION_PARENTHESES = rf'^({FRONT_OPTIONAL_TAGS_WITH_HYPHEN})(?:{SPEAKER}|{SPEAKER_PARENTHESES})?{DESCRIPTION_PARENTHESES}:?'
END_DESCRIPTION_PARENTHESES = rf'\s*{DESCRIPTION_PARENTHESES}:?\s*$'
INLINE_DESCRIPTION = r'(?:<[a-z]+>)?[\[(][A-Z]+[)\]](?:</[a-z]+>)?'
