import aiohttp
import logging

from rextester_py.data import languages, compiler_args


logging.getLogger(__name__)


async def __fetch(session, url, data):
    async with session.get(url, data=data) as response:
        return await response.json()


async def rexec_aio(lang, code, stdin=None):
    if lang.lower() not in languages:
        raise UnknownLanguage("Unknown Language")

    data = {
        "LanguageChoice": languages.get(
            lang.lower()),
        "Program": code,
        "Input": stdin,
        "CompilerArgs": compiler_args.get(
            lang.lower())}

    async with aiohttp.ClientSession(raise_for_status=True) as session:
        response = await __fetch(session, "https://rextester.com/rundotnet/api", data)
        return RextesterResult(response.get("Result"),
                               response.get("Warnings"),
                               response.get("Errors"),
                               response.get("Stats"),
                               response.get("Files"))


class UnknownLanguage(Exception):
    pass


class RextesterResult(object):
    def __init__(self, results, warnings, errors, stats, files):
        self.results = results
        self.warnings = warnings
        self.errors = errors
        self.stats = stats
        self.files = files
