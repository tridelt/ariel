import docker
import ariel.classy as c
import os
import pprint
import json
import time

# def test_two():
#     assert c.multiplier(4) == 16

def test_hannah():
    # assert os.system('docker run --rm hannah pytest') == 0
    # assert os.system('docker run --rm hannah pytest')
    client = docker.from_env()
    
    container = client.containers.run("hannah",command='pytest',detach=True)
    status_code = container.wait()['StatusCode']
    out = container.logs(stdout=True, stderr=True).decode('ascii')
    container.remove()

    if status_code != 0:
        print(status_code)
        assert False, out