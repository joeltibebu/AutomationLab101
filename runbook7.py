from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def test_another_cmd(task):
    task.run(task=netmiko_send_command, command_string="show interface g0/0")
    
results = nr.run(task=test_another_cmd)
print_result(results)