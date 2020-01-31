# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "any_IP"
  config.vm.provision "shell", path: "setup.sh"
  config.vm.synced_folder "./", "/var/www/", type: "virtualbox"
  config.vm.provider :virtualbox do |vb|
    vb.gui = true
    vb.memory = "1024"
  end
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
end
