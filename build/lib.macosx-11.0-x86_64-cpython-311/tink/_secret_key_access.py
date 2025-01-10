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
"""Gives access to secret Tink keys and keysets.

WARNING

Reading or writing secret keys is a bad practice, usage of this API should be
restricted.
"""

from tink import core


class SecretKeyAccess(core.KeyAccess):
  """An access token that gives access to all keys."""
  pass


TOKEN = SecretKeyAccess()
