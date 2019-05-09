import requests
import logging

from rextester_py.data import languages, compiler_args

URL = "https://rextester.com/rundotnet/api"

logging.getLogger(__name__)


def rexec(lang, code, stdin=None):
    if lang.lower() not in languages:
        raise CompilerError("Unknown language")

    data = {
        "LanguageChoice": languages.get(
            lang.lower()),
        "Program": code,
        "Input": stdin,
        "CompilerArgs": compiler_args.get(
            lang.lower())}

    response = requests.post(URL, data=data)
    response.raise_for_status()

    if not code:
        raise CompilerError("There's no code to execute")

    response = response.json()

    return RextesterResult(response.get("Result"),
                           response.get("Warnings"),
                           response.get("Errors"),
                           response.get("Stats"),
                           response.get("Files"))


class CompilerError(Exception):
    pass


class UnknownLanguage(Exception):
    pass


class RextesterResult(object):
    def __init__(self, results, warnings, errors, stats, files):
        self.results = results
        self.warnings = warnings
        self.errors = errors
        self.stats = stats
        self.files = files
