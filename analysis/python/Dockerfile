# pyodide only bundles a single version of python
FROM python:3.13-slim as builder

# jupyterlite-core: build jupyterlite site
# jupyterlite-pyodide-kernel: pyodide kernel for jupyterlite
RUN pip install --upgrade pip && \
    pip install jupyterlite-core jupyterlite-pyodide-kernel

# add pyodide tar ball to /app
WORKDIR /app
ADD https://github.com/pyodide/pyodide/releases/download/0.29.3/pyodide-0.29.3.tar.bz2 .

RUN mkdir /app/wheelhouse && \
    pip download --only-binary=:all: --dest /app/wheelhouse \
    uproot matplotlib

RUN jupyter lite build \
    --pyodide pyodide-0.29.3.tar.bz2 \
    --piplite-wheels /app/wheelhouse

# Stage 2
FROM nginx:alpine

WORKDIR /usr/share/nginx/html/

COPY --from=builder /app/_output/ .

# ensure the data directory exists for the bind mount
RUN mkdir -p geant4

# indicate that this is a web server
EXPOSE 80
