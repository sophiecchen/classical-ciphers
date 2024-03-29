Classical Ciphers
===========================
By Sophie Chen

This repository contains a collection classical ciphers.

| Cipher | Command to Run | Description |
| - | - | - |
| Caesar Cipher | `python3 caesar.py [-e\|-d] [shift] [message]` | Implements the Caesar cipher, a well-known substitution cipher that shifts each letter in the plaintext down the alphabet a fixed number of times. |
| Hill Cipher | `python3 hill.py [-e\|-d] [message]` | Implements the Hill cipher, a linear algebra-based polygraphic substitution cipher, for messages with a length multiple of 3 on a hard-coded key. |
| Vigenère Cipher | `python3 vigenere.py [-e\|-d] [key] [message]` | Implements the Vigenère cipher, a cipher that encodes each plaintext letter with a different Caesar cipher. |
