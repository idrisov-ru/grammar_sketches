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

import pynini
import harmony

EN_HU_dict = pynini.string_file(
    "./dict/en_hu.tsv", input_token_type="utf8", output_token_type="utf8")
N_low_v = pynini.string_file(
    "./dict/HU_N_low_vowel.tsv", input_token_type="utf8", output_token_type="utf8")
regular_stem = EN_HU_dict @ (pynini.project(EN_HU_dict,
                                            "output") - pynini.project(N_low_v, "input"))
N_low_v_stem = EN_HU_dict @ N_low_v

NOM = pynini.cross("-NOM", "")
PL = pynini.cross("-PL", "k")
ILL = pynini.cross("-ILL", "bA")

NOUN = ((EN_HU_dict + (NOM | ILL)
        | (N_low_v_stem | regular_stem) + PL + ILL.ques) @ harmony.HARMONY).optimize()
