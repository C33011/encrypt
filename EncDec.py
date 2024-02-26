import tkinter as tk
from cryptography.fernet import Fernet

class FileEncryptorDecryptor:
    def __init__(self):
        self.key = None

    def generate_key(self):
        self.key = Fernet.generate_key()

    def encrypt(self, plaintext):
        if not self.key:
            raise ValueError("Key not generated")
        cipher_suite = Fernet(self.key)
        return cipher_suite.encrypt(plaintext.encode())

    def decrypt(self, ciphertext):
        if not self.key:
            raise ValueError("Key not generated")
        cipher_suite = Fernet(self.key)
        return cipher_suite.decrypt(ciphertext).decode()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("File Encryptor/Decryptor")

        self.file_handler = FileEncryptorDecryptor()

        self.input_label = tk.Label(master, text="Enter Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.grid(row=0, column=1, padx=5, pady=5)

        self.output_label = tk.Label(master, text="Output:")
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.output_text = tk.Text(master, height=5, width=50, state="disabled")
        self.output_text.grid(row=1, column=1, padx=5, pady=5)

        self.key_label = tk.Label(master, text="Enter Key:")
        self.key_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.key_entry = tk.Entry(master, show="*")
        self.key_entry.grid(row=2, column=1, padx=5, pady=5)

        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, padx=5, pady=5)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=3, column=1, padx=5, pady=5)

    def encrypt(self):
        plaintext = self.input_text.get("1.0", "end-1c")
        try:
            self.file_handler.generate_key()
            ciphertext = self.file_handler.encrypt(plaintext)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", ciphertext.decode())
            self.output_text.config(state="disabled")
            self.key_entry.delete(0, "end")
            self.key_entry.insert(0, self.file_handler.key.decode())
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def decrypt(self):
        ciphertext = self.input_text.get("1.0", "end-1c")
        key = self.key_entry.get()
        try:
            self.file_handler.key = key.encode()
            plaintext = self.file_handler.decrypt(ciphertext.encode())
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", plaintext)
            self.output_text.config(state="disabled")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
