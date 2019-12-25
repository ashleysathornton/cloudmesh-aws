from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class AwsCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_aws(self, args, arguments):
        """
        ::

          Usage:
                aws --file=FILE
                aws list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        VERBOSE(arguments)

        Console.error("This is just a sample")
        return ""
