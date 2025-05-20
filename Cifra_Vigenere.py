"""
    Arquivo que contem o codificador e o Decodificador.
    Importar esse arquivo para poder usar a cifra de Vigenere.
    Nele é possivel escolher entre usar a operação XOR (padrão) ou a adição
    para criptografar e descriptografar o arquivo. Lembre de manter 
    esse parametro igual para o criptografia e a descriptografia.
"""



class Vigenere():

    def __init__(self, xor_or_add="xor"):
        """
        Initializes the Vigenere cipher with options for bitwise operations and XOR or addition.
        :param xor_or_add: If "xor", uses XOR for encryption; if not "xor", uses addition.
        """
        self.xor = (xor_or_add == "xor")

    
    def encrypt(self, arq_text, arq_key = "key.txt"):
        """
        Encrypts a file using the Vigenere cipher.
        :param arquivo: Path to the file to be encrypted.
        :param key: Key to be used for encryption.
        :return: None
        """
        with open(arq_text, 'rb') as f, open(arq_key, 'rb') as k:
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
                data[i] = (data[i] ^ key[i%key_size])
                    
            # Addition operation
            else:
                data[i] = (data[i] + key[i%key_size]) % 256


        arq = arq_text.split(".")
        nome = arq[0] + "_cifrado" + "." + "bin"
        with open(nome, 'wb') as output_file:
            output_file.write(data)
        print(f"# Arquivo {arq_text} cifrado com sucesso e salvo como {nome}.")
            

    def decrypt(self, arq_crypt, arq_key = "key.txt"):
        """
        Decrypts a file using the Vigenere cipher.
        :param arquivo: Path to the file to be decrypted.
        :param key: Key to be used for decryption.
        :return: None
        """
        with open(arq_crypt, 'rb') as f, open(arq_key, 'rb') as k:
            data = f.read()
            key = k.read()
            key_size = len(key)
            # key = key * (len(data) // len(key)) + key[:len(data) % len(key)]
        
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

        arq = arq_crypt.split(".")
        nome = "_".join(arq[0].split("_")[:-1]) + "_decifrado" + "." + "txt"
        with open(nome, 'wb') as output_file:
            output_file.write(data)
        print(f"# Arquivo {arq_crypt} decifrado com sucesso e salvo como {nome}.")
        
if __name__ == "__main__":
    codificador = Vigenere(xor_or_add="xor")
    print()
    print("#" * 100)
    arquivo = "Dom_Casmurro.txt"
    codificador.encrypt(arquivo)
    
    arquivo = "Dom_Casmurro_cifrado.bin"
    codificador.decrypt(arquivo)
    print("#" * 100)
    print()
    with open("Dom_Casmurro.txt", 'rb') as f_original, open("Dom_Casmurro_decifrado.txt", 'rb') as f_decifrado:
        f_decifrado = f_decifrado.read()
        f_original = f_original.read()
        if f_decifrado == f_original:
            print("O arquivo decifrado é igual ao arquivo original.\n")
        else:
            print("O arquivo decifrado é diferente do arquivo original.\n")
