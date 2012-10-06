import sublime, sublime_plugin

import subprocess

class RevealInPathFinderCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        fileName = self.view.file_name()
        cmd      = ["open", "-a", "Path Finder.app", fileName]
        # print "%s cmd: %s" % (__name__, repr(cmd))

        (stdout, stderr) = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            ).communicate()

        if stdout: print "%s stdout: %s" % (__name__, stdout)
        if stdout: print "%s stderr: %s" % (__name__, stderr)

    def description(self):
        return "Reveal in Path Finder"