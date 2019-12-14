#
# Cookbook:: apiserver
# Recipe:: apiserverinstall
#
# Copyright:: 2019, The Authors, All Rights Reserved.


apt_update "update apt" do
    frequency 86400
    action :periodic
end

docker_service 'default' do
    action [:create, :start]
end

execute 'enable docker permission' do
    command 'chmod 777 /var/run/docker.sock'
    # elevated true
end