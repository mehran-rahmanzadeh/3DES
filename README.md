## 3DES Encryption/Decryption in Pure Python

This project demonstrates a pure-Python implementation of the 3DES (Triple DES) algorithm, along with a single-DES module.

### Project structure

* **DES** (`scripts/des.py`): Implements the classic DES block cipher:

  1. Initial Permutation
  2. 16× rounds of the mangler function
  3. Swap halves
  4. Final Permutation

  For each of the 16 rounds, we:

  * Generate a 48-bit subkey (Choice-1 permute, rotate, Choice-2 permute)
  * Expand 32 bits to 48 bits
  * XOR with the subkey
  * Substitute via S-boxes (48 → 32 bits)
  * Permute (transposition)
  * XOR with the left half
  * Swap halves at the end of all rounds

* **3DES** (`scripts/triple_des.py`): Wraps the DES module into the Triple-DES (E‑D‑E) sequence:

  1. Encrypt with key 1
  2. Decrypt with key 2
  3. Encrypt with key 3

  You can pass the **same** key for all stages (classic DES), **two** distinct keys (112-bit security), or **three** distinct keys (168-bit keying). Padding is optional to handle data not aligned to 8-byte blocks.

* **Example** (`main.py`): Shows how to encrypt and decrypt a sample message.

### Operation mode

* **ECB Mode**: Basic mode for block-by-block.

### Getting Started

1. **Clone this repo**

   ```bash
   git clone https://github.com/mehran-rahmanzadeh/3DES.git
   cd 3DES
   ```
2. **Run the example**

   ```bash
   python3 main.py
   ```

   You should see a 3 sample scenarios, same key for all 3 stages, 2 duplicated keys and 1 different key, 3 unique keys for all the stages.

### Usage

In `main.py`, you’ll find code like:

```python
from scripts.triple_des import encrypt, decrypt

PADDING = True
plaintext = b"Hello I'm mehran and here is my secret message"
key1 = b'0123456789ABCDEF'
key2 = b'23456789ABCDEF01'
key3 = b'3456789ABCDEF012'
ct = encrypt(plaintext, key1, key2, key3,padding=PADDING)
print('Ciphertext:', ct.hex().upper())
pt = decrypt(ct, key1, key2, key3, padding=PADDING)
print('Decrypted:', pt)
```
