import os
import locale
import subprocess
import sublime, sublime_plugin


class OpenInSourcetreeCommand(sublime_plugin.WindowCommand):


    def run(self, *args):
        sublime.status_message(__name__ + ': running')

        settings   = sublime.load_settings('Default.sublime-settings')
        stree_path = self.get_stree_path(settings)
        path       = self.get_path()

        if path in ['', None]:
            sublime.status_message(__name__ + ': No place to open Source Tree to')
            return False

        if stree_path in ['', None]:
            sublime.error_message(__name__ + ': stree executable path not set, incorrect or no stree?')
            return False


        if settings.get('detect_git', True):
            path = self.get_git_path(path)

        if stree_path.endswith(".app"):
            subprocess.call(['open', '-a', stree_path, path])
        else:
            p = subprocess.Popen([stree_path], cwd=path.encode(locale.getpreferredencoding(do_setlocale=True)), shell=True)


    def get_git_path(self, path):
        git_path = path
        while (git_path != '/') or ('.git' in os.listdir(git_path)):
            git_path = os.path.dirname(git_path)

        if git_path != '/':
            return git_path
        else:
            return path


    def get_path(self):
        if self.window.active_view():
            path = self.window.active_view().file_name()
        elif self.window.folders():
            path = self.window.folders()[0]
        else:
            return None

        if os.path.isfile(path):
            path = os.path.dirname(path)

        return path


    def get_stree_path(self, settings):
        stree_path = settings.get('stree_path', '/usr/local/bin/stree')

        if not os.path.isfile(stree_path):
            mac_path = '/Applications/SourceTree.app'
            if os.path.isdir(mac_path):
                stree_path = mac_path
            else:
                stree_path = None

        return stree_path
