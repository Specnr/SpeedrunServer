import sys


def update_properties(seed):
    with open("./server.properties", "r+") as file:
        lines = []
        for line in file:
            if line.startswith("level-seed"):
                line = f"level-seed={seed}\n"
            lines.append(line)
        file.seek(0)
        file.writelines(lines)
        file.truncate()


if __name__ == "__main__":
    update_properties(sys.argv[1] if len(sys.argv) >= 2 else "")
