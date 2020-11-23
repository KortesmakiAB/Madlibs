"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        # f'{{<span>{val}</span>}}') # this works
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", f'<span>{val}</span>')

        return text



# instantiation
story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
    "Option-1"
)

story2 = Story(
    ["name", "place", "verb", "adjective", "plural_noun"],
    """There once was a man named {name} who lived in a {adjective} {place}. He loved to {verb} {plural_noun}.""",
    "Option-2"
)

stories = {"story1": story1, "story2": story2}