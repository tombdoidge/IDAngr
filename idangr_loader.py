# idangr_loader.py - IDA will load this file as the plugin entrypoint

import idangr.plugin as plugin

# Define plugin entry point
PLUGNAME = "IDAngr"

def PLUGIN_ENTRY():
    return plugin.IDAngrPlugin()
