# Lecture Notes: Protecting Data at Rest with Device Encryption


## Topic 1: Cryptography Fundamentals

- **Why** (5 min)
  - Let's make sure we cover cryptography basic concepts to ensure we're ready for certification exams.
- **What** (10 min)
  - Ciphers: Algorithms used for encryption or decryption
  - Classical Ciphers
    - Substitution Cipher: Plaintext substituted for ciphertext
    - Transposition Cipher: Plain text rearranged to form ciphertext
  - Key-based
    - Key-based
      - Symmetric key algorithm
        - Uses only one key for both encryption and decryption.
      - Asymmetric key algorithm
        - Requires two keys, one for encryption and one for decryption.
    - Input-based
      - Block cipher
        - Groups data into blocks instead of bits
        - Simpler than stream cipher
      - Stream cipher
        - Start with a secret key
        - Combines the stream with plaintext to produce ciphertext


## Topic 2: Ransomware

- **Why** (5 min)
  - Why is ransomware so prolific?
    - Easy way for cyber-criminals to profit
- **What** (10 min)
  - What is ransomware?
    - Type of malware that upon execution will encrypt sectors of the targeted file server or hard disk
    - Key belongs only to the ransomware creator
- **How** (30 min)
  - How to defend against it?
    - US Dept. of the Treasury released a [statement](https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_10012020_1.pdf) on Oct 1 2020
      - Payments to nation state actors may incur legal liability on the ransomware victim
    - Increase data availability by securely backing up important data to an outside location
  - How is ransomware created?
    - Ref. to today's Ops Challenge


## Topic 3: Rootkits

- **Why** (5 min)
  - Why are rootkits so dangerous?
    - Designed to obscure system compromise
    - They replace or substitute administrator utilities and capabilities with modified versions that hide malicious activity
    - Designed to provide back doors for the attacker to use later

- **What** (5 min)
  - What are rootkits?
    - Rootkits are a collection of software put in place by an attacker that is designed to obscure system compromise
    - Types:
      - Hypervisor: these rootkits modify the boot sequence of the host system to load a VM as the host OS
      - Hardware (firmware): hide in hardware devices or firmware
      - Boot loader: replace the boot loader with one controlled by the attacker
      - Application: directed to replace valid application files with Trojan binaries. Work inside an application and change the application's behavior, user rights and actions.
      - Kernel: attacks the boot sectors and kernel level of the OS itself, replacing kernel code with back-door code.
        - These are the most dangerous ones
      - Library: use system-level calls to hide their existence
    - Examples:
      - Horsepill
      - Grayfish
      - Sirefef
      - Azazel
      - ZeroAccess

## Topic 4: Protecting Data at Rest with Device Encryption

- **Why** (5 min)
- Why is encrypting data at rest helpful?
  - Protects data confidentiality in event of data theft
    - Great for defending sensitive data
  - Many organizations require all hard disks to be encrypted

- **What** (10 min)
- What does encrypting data at rest do?
  - Scrambles data, increasing confidentiality

- What is full disk encryption (FDE)?
  - Encryption of *all* data stored on a disk.
  - Objective is to maintain data confidentiality.

- What is BitLocker? Ref. [BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
  - "BitLocker Drive Encryption is a data protection feature that integrates with the operating system and addresses the threats of data theft or exposure from lost, stolen, or inappropriately decommissioned computers.
  - BitLocker provides the most protection when used with a Trusted Platform Module (TPM) version 1.2 or later. The TPM is a hardware component installed in many newer computers by the computer manufacturers. It works with BitLocker to help protect user data and to ensure that a computer has not been tampered with while the system was offline."
  - Show [screenshot of TPM chip setting in BIOS](https://forumscdn.lenovo.com/old_attach/116128iB2B4695756F7AFCE.jpg)

- What is LUKS?
  - Pull up [official LUKS Gitlab](https://gitlab.com/cryptsetup/cryptsetup/blob/master/README.md)
  - Linux Unified Key Setup is a disk encryption specification created in 2004 intended for Linux OS.
  - Provides a common standard for Linux hard disk encryption
  - Benefits
    - Compatibility via standardization
    - Secure against low entropy attacks
    - Support for multiple keys
    - Effective passphrase revocation
    - Free
  - Platform independent standard applied, making LUKS useful on different programs
  - Uses enhanced version of `cryptsetup` with `dm-crypt` on the backend for disk encryption

- What is eCryptfs?
  - Linux stacked file system, NOT a FDE solution
  - Useful for non-FDE encryption needs over entire directories in Linux
  - Capable of creating encrypted directory and mounting it on any directory
  - Stores cryptographic metadata on file headers

# Lecture Notes: Ops Challenge 07

## Python os.walk()

- OS.walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.
- For each directory in the tree rooted at directory top (including top itself), yields a 3-tuple (dirpath, dirnames, filenames)
  - **root**: Prints out directories only from what you specified
  - **dirs**: Prints out sub-directories from root
  - **files**: Prints out all files from root and directories

**Example**

```python
# Driver function
import os

if __name__ == "__main__":
  for (root,dirs,files) in os.walk('.', topdown=True):
    print(root)
    print(dirs)
    print(files)
    print('--------------------------------------------')
```
