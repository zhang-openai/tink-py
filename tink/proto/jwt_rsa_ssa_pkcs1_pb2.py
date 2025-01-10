# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tink/proto/jwt_rsa_ssa_pkcs1.proto
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
    'tink/proto/jwt_rsa_ssa_pkcs1.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"tink/proto/jwt_rsa_ssa_pkcs1.proto\x12\x12google.crypto.tink\"\xe7\x01\n\x17JwtRsaSsaPkcs1PublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12>\n\talgorithm\x18\x02 \x01(\x0e\x32+.google.crypto.tink.JwtRsaSsaPkcs1Algorithm\x12\t\n\x01n\x18\x03 \x01(\x0c\x12\t\n\x01\x65\x18\x04 \x01(\x0c\x12I\n\ncustom_kid\x18\x05 \x01(\x0b\x32\x35.google.crypto.tink.JwtRsaSsaPkcs1PublicKey.CustomKid\x1a\x1a\n\tCustomKid\x12\r\n\x05value\x18\x01 \x01(\t\"\xb2\x01\n\x18JwtRsaSsaPkcs1PrivateKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12?\n\npublic_key\x18\x02 \x01(\x0b\x32+.google.crypto.tink.JwtRsaSsaPkcs1PublicKey\x12\t\n\x01\x64\x18\x03 \x01(\x0c\x12\t\n\x01p\x18\x04 \x01(\x0c\x12\t\n\x01q\x18\x05 \x01(\x0c\x12\n\n\x02\x64p\x18\x06 \x01(\x0c\x12\n\n\x02\x64q\x18\x07 \x01(\x0c\x12\x0b\n\x03\x63rt\x18\x08 \x01(\x0c\"\xa1\x01\n\x17JwtRsaSsaPkcs1KeyFormat\x12\x0f\n\x07version\x18\x01 \x01(\r\x12>\n\talgorithm\x18\x02 \x01(\x0e\x32+.google.crypto.tink.JwtRsaSsaPkcs1Algorithm\x12\x1c\n\x14modulus_size_in_bits\x18\x03 \x01(\r\x12\x17\n\x0fpublic_exponent\x18\x04 \x01(\x0c*J\n\x17JwtRsaSsaPkcs1Algorithm\x12\x0e\n\nRS_UNKNOWN\x10\x00\x12\t\n\x05RS256\x10\x01\x12\t\n\x05RS384\x10\x02\x12\t\n\x05RS512\x10\x03\x42`\n\x1c\x63om.google.crypto.tink.protoP\x01Z>github.com/tink-crypto/tink-go/v2/proto/rsa_ssa_pkcs1_go_protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tink.proto.jwt_rsa_ssa_pkcs1_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.google.crypto.tink.protoP\001Z>github.com/tink-crypto/tink-go/v2/proto/rsa_ssa_pkcs1_go_proto'
  _globals['_JWTRSASSAPKCS1ALGORITHM']._serialized_start=637
  _globals['_JWTRSASSAPKCS1ALGORITHM']._serialized_end=711
  _globals['_JWTRSASSAPKCS1PUBLICKEY']._serialized_start=59
  _globals['_JWTRSASSAPKCS1PUBLICKEY']._serialized_end=290
  _globals['_JWTRSASSAPKCS1PUBLICKEY_CUSTOMKID']._serialized_start=264
  _globals['_JWTRSASSAPKCS1PUBLICKEY_CUSTOMKID']._serialized_end=290
  _globals['_JWTRSASSAPKCS1PRIVATEKEY']._serialized_start=293
  _globals['_JWTRSASSAPKCS1PRIVATEKEY']._serialized_end=471
  _globals['_JWTRSASSAPKCS1KEYFORMAT']._serialized_start=474
  _globals['_JWTRSASSAPKCS1KEYFORMAT']._serialized_end=635
# @@protoc_insertion_point(module_scope)
