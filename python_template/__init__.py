import importlib
import os
import types
from importlib.machinery import SourceFileLoader

def _import_from_path(path: str):
    """ 
    Given a filepath, return the module
    This function uses ModuleType to load the module: 
    
    """
    name = os.path.basename(path).replace(".py", "")
    loader = SourceFileLoader(name, path)
    mod = types.ModuleType(loader.name)
    mod.__file__ = path
    mod.__package__ = name
    mod.__loader__ = loader
    try:
        loader.exec_module(mod)
    except ModuleNotFoundError as e:
        if not str(e).endswith(f" {name}"):
            # Failed import of some other module in the module file
            raise e
    return mod

def _def_from_path(path: str):
    """Return definition function or object at provided path"""
    mod = _import_from_path(path)
    if mod:
        try:
            definition = getattr(mod, mod.__name__)
        except AttributeError:
            return None
    else:
        return None
    return definition


def reloadable(func):
    def wrapper(*args, **kwargs):
        wrapper.definition = func
        return wrapper.definition(*args, **kwargs)
    wrapper.definition = func
    return wrapper


def import_space_defs(space_path, load_defs: bool = True, search_def: str = None):
    """Import all modules in the given directory path and return a dictionary of modules
    keyed by definition name
    if search_def is set, will stop search after finding the provided module name"""
    space_defs = {}
    # Find directories at the space level
    for dirpath, dirs, files in os.walk(space_path):
        for dir_name in dirs:
            if dir_name.startswith("_"):
                # e.g. __pycache__
                continue
            def_filename = os.path.join(dirpath, dir_name, dir_name + ".py")
            try:
                if load_defs:
                    # Get function with same name inside module
                    definition = _def_from_path(def_filename)
                else:
                    definition = def_filename
                if definition:
                    space_defs[dir_name] = definition
                    # Add definition to global namespace
                    globals()[dir_name] = definition
                if search_def is not None and search_def == dir_name:
                    break
            except FileNotFoundError:
                pass
    return space_defs

space_path = os.path.dirname(__file__)
import_space_defs(space_path)