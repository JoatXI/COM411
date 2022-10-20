from importlib.resources import path
import os

def run(cwd):
    print("Processing...")

    cwd = os.getcwd()
    print(f"The current working directory is: {cwd}")

    for file in os.listdir(cwd):
        print(f"The directory contains the following files: {file}")

run("Processing")

