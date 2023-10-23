import sys


def getOptions():
    # get options from arguments supplied
    arguments = sys.argv[1:]
    return list(filter(lambda x: x.startswith("-"), arguments))


def getFileName():
    # get filename form arguments
    arguments = sys.argv[1:]
    return (
        arguments[-1]
        if len(arguments) > 0 and not arguments[-1].startswith("-")
        else None
    )


def readInput(filename=None):
    #read input as bytes from file supplied for the stdin
    if filename:
        try:
            with open(filename, "rb") as file:
                input_data = file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return
    else:
        input_data = bytes(sys.stdin.read(), "utf-8")
    return input_data


if __name__ == "__main__":
    options = getOptions()
    options = options if len(options) > 0 else ["-l", "-w", "-c"]
    inputInBytes = readInput(getFileName())
    for option in options:
        match option:
            # count bytes
            case "-c":
                byteCount = len(inputInBytes)
                print(f"Byte count : {byteCount}")
            # count characters
            case "-m":
                charCount = len(inputInBytes.decode("utf-8"))
                print(f"Character count : {charCount}")
            # count lines
            case "-l":
                lineCount = len(inputInBytes.decode("utf-8").split("\n"))
                lineCount = lineCount - 1 if lineCount > 0 else 0
                print(f"Line count : {lineCount}")
            # count words
            case "-w":
                wordCount = len(inputInBytes.decode("utf-8").split())
                print(f"Word count : {wordCount}")
