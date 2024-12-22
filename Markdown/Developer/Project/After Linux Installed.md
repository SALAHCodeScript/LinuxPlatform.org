# Ubuntu
### 1. Customize Linux:
##### Change your settings and theme as you like.
### 2. Update:
##### Check for a new updates in .
```bash
sudo apt update -y
sudo apt upgrade -y
```
### 3. Install Drivers:
##### Verfiy if there is drivers to download in driver manager.
### 4. Install Packages:
##### Tools:
```bash
sudo apt install -y curl git zsh neovim tmux bat tree xclip fzf yt-dlp
```
##### Networks:
```bash
sudo apt install -y nmap traceroute openssh-server
```
##### Programming Languages:
```bash
sudo apt install -y build-essential nasm mysql-server mysql-client sqlite3 nodejs npm default-jdk php apache2 ruby-full docker.io perl yara jq
```
### 5. Switch to ZSH Shell:
##### 
```bash
sudo chsh -s $(which zsh)
```
### 6. Restart Linux:
##### Reboot your system to display the changes.
```bash
sudo apt reboot now
```
### 7. Improve ZSH Shell:
##### Oh My Zsh Installation:
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
##### Install Powerlevel10k:
```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```
##### Install Plugins:
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
sudo apt install command-not-found
git clone https://github.com/zsh-users/zsh-history-substring-search $ZSH_CUSTOM/plugins/zsh-history-substring-search
```
##### Edit .zshrc File:
```bash
# Enable Powerlevel10k Theme
ZSH_THEME="powerlevel10k/powerlevel10k"

# Plugins
plugins=(
  git                       # Helpful Git commands and shortcuts
  zsh-syntax-highlighting   # Syntax highlighting for better readability
  zsh-autosuggestions       # Suggestions based on previous commands
  command-not-found         # Suggests commands when a typo is made
  history                   # Better history management
)
```
### 8. Get PowerShell:
##### Install Powershell:
```bash
sudo apt install -y wget apt-transport-https software-properties-common
wget -q "https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb"
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install -y powershell
```
##### Install Oh My Posh:
```bash
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O oh-my-posh
chmod +x oh-my-posh
sudo mv oh-my-posh /usr/local/bin/
```
##### Install Themes:
```bash
mkdir ~/.poshthemes
wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip
unzip themes.zip -d ~/.poshthemes
chmod u+rw ~/.poshthemes/*.json
```
##### Edit $PROFILE File:
```bash
oh-my-posh init pwsh | Invoke-Expression
oh-my-posh init pwsh --config ~/.poshthemes/paradox.omp.json | Invoke-Expression
```
### 9. Get Python:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.13
python3.13 -m ensurepip --upgrade
```
### 10. Install Programs:
##### Google Chrome
##### VSCode
##### Gimp
##### Godot 3.6
##### TLauncher
##### Ventoy
### 11. Get your Data:
##### Copy your data from your flash disk to your linux system.

