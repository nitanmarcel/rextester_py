import aiohttp

from rextester_py.langs import languages


async def __fetch(session, url, data):
    async with session.get(url, data=data) as response:
        return await response.json()


async def rexec(lang, code, stdin):
    if lang.lower() not in languages:
        raise UnknownLanguage("Unknown Language")

    data = {
        "LanguageChoice": languages[lang.lower()],
        "Program": code,
        "Input": stdin}

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
