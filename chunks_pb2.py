# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='chunks.proto',
  package='replicant',
  serialized_pb='\n\x0c\x63hunks.proto\x12\treplicant\"6\n\tChunkInfo\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x0e\n\x06\x66rozen\x18\x03 \x01(\x08\"1\n\x05\x43hunk\x12\n\n\x02id\x18\x01 \x02(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\r\n\x05\x63hunk\x18\x03 \x01(\t2\xb5\x01\n\rReplicantSrvr\x12\x33\n\tSendChunk\x12\x10.replicant.Chunk\x1a\x14.replicant.ChunkInfo\x12\x32\n\x08GetChunk\x12\x14.replicant.ChunkInfo\x1a\x10.replicant.Chunk\x12;\n\rUnfreezeChunk\x12\x14.replicant.ChunkInfo\x1a\x14.replicant.ChunkInfoB\x03\x90\x01\x01')




_CHUNKINFO = descriptor.Descriptor(
  name='ChunkInfo',
  full_name='replicant.ChunkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='replicant.ChunkInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='owner', full_name='replicant.ChunkInfo.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='frozen', full_name='replicant.ChunkInfo.frozen', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=81,
)


_CHUNK = descriptor.Descriptor(
  name='Chunk',
  full_name='replicant.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='replicant.Chunk.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='owner', full_name='replicant.Chunk.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='chunk', full_name='replicant.Chunk.chunk', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=83,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ChunkInfo'] = _CHUNKINFO
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK

class ChunkInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHUNKINFO
  
  # @@protoc_insertion_point(class_scope:replicant.ChunkInfo)

class Chunk(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHUNK
  
  # @@protoc_insertion_point(class_scope:replicant.Chunk)


_REPLICANTSRVR = descriptor.ServiceDescriptor(
  name='ReplicantSrvr',
  full_name='replicant.ReplicantSrvr',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=135,
  serialized_end=316,
  methods=[
  descriptor.MethodDescriptor(
    name='SendChunk',
    full_name='replicant.ReplicantSrvr.SendChunk',
    index=0,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_CHUNKINFO,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='GetChunk',
    full_name='replicant.ReplicantSrvr.GetChunk',
    index=1,
    containing_service=None,
    input_type=_CHUNKINFO,
    output_type=_CHUNK,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='UnfreezeChunk',
    full_name='replicant.ReplicantSrvr.UnfreezeChunk',
    index=2,
    containing_service=None,
    input_type=_CHUNKINFO,
    output_type=_CHUNKINFO,
    options=None,
  ),
])

class ReplicantSrvr(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _REPLICANTSRVR
class ReplicantSrvr_Stub(ReplicantSrvr):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _REPLICANTSRVR

# @@protoc_insertion_point(module_scope)
