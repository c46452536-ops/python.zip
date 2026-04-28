from rich.console import Console
from rich.prompt import Prompt
from engine import highlight

console = Console()

def repl():
    console.print("[green]Python REPL[/green] (type exit)")

    while True:
        code = Prompt.ask(">>> ")

        if code == "exit":
            break

        try:
            console.print(highlight(code))
            result = eval(code, {})

            if result is not None:
                console.print(result)

        except Exception:
            try:
                exec(code, {})
            except Exception as e:
                console.print(f"[red]{e}[/red]")
