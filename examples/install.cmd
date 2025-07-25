python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\boomi-1.0.0-py3-none-any.whl --force-reinstall
