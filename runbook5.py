from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def send_command(task):
    task.run(task=send_configs_from_file, file="randomconfig.txt")
        
results = nr.run(task=send_command)
print_result(results)