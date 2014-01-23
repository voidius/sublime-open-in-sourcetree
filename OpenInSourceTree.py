import os
import locale
import subprocess
import sublime, sublime_plugin


class OpenInSourcetreeCommand(sublime_plugin.WindowCommand):

    FALLBACK_STREE_PATH = '/usr/local/bin/stree'
    FALLBACK_STREE_MAC_PATH = '/Applications/SourceTree.app'

    settings = sublime.load_settings('OpenInSourceTree.sublime-settings')

    def run(self, *args):
        sublime.status_message(__name__ + ': running')

        stree_path = self.get_stree_path()
        path       = self.get_path()

        if path in ['', None]:
            sublime.status_message(__name__ + ': No place to open SourceTree to')
            return False

        if stree_path in ['', None]:
            sublime.error_message(__name__ + ': No SourceTree executable found: is it installed?')
            return False

        if self.settings.get('detect_git', True):
            path = self.get_git_path(path)

        if stree_path.endswith(".app"):
            subprocess.call(['open', '-a', stree_path, path])
        else:
            subprocess.Popen([stree_path], cwd=path.encode(locale.getpreferredencoding(do_setlocale=True)), shell=True)


    def get_git_path(self, initial_path):
        git_path = initial_path
        while ('.git' not in os.listdir(git_path)) and (git_path != '/'):
            git_path = os.path.dirname(git_path)

        if git_path != '/':
            return git_path
        else:
            return initial_path


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


    def get_stree_path(self):
        stree_path = self.settings.get('stree_path', self.FALLBACK_STREE_PATH)

        if stree_path == None:
            stree_path = self.FALLBACK_STREE_PATH

        if not os.path.isfile(stree_path):
            mac_path = self.FALLBACK_STREE_MAC_PATH
            if os.path.isdir(mac_path):
                stree_path = mac_path
            else:
                stree_path = None

        return stree_path
