import docker
import ariel.classy as c
import os

# def test_two():
#     assert c.multiplier(4) == 16

def test_hannah():
    assert os.system('docker run --rm hannah pytest') == 0
    # assert os.system('docker run --rm hannah pytest')
    # client = docker.from_env()
    # client.containers.run("tridelt/hannah",command='pytest',remove=True,)

    # try:
    #     client.containers.run("hannah",command='pytest',remove=True,)
    # except:
    #     pass
    # assert True