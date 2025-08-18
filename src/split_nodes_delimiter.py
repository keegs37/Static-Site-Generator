from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        if "*" not in text and "_" not in text and "`" not in text and "**" not in text:
            raise Exception("No delimiter found in node {node}")

        
        start_index = text.find(delimiter)
        end_index = text.find(delimiter, start_index + len(delimiter))
            
        if end_index == -1:
            raise Exception(f'Closing delimiter "{delimiter}" not found')
            
        delimited_text = text[start_index: end_index + len(delimiter)]
        
        partitioned_text = text.partition(delimited_text)
        
        if delimiter == "**":
            new_nodes.append(TextNode(f'{partitioned_text[0]}', TextType.TEXT))
            new_nodes.append(TextNode(f'{partitioned_text[1][len(delimiter):len(partitioned_text[1]) - len(delimiter)]}', TextType.BOLD))
            new_nodes.append(TextNode(f'{partitioned_text[2]}', TextType.TEXT))
        
        elif delimiter == "_":
            new_nodes.append(TextNode(f'{partitioned_text[0]}', TextType.TEXT))
            new_nodes.append(TextNode(f'{partitioned_text[1][len(delimiter):len(partitioned_text[1]) - len(delimiter)]}', TextType.ITALIC))
            new_nodes.append(TextNode(f'{partitioned_text[2]}', TextType.TEXT))
        
        elif delimiter == "`":
            new_nodes.append(TextNode(f'{partitioned_text[0]}', TextType.TEXT))
            new_nodes.append(TextNode(f'{partitioned_text[1][len(delimiter):len(partitioned_text[1]) - len(delimiter)]}', TextType.CODE))
            new_nodes.append(TextNode(f'{partitioned_text[2]}', TextType.TEXT))

        
    return new_nodes    



