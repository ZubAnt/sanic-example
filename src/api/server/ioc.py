from injector import Injector

from server.configuration import Configuration

ioc = Injector([Configuration()])
