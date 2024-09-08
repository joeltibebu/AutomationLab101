from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

command_list = ["show version", "show ip int br", "show run"]

def show_test(task):
    for cmd in command_list:
        task.run(task=send_command, command=cmd)
        
results = nr.run(task=show_test)
print_result(results)