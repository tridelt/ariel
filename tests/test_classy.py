import docker
import ariel.classy as c
import os
import pprint
import json

# def test_two():
#     assert c.multiplier(4) == 16

def test_hannah():
    # assert os.system('docker run --rm hannah pytest') == 0
    # assert os.system('docker run --rm hannah pytest')
    client = docker.from_env()
    try:
        container = client.containers.run("hannah",command='pytest',stderr=True,detach=True)
        container.wait()
    except:
        pass

    out = container.logs(stdout=True, stderr=False)
    err = container.logs(stdout=False, stderr=True)

    print(out)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(out.decode('ascii'))
    print('')
    print('')
    print('')
    print('')
    print('')
    print(err)
    # print(json.loads(str(err)))


    # pprint.pprint(err)

    assert False