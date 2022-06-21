from tokens import Token

def print_tokens(tokens : list[Token]):
    for token in tokens:
        print(f"{token.loc} {token.type.name} {token.value}")