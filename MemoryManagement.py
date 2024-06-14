'''
import re


class MemoryManager:
    def __init__(self, allocator):
        self.allocator = allocator
    
    def allocate(self, process, request_size):
        memory_view = self.allocator.memory_view()

        block_start = 0
        i = 0
        while i < 256:
            if memory_view[i] is not None:
                current_process = memory_view[i]
                length = current_process.block
                self.allocator.free_memory(current_process)
                self.allocator.allocate_memory(block_start, length, current_process)
                block_start += length
                i += length
            else:
                i += 1
                

        memory_view = self.allocator.memory_view()

        # You need to complete the code here. 

        # The input of this function contains two parameters: 
        #   process -- the process requesting memory, you don't need to
        #              do anything for process, just pass it to the 
        #              'self.allocator.allocate_memory' function at the 
        #              end of this function.
        #   request_size -- an integer indicating how many memory blocks 
        #                   this process requests.

        # The first line returns 'memory_view', a list of memory blocks.
        # If a memory block is free, the corresponding item of the list
        # will be None, otherwise the item will be the process object.
        
        # The total size of the memory is 256 blocks.

        # You need to decide which memory to allocate to the process based
        # on 'memory_view' and 'request_size'. When you make a decision, 
        # pass the starting address of the memory (i.e. 'block_start')
        # along with 'request_size' and 'process' to the function
        # 'self.allocator.allocate_memory' (see below).

        # Memory blocks will be automatically reclaimed according to 
        # the definition in the process objects.

        

        block_start = None
        best_block_size = 257  

        i = 0
        while i < 256:
            if memory_view[i] is None:
                j = i
                current_block_size = 0
                while j < 256 and memory_view[j] is None:
                    current_block_size += 1
                    j += 1

                if current_block_size >= request_size and current_block_size < best_block_size:
                    block_start = i
                    best_block_size = current_block_size
                
                i = j  # Move to the next block of memory
            else:
                i += 1  # Skip over allocated memory

        #self.allocator.allocate_memory(block_start, request_size, process)
        
        if block_start != None:
            self.allocator.allocate_memory(block_start, request_size, process)
'''

import re


class MemoryManager:
    def __init__(self, allocator):
        self.allocator = allocator

    def allocate(self, process, request_size):
        memory_view = self.allocator.memory_view()

        block_start = 0
        i = 0
        while i < 256:
            if memory_view[i] is not None:
                current_process = memory_view[i]
                length = current_process.block
                self.allocator.free_memory(current_process)
                self.allocator.allocate_memory(block_start, length, current_process)
                block_start += length
                i += length
            else:
                i += 1

        self.allocator.allocate_memory(block_start, request_size, process)
