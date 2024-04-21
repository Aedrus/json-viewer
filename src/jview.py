# ================================================
# JView is a simple utility program that takes any json file and converts it into a readable format. No more large, jumbled json files.
# ================================================
# Library and Module Imports
from pathlib import Path
from enum import Enum
from typing import Optional

import typer
from typing_extensions import Annotated
from rich.console import Console
from rich.panel import Panel

from utils import file_utils as utils

# Global Variables & Structures
DEFAULT_EXTENSION = ".txt"
FALLBACK_FILE_NAME = "converted_file"

# Typer App Declerations
app = typer.Typer()
err_console = Console(stderr=True)
notice_console = Console()

# Class Definitions
class FormatTypes(Enum):
    """Enumations for the type of data being pulled from source_file."""
    PROPERTIES = "properties"
    VALUES = "values"
    BOTH = "both"

# This function executes the program when passed.
@app.command()
def main(
    source_file: Annotated
        [
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
            typer.Argument
            (
                formats=str,
                help="The name of the new file created after processing. If ommited, the original file name is used."
            )
        ]
    = None,
    format: Annotated
        [
            FormatTypes,
            typer.Argument
            (
                help="The format of the new file. Dictates what JSON data will be written to the new file."
            )
        ]
        = "both",
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
        new_file_choice = input("Do you want to use the original file name for the converted file? (y/n): ")
        if new_file_choice == "y":
            notice_console.print(Panel
                (
                    "No new_file argument provided. Using original file name for converted file.",
                    title="Notice",
                    title_align="left",
                    border_style="yellow italic"
                ))
            new_file = source_file.name.split(".", -1)[0] + DEFAULT_EXTENSION
        else:
            notice_console.print(Panel
                (
                    "No new_file argument provided. Using fallback file name for converted file.",
                    title="Notice",
                    title_align="left",
                    border_style="yellow italic"
                ))
            new_file = FALLBACK_FILE_NAME + DEFAULT_EXTENSION

    elif utils.has_duplicates(new_file, "."):
        err_console.print(Panel
            (
                f"The new_file argument {new_file} has an invalid or duplicate extension. Please check the argument and try again.", 
                title="Error", 
                title_align="left",
                border_style="red"
            ))
        raise typer.Exit()

    elif new_file.endswith("."):
        new_file = new_file.split(".", -1)[0] + DEFAULT_EXTENSION

    elif new_file.__contains__(".") == False:
        new_file = new_file + DEFAULT_EXTENSION

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
    filtered_content = utils.filter_keys(content)
    print(filtered_content)

if __name__ == "__main__":
    app()