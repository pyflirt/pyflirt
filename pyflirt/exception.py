from dataclasses import dataclass

# Base exception class for all pyflirt errors
class PyflirtError(Exception):
    """Base class for all pyflirt exceptions."""
    pass

# More modern approach using @dataclass (though not necessary for simple exceptions)
@dataclass
class LanguageNotFoundError(PyflirtError):
    """Raised when the specified language is not found."""
    language: str = "Unknown"

    def __str__(self):
        return f"Language '{self.language}' not found."

@dataclass
class TypeNotFoundError(PyflirtError):
    """Raised when the specified flirt line type is not found."""
    type: str = "Unknown"

    def __str__(self):
        return f"Type '{self.type}' not found."
