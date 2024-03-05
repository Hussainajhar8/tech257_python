# SSH Key Pair Generation and Configuration

## 1. Generate Key Pair

To generate an SSH key pair:
1. Change directory to `.ssh/`:
   ```bash
   cd ~/.ssh/
   ```
2. Use the following command to generate the key pair:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "mhussain@spartaglobal.com"
   ```

## 2. Copy Public Key to GitHub

After generating the key pair, copy the public key and add it to your GitHub account:
1. Display the contents of the public key:
   ```bash
   cat id_rsa.pub
   ```
2. Copy the displayed public key.
3. Proceed to GitHub and navigate to Settings.
4. Under Settings, find the option for Deploy keys.
5. Add the copied public key as a new SSH key. This allows GitHub to recognize your SSH key when you interact with repositories.

## 3. Create SSH Agent and Configure with Private Key

To configure SSH agent with the private key for GitHub access:
1. Create an SSH agent process:
   ```bash
   eval `ssh-agent`
   ```
2. Add the SSH key to the SSH agent:
   ```bash
   ssh-add ~/.ssh/<private_key_name>
   ```

## 4. Test Connection to GitHub

Once the SSH key pair is generated, added to GitHub, and SSH agent is configured, you can test the connection to GitHub:
```bash
git clone <SSH link to repo>
```

