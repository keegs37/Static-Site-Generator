from textnode import TextType, TextNode

def main():
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)
    


if __name__ == "__main__":
    main()