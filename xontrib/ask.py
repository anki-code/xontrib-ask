"""
TODO: Please add here the short description of the xontrib to show in `xonfig web`.
"""
from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.completion import Completer, Completion
from xonsh.built_ins import XSH


__all__ = ()

class DynamicCompleter(Completer):
    def get_completions(self, document, complete_event):
        current_input = document.text

        for f in Path('.').glob('*'):
            fname = str(f)
            if fname.lower().startswith(current_input.lower()):
                yield Completion(str(f), start_position=-len(current_input))


class Ask:
    def get_list(self):
        return [str(f) for f in Path('.').glob('*')] + [str(f) for f in Path('..').glob('*')]

    def show_list_and_choose(self, title, options=None):
        title = title.strip() + ': '
        options = self.get_list()
        if options is None:
            completer = DynamicCompleter()
        else:
            completer = WordCompleter(options, ignore_case=True)

        choice = prompt(title, completer=completer, complete_while_typing=True)

        if choice in options:
            return choice
        else:
            print("Invalid choice, please try again.")
            return self.show_list_and_choose()

    def __call__(self, *a, **kw):
        return self.show_list_and_choose(*a, **kw)


ask = Ask()
