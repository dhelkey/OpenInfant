#Initial open-neo package. This can be expanded into a package with a 
# folder based architecture
import os
import psutil
import time
from IPython.display import display, Markdown

#Define common paths and files
PATH_DATA_ICD = os.path.join('data','icd')
PATH_DATA_ZIP = os.path.join('data','zip')

################################################
#Helper functions
################################################

#Functions for writing, reading, and displaying files
def wF(outfile, file_contents):
    """Write file_contents to outfile"""
    with open(outfile, 'w') as f:
        f.write(file_contents)

def rF(infile):
    """Read infile contents"""
    with open(infile,'r') as f:
        return f.read()

def dF(infile):
    """Display File using Markdown"""
    display(Markdown(infile))
    
class computeInfo:
    def __init__(self):
        self.start_time = time.time()
        self.initial_memory = psutil.Process()\
            .memory_info().rss / (1024 ** 2)  # Memory in MB
        self.last_memory = self.initial_memory

    def info(self):
        """Displays elapsed time, current memory usage,
          and memory changes since last call."""
        current_time = time.time()
        current_memory = psutil.Process()\
            .memory_info().rss / (1024 ** 2)  # Memory in MB
        elapsed_time = current_time - self.start_time
        memory_change = current_memory - self.last_memory
        total_memory_change = current_memory - self.initial_memory

        # Calculate H:M:S from elapsed_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Helper function to format memory in MB and GB
        def format_memory(memory_in_mb):
            memory_in_gb = memory_in_mb / 1024  # Convert MB to GB
            return f"{memory_in_mb:.0f} MB ({memory_in_gb:.1f} GB)"

        print(f"Elapsed Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
        print(f"Current Memory Usage: {format_memory(current_memory)}")
        print(f"Memory Change Since Last Call: {format_memory(memory_change)}")
        print(f"Total Memory Change Since Instantiation: {format_memory(total_memory_change)}")

        # Update last memory usage for the next call
        self.last_memory = current_memory

# #Usage
# compute_info = ComputeInfo() 
# compute_info.info() #Display initial compute info
# .....
# .....
# compute_info.info()  # Display compute info