import briltxt
from .to_ssa import to_ssa
from .examples import bril_dict
import json
from .form_blocks import form_blocks

print_prog = briltxt.print_prog


def parse_bril(prog):
    return json.loads(briltxt.parse_bril(prog))
