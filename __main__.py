"""
When this module is zipped and run (zip hammer.zip -r .; python hammer.zip)
python looks for __main__ and will run it if it exists.

So here we are, fire up the real main() from hammer.
"""

import kle2pcb

if __name__ == "__main__":
    kle2pcb.main()
