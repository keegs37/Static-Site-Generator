def markdown_to_blocks(markdown):
    check_newlines = markdown.split("\n")
    
    i = 0
    while i + 1 < len(check_newlines):
        if check_newlines[i] == "" and check_newlines[i + 1] == "":
            del check_newlines[i]
            
           
        i += 1
    blocks = "\n".join(check_newlines)
    
    blocks = blocks.strip()
    blocks = blocks.split("\n\n")
     
    return blocks

