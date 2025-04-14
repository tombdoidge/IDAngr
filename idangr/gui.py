######################################################
# Author: Andrea Fioraldi <andreafioraldi@gmail.com> #
# License: BSD 2-Clause                              #
######################################################

from . import manage
from . import init_gui
from . import main_gui

print("######### IDAngr GUI #########")

def show():
    if not manage.is_initialized():
        from .init_gui import IDAngrConnectDialog
        if IDAngrConnectDialog.go():
            from .main_gui import idangr_panel_show
            idangr_panel_show()
    else:
        from .main_gui import idangr_panel_show
        idangr_panel_show()

def simulation_manager():
    if not manage.is_initialized():
        raise RuntimeError("GUI not initialized")
    else:
        from .main_gui import _idangr_ctx
        if _idangr_ctx.simman is None:
            raise RuntimeError("Simulation Manager not found in GUI")
        return _idangr_ctx.simman

def found_state():
    if not manage.is_initialized():
        raise RuntimeError("GUI not initialized")
    else:
        from .main_gui import _idangr_ctx
        if _idangr_ctx.foundstate is None:  # fixed typo: was "foundtstate"
            raise RuntimeError("State not found in GUI")
        return _idangr_ctx.foundstate
