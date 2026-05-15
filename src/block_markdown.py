def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        print(block)
        if not block:
            continue
        blocks.append(block.strip())

    return blocks
