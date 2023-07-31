# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpclib/health/v1/health.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import grpclib.health.v1.health_pb2


class HealthBase(abc.ABC):

    @abc.abstractmethod
    async def Check(self, stream: 'grpclib.server.Stream[grpclib.health.v1.health_pb2.HealthCheckRequest, grpclib.health.v1.health_pb2.HealthCheckResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Watch(self, stream: 'grpclib.server.Stream[grpclib.health.v1.health_pb2.HealthCheckRequest, grpclib.health.v1.health_pb2.HealthCheckResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpc.health.v1.Health/Check': grpclib.const.Handler(
                self.Check,
                grpclib.const.Cardinality.UNARY_UNARY,
                grpclib.health.v1.health_pb2.HealthCheckRequest,
                grpclib.health.v1.health_pb2.HealthCheckResponse,
            ),
            '/grpc.health.v1.Health/Watch': grpclib.const.Handler(
                self.Watch,
                grpclib.const.Cardinality.UNARY_STREAM,
                grpclib.health.v1.health_pb2.HealthCheckRequest,
                grpclib.health.v1.health_pb2.HealthCheckResponse,
            ),
        }


class HealthStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Check = grpclib.client.UnaryUnaryMethod(
            channel,
            '/grpc.health.v1.Health/Check',
            grpclib.health.v1.health_pb2.HealthCheckRequest,
            grpclib.health.v1.health_pb2.HealthCheckResponse,
        )
        self.Watch = grpclib.client.UnaryStreamMethod(
            channel,
            '/grpc.health.v1.Health/Watch',
            grpclib.health.v1.health_pb2.HealthCheckRequest,
            grpclib.health.v1.health_pb2.HealthCheckResponse,
        )
