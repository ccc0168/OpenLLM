# Copyright 2023 BentoML Team. All rights reserved.
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
from __future__ import annotations

import openllm

START_FLAN_T5_COMMAND_DOCSTRING = """\
Run a LLMServer for FLAN-T5 model and variants.

\b
> See more information about FLAN-T5 at [huggingface/transformers](https://huggingface.co/docs/transformers/model_doc/flan-t5)

\b
## Usage

By default, this model will use the PyTorch model for inference. However, this model supports both Flax and Tensorflow.

\b
- To use Flax, set the environment variable ``OPENLLM_FLAN_T5_FRAMEWORK="flax"``

\b
- To use Tensorflow, set the environment variable ``OPENLLM_FLAN_T5_FRAMEWORK="tf"``

\b
FLAN-T5 Runner will use google/flan-t5-large as the default model. To change any to any other FLAN-T5
saved pretrained, or a fine-tune FLAN-T5, provide ``OPENLLM_FLAN_T5_PRETRAINED='google/flan-t5-xxl'``
"""

DEFAULT_PROMPT_TEMPLATE = """Answer the following question:\nQuestion: {instruction}\nAnswer:"""


class FlanT5Config(openllm.LLMConfig):
    """FLAN-T5 was released in the paper [Scaling Instruction-Finetuned Language Models](https://arxiv.org/pdf/2210.11416.pdf)
    - it is an enhanced version of T5 that has been finetuned in a mixture of tasks.

    Refer to [FLAN-T5's page](https://huggingface.co/docs/transformers/model_doc/flan-t5) for more information.
    """

    class GenerationConfig:
        temperature: float = 0.9
        max_new_tokens: int = 2048
        top_k: int = 50
        top_p: float = 0.4
        repetition_penalty = 1.0
