import argparse
from .pyflirt import get_flirt, LanguageNotFoundError, TypeNotFoundError 

def create_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="flirt lines of any type in any language."
    )

    parser.add_argument(
        "-t", "--type",
        choices=["simple", "advance", "all"],
        default="simple",
        help="Flirt lines type."
    )

    parser.add_argument(
        "-l", "--language",
        choices=[
            "en", "de", "es", "fr", "it", "hu", "lt", "pl", "cs",
            "ru", "sv", "pt", "hi", "ar", "tr", "ja", "ko", "bn",
            "fa", "ta", "te", "nl", "id", "el", "he", "uk", "ur", "th",
            "ro", "sk", "sr", "ml", "mr", "kn", "pa", "ms", "et", "lv", 
            "vi", "tl", "da", "bg", "fi", "hr"
        ],
        default="en",
        help="Flirt line language."
    )

    return parser

def main() -> None:
    parser = create_argparser()
    args = parser.parse_args()

    try:
        flirt = get_flirt(language=args.language, type=args.type)
        print(flirt)

    except LanguageNotFoundError:
        print(f"No such language: {args.language}")
        exit(1)

    except TypeNotFoundError:
        print(f"No such type: {args.type}")
        exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
