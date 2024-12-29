# Vagrantfile
Vagrant.configure("2") do |config|
  # Define the main VM
  config.vm.define "main" do |main|
    main.vm.box = "ubuntu/jammy64"
    main.vm.box_version = "20240712.0.0"
    main.vm.hostname = "main"
    # Configure a bridged network with a specific interface
    # this machine will host for monitoring tools with ip forwarding
    main.vm.network "forwarded_port", guest: 9090, host: 9090
    main.vm.network "forwarded_port", guest: 3000, host: 3000
    main.vm.network "forwarded_port", guest: 9100, host: 9100
    main.vm.network "forwarded_port", guest: 9586, host: 9586

    # main.vm.network "public_network", ip: "192.168.1.101", bridge: "WiFi"
    main.vm.network "private_network", ip: "172.20.20.10"
    main.vm.provider "virtualbox" do |vb|
      vb.name = "MainVM"
      vb.memory = 3072
      vb.cpus = 3
    end
    
    main.vm.provision "shell", inline: <<-SHELL
      sudo apt update -y && sudo apt upgrade -y
      echo "Main VM setup complete."
    SHELL
  end

  
  config.vm.define "client1" do |client1|
    client1.vm.box = "ubuntu/jammy64"
    client1.vm.box_version = "20240712.0.0"
    client1.vm.hostname = "client1"
    # Configure a bridged network with a specific interface

    # client1.vm.network "public_network", ip: "192.168.1.102", bridge: "WiFi"
    client1.vm.network "private_network", ip: "172.20.20.11"
    client1.vm.provider "virtualbox" do |vb|
      vb.name = "ClientVM1_Docker"
      vb.memory = 512
      vb.cpus = 1
    end
    client1.vm.provision "shell", inline: <<-SHELL
    sudo apt update -y && sudo apt upgrade -y
    echo "Client VM setup complete."
    SHELL
  end
  
  config.vm.define "client2" do |client2|
    client2.vm.box = "ubuntu/jammy64"
    client2.vm.box_version = "20240712.0.0"
    client2.vm.hostname = "client2"
    # Configure a bridged network with a specific interface
    # client2.vm.network "public_network", ip: "192.168.1.103", bridge: "WiFi"
    client2.vm.network "private_network", ip: "172.20.20.12"
    
    client2.vm.provider "virtualbox" do |vb|
      vb.name = "ClientVM2"
      vb.memory = 512
      vb.cpus = 1
    end
    client2.vm.provision "shell", inline: <<-SHELL
    sudo apt update -y && sudo apt upgrade -y
    echo "Client VM setup complete."
    SHELL
  end
end
