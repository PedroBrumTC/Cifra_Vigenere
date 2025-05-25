"""
    Arquivo que contem o codificador e o Decodificador.
    Importar esse arquivo para poder usar a cifra de Vigenere.
    Nele é possivel escolher entre usar a operação XOR (padrão) ou a adição
    para criptografar e descriptografar o arquivo. Lembre de manter 
    esse parametro igual para o criptografia e a descriptografia.
"""

def setKey(key: str, arq: str = "key.txt"):
    with open(arq, "w") as f:
        f.write(key)
    return

def setmsg(msg: str, arq: str = "input.txt"):
    with open(arq, "w") as f:
        f.write(msg)
    return

class Vigenere():

    def __init__(self, xor_or_add="add"):
        """
        Initializes the Vigenere cipher with options for bitwise operations and XOR or addition.
        :param xor_or_add: If "xor", uses XOR for encryption; if not "xor", uses addition.
        """
        self.xor = (xor_or_add == "xor")

    
    def cypher(self, input = "input.txt", output = "cypher.bin", arq_key = "key.txt"):
        """
        Encrypts a file using the Vigenere cipher.
        :param arquivo: Path to the file to be encrypted.
        :param key: Key to be used for encryption.
        :return: None
        """
        with open(input, 'rb') as f, open(arq_key, 'rb') as k:
            data = f.read()
            key = k.read()
            key_size = len(key)
            # key = key * (len(data) // len(key)) + key[:len(data) % len(key)]
        
        # Encrypt the data
        data = bytearray(data)
        key = bytearray(key)
        for i in range(len(data)):
            # XOR operation
            if self.xor:
                c = key[i%key_size]
                print(c)
                data[i] = (data[i] ^ key[i%key_size])
                    
            # Addition operation
            else:
                data[i] = (data[i] + key[i%key_size]) % 256


        
        with open(output, 'wb') as output_file:
            output_file.write(data)
        print(f"# Arquivo {input} cifrado com sucesso e salvo como {output}.")
            

    def decypher(self, input = "cypher.bin", output = "decypher.txt", arq_key = "key.txt"):
        """
        Decrypts a file using the Vigenere cipher.
        :param arquivo: Path to the file to be decrypted.
        :param key: Key to be used for decryption.
        :return: None
        """
        with open(input, 'rb') as f, open(arq_key, 'rb') as k:
            data = f.read()
            key = k.read()
            key_size = len(key)
            # key = key * (len(data) // len(key)) + key[:len(data) % len(key)]
        if key_size > 0:
            # Decrypt the data
            data = bytearray(data)
            key = bytearray(key)
            for i in range(len(data)):
                # XOR operation
                if self.xor:
                    data[i] = (data[i] ^ key[i%key_size])
                    
                # Addition operation
                else:
                    data[i] = (data[i] - key[i%key_size]) % 256

            
            with open(output, 'wb') as output_file:
                output_file.write(data)
            print(f"# Arquivo {input} decifrado com sucesso e salvo como {output}.")



if __name__ == "__main__":
    modo = input("Deseja usar XOR ou ADD para a cifra?").lower()
    if modo in ["xor", "add"]:
        codificador = Vigenere(xor_or_add=modo)
    else: 
        codificador = Vigenere(xor_or_add="add")

    criptografar = input("Deseja criptografar um arquivo? (y/n)").lower()
    if criptografar == "y":
        entradaC = input("Qual arquivo deseja criptografar? \n") 
        if entradaC == "":
            entradaC = "input.txt"
        saidaC = input("Como deseja salva-lo? \n")
        if saidaC == "":
            saidaC = "cypher.bin"

        codificador.cypher(input = entradaC, output = saidaC)
    
    descriptografar = input("Deseja descriptografar um arquivo? (y/n)").lower()
    if descriptografar == "y":
        entradaD = input("Qual arquivo deseja descriptografar? \n") 
        if entradaD == "":
            entradaD = "cypher.bin"
        saidaD = input("Como deseja salva-lo? \n")
        if saidaD == "":
            saidaD = "decypher.txt"

        codificador.decypher(input = entradaD, output = saidaD)
