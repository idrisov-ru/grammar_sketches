# Copyright 2022 Ruslan Idrisov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Iterable
import pynini

# priority union function
# excerpt from pynini/examples/plurals.py
def _priority_union(q: pynini.Fst, r: pynini.Fst,
                    sigma: pynini.Fst) -> pynini.Fst:
    complement_domain_q = sigma - pynini.project(q, "input")
    return pynini.union(q, complement_domain_q @ r)

# pynini.union doesn't work with utf8 strings
# so let's clean corresponding boilerplate a bit
def fst_utf8(s: Iterable) -> pynini.Fst:
	return pynini.string_map(s, input_token_type="utf8", output_token_type="utf8")