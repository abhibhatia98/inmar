from injector import Injector

from shared.logging.logger import Logger


class Mediator:
    handlers = {}
    injector: Injector

    def send(self, entity):
        entity_type = type(entity)
        handler = self.injector.get(Mediator.handlers[entity_type])
        result = handler.handle(entity)
        return result

    def send_all(self, entities):
        for entity in entities:
            self.send(entity)

    @staticmethod
    def register_handler(key):
        def wrapper(*args, **kwargs):
            Mediator.handlers[key] = args[0]
            return key
        return wrapper
