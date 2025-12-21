import dataclasses


@dataclasses.dataclass
class MqttMessage:
    """
    Container for `capmqtt`'s `message` response items.
    """

    topic: str
    payload: str | bytes
    userdata: dict | None


@dataclasses.dataclass
class MqttSettings:
    host: str
    port: int
    username: str
    password: str
