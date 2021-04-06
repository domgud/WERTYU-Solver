from converter import Converter

rows = [['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\''],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']]

# input = "O S, GOMR YPFSU/"
input = "O S, YJR [OVL;R"
converter = Converter(rows)
result = converter.convert(input)

print(f"Input text: {input}")
print(f"Output text: {result}")