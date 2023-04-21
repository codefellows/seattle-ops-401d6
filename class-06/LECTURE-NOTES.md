# Lecture Notes: Data File Encryption and Hashing

In the previous class, we introduced encryption and hashing tools primarily concerned with data at rest. Today we'll explore why data in motion is critical to the security of an organization, and how we can protect it.

## Ops Challenge Demo - Symmetric Cryptography

Before you get into the Ops Challenge, be sure to define the terms used.

- A **cryptographic key** is a string of characters used within an encryption algorithm for altering plaintext into ciphertext data.
  - Like a physical key, it locks (encrypts) data. Only the right key can unlock (decrypt) it.

- **Symmetric key encryption** (also called symmetric cryptography) uses the same cryptographic key for the encryption of the plaintext and decryption of the ciphertext.

## Secure File Transmission

**Why**

- Data in motion presents its own set of concerns
  - Data confidentiality
    - PII, trade secrets, customer lists, key employee salaries, marketing strategies, source codes, etc. fall into the wrong hands.
  - Data integrity
    - Data remains unchanged
    - Or if changed, you can be made aware
  - Data source authenticity
    - The data actually came from who it claimed to
    - MITM attack

**What**

- What are the three types of data states?
  - "**Data at rest**—this state means that the data is in some sort of persistent storage media.
  - **Data in transit (or data in motion)** is the state when data is transmitted over a network.
  - Examples of types of data that may be in transit include website traffic, remote access traffic, data being synchronized between cloud repositories, and more. In this state, data can be protected by a transport encryption protocol, such as TLS or IPSec.
  - **Data in use (or data in processing)** is the state when data is present in volatile memory, such as system RAM or CPU registers and cache." -CompTIA
- What is a man-in-the-middle (MitM) attack?
  - A **MitM or on-path attack** is where the threat actor gains a position between two hosts, and transparently captures, monitors, and relays all communication between the hosts.
- How is a Man-in-the-Middle attack performed?
  - Sniffing
  - Packet capture
  - Packet alteration
  - MAC cloning
  - Examples: Wi-Fi eavesdropping, email hijacking, IP spoofing
- What are data transmission security protocols?
  - Transport Layer Security (TLS)
    - **TLS** is typically used with the HTTP application (referred to as HTTPS or HTTP Secure)
    - Can also be used to secure other application protocols and as a virtual private networking (VPN) solution.
    - Versions 1.3, 1.2, 1.1. 1.0
  - Downgrade attack
    - A **downgrade attack** is when a man-in-the-middle tries to force the use of a weak cipher suite and SSL/TLS version.
    - TLS 1.3 is impervious to downgrade attack.
  - **File Transfer Protocol (FTP)** facilitates the transfer of files between hosts.
    - Uses TCP/IP.
    - Username/password authentication. Credentials sent in cleartext.
    - Connection established on TCP port 21.
  - **Secure File Transfer Protocol (SFTP)** facilitates the secure transfer of files between hosts.
    - Uses SSH.
    - Username/password authentication. Credentials encrypted.
    - Connection established on TCP port 22.
- What other data-in-motion security protocols are there?
  - IPsec
  - SSL, TLS
  - Email
    - Secure SMTP (SMTPS)
      - Uses implicit TLS
    - Secure POP (POP3S)
      - Secured version of POP
      - Uses TCP port 995
    - Secure IMAP (IMAPS)
      - IMAP4 supports permanent connections to server
      - Multiple concurrent connections
