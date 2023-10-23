from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Static, Button


class TimeDisplay(Static):
    pass


class Stopwatch(Static):
    def compose(self):
        yield Button('Start', id='start', variant='success')
        yield Button('Stop', id='stop', variant='error')
        yield Button('Reset', id='reset')
        yield TimeDisplay('00:00:00:00')


class StopwatchApp(App):
    CSS_PATH = 'stopwatch.tcss'
    BINDINGS = [('d', 'toggle_dark')]

    def compose(self):
        yield Header()
        yield Footer()
        yield ScrollableContainer(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self):
        self.dark = not self.dark


if __name__ == '__main__':
    app = StopwatchApp()
    app.run()
