#! /bin/bash
set -e

echo "Please enter your Server Public IP: "
read Server_Access_IP

echo "Please enter your Server Public Key: "
read Server_publickey

echo "Please enter your Client IP address for VPN: "
read C_IP

echo "Please enter your Client ID: "
read Clientid 

# Clientid=$((RANDOM % 1000000))

wg genkey > "${Clientid}_privatekey"
cat "${Clientid}_privatekey" | wg pubkey > "${Clientid}_publickey"

wg_status=$(wg show wg0)

if [[ -n "$wg_status" ]]; then
    # If WireGuard is running, bring it down
    echo "WireGuard is up. Bringing it down..."
    sudo wg-quick down wg0
    sudo systemctl stop wg-quick@wg0
else
    # If WireGuard is not running, notify the user
    echo "WireGuard is already down."
fi


echo "[Peer]" >> /etc/wireguard/wg0.conf
echo "PublicKey = $(cat ${Clientid}_publickey)" >> /etc/wireguard/wg0.conf
echo "AllowedIPs = ${C_IP}/32" >> /etc/wireguard/wg0.conf

sudo wg-quick up wg0

echo "Server Configuration is updated with the New Client ID: ${Clientid}"


cat <<EOF > Client_config.sh

#!/bin/bash

# Install WireGuard and resolvconf
sudo apt update -y 
sudo apt install wireguard -y
sudo apt install resolvconf -y

# Enable and start resolvconf service
sudo systemctl enable resolvconf
sudo systemctl start resolvconf

# Create the WireGuard configuration file
cat <<EOL > /etc/wireguard/wg0.conf
[Interface]
Address = ${C_IP}/32
PrivateKey = $(cat ${Clientid}_privatekey)
DNS = 1.1.1.1

[Peer]
PublicKey = ${Server_publickey}
Endpoint = ${Server_Access_IP}:51820
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
EOL

# Start the WireGuard interface
sudo wg-quick up wg0
sudo systemctl start wg-quick@wg0
EOF

# Make the client script executable
chmod +x Client_config.sh

echo "Client Configuration file is created with name Client_config.sh"
