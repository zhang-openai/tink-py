# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tink/proto/ed25519.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'tink/proto/ed25519.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18tink/proto/ed25519.proto\x12\x12google.crypto.tink\"#\n\x10\x45\x64\x32\x35\x35\x31\x39KeyFormat\x12\x0f\n\x07version\x18\x01 \x01(\r\"6\n\x10\x45\x64\x32\x35\x35\x31\x39PublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x11\n\tkey_value\x18\x02 \x01(\x0c\"q\n\x11\x45\x64\x32\x35\x35\x31\x39PrivateKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x11\n\tkey_value\x18\x02 \x01(\x0c\x12\x38\n\npublic_key\x18\x03 \x01(\x0b\x32$.google.crypto.tink.Ed25519PublicKeyBZ\n\x1c\x63om.google.crypto.tink.protoP\x01Z8github.com/tink-crypto/tink-go/v2/proto/ed25519_go_protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tink.proto.ed25519_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.crypto.tink.protoP\001Z8github.com/tink-crypto/tink-go/v2/proto/ed25519_go_proto'
  _globals['_ED25519KEYFORMAT']._serialized_start=48
  _globals['_ED25519KEYFORMAT']._serialized_end=83
  _globals['_ED25519PUBLICKEY']._serialized_start=85
  _globals['_ED25519PUBLICKEY']._serialized_end=139
  _globals['_ED25519PRIVATEKEY']._serialized_start=141
  _globals['_ED25519PRIVATEKEY']._serialized_end=254
# @@protoc_insertion_point(module_scope)
