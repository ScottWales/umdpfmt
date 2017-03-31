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

import sys
import setuptools
import subprocess

def antlr_gen(config):
    print("running antlr4")
    target = '-Dlanguage=Python%d'%(sys.version_info[0])
    command = ['java', '-jar', 'antlr-4.7-complete.jar', \
            target, 'umdpfmt/parser/Fortran.g4']
    subprocess.check_call(command)


class AntlrGen(setuptools.Command):
    description = "Generate Antlr parser"
    command_name = "antlrgen"
    user_options = []

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

    def run(self):
        antlr_gen(None)

