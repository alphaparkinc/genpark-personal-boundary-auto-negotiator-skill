import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PersonalBoundaryAutoNegotiatorClient

def main():
    client = PersonalBoundaryAutoNegotiatorClient()
    res = client.negotiate_boundary_response()
    print("=== Personal Boundary Auto-Negotiator Output ===")
    print(f"Sender: {res['sender_name']} ({res['sender_role']}) | VIP: {res['is_vip_sender']}")
    print(f"Verdict: {res['arbitrated_verdict']} (Strength: {res['boundary_defense_strength']})")
    print(f"Dispatch Mode: {res['recommended_dispatch_mode']}")
    print(f"\nSynthesized Boundary Defense Response:")
    print(f"\"{res['synthesized_response']}\"")

if __name__ == '__main__':
    main()
