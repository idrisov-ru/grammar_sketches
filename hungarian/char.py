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

# Alphabet symbols
# Hungarian
hun_lower = pynini.string_file("./dict/hungarian_lowercase.tsv", input_token_type="utf8", output_token_type="utf8")
hun_upper = pynini.string_file("./dict/hungarian_uppercase.tsv", input_token_type="utf8", output_token_type="utf8")
HUN = hun_lower | hun_upper

# English
eng_upper = pynini.string_file("./dict/english_uppercase.tsv", input_token_type="utf8", output_token_type="utf8")
eng_lower = pynini.string_file("./dict/english_lowercase.tsv", input_token_type="utf8", output_token_type="utf8")
ENG = eng_lower | eng_upper

# Other symbols
DIGIT = pynini.string_file("./dict/digit.tsv", input_token_type="utf8", output_token_type="utf8")
PUNCT = pynini.string_file("./dict/punctuation.tsv", input_token_type="utf8", output_token_type="utf8")
SPACE = pynini.union(" ", "	")
NONALPHA = DIGIT | PUNCT | SPACE

# All symbols
CHAR = HUN | ENG | NONALPHA
SIGMA_STAR = CHAR.closure().optimize()
