import openai
import config
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = config.api_keys

    print("[bold blue]ChatGPT API en Python[/bold blue]")

    table = Table("Comando","Descripcion")
    table.add_row("salir","Salir de la aplicacion")
    table.add_row("new","Iniciar otra conversacion")
    print(table)

    context = config.context
    messages = [context]

    while True:

        content = __prompt()
        if content == "new":
            print(f"[bold blue]Nueva conversacion.[/bold blue]")
            messages=[context]
            content = __prompt()

        messages.append({"role":"user","content":content})

        response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
             messages=messages,
             temperature=2)
        response_content = response.choices[0].message.content

        messages.append({"role":"assistant","content":response_content})

        print(f"[bold blue]> [/bold blue] [green]{response_content}[/green]")

def __prompt() -> str:

        prompt = typer.prompt("\nEscribe tu pregunta: ")

        if prompt == "salir":
            exit = typer.confirm("Estas seguro?")
            if exit:
                print("!Hasta luego!")
                raise typer.Abort()
            return __prompt()
        
        return prompt


if __name__ == "__main__":
    typer.run(main)