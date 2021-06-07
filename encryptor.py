import pyDes

def show_logo():
    print("""


    ____|  \  |  ___|  _ \\ \   /  _ \__ __| _ \   _ \  
    __|     \ | |     |   |\   /  |   |  |  |   | |   | 
    |     |\  | |     __ <    |   ___/   |  |   | __ <  
    _____|_| \_|\____|_| \_\  _|  _|     _| \___/ _| \_\ 
                                        @amaresh-git-dev

    """)

show_logo()
def choice():
    print("Enter your choice")
    print("[+] 1 for encryption")
    print("[+] 2 for decryption")

    option = input().strip()

    if option == '1':


        def img_encryptor(im_path, key):

            encryptor = pyDes.triple_des(
                key, pyDes.ECB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

            with open(im_path, 'rb') as im_file:

                image = im_file.read()

            encrypted_data = encryptor.encrypt(image)
            
            
            with open(f"{im_path.split('.')[0]}.{ext}", 'wb') as enc_file:
                enc_file.write(encrypted_data)


        if __name__ == '__main__':

            try:
                im_path = input(
                    r'Please enter the path and image name with extentiion of the image you want to encrypt : ')

                key = input(
                    "Please enter the encryption key, It must contain 24 characters and shouldn't have any spaces: ")

                if len(key.strip()) != 24 or ' ' in key.strip():
                    key = input(
                        "Invalid key... Please try again with a key with 24 characters and no spaces in it: ")

                key = bytes(str(key), encoding='utf-8')

                ext = input("Enter an extention: ")
                if not ext.strip():
                    ext = 'enc'


                try:
                    img_encryptor(im_path, key)
                    print(
                        f'Encrypting {im_path} with key {key.decode("utf-8")}, It may take several mins...')

                    
                    
                

                    print(
                        f"{im_path} encrypted successfully and stored as {im_path.split('.')[0]}.{ext}")
                except FileNotFoundError:
                    print("The file you have specified doesn't exist, Please try again with a valid file..")

            except KeyboardInterrupt:
                print("\nExiting...")
                exit()
            except Exception as e:
                print(f"\nSome error occurred, error detail: {e}")
        

    elif option == '2':

        def img_decryptor(enc_file_path, key, file_ext):

            decryptor = pyDes.triple_des(
                key, pyDes.ECB, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

            with open(enc_file_path, 'rb') as enc_file:
                encrypted_data = enc_file.read()
                decrypted_data = decryptor.decrypt(encrypted_data)

            with open(f"{enc_file_path.split('.')[0]}_decryptred.{file_ext}", 'wb') as img_file:
                img_file.write(decrypted_data)


        if __name__ == '__main__':

            try:
                enc_file_path = input(
                    r'Please enter the path of the file you want to decrypt: ')


                ext = input("Please enter the extension of the file before encryption(eg:- jpg, png the default is jpg hit enter if you want to go with it): ")

                if not ext.strip():
                    ext = 'jpg'

                key = input(
                    "Please enter the decryption key, It must contain 24 characters and shouldn't have any spaces: ")

                if len(key.strip()) != 24 or ' ' in key.strip():
                    key = input(
                        "Invalid key... Please try again with a key with 24 characters and no spaces in it: ")

                key = bytes(str(key), encoding='utf-8')

                try:
                    print(
                        f'Decrypting {enc_file_path} with key {key.decode("utf-8")}... It may take several mins.')

                    img_decryptor(enc_file_path, key, ext)

                    print(f"{enc_file_path} decrypted successfully and stored as {enc_file_path.split('.')[0]}_decrypted.{ext}")

                except FileNotFoundError:
                    print("The file you have specified doesn't exist, Please try again with a valid file..")
            except KeyboardInterrupt:
                print("\nExiting...")
                exit()
            except Exception as e:
                print(f"\nSome error occurred, error detail: {e}")
        
    else:
        print("INVALID choice.....", choice())

choice()
