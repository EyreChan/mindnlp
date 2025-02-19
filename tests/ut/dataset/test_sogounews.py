# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""
Test SogouNews
"""
import os
import shutil
import unittest
import pytest
from mindnlp import load_dataset
from mindnlp.dataset import SogouNews


class TestSogouNews(unittest.TestCase):
    r"""
    Test SogouNews
    """

    @classmethod
    def setUpClass(cls):
        cls.root = os.path.join(os.path.expanduser("~"), ".mindnlp")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root)

    @pytest.mark.dataset
    @pytest.mark.local
    def test_sogounews(self):
        """Test sogounews"""
        num_lines = {
            "train": 450000,
            "test": 60000,
        }
        dataset_train, dataset_test = SogouNews(
            root=self.root, split=("train", "test")
        )
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

        dataset_train = SogouNews(root=self.root, split="train")
        dataset_test = SogouNews(root=self.root, split="test")
        assert dataset_train.get_dataset_size() == num_lines["train"]
        assert dataset_test.get_dataset_size() == num_lines["test"]

    @pytest.mark.dataset
    @pytest.mark.local
    def test_sogounews_by_register(self):
        """test sogounews by register"""
        _ = load_dataset(
            "SogouNews",
            root=self.root,
            split=("train", "test"),
        )
