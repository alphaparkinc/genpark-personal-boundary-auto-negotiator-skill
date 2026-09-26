import json, sys
from client import PersonalBoundaryAutoNegotiatorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "personal-boundary-auto-negotiator", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "negotiate_boundary_response", "description": "Arbitrates incoming communications, defends personal deep-work boundaries, and synthesizes empathetic asynchronous deflections."}]}}
    elif method == "tools/call":
        client = PersonalBoundaryAutoNegotiatorClient()
        res = client.negotiate_boundary_response()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = PersonalBoundaryAutoNegotiatorClient()
        print(json.dumps(client.negotiate_boundary_response(), indent=2))
