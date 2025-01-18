def ceaser(original_text, shift_amount, decode_or_encode):
    cypher_text = ""
    if decode_or_encode == "encode":
        for letter in original_text:
            if letter not in alphabet:
                cypher_text += letter
            else:
                shifted_index = (alphabet.index(letter) + shift_amount)%(len(alphabet))
                cypher_text += alphabet[shifted_index]
    elif decode_or_encode == "decode":
        for letter in message:
            if letter not in alphabet:
                cypher_text += letter
            else:
                shifted_index = (alphabet.index(letter) - shift_amount)%(len(alphabet))
                decrypted_text += alphabet[shifted_index]
    print(f"Here is the encoded result {cypher_text}")



game_continue = False
while not game_continue:
    alphabet = ['a', 'b', 'c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encyript or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))
    ceaser(text, shift, direction)
    continues = input("Do you want to continue to play: 'yes' or 'no: '")
    if continues == "no":
        game_continue = True