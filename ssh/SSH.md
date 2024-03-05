# Research on SSH

SSH (Secure Shell) is a cryptographic network protocol that allows secure communication between two computers over an unsecured network.
It provides a secure channel for data exchange and remote command execution.

## What is SSH?

SSH stands for Secure Shell or Secure Socket Shell. It provides a secure way to access and manage remote devices or servers securely over a network.
SSH encrypts data during transmission, preventing unauthorized access to sensitive information.

![img_1.png](img_1.png)

## Why Use SSH Over HTTPS?

While HTTPS (Hypertext Transfer Protocol Secure) also provides secure communication over the internet, SSH offers several advantages:
- SSH encrypts the entire communication session, including the authentication process, whereas HTTPS only encrypts the data being transmitted.
- SSH supports key-based authentication, which eliminates the need to enter passwords and provides stronger security.
- SSH is more suitable for remote server administration and secure file transfer protocols like SCP (Secure Copy Protocol) and SFTP (SSH File Transfer Protocol).

## Creating an SSH Key Pair

To create an SSH key pair, follow these steps:
1. Open a terminal or command prompt.
2. Use the `ssh-keygen` command to generate a new SSH key pair.
Here is an example of a command to create a key pair for SSH:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
3. Follow the prompts to specify the file location and passphrase .

## Best Practices When Using/Implementing SSH
- Use Strong Passphrases: If you choose to use a passphrase for your SSH key pair, ensure it is strong and unique.
- Protect Private Keys: Store private keys securely and avoid sharing them with unauthorized users.
- Disable Root Login: Disable direct root login via SSH to enhance security.
- Update Regularly: Keep SSH software and configurations up to date, rotate and audit keys.
- Use Two-Factor Authentication (2FA): Implement 2FA for SSH authentication for an added layer of security.
- Monitor SSH Logs: Regularly monitor SSH logs for suspicious activities and unauthorized access attempts.

