"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ServerReflectionRequest(google.protobuf.message.Message):
    """The message sent by the client when calling ServerReflectionInfo method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOST_FIELD_NUMBER: builtins.int
    FILE_BY_FILENAME_FIELD_NUMBER: builtins.int
    FILE_CONTAINING_SYMBOL_FIELD_NUMBER: builtins.int
    FILE_CONTAINING_EXTENSION_FIELD_NUMBER: builtins.int
    ALL_EXTENSION_NUMBERS_OF_TYPE_FIELD_NUMBER: builtins.int
    LIST_SERVICES_FIELD_NUMBER: builtins.int
    host: typing.Text
    file_by_filename: typing.Text
    """Find a proto file by the file name."""

    file_containing_symbol: typing.Text
    """Find the proto file that declares the given fully-qualified symbol name.
    This field should be a fully-qualified symbol name
    (e.g. <package>.<service>[.<method>] or <package>.<type>).
    """

    @property
    def file_containing_extension(self) -> global___ExtensionRequest:
        """Find the proto file which defines an extension extending the given
        message type with the given field number.
        """
        pass
    all_extension_numbers_of_type: typing.Text
    """Finds the tag numbers used by all known extensions of extendee_type, and
    appends them to ExtensionNumberResponse in an undefined order.
    Its corresponding method is best-effort: it's not guaranteed that the
    reflection service will implement this method, and it's not guaranteed
    that this method will provide all extensions. Returns
    StatusCode::UNIMPLEMENTED if it's not implemented.
    This field should be a fully-qualified type name. The format is
    <package>.<type>
    """

    list_services: typing.Text
    """List the full names of registered services. The content will not be
    checked.
    """

    def __init__(self,
        *,
        host: typing.Text = ...,
        file_by_filename: typing.Text = ...,
        file_containing_symbol: typing.Text = ...,
        file_containing_extension: typing.Optional[global___ExtensionRequest] = ...,
        all_extension_numbers_of_type: typing.Text = ...,
        list_services: typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["all_extension_numbers_of_type",b"all_extension_numbers_of_type","file_by_filename",b"file_by_filename","file_containing_extension",b"file_containing_extension","file_containing_symbol",b"file_containing_symbol","list_services",b"list_services","message_request",b"message_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["all_extension_numbers_of_type",b"all_extension_numbers_of_type","file_by_filename",b"file_by_filename","file_containing_extension",b"file_containing_extension","file_containing_symbol",b"file_containing_symbol","host",b"host","list_services",b"list_services","message_request",b"message_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message_request",b"message_request"]) -> typing.Optional[typing_extensions.Literal["file_by_filename","file_containing_symbol","file_containing_extension","all_extension_numbers_of_type","list_services"]]: ...
global___ServerReflectionRequest = ServerReflectionRequest

class ExtensionRequest(google.protobuf.message.Message):
    """The type name and extension number sent by the client when requesting
    file_containing_extension.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CONTAINING_TYPE_FIELD_NUMBER: builtins.int
    EXTENSION_NUMBER_FIELD_NUMBER: builtins.int
    containing_type: typing.Text
    """Fully-qualified type name. The format should be <package>.<type>"""

    extension_number: builtins.int
    def __init__(self,
        *,
        containing_type: typing.Text = ...,
        extension_number: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["containing_type",b"containing_type","extension_number",b"extension_number"]) -> None: ...
global___ExtensionRequest = ExtensionRequest

class ServerReflectionResponse(google.protobuf.message.Message):
    """The message sent by the server to answer ServerReflectionInfo method."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALID_HOST_FIELD_NUMBER: builtins.int
    ORIGINAL_REQUEST_FIELD_NUMBER: builtins.int
    FILE_DESCRIPTOR_RESPONSE_FIELD_NUMBER: builtins.int
    ALL_EXTENSION_NUMBERS_RESPONSE_FIELD_NUMBER: builtins.int
    LIST_SERVICES_RESPONSE_FIELD_NUMBER: builtins.int
    ERROR_RESPONSE_FIELD_NUMBER: builtins.int
    valid_host: typing.Text
    @property
    def original_request(self) -> global___ServerReflectionRequest: ...
    @property
    def file_descriptor_response(self) -> global___FileDescriptorResponse:
        """This message is used to answer file_by_filename, file_containing_symbol,
        file_containing_extension requests with transitive dependencies. As
        the repeated label is not allowed in oneof fields, we use a
        FileDescriptorResponse message to encapsulate the repeated fields.
        The reflection service is allowed to avoid sending FileDescriptorProtos
        that were previously sent in response to earlier requests in the stream.
        """
        pass
    @property
    def all_extension_numbers_response(self) -> global___ExtensionNumberResponse:
        """This message is used to answer all_extension_numbers_of_type requst."""
        pass
    @property
    def list_services_response(self) -> global___ListServiceResponse:
        """This message is used to answer list_services request."""
        pass
    @property
    def error_response(self) -> global___ErrorResponse:
        """This message is used when an error occurs."""
        pass
    def __init__(self,
        *,
        valid_host: typing.Text = ...,
        original_request: typing.Optional[global___ServerReflectionRequest] = ...,
        file_descriptor_response: typing.Optional[global___FileDescriptorResponse] = ...,
        all_extension_numbers_response: typing.Optional[global___ExtensionNumberResponse] = ...,
        list_services_response: typing.Optional[global___ListServiceResponse] = ...,
        error_response: typing.Optional[global___ErrorResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["all_extension_numbers_response",b"all_extension_numbers_response","error_response",b"error_response","file_descriptor_response",b"file_descriptor_response","list_services_response",b"list_services_response","message_response",b"message_response","original_request",b"original_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["all_extension_numbers_response",b"all_extension_numbers_response","error_response",b"error_response","file_descriptor_response",b"file_descriptor_response","list_services_response",b"list_services_response","message_response",b"message_response","original_request",b"original_request","valid_host",b"valid_host"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["message_response",b"message_response"]) -> typing.Optional[typing_extensions.Literal["file_descriptor_response","all_extension_numbers_response","list_services_response","error_response"]]: ...
global___ServerReflectionResponse = ServerReflectionResponse

class FileDescriptorResponse(google.protobuf.message.Message):
    """Serialized FileDescriptorProto messages sent by the server answering
    a file_by_filename, file_containing_symbol, or file_containing_extension
    request.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_DESCRIPTOR_PROTO_FIELD_NUMBER: builtins.int
    @property
    def file_descriptor_proto(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]:
        """Serialized FileDescriptorProto messages. We avoid taking a dependency on
        descriptor.proto, which uses proto2 only features, by making them opaque
        bytes instead.
        """
        pass
    def __init__(self,
        *,
        file_descriptor_proto: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_descriptor_proto",b"file_descriptor_proto"]) -> None: ...
global___FileDescriptorResponse = FileDescriptorResponse

class ExtensionNumberResponse(google.protobuf.message.Message):
    """A list of extension numbers sent by the server answering
    all_extension_numbers_of_type request.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    BASE_TYPE_NAME_FIELD_NUMBER: builtins.int
    EXTENSION_NUMBER_FIELD_NUMBER: builtins.int
    base_type_name: typing.Text
    """Full name of the base type, including the package name. The format
    is <package>.<type>
    """

    @property
    def extension_number(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        base_type_name: typing.Text = ...,
        extension_number: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_type_name",b"base_type_name","extension_number",b"extension_number"]) -> None: ...
global___ExtensionNumberResponse = ExtensionNumberResponse

class ListServiceResponse(google.protobuf.message.Message):
    """A list of ServiceResponse sent by the server answering list_services request."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SERVICE_FIELD_NUMBER: builtins.int
    @property
    def service(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ServiceResponse]:
        """The information of each service may be expanded in the future, so we use
        ServiceResponse message to encapsulate it.
        """
        pass
    def __init__(self,
        *,
        service: typing.Optional[typing.Iterable[global___ServiceResponse]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["service",b"service"]) -> None: ...
global___ListServiceResponse = ListServiceResponse

class ServiceResponse(google.protobuf.message.Message):
    """The information of a single service used by ListServiceResponse to answer
    list_services request.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    """Full name of a registered service, including its package name. The format
    is <package>.<service>
    """

    def __init__(self,
        *,
        name: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name",b"name"]) -> None: ...
global___ServiceResponse = ServiceResponse

class ErrorResponse(google.protobuf.message.Message):
    """The error code and error message sent by the server when an error occurs."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ERROR_CODE_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    error_code: builtins.int
    """This field uses the error codes defined in grpc::StatusCode."""

    error_message: typing.Text
    def __init__(self,
        *,
        error_code: builtins.int = ...,
        error_message: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_code",b"error_code","error_message",b"error_message"]) -> None: ...
global___ErrorResponse = ErrorResponse