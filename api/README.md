## Docker API

This is a simple implementation of a router based fastapi API. It suppports two existing router endpoints: `database` and `prediction`

### How to extend this endpoint

For local development and testing, you will need to launch a virtual environment from this directory. This service was developed using `uv`. To get started iniitialize a virtual environment with uv sync.

You can test the application locally using `uvicorn app.main:app --host "0.0.0.0" --port "8000"`.

> Note you will a postgres instance running in order to test queries or database connectivity.

### Asynchronous code

This API leverages asynchronous operations. Most I/O operations within an API should be awaited via `async` and `await` syntax to reduce response latencies. The existing functions here show a basic structure of how to set up asynchronous operations. For more information see the [FastAPI writeup on async](https://fastapi.tiangolo.com/async/#asynchronous-code) (careful, it is AI generated)

