import sys
from cx_Freeze import setup, Executable

# A base "Win32GUI" é usada para GUI e oculta a janela do console
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("gerarpdf.pyw", base=base)]

setup(
    name="GerarPDF",
    version="1.0",
    description="Aplicativo para converter arquivos Word para PDF",
    executables=executables
)