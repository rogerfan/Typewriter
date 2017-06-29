scrollbuffer
==========

This plugin provides a buffer ahead of scrolling in Sublime Text 3\*. Code is based on the [Typewriter](https://github.com/alehandrof/Typewriter) package by Alex Armstrong.


## Usage

The scrollbuffer mode can be toggled via the command palette through the `Scrollbuffer Mode (Toggle)` command. It can also be enabled by including `"scrollbuffer_mode": true` in your settings file.


### Warnings

- For best results in Scrolling mode you should set `"scroll_past_end": true`. (By default it is set to `true` in Windows and Linux, but `false` in OSX.)


## Changelog & History

- **0.1** - Initial release with code based on [Typewriter](https://github.com/alehandrof/Typewriter).


## Issues/Todo

- Buffered scrolling will not work with multiple cursors.


## Alternatives

- [Typewriter](https://github.com/alehandrof/Typewriter) provides typewriter scrolling.
- [BufferScroll](https://github.com/SublimeText/BufferScroll) also provides a version of typewriter scrolling and many other features besides.
- [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) has added typewriter scrolling among other more Markdown-specific features.
