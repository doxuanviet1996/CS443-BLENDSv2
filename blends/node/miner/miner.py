import threading

import requests

from ... import PORT
from ..crypto import get_hash
from ..model import Block
from ..parser import Parser
from ..util import now


class Miner:
    def __init__(self,
                 block: Block,
                 mining: threading.Event,
                 main_queue: queue.Queue = None):
        self.parser = Parser()
        self.block = block
        self.mining = mining
        self.main_queue = main_queue

    def mine_block(self):
        idx = 0
        while True:
            idx += 1
            if idx % 100000 == 0 and not self.mining.is_set():
                return False
            """
            Step 1: Your mining code
            """

            raise NotImplementedError
            return False

    def mine(self):
        if self.mine_block():
            self.new_block_mint()

    def new_block_mint(self):
        if self.main_queue:
            self.main_queue.put(self.block)
