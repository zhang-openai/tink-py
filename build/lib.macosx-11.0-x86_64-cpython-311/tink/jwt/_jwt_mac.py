# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Interface for JwtMac."""

import abc

from typing import Optional

from tink.jwt import _jwt_validator
from tink.jwt import _raw_jwt
from tink.jwt import _verified_jwt


class JwtMac(metaclass=abc.ABCMeta):
  """Interface for authenticating and verifying JWT with JWS MAC.

  Sees RFC 7519 and RFC 7515. Security guarantees: similar to MAC.
  """

  @abc.abstractmethod
  def compute_mac_and_encode(self, token: _raw_jwt.RawJwt) -> str:
    """Computes a MAC and encodes the token.

    Args:
      token: The RawJwt token to be MACed and encoded.

    Returns:
      The MACed token encoded in the JWS compact serialization format.
    Raises:
      tink.TinkError if the operation fails.
    """
    raise NotImplementedError()

  @abc.abstractmethod
  def verify_mac_and_decode(
      self, compact: str,
      validator: _jwt_validator.JwtValidator) -> _verified_jwt.VerifiedJwt:
    """Verifies, validates and decodes a MACed compact JWT token.

    The JWT is validated against the rules in validator. That is, every claim in
    validator must also be present in the JWT. For example, if validator
    contains an issuer (iss) claim, the JWT must contain an identical claim.
    The JWT can contain claims that are NOT in the validator, which are then
    ignored. However, if the JWT contains a list of audiences, the validator
    must also contain an audience in the list.

    If the JWT contains timestamp claims such as expiration (exp), issued_at
    (iat) or not_before (nbf), they will also be validated. Validator allows to
    set a clock skew, to deal with small clock differences among different
    machines.

    Args:
      compact: A MACed token encoded in the JWS compact serialization format.
      validator: A JwtValidator that validates the token.

    Returns:
      A VerifiedJwt.
    Raises:
      tink.TinkError if the operation fails.
    """
    raise NotImplementedError()


class JwtMacInternal(metaclass=abc.ABCMeta):
  """Internal interface for authenticating and verifying JWT with JWS MAC.

  "kid" is an optional value that is set by the wrapper for keys with output
  prefix TINK. It is set to None for output prefix RAW.
  """

  @abc.abstractmethod
  def compute_mac_and_encode_with_kid(self, token: _raw_jwt.RawJwt,
                                      kid: Optional[str]) -> str:
    raise NotImplementedError()

  @abc.abstractmethod
  def verify_mac_and_decode_with_kid(
      self, compact: str, validator: _jwt_validator.JwtValidator,
      kid: Optional[str]) -> _verified_jwt.VerifiedJwt:
    raise NotImplementedError()
