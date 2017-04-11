# ----------------------------------------------------------------------------
# Copyright 2016 Nervana Systems Inc.
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
# ----------------------------------------------------------------------------

from __future__ import print_function
import numpy as np
import ngraph as ng
from ngraph.testing import executor
import pytest
from ngraph.frontends.caffe.cf_importer.importer import CaffeImporter
from os.path import join
pytestmark = pytest.mark.transformer_dependent("module")
PROTO_PATH = "ngraph/frontends/caffe/tests/protos/"

def test_scalar_dummy_data():
    importer = CaffeImporter()
    importer.parse_net_def(join(PROTO_PATH,"scalar_dummy_data.prototxt"))
    op = importer.get_op_by_name("A")
    with executor(op) as ex:
        res = ex()
    assert(res == 1.)

def test_vector_dummy_data():
    importer = CaffeImporter()
    importer.parse_net_def(join(PROTO_PATH,"tensor_dummy_data.prototxt"))
    op = importer.get_op_by_name("A")
    a = np.full((2,3),4.)
    with executor(op) as ex:
        res = ex()
    assert(np.array_equal(res,a))

