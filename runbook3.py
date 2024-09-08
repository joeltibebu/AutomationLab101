from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def send_command(task):
    task.run(task=send_config, config="ntp server  2.2.2.2")
        
results = nr.run(task=send_command)
print_result(results)