import random
from .ar_flirt import ar_flirt
from .bn_flirt import bn_flirt
from .bg_flirt import bg_flirt
from .hr_flirt import hr_flirt
from .cs_flirt import cs_flirt
from .da_flirt import da_flirt
from .nl_flirt import nl_flirt
from .en_flirt import en_flirt
from .et_flirt import et_flirt
from .tl_flirt import tl_flirt
from .fi_flirt import fi_flirt
from .fr_flirt import fr_flirt
from .de_flirt import de_flirt
from .el_flirt import el_flirt
from .he_flirt import he_flirt
from .hi_flirt import hi_flirt
from .hu_flirt import hu_flirt
from .id_flirt import id_flirt
from .it_flirt import it_flirt
from .ja_flirt import ja_flirt
from .kn_flirt import kn_flirt
from .ko_flirt import ko_flirt
from .lv_flirt import lv_flirt
from .lt_flirt import lt_flirt
from .ms_flirt import ms_flirt
from .ml_flirt import ml_flirt
from .mr_flirt import mr_flirt
from .pl_flirt import pl_flirt
from .pt_flirt import pt_flirt
from .pa_flirt import pa_flirt
from .fa_flirt import fa_flirt
from .ro_flirt import ro_flirt
from .ru_flirt import ru_flirt
from .sr_flirt import sr_flirt
from .sk_flirt import sk_flirt
from .es_flirt import es_flirt
from .sv_flirt import sv_flirt
from .ta_flirt import ta_flirt
from .te_flirt import te_flirt
from .th_flirt import th_flirt
from .tr_flirt import tr_flirt
from .uk_flirt import uk_flirt
from .ur_flirt import ur_flirt
from .vi_flirt import vi_flirt
from typing import get_args, Literal, Any, Generator
from .exception import LanguageNotFoundError, TypeNotFoundError

all_flirt: dict[str, list[str]] = {
    "ar": ar_flirt,
    "bg": bg_flirt,
    "bn": bn_flirt,
    "cs": cs_flirt,
    "da": da_flirt,
    "de": de_flirt,
    "el": el_flirt,
    "en": en_flirt,
    "es": es_flirt,
    "et": et_flirt,
    "fa": fa_flirt,
    "fi": fi_flirt,
    "fr": fr_flirt,
    "he": he_flirt,
    "hi": hi_flirt,
    "hr": hr_flirt,
    "hu": hu_flirt,
    "id": id_flirt,
    "it": it_flirt,
    "ja": ja_flirt,
    "kn": kn_flirt,
    "ko": ko_flirt,
    "lt": lt_flirt,
    "lv": lv_flirt,
    "ml": ml_flirt,
    "mr": mr_flirt,
    "ms": ms_flirt,
    "nl": nl_flirt,
    "pa": pa_flirt,
    "pl": pl_flirt,
    "pt": pt_flirt,
    "ro": ro_flirt,
    "ru": ru_flirt,
    "sk": sk_flirt,
    "sr": sr_flirt,
    "sv": sv_flirt,
    "ta": ta_flirt,
    "te": te_flirt,
    "th": th_flirt,
    "tl": tl_flirt,
    "tr": tr_flirt,
    "uk": uk_flirt,
    "ur": ur_flirt,
    "vi": vi_flirt,
}

LANGUAGES = Literal[
    "ar",
    "bg",
    "bn",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "et",
    "fa",
    "fi",
    "fr",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "kn",
    "ko",
    "lt",
    "lv",
    "ml",
    "mr",
    "ms",
    "nl",
    "pa",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sr",
    "sv",
    "ta",
    "te",
    "th",
    "tl",
    "tr",
    "uk",
    "ur",
    "vi",
]

TYPES = Literal[
    "simple",
    "advance",
    "all",
]

LANGUAGE_VALUES: set[str] = set(get_args(LANGUAGES))
TYPES_VALUES: set[str] = set(get_args(TYPES))

def get_flirts(
    language: LANGUAGES = "en",
    type: TYPES = "simple"
) -> list[str]:
    """
    Get a list of flirt lines from the given language and tye.
    """
    try:
        flirts_by_type = all_flirts[language]
    except KeyError:
        raise LanguageNotFoundError(language)

    try:
        return flirts_by_type[type]
    except KeyError:
        raise TypeNotFoundError(
            f"No such type '{type}' in language '{language}'"
        )

def get_flirt(
    language: LANGUAGES = "en",
    type: TYPES = "simple"
) -> str:
    """
    Get a single flirt line from the given language and type.
    """
    flirts = get_flirts(language, type)
    return random.choice(flirts)

def get_random_flirt() -> str:
    language = random.choice(list(LANGUAGE_VALUES))
    type = random.choice(list(TYPES_VALUES))
    return get_flirt(language, type)

def search_flirts(keyword: str, language: LANGUAGES = "en", type: TYPES = "all") -> list[str]:
    flirts = get_flirts(language, type)
    return [line for line in flirts if keyword.lower() in line.lower()]
    
def loop(
    language: LANGUAGES = "en",
    type: TYPES = "simple"
) -> Generator[str, Any, Any]:
    """
    Generate flirt lines on loop.
    """
    while True:
        yield get_flirt(language, type)
