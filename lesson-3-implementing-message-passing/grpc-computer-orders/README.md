## Commands used
```
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment (always run this when openning a new terminal)
cd .venv
source bin/activate

# Install grpc tools
pip install grpcio-tools grpcio

# Generate grpc files from the proto specification
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ order.proto

# Start server
python main.py

# Start client 
python writer.py
```
