в редакторе «VS Code» можно легко форматировать код либо с помощью комбинации клавиш «Shift+Alt+F» (действует на весь код в текущем файле), либо с помощью комбинации клавиш «Ctrl+K Ctrl+F» (действует только на код, входящий в текущее выделение).

settings.json - глобальный
{
    "extensions.autoCheckUpdates": false,
    "update.enableWindowsBackgroundUpdates": false,
    "extensions.autoUpdate": false,
    "update.showReleaseNotes": false,
    "update.mode": "none",

    "debug.inlineValues": "on",
    "debug.autoExpandLazyVariables": true,
    "editor.wordWrap": "on",
    "editor.wordWrapColumn": 180,
    "editor.fontSize": 12,
    "editor.lineHeight": 18,
    "editor.fontFamily": "Consolas, 'Courier New',monospace",
    "editor.autoIndent": "advanced",
    "editor.quickSuggestionsDelay": 700,
    "html.autoClosingTags": true,
    "javascript.autoClosingTags": true,
    "css.format.enable": true,
    "workbench.colorTheme": "Visual Studio Light",
    "terminal.integrated.cursorStyle": "line",
    "terminal.integrated.cursorBlinking": true,
    "workbench.startupEditor": "none",
    "explorer.autoReveal": false,
    "explorer.compactFolders": true,
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "editor.minimap.enabled": false,
    "breadcrumbs.enabled": false,
    "window.autoDetectHighContrast": false,
    "window.commandCenter": false,
    "chat.editor.fontSize": 12,
    "[html]": {
        "editor.defaultFormatter": "vscode.html-language-features"
    },
    "[javascript]": {
        "editor.defaultFormatter": "vscode.typescript-language-features"
    },
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
  "[django-html]": {
    "editor.formatOnSave": false,
    "editor.defaultFormatter": "junstyle.vscode-django-support"
  },

      "files.associations": {
        "**/*/templates/*.html": "django-html",
        "**/templates/*/*.html": "django-html",
        "**/templates/*/*/*.html": "django-html",
        "**/views/**/*.html": "django-html",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },

    
    "explorer.confirmDragAndDrop": false,
    "files.refactoring.autoSave": false,
    "workbench.enableExperiments": false,
     
}