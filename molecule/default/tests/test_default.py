import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_apache_service(host):
    s = host.service('httpd')

    assert s.is_running
    assert s.is_enabled


def test_apache_socket(host):
    assert host.socket("tcp://80").is_listening
