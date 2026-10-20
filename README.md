# Xiaomi Router Patcher (XMiR-Patcher)

[![Download latest](https://img.shields.io/badge/🡇-Download%20latest-green)](https://github.com/sandro-defender/Xiaomi-Router-patcher/archive/refs/heads/main.zip)
![ViewCount](https://views.whatilearened.today/views/github/sandro-defender/Xiaomi-Router-patcher.svg)
[![Official legacy firmware download](https://img.shields.io/badge/📦-Official%20legacy%20firmware-blue)](https://mirom.ezbox.idv.tw/en/miwifi)

A powerful firmware patching tool for Xiaomi routers that supports exploiting known vulnerabilities, enabling SSH, installing language packs, flashing firmware, and more for a wide range of Xiaomi router models.

## 📋 Table of Contents

- [Supported Devices](#supported-devices)
- [Features](#features)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Detailed Feature Description](#detailed-feature-description)
- [Troubleshooting](#troubleshooting)
- [Security Notes](#security-notes)
- [Development](#development)
- [Contributing](#contributing)

## 🔧 Supported Devices

### Fully Supported Models
This tool supports the following Xiaomi router models (sorted by model ID):

#### 1st Generation Series
- **R1CM** (miwifi-mini) - Xiaomi Router Mini
- **R1CL** (miwifi-nano) - Xiaomi Router Nano
- **R2D** - Xiaomi Router 2
- **R2CM** - Xiaomi Router 2

#### 3rd Generation Series
- **R3** - Xiaomi Router 3
- **R3D** (r3d) - Xiaomi Router 3D
- **R3L** (miwifi-3c) - Xiaomi Router 3C
- **R3P** (mi-router-3-pro) - Xiaomi Router 3 Pro
- **R3A** - Xiaomi Router 3A
- **R3G** (mi-router-3g) - Xiaomi Router 3G
- **R3GV2** (mi-router-3g-v2) - Xiaomi Router 3G V2

#### 4th Generation Series
- **R4** (mi-router-4) - Xiaomi Router 4
- **R4C** (mi-router-4q) - Xiaomi Router 4Q
- **R4A** (mi-router-4a-gigabit) - Xiaomi Router 4A Gigabit Edition
- **R4CM** (mi-router-4c) - Xiaomi Router 4C
- **R4AC** (mi-router-4a-100m) - Xiaomi Router 4A 100M Edition

#### AC Series
- **R2100** (mi-router-ac2100) - Xiaomi Router AC2100
- **RM2100** (redmi-router-ac2100) - Redmi Router AC2100
- **R2200** - Xiaomi Router AC2200
- **R2350** (aiot-ac2350) - Xiaomi AIoT Router AC2350
- **R2600** - Xiaomi Router AC2600

#### AX Series (Wi-Fi 6)
- **R3600** (ax3600) - Xiaomi Router AX3600
- **R1350** - Xiaomi Router AX1350
- **RA67** - Redmi Router AX1800C
- **RA69** (ax6) - Xiaomi Router AX6
- **RA70** (ax9000) - Xiaomi Router AX9000
- **RA71** - Redmi Router AX1800
- **RA72** - Xiaomi Router AX6000
- **RA75** (mi-ra75) - Xiaomi Router RA75
- **RA80/RA82** - Xiaomi Router AX3000

#### Enterprise Series
- **CR6006** (mi-router-cr6606) - Xiaomi Enterprise Router CR6606
- **CR6008** (mi-router-cr6608) - Xiaomi Enterprise Router CR6608
- **CR6009** (mi-router-cr6609) - Xiaomi Enterprise Router CR6609

#### TR Series
- **TR608** - Xiaomi Router TR608
- **TR609** - Xiaomi Router TR609

#### Other Models
- **P01** - Xiaomi Portable Router
- **D01** - Xiaomi Router HD
- **IR1200G** - Xiaomi Router 1200G
- **RM1800** - Redmi Router 1800
- **R2100D** - Xiaomi Router AC2100D
- **RA50** - Xiaomi Router RA50

> **Note**: Feature support may vary by model. Please read the relevant instructions carefully before proceeding.

## ✨ Features

### Core Features
- 🔓 **Exploit**: Automatically detect and exploit known Xiaomi router vulnerabilities
- 🔑 **SSH Enable**: Permanently enable SSH access for advanced management
- 🌐 **Multi-language Support**: Install English / Russian / Chinese language packs with English menu interface
- 💾 **Full Backup**: Create a complete backup of the router firmware
- 🔄 **Firmware Flashing**: Install custom firmware
- ⚡ **Bootloader Replacement**: Install third-party bootloaders such as Breed

### Advanced Features
- 📊 **Device Info Reading**: Retrieve detailed hardware and system information
- 🔐 **Password Change**: Change the router root password
- 📋 **Log Reading**: Read system logs and kernel messages
- ⚙️ **Partition Backup**: Create backups of specific partitions
- 🚀 **Boot Settings**: Set kernel boot address
- 🔧 **Feature Unlock**: Unlock hidden router features

## 🚀 Installation

### Windows Users

1. **Download the bundle**
   ```
   Download and extract the project files to any directory
   ```

2. **Run the tool**
   ```
   Double-click run.bat
   ```

3. **Automatic environment setup**
   - The tool uses the bundled Python environment automatically
   - No manual Python or dependency installation required

### Linux / macOS Users

1. **System requirements**
   ```bash
   # Make sure Python 3.8+ and OpenSSL are installed
   python3 --version  # should show 3.8 or higher
   openssl version    # confirm OpenSSL is installed
   ```

2. **Install dependencies**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install python3 python3-pip python3-venv openssl
   
   # CentOS/RHEL
   sudo yum install python3 python3-pip openssl
   
   # macOS (using Homebrew)
   brew install python3 openssl
   ```

3. **Download and run**
   ```bash
   # Clone the project
   git clone https://github.com/sandro-defender/Xiaomi-Router-patcher.git
   cd Xiaomi-Router-patcher
   
   # Run the tool
   chmod +x run.sh
   ./run.sh
   ```

### Docker Users

```bash
# Build Docker image
docker build -t xmir-patcher .

# Run container
docker run -it --network host xmir-patcher
```

## 📖 Usage Guide

### Step 1: Prepare Connection

1. **Network connection**
   - Make sure your computer and Xiaomi router are on the same network
   - Note the router's IP address (usually 192.168.31.1)
   - Ensure you can access the router admin panel normally

2. **Launch the tool**
   - Windows: double-click `run.bat`
   - Linux/macOS: run `./run.sh`

### Step 2: Basic Configuration

After launching, you will see the main menu:

```
==========================================================

Xiaomi MiR Patcher  

 1 - Set IP-address (current value: 192.168.31.1)
 2 - Connect to device (install exploit)
 3 - Read full device info
 4 - Create full backup
 5 - Install EN/RU languages
 6 - Install permanent SSH
 7 - Install firmware (from directory "firmware")
 8 - {{{ Other functions }}}
 9 - Change language
 10 - [[ Reboot device ]]
 0 - Exit

Select:
```

### Step 3: Perform Operations

#### Required First Steps

1. **Set IP Address (Option 1)**
   ```
   Select 1 → Enter router IP address → Press Enter to confirm
   ```

2. **Connect Device and Install Exploit (Option 2)**
   ```
   Select 2 → The tool will automatically detect the device model and install the appropriate exploit
   ```
   
   > ⚠️ **Important**: This is a prerequisite for all subsequent operations. This step must succeed first!

#### Common Workflows

1. **Full Backup (highly recommended first)**
   ```
   Select 4 → The tool will create a complete firmware backup saved in the backup directory
   ```

2. **Enable SSH Access**
   ```
   Select 6 → The tool will permanently enable SSH access, default credentials: root/root
   ```

3. **Install Language Pack**
   ```
   Select 5 → Install English/Russian/Chinese language packs to add more languages to the router UI
   ```

#### Language Settings

On the first launch, the language selection menu is shown:
```
Language

 1 - English
 2 - Chinese
 3 - Russian

Select language [1-English, 2-Chinese, 3-Russian]: 
```

Enter the corresponding number to switch to that menu language. The language setting is saved in `config.json`.

**English Interface Preview**:
```
==========================================================

Xiaomi MiR Patcher  

 1 - Set IP-address (current value: 192.168.31.1)
 2 - Connect to device (install exploit)
 3 - Read full device info
 4 - Create full backup
 5 - Install EN/RU/ZH languages
 6 - Install permanent SSH
 7 - Install firmware (from directory "firmware")
 8 - {{{ Other functions }}}
 9 - Change language
 10 - [[ Reboot device ]]
 0 - Exit

Select: 
```

## 🔍 Detailed Feature Description

### Main Menu Features

#### 1. Set IP Address
- **Purpose**: Set the target router's IP address
- **Default**: 192.168.31.1
- **When to use**: When the router IP is not the default

#### 2. Connect Device (Install Exploit)
- **Purpose**: Detect device model and install the corresponding exploit
- **Supported exploits**:
  - `c_upload/netspeed` - for older models
  - `get_icon` - for newer models
- **Process**:
  1. Automatically detect router model
  2. Choose the appropriate exploit method
  3. Upload and execute the exploit code
  4. Enable SSH and Telnet access

#### 3. Read Full Device Info
- **Includes**:
  - Hardware model and version
  - Firmware version info
  - Partition table structure
  - Memory and storage info
  - Network configuration
- **Output**: `outdir/` directory

#### 4. Create Full Backup
- **Contents**:
  - Raw data of all partitions
  - Bootloader
  - Kernel image
  - Root filesystem
  - Configuration data
- **Format**: Binary image files
- **Location**: `backup/` directory

#### 5. Install Multi-language Pack

**Supported languages**:
- **English**: Complete English UI and language pack
- **Chinese**: Complete Chinese UI and language pack
- **Russian**: Complete Russian UI and language pack

**Features**:
- 🌐 **Smart language selection**: First run shows language menu automatically
- 💾 **Persistent config**: Language choice saved in `config.json` and applied on next launch
- 🔄 **Live switching**: Switch language by re-running the language menu
- 📱 **Complete localization**: Menus, prompts, error messages, etc.
- 🎯 **Router language pack**: Install corresponding language pack files for the router

**Installation method**: 
1. Upload language files to the router
2. Modify system configuration
3. Restart related services
4. **Uninstall**: Use extended menu option 5 to uninstall

**Technical details**:
- UTF-8 encoding for multilingual display
- Windows batch files use `chcp 65001` for Unicode support
- Modular translation system, easy to extend with new languages
- Standardized `.po` based language pack management

#### 6. Install Permanent SSH
- **Function**: Enable persistent SSH access
- **Default credentials**: 
  - Username: `root`
  - Password: `root`
- **Port**: 22
- **Note**: Persists after reboot

#### 7. Install Firmware
- **Supported formats**: 
  - Standard Xiaomi firmware format
  - OpenWrt firmware (if compatible)
- **Location**: Put firmware files in `firmware/` directory
- **Process**: Automated flashing flow

#### 8. Other Functions (Extended Menu)
Enter the extended menu for more advanced options.

#### 9. Reboot Device
Safely reboot the router.

### Extended Menu Features

#### 1. Set IP Address
Same as main menu option 1.

#### 2. Change Root Password
- **Purpose**: Change the router's root user password
- **Security**: Improve system security

#### 3. Read dmesg and syslog
- **Contents**:
  - Kernel log (dmesg)
  - System log (syslog)
- **Purpose**: Troubleshooting and system analysis

#### 4. Create Specified Partition Backup
- **Flexibility**: Choose a specific partition to back up
- **Common partitions**:
  - `bootloader` - bootloader
  - `kernel` - kernel
  - `rootfs` - root filesystem
  - `overlay` - configuration data

#### 5. Uninstall EN/RU Language Pack
Restore to the original Chinese interface.

#### 6. Set Kernel Boot Address
- **Purpose**: Modify kernel load address
- **Use case**: When installing custom firmware

#### 7. Install Breed Bootloader
- **Breed features**:
  - Powerful third-party bootloader
  - Web-based firmware flashing
  - Brick protection
- **Supported models**: 
  - R3: `pb-boot-xiaomi3-20190317-61b6d33.img`
  - R3G, R3P, RM2100, RA71: `breed_r3g_eng.bin`
  - CR6606, CR6608, CR6609, TR608, TR609: `pb-boot-cr660x.img`
- **Install command**: `python3 install_bl.py breed`

#### 7a. Install Stock U-Boot Bootloader
- **U-Boot features**:
  - Stock device bootloader
  - Device-specific boot program
  - Restore stock boot environment
- **Supported models**: 
  - R3G: `uboot_r3g.bin`
  - R3P: `uboot_r3p.bin`
  - RM2100: `uboot_rm2100.bin`
- **Install command**: `python3 install_bl.py uboot`

#### 8. Test Function
For development and debugging.

#### 9. Reboot Device
Same as main menu option 9.

## 🛠️ Troubleshooting

### Common Issues

#### 1. Connection Failed
**Issue**: Cannot connect to router
**Solution**:
```bash
# Check network connectivity
ping 192.168.31.1

# Check router admin panel
curl -I http://192.168.31.1

# Confirm IP address is correct
# Some routers may use 192.168.1.1
```

#### 2. Exploit Failed
**Issue**: "Exploit not working" error
**Possible causes**:
- Firmware version too new, vulnerability already patched
- Router model not supported
- Unstable network connection

**Solution**:
```bash
# Check if device model is supported
# Try downgrading firmware (if possible)
# Check network stability
```

#### 3. SSH Connection Issue
**Issue**: SSH connection refused
**Solution**:
```bash
# Check SSH service status
ssh root@192.168.31.1

# If refused, re-run option 6
# Check firewall settings
```

#### 4. Firmware Flashing Failed
**Issue**: Error during firmware installation
**Solution**:
- Ensure firmware matches device model
- Verify firmware file integrity
- Ensure enough storage space
- Check power stability

#### 5. Python Dependency Issue
**Issue**: ModuleNotFoundError
**Solution**:
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or use virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Recovery Mode

If the router is bricked, try the following:

#### 1. Restore via Breed (if installed)
1. Power off router
2. Hold reset button
3. Power on, wait 10 seconds
4. Visit `192.168.1.1` in browser
5. Flash firmware via web UI

#### 2. Restore from Backup
1. Connect to router via SSH
2. Restore partition with dd:
```bash
# Restore full firmware (use with caution!)
dd if=/tmp/backup.bin of=/dev/mtdblock0

# Restore specific partition
dd if=/tmp/kernel_backup.bin of=/dev/mtdblock2
```

#### 3. TFTP Recovery Mode
Some models support TFTP recovery:
1. Set computer IP to 192.168.1.2
2. Run TFTP server
3. Hold reset and power on router
4. Transfer firmware file

## ⚠️ Security Notes

### Risk Disclaimer
- **⚠️ Flashing firmware is risky, proceed with caution!**
- **⚠️ Any firmware modification may brick the device!**
- **⚠️ Modifying firmware may void official warranty!**
- **⚠️ Always create a full backup before proceeding!**

### Security Recommendations

#### Before Operation
1. **Full backup**: Always run option 4 to create a complete backup first
2. **Stable power**: Ensure stable power during operation
3. **Stable network**: Ensure stable network connection
4. **Sufficient time**: Do not operate when pressed for time

#### Password Security
1. **Change default password**: Change the default password immediately after enabling SSH
```bash
passwd root
```

2. **Disable unnecessary services**:
```bash
# Disable Telnet if not needed
/etc/init.d/telnet disable
```

3. **Configure firewall**:
```bash
# Restrict SSH access by IP range
iptables -A INPUT -p tcp --dport 22 -s 192.168.31.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP
```

#### Firmware Security
1. **Verify firmware source**: Only use firmware from trusted sources
2. **Verify integrity**: Use MD5 or SHA256 checks
3. **Incremental upgrade**: Avoid jumping too many versions at once

## 🔧 Development

### Project Structure
```
Xiaomi-Router-patcher/
├── menu.py              # Main menu interface
├── gateway.py           # Gateway communication module
├── connect*.py          # Various exploit scripts
├── xqmodel.py           # Device model definitions
├── read_info.py         # Device info reading
├── create_backup.py     # Backup functionality
├── install_*.py         # Various install features
├── unlock_features.py   # Feature unlock
├── xmir_base/           # Core libraries
│   ├── ubireader/       # UBI filesystem reader
│   ├── fdt/             # Device tree handling
│   └── telnetlib/       # Telnet library
├── data/                # Data files
│   ├── payload/         # Exploit payloads
│   ├── payload_ssh/     # SSH-related scripts
│   └── *.po             # Language pack files
├── bootloader/          # Bootloader files
├── firmware/            # Firmware storage directory
└── python/              # Bundled Python for Windows
```

### Core Module Description

#### Gateway Class (gateway.py)
Handles communication with the router, including:
- HTTP/HTTPS requests
- SSH connections
- Telnet connections
- FTP transfers
- Device detection

#### Exploit Modules (connect*.py)
- `connect1.py`: c_upload/netspeed vulnerability
- `connect7.py`: get_icon vulnerability
- Supports many Xiaomi router models

#### Device Model (xqmodel.py)
Defines all supported device models and attributes.

### Adding New Device Support

1. **Add device definition in xqmodel.py**:
```python
mi(42, "NEW_MODEL", "", "device-alt-name")
```

2. **Add detection logic in connect.py**:
```python
if gw.model_id == get_modelid_by_name('NEW_MODEL'):
    # Use appropriate exploit method
```

3. **Test new device**:
```python
# Create test script to verify functionality
```

### Custom Exploit

Refer to existing connect scripts. Main steps:

1. **Detect device**:
```python
gw.detect_device()
```

2. **Install payload**:
```python
install_exploit(api='API/endpoint')
```

3. **Execute feature**:
```python
run_exploit('function_name', timeout=10)
```

## 🤝 Contributing

### How to Contribute

1. **Fork the project**
2. **Create feature branch**:
```bash
git checkout -b feature/new-feature
```

3. **Commit changes**:
```bash
git commit -am 'Add new feature'
```

4. **Push branch**:
```bash
git push origin feature/new-feature
```

5. **Create Pull Request**

### Contribution Ideas

- Support new router models
- Fix existing exploits
- Improve UI
- Add new features
- Improve documentation
- Fix bugs

### Code Style

- Use Python 3.8+ syntax
- Follow PEP 8 style
- Add appropriate comments
- Write tests

### Reporting Issues

Please report bugs or feature requests in GitHub Issues:
- Describe the issue in detail
- Provide reproduction steps
- Include system environment info
- Attach relevant logs

## 📄 License

This project is licensed under GPL-3.0. See [LICENSE](LICENSE) for details.

## 💝 Donations

If this project helped you, please consider supporting development:

[![Donations Page](https://github.com/andry81-cache/gh-content-static-cache/raw/master/common/badges/donate/donate.svg)](https://github.com/remittor/donate)

## 📞 Contact

- **GitHub Issues**: [Report issues](https://github.com/sandro-defender/Xiaomi-Router-patcher/issues)
- **GitHub Discussions**: [Discussions](https://github.com/sandro-defender/Xiaomi-Router-patcher/discussions)

## 🙏 Acknowledgements

- Thanks to all contributors of the original project
- Thanks to Xiaomi router hacking community
- Thanks to OpenWrt project
- Thanks to all testers for feedback

---

**⚠️ Disclaimer**: This tool is for learning and research purposes only. Any operation performed with this tool is at the user's own risk. The developers are not responsible for any damage caused by using this tool.

## 🖼️ Interface Preview

![Successful execution](image/display-successful.png)
*Interface after successful execution*
![SSH connected](image/display-ssh.png)
*Interface after SSH connection*
![Persistent SSH](image/display-permanent-ssh.png)
*Interface after permanent SSH enabled*

---

## Quick Start Summary

**XMiR-Patcher** is a comprehensive firmware patcher for Xiaomi routers that supports:

- **50+ Xiaomi router models** from R1CM to latest AX series
- **Exploit installation** for gaining root access
- **Permanent SSH access** with customizable credentials
- **Full firmware backup** and selective partition backup
- **Custom firmware installation** including OpenWrt support
- **Bootloader replacement** (Breed support for R3/R3G/R3P/RM2100/RA71/CR660x/TR60x series, U-Boot support for R3G/R3P/RM2100)
- **Multi-language support** (EN/RU/ZH language packs with English menu interface)
- **Advanced features** like password change, log reading, feature unlocking

### Quick Start
**Windows**: Run `run.bat` | **Linux/macOS**: Run `./run.sh`

### Basic Usage Flow
1. Set router IP address (default: 192.168.31.1)
2. Connect and install exploit (essential first step)
3. Create full backup (highly recommended)
4. Enable permanent SSH access
5. Install custom firmware or additional features

**⚠️ Warning**: Firmware modification carries risks. Always backup before proceeding!
