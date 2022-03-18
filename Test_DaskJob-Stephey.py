import os

import dask
from dask.distributed import Client
from scipy import interpolate

print('###############\nStart!\n###############')

scheduler_file = os.path.join(os.environ["SCRATCH"], "scheduler.json")

print("here is our scheduler file")
print(scheduler_file)

#dask.config.config["distributed"]["dashboard"]["link"] = "{JUPYTERHUB_SERVICE_PREFIX}proxy/{host}:{port}/status"

client = Client(scheduler_file=scheduler_file)

WorkerNo = len(client.processing())
# print('{} workers created'.format( WorkerNo ) )

print('###############')

# if WorkerNo < 31:
#     raise ValueError('Worker Not Enough! No. of worker is {}.'.format(WorkerNo) )

print("hello form dask, here is our client")
print(client)
print('{} workers created'.format( WorkerNo ) )

print('###############\nFinish!\n###############')