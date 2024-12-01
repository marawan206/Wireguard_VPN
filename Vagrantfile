# Vagrantfile
Vagrant.configure("2") do |config|
  # Define the main VM
  config.vm.define "main" do |main|
    main.vm.box = "ubuntu/jammy64"
    main.vm.box_version = "20240712.0.0"
    main.vm.hostname = "main"
    # Configure a bridged network with a specific interface
    main.vm.network "public_network", ip: "192.168.1.100", bridge: "WiFi"
    main.vm.provider "virtualbox" do |vb|
      vb.name = "MainVM"
      vb.memory = 1024
      vb.cpus = 2
    end
    main.vm.provision "shell", inline: <<-SHELL
      sudo apt update -y && sudo apt upgrade -y
      echo "Main VM setup complete."
    SHELL
  end

  # Define the client VM
  config.vm.define "client" do |client|
    client.vm.box = "ubuntu/jammy64"
    client.vm.box_version = "20240712.0.0"
    client.vm.hostname = "client"
    # Configure a bridged network with a specific interface
    client.vm.network "public_network", ip: "192.168.1.101", bridge: "WiFi"
    client.vm.provider "virtualbox" do |vb|
      vb.name = "ClientVM"
      vb.memory = 1024
      vb.cpus = 2
    end
    client.vm.provision "shell", inline: <<-SHELL
      sudo apt update -y && sudo apt upgrade -y
      echo "Client VM setup complete."
    SHELL
  end
end
  