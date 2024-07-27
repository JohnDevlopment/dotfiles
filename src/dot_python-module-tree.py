from pathlib import Path
from argparse import ArgumentParser
from typing import TYPE_CHECKING
import itertools
import re

if TYPE_CHECKING:
    from typing import Any
    from argparse import Namespace

def print_tree(directory: Path, prefix: str) -> None:
    """
    Recursively print the contents of a package.

    This prints the qualified name of each submodule and
    subpackage under DIRECTORY. DIRECTORY must be a path to the
    package.

    PREFIX is changed during each recursion, but its initial
    value should be the name of the package itself.
    """
    # Get the list of all files and directories
    def _filter(x: Path) -> bool:
        """
        Test that X is either a Python file or a directory.
        """
        return (
            (x.is_file() and x.suffix[1:] == "py") or
            x.is_dir()
        )
    # These iterators filter out anything that isn't a directory or Python
    # source file
    it = filter(_filter, directory.iterdir())
    it = itertools.filterfalse(
        lambda x: re.fullmatch(r'__(?:init|main|pycache)__', x.stem),
        it
    )
    for item in it:
        if item.is_dir():
            # Is a directory, so recurse with the updated prefix
            new_prefix = f"{prefix}.{item.stem}"
            print(new_prefix)
            print_tree(item, new_prefix)
        else:
            print(f"{prefix}.{item.stem}")

def parse_arguments() -> tuple[Path, str]:
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument('package_dir', metavar="PACKAGE_DIR", type=Path,
                        help="directory where the package is located")
    parser.add_argument('package_name', metavar="PACKAGE_NAME")
    args = parser.parse_args()

    return args.package_dir, args.package_name

package_dir, package_name = parse_arguments()

print_tree(package_dir, package_name)
