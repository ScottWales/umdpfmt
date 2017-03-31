#!/usr/bin/env python
# Copyright 2017 ARC Centre of Excellence for Climate Systems Science
# author: Scott Wales <scott.wales@unimelb.edu.au>
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
from __future__ import print_function

from umdpfmt.parser import *

import os.path
from antlr4 import *

def pytest_generate_tests(metafunc):
    if 'specimen' in metafunc.fixturenames:
        specimendir = os.path.join(os.path.dirname(__file__), 'specimens')
        (_, _, specimens) = next(os.walk(specimendir))
        metafunc.parametrize('specimen', [os.path.join(specimendir, x) for x in specimens])

def test_parse_specimen(specimen):
    fs = FileStream(specimen)
    lexer = FortranLexer(fs)
    tokens = CommonTokenStream(lexer)
    parser = FortranParser(tokens)
    parser._errHandler = BailErrorStrategy()
    tree = parser.fortranFile()

