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
import char
from util import fst_utf8

C = fst_utf8([
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
])

back_V = fst_utf8(["a", "á", "o", "ó", "u", "ú"])
front_rounded_V = fst_utf8(["ö", "ő", "ü", "ű"])
neutral_V = fst_utf8(["e", "é", "i", "í"])

# Archiphonemic vowels
# Example			| Archiphoneme symbol
# -hoz/-hez/-höz	| Ö
# -ból/-ből			| Ó
# -nál/-né			| Á
# -ak/-ek			| A
# -ok/-ek			| O
# -ul/-ül			| U

# Harmony rules
# first rule: back
# example: házakon
# second rule: front unrounded
# example: könyveken
# third rule: front rounded
# example: könyvön
back_transform = fst_utf8(
    [("Ö", "o"), ("Ó", "ó"), ("Á", "á"), ("A", "a"), ("O", "o"), ("U", "u")])
front_rounded_transform = fst_utf8([("Ö", "ö")])
front_unrounded_transform = fst_utf8(
    [("Ö", "e"), ("Ó", "ő"), ("Á", "é"), ("A", "e"), ("O", "e"), ("U", "ü")])

back_harmony = pynini.cdrewrite(
    back_transform,
    back_V + (neutral_V | C).star,
    "",
    char.SIGMA_STAR
)
front_rounded_harmony = pynini.cdrewrite(
    front_rounded_transform,
    front_rounded_V + (neutral_V | C).star,
    "",
    char.SIGMA_STAR
)
front_unrounded_harmony = pynini.cdrewrite(
    front_unrounded_transform,
    (neutral_V | front_rounded_V) + C.star,
    "",
    char.SIGMA_STAR
)

HARMONY = back_harmony @ front_rounded_harmony @ front_unrounded_harmony
