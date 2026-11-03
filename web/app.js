// Runs the Python game in the browser: Pyodide executes the code in fury/
// and xterm.js draws the terminal it prints to.

// Every file in the fury package. tests/test_web.py checks this list.
const PY_FILES = [
    "fury/__init__.py",
    "fury/__main__.py",
    "fury/art.py",
    "fury/colors.py",
    "fury/game.py",
    "fury/leaderboard.py",
    "fury/login.py",
    "fury/main_menu.py",
    "fury/register.py",
    "fury/store.py",
    "fury/term.py",
    "fury/user_menu.py",
];

// The ASCII art is drawn for a 50 column terminal.
const COLS = 50;

const FONT_FAMILY = '"DejaVu Sans Mono", Menlo, Consolas, "Liberation Mono", monospace';

const container = document.getElementById("terminal");
const term = new Terminal({
    cols: COLS,
    rows: 30,
    convertEol: true,
    cursorBlink: true,
    fontFamily: FONT_FAMILY,
    theme: { background: "#000000" },
});
const fitAddon = new FitAddon.FitAddon();
term.loadAddon(fitAddon);
term.open(container);

// Width of one character as a fraction of the font size.
const context = document.createElement("canvas").getContext("2d");
context.font = `100px ${FONT_FAMILY}`;
const CHAR_RATIO = context.measureText("W").width / 100;

// Picks the biggest font that still fits 50 columns, then fills the height.
function fitTerminal() {
    // Leave room for the scrollbar.
    const width = container.clientWidth - 16;
    term.options.fontSize = Math.max(9, Math.min(20, Math.floor(width / (COLS * CHAR_RATIO))));
    const dims = fitAddon.proposeDimensions();
    if (dims && dims.rows > 0) {
        term.resize(COLS, Math.max(10, dims.rows));
    }
}
fitTerminal();
window.addEventListener("resize", fitTerminal);

// Line input for the game. Python awaits furyReadLine() whenever it asks
// for input. Like a real terminal, lines typed before the game asks are
// queued instead of lost.
let pendingLine = null;
let lineBuffer = "";
const typedLines = [];

window.furyReadLine = () => new Promise((resolve) => {
    if (typedLines.length) {
        resolve(typedLines.shift());
    } else {
        pendingLine = resolve;
    }
});

term.onData((data) => {
    for (const ch of data) {
        if (ch === "\r") {
            term.write("\r\n");
            const line = lineBuffer;
            lineBuffer = "";
            if (pendingLine) {
                const resolve = pendingLine;
                pendingLine = null;
                resolve(line);
            } else {
                typedLines.push(line);
            }
        } else if (ch === "\x7f" || ch === "\b") {
            if (lineBuffer) {
                lineBuffer = lineBuffer.slice(0, -1);
                term.write("\b \b");
            }
        } else if (ch >= " ") {
            lineBuffer += ch;
            term.write(ch);
        }
    }
});

document.getElementById("restart").addEventListener("click", () => {
    window.location.reload();
});

async function start() {
    term.write("\x1b[33mLoading the battlefield...\x1b[0m\r\n");
    term.focus();

    const pyodide = await loadPyodide();
    // Pyodide reuses the buffer it passes in, so copy it before xterm reads it.
    const write = (buffer) => {
        term.write(buffer.slice());
        return buffer.length;
    };
    pyodide.setStdout({ write });
    pyodide.setStderr({ write });

    pyodide.FS.mkdirTree("/home/pyodide/fury");
    const sources = await Promise.all(PY_FILES.map(async (path) => {
        const response = await fetch(path);
        if (!response.ok) throw new Error(`Couldn't load ${path} (${response.status})`);
        return [path, await response.text()];
    }));
    for (const [path, source] of sources) {
        pyodide.FS.writeFile(`/home/pyodide/${path}`, source);
    }

    term.reset();
    await pyodide.runPythonAsync(`
import sys
sys.path.insert(0, "/home/pyodide")
from fury.__main__ import main
await main()
`);
}

start().catch((error) => {
    console.error(error);
    term.write(`\r\n\x1b[31mSomething went wrong: ${error.message}\x1b[0m\r\n`);
    term.write("Press 'Restart game' to try again.\r\n");
});
