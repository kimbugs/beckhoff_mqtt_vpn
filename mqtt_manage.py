import struct
import datetime
import paho.mqtt.client as mqtt

UNPACK_PARAMS = {
    'c': 1, 'b': 1, 'B': 1, '?': 1,
    'h': 2, 'H': 2,
    'i': 4, 'I': 4, 'l': 4, 'L': 4, 'f': 4,
    'q': 8, 'Q': 8, 'd': 8
}


# noinspection PyBroadException,PyUnusedLocal
class MqttManage:
    CONFIG = {
        "ip": "192.168.0.128",
        "port": 1883,
        "keepalive": 60,
        "username": "user",
        "password": "1234"
    }

    def __init__(self, channel, interface):
        self.interface = interface
        self.channel = channel
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        #self.client.username_pw_set(self.CONFIG['username'], self.CONFIG['password'])
        self.client.connect(self.CONFIG['ip'], self.CONFIG['port'], self.CONFIG['keepalive'])

    def on_connect(self, client, mosq, obj, rc):
        self.client.subscribe(self.channel)

    def on_message(self, client, userdata, msg):
        params = self.__unpack(msg.payload)
        print(params)

    def loop(self):
        print("Mqtt Sub Start")
        self.client.loop_forever()

    def __unpack(self, byte_data):
        proc = {"current": 0, "previous": 0}
        params = {}
        try:
            for key, value in self.interface:
                params[key] = {}
                for name, unpack_type in value:
                    proc['previous'] = proc['current']
                    proc['current'] += UNPACK_PARAMS[unpack_type]
                    process_value = byte_data[proc['previous']:proc['current']]
                    unpack_value = struct.unpack(unpack_type, process_value)[0]
                    params[key][name] = unpack_value
            return params
        except:
            return None
        
    @classmethod
    def write(cls, key, value):
        # InitInstance
        m = mqtt.Client("python_pub")
        #m.username_pw_set(cls.CONFIG['username'], cls.CONFIG['password'])
        # Mqtt Connect
        m.connect(cls.CONFIG['ip'], cls.CONFIG['port'])

        # Publish Parameters
        m.publish(key, value)
