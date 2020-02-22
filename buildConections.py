# pedir imputs para que tengamos esta propiedad:
def buildRouter(routInfo):
    name = routInfo[0]
    newRouter = router(name)
    routInfo.pop(0)
    for interface in routInfo:
        newRouter.interfaces.append(interface)
    return newRouter


def getComands(routersList):
    comandos = []
    comandos2 = []
    for router in routersList:
        comandos = comandos + (setRouters(router))
        comandos2 = comandos2 + (setInterfacesPeers(router))

    return comandos + comandos2


def setRouters(router):
    comandos = []
    comandos.append(
        "set routing-instances {} instance-type virtual-router".format(router.name))

    for interface in router.interfaces:
        comandos.append(
            "set routing-instances {} interface lt-0/0/0.{}".format(router.name, interface))
    return comandos


def setInterfacesPeers(router):
    comandos = []
    for interface in router.interfaces:
        interface = int(interface)
        if interface % 2 is 0:
            interfacePareja = interface - 1
        else:
            interfacePareja = interface + 1
        # aqui construyo el comando.

        comandos.append(
            "set interfaces lt-0/0/0.{} encapsulation ethernet".format(interface))
        comandos.append(
            "set interfaces lt-0/0/0.{} peer-unit {}".format(interface, interfacePareja))
    return comandos
    # formatting a string using a numeric constant


class router:
    def __init__(self, name):
        self.name = name
        self.interfaces = []


RFile = open("routers.txt", "r")

routersList = []
for line in RFile:
    routInfo = line.split()
    routersList.append(buildRouter(routInfo))

comandos = getComands(routersList)
comandosFile = open("comandos.txt", "w")
for comando in comandos:
    comandosFile.write(comando)
    comandosFile.write('\n')
comandosFile.close()
