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

import sys
import pynini
import util
import char
import noun
from pynini.lib import rewrite


def test_generator(tokens):
    generator = util._priority_union(noun.NOUN,
                                     char.SIGMA_STAR, char.SIGMA_STAR)
    for token in tokens:
        for rw in rewrite.rewrites(token, generator, input_token_type="utf8", output_token_type="utf8"):
            print(rw)


def test_parser(tokens):
    generator = util._priority_union(noun.NOUN,
                                     char.SIGMA_STAR, char.SIGMA_STAR)
    parser = pynini.invert(generator)
    for token in tokens:
        for rw in rewrite.rewrites(token, parser, input_token_type="utf8", output_token_type="utf8"):
            print(rw)


if __name__ == "__main__":
    #    test_generator(sys.argv[1].split())
    test_generator(["woman-ILL",
                    "house-ILL",
                    "man-ILL",
                    "woman-PL-ILL",
                    "house-PL-ILL",
                    "man-PL-ILL"])
