import docker
import ariel.classy as c

# def test_two():
#     assert c.multiplier(4) == 16

def test_hannah():
    client = docker.from_env()
    client.containers.run("tridelt/hannah",command='pytest',remove=True,)

    # try:
    #     client.containers.run("hannah",command='pytest',remove=True,)
    # except:
    #     pass
    assert True