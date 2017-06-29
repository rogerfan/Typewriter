# originally created by:
# + castles_made_of_sand
# + facelessuser
# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806

import sublime
import sublime_plugin


plugin_settings = None


def plugin_loaded():
    global plugin_settings
    plugin_settings = sublime.load_settings('Typewriter.sublime-settings')


def move_cursor_to_eof(view):
    eof = view.size()
    sel = view.sel()[0]
    if sel.a != eof:
        view.sel().clear()
        view.sel().add(sublime.Region(eof))
        view.show(eof)


class TypewriterMode(sublime_plugin.EventListener):

    def __init__(self):
        self.center_view_on_next_selection_modified = False

    def on_selection_modified(self, view):
        settings = view.settings()
        if settings.get('typewriter_mode_typing') == 1:
            move_cursor_to_eof(view)
        if (settings.get('typewriter_mode_scrolling') and
                self.center_view_on_next_selection_modified):
            self.center_view(view)
            self.center_view_on_next_selection_modified = False

    def on_post_text_command(self, view, command_name, args):
        if not view.settings().get('typewriter_mode_scrolling'):
            return
        if command_name in plugin_settings.get('scrolling_mode_center_on_commands', []):
            self.center_view(view)

    def on_window_command(self, window, command_name, args):
        # This is to work around a bug in Sublime Text 3 wherein on_post_window_command
        # is not being called. Ideally that is where we should call center_view so that
        # the view is centered on the new location. Instead, we 'remember' here that
        # we need to center the view on the next selection_modified event.
        if not window.active_view().settings().get('typewriter_mode_scrolling'):
            return

        scrolling_mode_center_on_next_selection_modified_commands = \
            plugin_settings.get('scrolling_mode_center_on_next_selection_modified_commands', [])

        if command_name in scrolling_mode_center_on_next_selection_modified_commands:
            self.center_view_on_next_selection_modified = True

    def on_modified(self, view):
        if not view.settings().get('typewriter_mode_scrolling'):
            return
        self.center_view(view)

    # Center View
    def center_view(self, view):
        buff_lines = plugin_settings.get('scrolling_buffer')
        lineheight = view.line_height()
        buff = buff_lines*lineheight

        visible = view.visible_region()
        vis_top = view.viewport_position()[1]
        vis_bot = vis_top + view.viewport_extent()[1]
        vis_height = view.viewport_extent()[1]/2 +1

        sel = view.sel()
        region = sel[0] if len(sel) == 1 else None
        if region is not None:
            cursor = view.text_to_layout(region.b)[1]
            lim_top = vis_top + buff
            lim_bot = vis_bot - buff

            if cursor >= lim_bot:
                target = list(view.text_to_layout(region.b))
                target[1] = cursor + buff - vis_height
                if vis_bot - vis_height < target[1]:
                    view.show_at_center(view.layout_to_text(tuple(target)))
            elif cursor <= lim_top:
                target = list(view.text_to_layout(region.b))
                target[1] = cursor - buff + vis_height
                if vis_top + vis_height > target[1]:
                    view.show_at_center(view.layout_to_text(tuple(target)))
