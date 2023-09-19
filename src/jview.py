# ================================================
# JView is a simple utility program that takes any json file and converts it into a readable format. No more large, jumbled json files.
# ================================================
# Library and Module Imports
import string
from pathlib import Path

import file_utils
from file_utils import has_suffix
from file_utils import filter_keys

import typer
from typing_extensions import Annotated
from typing import Optional
from rich.console import Console
from rich.panel import Panel

# Typer App Decleration
app = typer.Typer()
err_console = Console(stderr=True)
notice_console = Console()

# Global Variables
DEF_EXT = ".txt"

# This function executes the program when passed.
@app.command()
def run(
    source_file: Annotated[
        Path, 
        typer.Argument
        (
            exists=True, 
            readable=True,
            file_okay=True,
            dir_okay=False,
            help="The path of the source file to convert. Must be a valid directory or file with extension .json."
        )
    ],
    new_file: Annotated
    [
        str, 
        typer.Argument(
            formats=str,
            help="The name of the new file created after processing. If ommited, the original file name is used.")
    ]
    = None,
    ):

    # Source_File Argument Conditions
    if source_file.suffix != ".json":
        err_console.print(Panel
            (
                f"The path {source_file} is not a valid json file. Please check the path and try again.", 
                title="Error", 
                title_align="left",
                border_style="red"
            ))
        raise typer.Exit()

    # New_File Argument Conditions
    if new_file == None:
        notice_console.print(Panel
            (
                "No new_file argument provided. Using original file name for new file.",
                title="Notice",
                title_align="left",
                border_style="yellow italic"
            ))
        new_file = source_file.name.split(".", -1)[0] + DEF_EXT
    
    elif has_suffix(new_file, "."):
        new_file = new_file.split(".", -1)[0] + DEF_EXT

    elif new_file.__contains__(".") == False:
        new_file = new_file + DEF_EXT

    # File Processing
    processFile(source_file, new_file)

    return print("All checks passed!")

def processFile(source_file: Path, new_file: str, criteria: Optional[str] = None):
    # Filters for criteria.
    if criteria == None:
        file_filter = lambda char: char == "a"

    # Open the file and read its contents into memory.
    with open(source_file, "r") as file:
        content = file.read()

    # Filter the contents based on criteria.
    filtered_content = filter_keys(content)
    print(filtered_content)

if __name__ == "__main__":
    app()