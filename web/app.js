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

const IS_TOUCH = window.matchMedia("(pointer: coarse)").matches;

// Picks the biggest font that still fits 50 columns, then fills the height.
// The page follows the visible viewport, so the on-screen keyboard on a
// phone shrinks the terminal instead of covering the prompt.
function fitTerminal() {
    const viewport = window.visualViewport;
    if (viewport) {
        document.body.style.height = `${viewport.height}px`;
        window.scrollTo(0, 0);
    }
    const size = container.clientWidth / (COLS * CHAR_RATIO);
    term.options.fontSize = Math.max(8, Math.min(20, Math.floor(size * 2) / 2));
    const dims = fitAddon.proposeDimensions();
    if (dims && dims.rows > 0) {
        term.resize(COLS, Math.max(10, dims.rows));
    }
    // Lines the header, footer and keys up with the terminal's edges.
    const screen = container.querySelector(".xterm-screen");
    document.documentElement.style.setProperty("--term-width", `${screen.offsetWidth}px`);
    term.scrollToBottom();
}
fitTerminal();
window.addEventListener("resize", fitTerminal);
window.visualViewport?.addEventListener("resize", fitTerminal);

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

// Handles typed keys, pasted text and taps on the on-screen keys alike.
function handleInput(data) {
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
}

term.onData(handleInput);

// On phones, on-screen keys cover the menus, y/n questions and every shot
// (rows A-J, columns 1-10) without opening the keyboard, which would hide
// most of the board. Pressing them keeps the keyboard as it is.
const keys = document.getElementById("keys");
const NAMED_KEYS = { backspace: "\x7f", enter: "\r" };
if (IS_TOUCH) {
    const rows = ["ABCDEFGHIJ", "1234567890"].map((chars) => [...chars].map((ch) => {
        const button = document.createElement("button");
        button.type = "button";
        button.dataset.key = ch.toLowerCase();
        button.textContent = ch;
        return button;
    })).flat();
    keys.prepend(...rows);
    keys.hidden = false;
    document.getElementById("hint").textContent = "⌨ opens the keyboard.";
    keys.addEventListener("pointerdown", (event) => {
        if (event.target.closest("button")) event.preventDefault();
    });
    keys.addEventListener("click", (event) => {
        const button = event.target.closest("button");
        if (!button) return;
        if (button.dataset.key === "keyboard") {
            term.focus();
        } else {
            handleInput(NAMED_KEYS[button.dataset.key] ?? button.dataset.key);
        }
    });
    fitTerminal();
}

document.getElementById("restart").addEventListener("click", () => {
    window.location.reload();
});

async function start() {
    term.write("\x1b[33mLoading the battlefield...\x1b[0m\r\n");
    // On a phone this would pop the keyboard up over the intro.
    if (!IS_TOUCH) term.focus();

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
