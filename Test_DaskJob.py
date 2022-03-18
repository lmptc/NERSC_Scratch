import dask
from dask.distributed import Client

print('###############\nStart!\n###############')

scheduler_file = os.path.join(os.environ["SCRATCH"], "scheduler.json")

print("here is our scheduler file")
print(scheduler_file)

#dask.config.config["distributed"]["dashboard"]["link"] = "{JUPYTERHUB_SERVICE_PREFIX}proxy/{host}:{port}/status"

client = Client(scheduler_file=scheduler_file)

print("hello form dask, here is our client")
print(client)

print('###############\nFinish!\n###############')
