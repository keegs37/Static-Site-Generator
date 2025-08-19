from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        # Only raise if delimiter is missing and text is not empty
        if delimiter not in text and text != "":
            raise Exception(f"No delimiter '{delimiter}' found in node {node}")

        while True:
            start_index = text.find(delimiter)
            if start_index == -1:
                if text != "":
                    new_nodes.append(TextNode(text, TextType.TEXT))
                break

            end_index = text.find(delimiter, start_index + len(delimiter))
            if end_index == -1:
                raise Exception(f'Closing delimiter "{delimiter}" not found')

            if start_index > 0:
                new_nodes.append(TextNode(text[:start_index], TextType.TEXT))
            

            inner_text = text[start_index + len(delimiter):end_index]
            new_nodes.append(TextNode(inner_text, text_type))
            text = text[end_index + len(delimiter):]
            
    return new_nodes









