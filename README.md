# AshHTTPScanner

AshHTTPScanner is a Python-based HTTP/HTTPS response analysis tool.

## Features

- HTTP and HTTPS URL validation
- HTTP status code detection
- Protocol detection
- Server header extraction
- Content-Type detection
- Content-Length detection
- Response-time measurement
- Terminal reporting
- Report generation

## Project Structure

AshHTTPScanner/
├── banners/
├── core/
├── outputs/
├── reports/
└── main.py

## Technologies

- Python
- Requests
- urllib.parse

## Usage

python main.py

Enter a target URL when prompted.

## Example

Target URL: http://google.com

Status Code: 200
Server: ...
Content-Type: ...
Content-Length: ...
Response Time: ...

## Purpose

Built as a cybersecurity learning project to understand HTTP requests,
responses, headers, and modular Python project architecture.
